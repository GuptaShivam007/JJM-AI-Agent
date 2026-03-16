import requests
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def ask_agent(question):

    prompt = f"""
    You are an AI assistant analyzing Jal Jeevan Mission water supply data.

    Question: {question}

    Give a clear answer.
    """

    response = llm.invoke(prompt)
    # send log to API
    requests.post(
        "http://127.0.0.1:8000/log",
        json={"question": question, "answer": response}
    )

    return response
