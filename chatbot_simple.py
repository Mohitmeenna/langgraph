from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
import random
import re

class AgentState(TypedDict):
    messages: List[HumanMessage]

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! How are you doing?",
                "Hello! Nice to meet you!"
            ],
            'how_are_you': [
                "I'm doing great, thank you for asking!",
                "I'm well! How about you?",
                "I'm good! Thanks for asking.",
                "I'm fantastic! How are you?"
            ],
            'name': [
                "I'm a simple chatbot built with LangGraph!",
                "You can call me ChatBot. What's your name?",
                "I'm your friendly AI assistant!",
                "I'm just a simple chatbot here to help!"
            ],
            'help': [
                "I can chat with you about various topics!",
                "I'm here to have a conversation with you.",
                "Feel free to ask me anything or just chat!",
                "I can help answer questions or just talk!"
            ],
            'goodbye': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! It was nice chatting with you!",
                "Farewell! Hope to chat again soon!"
            ],
            'default': [
                "That's interesting! Tell me more.",
                "I see. Can you elaborate on that?",
                "Hmm, that's something to think about.",
                "I understand. What else would you like to discuss?",
                "That's a good point. What do you think about it?",
                "Interesting perspective! How did you come to that conclusion?",
                "I hear you. Is there anything specific you'd like to talk about?"
            ]
        }
        
        self.patterns = {
            'greeting': r'\b(hi|hello|hey|greetings)\b',
            'how_are_you': r'\b(how are you|how\'re you|how do you feel)\b',
            'name': r'\b(what\'s your name|who are you|what are you)\b',
            'help': r'\b(help|assist|support|what can you do)\b',
            'goodbye': r'\b(bye|goodbye|see you|farewell|exit)\b'
        }
    
    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower()
        
        for intent, pattern in self.patterns.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return random.choice(self.responses[intent])
        
        return random.choice(self.responses['default'])

# Initialize the chatbot
chatbot = SimpleChatbot()

def process(state: AgentState) -> AgentState:
    user_message = state["messages"][-1].content
    ai_response = chatbot.get_response(user_message)
    print(f"\nAI: {ai_response}")
    return state

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()

print("🤖 Simple Rule-Based Chatbot - Type 'exit' to quit")
print("💬 This chatbot uses pattern matching - no API required!")
print("🎯 Try: greetings, asking how I am, asking my name, asking for help")

user_input = input("\nYou: ")
while user_input.lower() not in ['exit', 'quit', 'bye']:
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("\nYou: ")

print("\n👋 Thanks for chatting! Goodbye!")
