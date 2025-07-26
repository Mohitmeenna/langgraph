from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[HumanMessage]

# Get API key from environment or prompt user
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("🔑 Get your free Gemini API key from: https://ai.google.dev/")
    print("📋 Steps:")
    print("   1. Go to https://ai.google.dev/")
    print("   2. Click 'Get API key in Google AI Studio'")
    print("   3. Sign in with Google account")
    print("   4. Create new API key")
    print("   5. Copy the key")
    print("")
    api_key = input("Enter your Gemini API key (or press Enter to use demo mode): ").strip()

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Use the latest model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Gemini API connected successfully!")
    except Exception as e:
        print(f"❌ Error connecting to Gemini: {e}")
        print("🔧 This might be because:")
        print("   - Invalid API key")
        print("   - Network connection issue")
        print("   - API key doesn't have proper permissions")
        print("   - Model name might be incorrect")
        model = None
else:
    print("⚠️  Running in demo mode - AI responses will be simulated")
    model = None

def process(state: AgentState) -> AgentState:
    if not model:
        # Demo mode responses when no API key
        user_message = state["messages"][-1].content.lower()
        
        demo_responses = {
            "hello": "Hello! I'm a Gemini-powered chatbot. To unlock my full potential, please provide a Gemini API key!",
            "hi": "Hi there! I'd love to chat, but I need a Gemini API key to give you real AI responses.",
            "how are you": "I'm doing well in demo mode! Get a free API key from https://ai.google.dev/ to chat with the real Gemini AI.",
            "what is": "I can answer questions about anything when you provide a Gemini API key!",
            "tell me": "I'd be happy to tell you anything when connected to Gemini AI!"
        }
        
        # Find matching response
        response = "I'm running in demo mode. To chat with real Gemini AI, please get a free API key from https://ai.google.dev/"
        for key, demo_response in demo_responses.items():
            if key in user_message:
                response = demo_response
                break
                
        print(f"\nAI (Demo Mode): {response}")
        return state
    
    user_message = state["messages"][-1].content
    
    try:
        response = model.generate_content(user_message)
        ai_response = response.text
        print(f"\nAI: {ai_response}")
    except Exception as e:
        print(f"\nAI: Sorry, I encountered an error: {e}")
        print("🔧 Try:")
        print("   - Check your internet connection")
        print("   - Verify your API key is correct")
        print("   - Make sure you have API quota remaining")
    
    return state

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()

print("🤖 Gemini Chatbot - Type 'exit' to quit")
user_input = input("\nYou: ")
while user_input.lower() != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("\nYou: ")
