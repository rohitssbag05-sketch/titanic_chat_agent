🚢 Titanic AI Data Analyst

A full-stack AI-powered chatbot that analyzes the Titanic dataset using natural language.

Built using:

FastAPI (Backend)

LangChain (LLM integration)

Streamlit (Frontend UI)

Matplotlib (Dynamic visualizations)

🏗️ Architecture
Streamlit (UI)
      ↓
FastAPI (REST API)
      ↓
LangChain (LLM Prompt Chain)
      ↓
Controlled Python Execution Engine
      ↓
Titanic Dataset (Pandas DataFrame)
💡 Design Decisions
1. Controlled Code Generation Instead of Autonomous Agents

Instead of relying on ReAct tool-calling agents (which can be unstable and unpredictable), this project uses:

Structured prompt-based Python code generation

Deterministic execution engine

Schema-aware column injection

Strict execution constraints

This ensures:

Reproducibility

Stability

No hallucinated dataset values

Reliable visualization generation

2. Schema-Aware Prompting

The model is explicitly provided with:

Exact dataframe column names

Case-sensitive enforcement

Execution constraints

This prevents column mismatch errors (e.g., fare vs Fare).

3. Safe Execution Layer

The executor:

Prevents CSV reloading

Rejects dangerous imports

Handles tuple-return plots

Rounds numeric outputs

Captures matplotlib figures safely

✨ Features

Natural language data analysis

Automatic statistical computation

Dynamic histogram & bar plots

Clean chat-style interface

Persistent conversation history

Deployment-ready structure

📊 Example Queries

What is the average ticket fare?

Show histogram of passenger ages

How many passengers embarked from each port?

What percentage of passengers survived?

⚙️ Running Locally
Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
🚀 Deployment Strategy

Backend deployed on Render

Frontend deployed on Streamlit Cloud

Dataset stored within repository