import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit  
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

# Streamlit page configuration
st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜️")
st.title("🦜️ LangChain: Chat with SQL DB")

# Constants
LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

# Sidebar for database selection and configuration
def configure_database():
    radio_opt = ["Use SQLite 3 Database - Student.db", "Connect to your SQL Database"]
    selected_opt = st.sidebar.radio("Choose the DB you want to chat with", radio_opt)
    
    if radio_opt.index(selected_opt) == 1:
        st.sidebar.subheader("MySQL Configuration")
        return {
            "type": MYSQL,
            "host": st.sidebar.text_input("MySQL Host name"),
            "user": st.sidebar.text_input("MySQL user"),
            "password": st.sidebar.text_input("MySQL Password", type="password"),
            "database": st.sidebar.text_input("MySQL Database")
        }
    else:
        return {"type": LOCALDB}

# Database connection function
@st.cache_resource(ttl="2h")
def get_database(config):
    if config["type"] == LOCALDB:
        db_path = (Path(__file__).parent / "student.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{db_path}?mode=rw", uri=True)
        return SQLDatabase(create_engine("sqlite://", creator=creator))
    elif config["type"] == MYSQL:
        connection_string = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
        return SQLDatabase(create_engine(connection_string))
    else:
        raise ValueError("Invalid database type")

def setup_agent(db, api_key):
    llm = ChatGroq(api_key=api_key, model="Llama-3.1-70b-Versatile", streaming=True)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    return create_sql_agent(
        llm,
        toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
    )

# Main application logic
def main():
    db_config = configure_database()
    groq_api_key = st.text_input("Groq API Key", type="password")

    if not groq_api_key:
        st.warning("Please enter your Groq API Key to continue.")
        return

    try:
        db = get_database(db_config)
    except Exception as e:
        st.error(f"Error connecting to database: {str(e)}")
        return

    agent = setup_agent(db, groq_api_key)

    # Chat interface
    if "messages" not in st.session_state or st.sidebar.button("Clear Message History"):
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_query = st.chat_input("Ask anything from the database")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)
        container = st.container()
        streamlit_callback = StreamlitCallbackHandler(container)
        try:
            response = agent.run(user_query, callbacks=[streamlit_callback])
            st.session_state.messages.append({"role": "assistant", "content": response})
            container.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()