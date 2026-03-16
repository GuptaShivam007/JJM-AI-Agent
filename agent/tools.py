from langchain.tools import Tool
import sqlite3

def query_database(question):
    conn = sqlite3.connect("database/jjm.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM water_data LIMIT 5"
    result = cursor.execute(query).fetchall()
    
    return result

tools = [
    Tool(
        name="JJM Database",
        func=query_database,
        description="Use this to answer questions about water coverage data"
    )
]