# 🦜️LangChain: Chat with SQL DB

This Streamlit application allows users to interact with SQL databases using natural language queries. It leverages the power of LangChain and Groq's language models to interpret user questions and generate appropriate SQL queries.

## Features

- Support for both SQLite and MySQL databases
- Natural language interface for querying databases
- Integration with Groq's LLM for advanced language understanding
- Streamlit-based user interface for easy interaction
- Real-time streaming of AI responses

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.7+
- A Groq API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/NastyRunner13/LangChain-ChatSQL.git
   cd LangChain-ChatSQL
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. In the sidebar, choose your database type:
   - For SQLite: Select "Use SQLite 3 Database - Student.db"
   - For MySQL: Select "Connect to your SQL Database" and fill in the required connection details

4. Enter your Groq API key in the text input field.

5. Start chatting with your database using natural language queries!

## How it Works

1. The app sets up a Streamlit interface for user interaction.
2. Users can select their database type (SQLite or MySQL) and provide necessary connection details.
3. The application uses LangChain to create an SQL agent with the Groq language model.
4. User queries are processed by the agent, which generates appropriate SQL queries.
5. Results are fetched from the database and presented to the user in a conversational format.

## Customization

- To use a different SQLite database, replace the `student.db` file in the project directory.
- For other SQL database types, modify the `get_database` function to support additional connection methods.

## Troubleshooting

- If you encounter database connection issues, double-check your connection details and ensure your database server is running and accessible.
- For API-related errors, verify that your Groq API key is correct and has the necessary permissions.

## Contributing

Contributions to improve the application are welcome! Please feel free to submit issues or pull requests.

For more information about the libraries used in this project, check out:
- [LangChain](https://python.langchain.com/docs/get_started/introduction.html)
- [Streamlit](https://docs.streamlit.io/)
- [Groq](https://groq.com/)
