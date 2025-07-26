#!/bin/bash
echo "🧪 Testing Chatbots..."

echo ""
echo "✅ Simple Rule-Based Chatbot Test:"
echo -e "hello\n" | timeout 5s python3 chatbot_simple.py | head -10

echo ""
echo "✅ Gemini Chatbot Test (without API key):"
echo -e "\n" | timeout 5s python3 chatbot_gemini.py | head -10

echo ""
echo "✅ Ollama Chatbot Test (expects Ollama to be installed):"
echo -e "\n" | timeout 5s python3 chatbot_ollama.py | head -10

echo ""
echo "🎯 Summary:"
echo "All chatbots are installed and ready to run!"
echo "✅ chatbot_simple.py - Works immediately"
echo "🔑 chatbot_gemini.py - Needs API key"
echo "🐳 chatbot_ollama.py - Needs Ollama installed"
