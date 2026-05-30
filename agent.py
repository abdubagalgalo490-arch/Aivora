import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()
api_key = os.getenv("GROQ_API_KEY") 
llm = ChatGroq(api_key=api_key,model="llama-3.3-70b-versatile")
system_prompt="""
you are Aivora, built by Galgalo.You are an intelligent AI Assistant.You are a helfull,consice and conversational """
messages =[SystemMessage(content=system_prompt)]
print("Welcome to Aivora, Type 'exit' to quit")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    messages.append(HumanMessage(content=user_input))
    response = llm.invoke(messages)
    print(f"Aivora: {response.content}")
    messages.append(AIMessage(content=response.content))