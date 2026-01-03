# ENG:
## Hospital Chatbot Agent (exam task from online course)

This project demonstrates a local LLM agent capable of interacting with both **Relational** Supabase + PostgreSQL and **Vector** Pinecone databases. The system allows uploading medical/administrative documents and querying them via a natural language chat interface.

### 🛠 Features:
* **Vector Database (Pinecone):** Used for RAG (Retrieval-Augmented Generation) to search through unstructured documents like PDFs and Word files, e.g. medical protocols, employee guidelines.
* **Relational Database (Supabase):** Used for structured SQL queries, e.g. employee records, hospital data.
* **LLM Agent:** Built with **LangChain** and **Google Gemini** using a ReAct (Reasoning + Acting) architecture.
* **File Processing:** Automatically chunks and embeds uploaded \`.docx\` and \`.pdf\` files.

### 🚀 Tech Stack:
* **Python 3.12** - Programming Language
* **Streamlit** - UI
* **LangChain** - Agent logic
* **Google Gemini** - LLM & Embeddings
* **Pinecone** - Vector Store
* **Supabase** - PostgreSQL

### 📂 Project Structure:
* **\`exam.py\`**: The main entry point. Run this file to start the Streamlit chatbot interface.
* **\`pineconedb.py\`**: Helper script used for parsing PDF/Docx files and uploading embeddings to the Pinecone index.
* **Security Note**: All API keys (Gemini, Pinecone, Supabase) are hidden and loaded from the \`.streamlit/secrets.toml\` folder. They are not shown in the repository for security reasons.

---------------------------------------------------------------------------

# UKR:
## Чат-бот для Лікарні (екзаменаційне завдання з онлайн курсів)

Цей проект демонструє роботу локального LLM-агента, який взаємодіє як з **реляційною** Supabase + PostgreSQL, так і з **векторною** Pinecone базами даних. Система дозволяє завантажувати медичні та адміністративні документи, а потім виконувати пошук по них через звичайний чат.

### 🛠 Функціонал:
* **Векторна БД (Pinecone):** Використовується для RAG (пошуку) по неструктурованих документах, таких як PDF та Word, наприклад: медичні протоколи, інструкції для працівників.
* **Реляційна БД (Supabase):** Використовується для SQL-запитів, наприклад: списки співробітників, дані лікарні.
* **LLM Агент:** Побудований на **LangChain** та **Google Gemini** з використанням архітектури ReAct (Reasoning + Acting).
* **Обробка файлів:** Автоматичне розбиття на фрагменти та ембедінг завантажених \`.docx\` та \`.pdf\` файлів.

### 🚀 Стек технологій:
* **Python 3.12** - ЯП
* **Streamlit** - Інтерфейс користувача (UI)
* **LangChain** - Логіка агента
* **Google Gemini** - LLM та Ембедінги
* **Pinecone** - Векторне сховище
* **Supabase** - PostgreSQL

### 📂 Структура проекту:
* **\`exam.py\`**: Головний файл. Запустіть цей файл, щоб відкрити інтерфейс чат-бота у Streamlit.
* **\`pineconedb.py\`**: Допоміжний скрипт для парсингу файлів PDF/Docx та завантаження векторів у базу даних Pinecone.
* **Безпека**: Усі API ключі (Gemini, Pinecone, Supabase) приховані та завантажуються з локальної папки \`.streamlit/secrets.toml\`. З міркувань безпеки вони відсутні у цьому репозиторії.