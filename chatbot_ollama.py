from typing import TypedDict, List
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
import requests
import json

class AgentState(TypedDict):
    messages: List[HumanMessage]

def check_ollama():
    """Check if Ollama is running and what models are available"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json().get("models", [])
            if models:
                print("✅ Ollama is running! Available models:")
                for model in models:
                    print(f"  - {model['name']}")
                return models[0]['name']  # Return first available model
            else:
                print("⚠️  Ollama is running but no models found. Install a model with: ollama pull llama2")
        return None
    except:
        print("❌ Ollama not found. Install it from: https://ollama.ai")
        return None

# Check for available model
model_name = check_ollama()

def process(state: AgentState) -> AgentState:
    if not model_name:
        print("\nAI: Ollama is not available. Please install and run Ollama.")
        return state
    
    user_message = state["messages"][-1].content
    
    try:
        # Call Ollama API
        payload = {
            "model": model_name,
            "prompt": user_message,
            "stream": False
        }
        
        response = requests.post("http://localhost:11434/api/generate", 
                               json=payload)
        
        if response.status_code == 200:
            ai_response = response.json().get("response", "I'm not sure how to respond.")
            print(f"\nAI: {ai_response}")
        else:
            print(f"\nAI: Error: {response.status_code}")
            
    except Exception as e:
        print(f"\nAI: Sorry, I encountered an error: {e}")
    
    return state

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()

print("🤖 Ollama Chatbot - Type 'exit' to quit")
print("📋 To install Ollama: https://ollama.ai")
print("📋 To install a model: ollama pull llama2")

user_input = input("\nYou: ")
while user_input.lower() != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("\nYou: ")
