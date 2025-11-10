# Langgraph-Chatbot
An interactive chatbot built using **LangGraph**, **LangChain**, and **Streamlit** — featuring persistent conversation history using SQLite checkpoints.   Each conversation thread is uniquely stored, allowing users to switch between multiple chat sessions seamlessly.

## 🚀 Features

- 🧩 **Multi-threaded chat sessions** — start new conversations or revisit past ones.
- 💾 **Persistent memory** — chat history saved in SQLite using LangGraph's `SqliteSaver`.
- 🧠 **LLM integration** — powered by OpenAI’s `ChatOpenAI` model.
- ⚡ **Dynamic thread management** — every conversation gets a unique UUID.
- 🧰 **Streamlit UI** — clean, sidebar-based interface for managing conversations.

---

## 🧱 Project Structure
LangGraph-Chat-Memory/                                            
│                                                                
├── streamlit_frontend.py # Streamlit app: UI + state management               
├── langgraph_backend.py # Backend: LangGraph setup and checkpoint persistence            
├── chatbot.db # SQLite database (auto-created for checkpoints)                    
├── .env # Environment file (for OpenAI API key)                          
├── requirements.txt # Python dependencies                                   
└── README.md # Documentation (this file)                                       

---

## ⚙️ Installation & Setup

### 1 Clone the repository

```bash
git clone https://github.com/<your-username>/LangGraph-Chat-Memory.git
cd LangGraph-Chat-Memory

### 2 Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt
streamlit
langchain-core
langchain-openai
langgraph
python-dotenv
sqlite3-binary

▶️ Run the Application

Start the Streamlit app:  streamlit run streamlit_frontend.py

Then open the app in your browser at:  http://localhost:8501

