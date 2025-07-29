import json
import streamlit as st
from uuid import uuid4
from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool, InfoSQLDatabaseTool, ListSQLDatabaseTool
from langchain_community.utilities.sql_database import SQLDatabase
import psycopg2
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine


# Отримання ключів
gemini = st.secrets.get("GEMINI_API_KEY")
pinecone_key = st.secrets.get("PINECONE_API_KEY")
supabase_url = st.secrets.get("SUPABASE_URL")
supabase_key = st.secrets.get("SUPABASE_KEY")


# Підключеня до Gemini, Pinecone і Supabase
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=gemini
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=gemini
)

pc = Pinecone(api_key=pinecone_key)
index_name = "exam-itstep"
index = pc.Index(index_name)
vector_store = PineconeVectorStore(index=index, embedding=embeddings)

load_dotenv()

user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")

DATABASE_URL = f"postgresql+pg8000://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(DATABASE_URL)
db = SQLDatabase(engine)


# Функції
sql_tools = [
    QuerySQLDataBaseTool(db=db),
    InfoSQLDatabaseTool(db=db),
    ListSQLDatabaseTool(db=db)
]


def add(document: str):
    '''
    Додає новий документ до векторної бази даних Pinecone
    :param document: str, документ
    :return: str, підтвердження або відмова
    '''
    id = str(uuid4())
    if document:
        title = document.strip().split("\n")[0]
        metadata = {"block_title": title}
        doc = Document(page_content=document, metadata=metadata)
        vector_store.add_documents([doc], ids=[id])

        with open("index_ids.json", "r", encoding="utf-8") as file:
            ids = json.load(file)

        ids[id] = metadata
        with open("index_ids.json", "w", encoding="utf-8") as file:
            json.dump(ids, file)

        return f'"{title}" додано'
    return 'Документ пустий, відмова'


def get(query: str):
    '''
    Шукає потрібний документ з векторної бази даних Pinecone
    :param query: str, запит
    :return: str, отримання документа або ні
    '''
    results = vector_store.similarity_search(query, k=1)
    return f"Найближчий документ:\n- {results[0].page_content}" if results else "Нічого не знайдено."


# Агент
agent = create_react_agent(llm, tools=[get, add] + sql_tools)


# Streamlit і інтерфейс
st.title("Чат-Бот Лікарні: Векторна та Реляційна бази даних")
st.markdown("Функції: `get(query)`, `add(document)` + SQL через Supabase")

if "messages" not in st.session_state:
    st.session_state["messages"] = [SystemMessage(content="Ти помічник адміністратора лікарні. Працюєш з Pinecone і Supabase.")]

user = st.chat_input("Введіть повідомлення: ")
if user:
    msg = HumanMessage(content=user)
    st.session_state["messages"].append(msg)
    result = agent.invoke({"messages": st.session_state["messages"]})
    st.session_state["messages"] = result["messages"]

for message in st.session_state['messages']:
    if isinstance(message, HumanMessage):
        role = 'human'
    elif isinstance(message, AIMessage):
        role = 'ai'
    else:
        continue
    with st.chat_message(role):
        st.markdown(message.content)
