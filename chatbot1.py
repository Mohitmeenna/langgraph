from typing import TypedDict, List
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")

class AgentState(TypedDict):
    messages: List[HumanMessage]
    conversation_history: str

# Initialize a free local LLM using Hugging Face
try:
    # Using a smaller, faster model that works well for chatbots
    chatbot = pipeline("text-generation", 
                      model="microsoft/DialoGPT-medium",
                      device=-1)  # Use CPU
    print("✅ Hugging Face model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    chatbot = None

def process(state: AgentState) -> AgentState:
    if not chatbot:
        print("\nAI: Sorry, the chatbot model is not available.")
        return state
    
    user_message = state["messages"][-1].content
    
    # Simple conversation using the local model
    try:
        # For DialoGPT, we need to format the conversation
        conversation = state.get("conversation_history", "")
        if conversation:
            prompt = f"{conversation}\nHuman: {user_message}\nAI:"
        else:
            prompt = f"Human: {user_message}\nAI:"
        
        # Generate response
        response = chatbot(prompt, 
                          max_length=len(prompt) + 50,
                          num_return_sequences=1,
                          temperature=0.7,
                          do_sample=True,
                          pad_token_id=50256)
        
        ai_response = response[0]['generated_text'][len(prompt):].strip()
        if not ai_response:
            ai_response = "I understand. Could you tell me more?"
        
        print(f"\nAI: {ai_response}")
        
        # Update conversation history
        new_history = f"{conversation}\nHuman: {user_message}\nAI: {ai_response}"
        state["conversation_history"] = new_history
        
    except Exception as e:
        print(f"\nAI: Sorry, I encountered an error: {e}")
    
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()

print("🤖 Simple Free Chatbot - Type 'exit' to quit")
user_input = input("\nYou: ")
while user_input.lower() != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)], "conversation_history": ""})
    user_input = input("\nYou: ")