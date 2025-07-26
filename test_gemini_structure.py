from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
import google.generativeai as genai

class AgentState(TypedDict):
    messages: List[HumanMessage]

# Test with fake API key to show error handling
try:
    genai.configure(api_key="fake_key_for_testing")
    model = genai.GenerativeModel('gemini-pro')
    print("✅ Gemini API configured")
except Exception as e:
    print(f"❌ Error: {e}")
    model = None

def process(state: AgentState) -> AgentState:
    user_message = state["messages"][-1].content
    print(f"\n🤖 Gemini AI: Hello! You said: '{user_message}'")
    print("⚠️  This is a demo. For real AI responses, get a free API key from: https://ai.google.dev/")
    return state

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()

# Test it
print("🧪 Testing Gemini Chatbot Structure...")
agent.invoke({"messages": [HumanMessage(content="Hello, how are you?")]})
print("✅ Gemini chatbot structure is working correctly!")
