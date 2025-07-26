# Free Chatbot Options with LangGraph

This folder contains 4 different chatbot implementations using free APIs and local models.

## 🚀 Quick Start Options

### 1. Simple Rule-Based Chatbot (Recommended for beginners)
**File**: `chatbot_simple.py`
- ✅ **No API key needed**
- ✅ **Works immediately**
- ✅ **No internet required**
- Uses pattern matching and predefined responses

**To run:**
```bash
python chatbot_simple.py
```

### 2. Ollama Local Chatbot (Best free option)
**File**: `chatbot_ollama.py`
- ✅ **Completely free**
- ✅ **Runs locally (private)**
- ✅ **High quality responses**
- Requires Ollama installation

**Setup:**
1. Install Ollama: https://ollama.ai
2. Install a model: `ollama pull llama2`
3. Run: `python chatbot_ollama.py`

### 3. Google Gemini Chatbot (Free tier)
**File**: `chatbot_gemini.py`
- ✅ **Free tier available**
- ✅ **High quality AI**
- 🔑 **Requires API key**

**Setup:**
1. Get free API key: https://ai.google.dev/
2. Install: `pip install google-generativeai`
3. Set environment variable: `export GEMINI_API_KEY=your_key`
4. Run: `python chatbot_gemini.py`

### 4. Hugging Face Transformers (Local AI)
**File**: `chatbot1.py` (modified)
- ✅ **Completely free**
- ✅ **Runs locally**
- ⚠️ **Large download first time**

**Setup:**
```bash
pip install transformers torch
python chatbot1.py
```

## 📋 Installation

```bash
# Basic requirements
pip install -r requirements_chatbot.txt

# For specific options, install additional packages as needed
```

## 🎯 Recommendations

1. **Start with**: `chatbot_simple.py` - Works immediately, no setup
2. **Best quality**: `chatbot_ollama.py` - Free, local, high-quality AI
3. **Cloud option**: `chatbot_gemini.py` - Good free tier from Google

## 🔧 Customization

Each chatbot can be customized by:
- Modifying the `process()` function
- Adding more nodes to the LangGraph
- Implementing conversation memory
- Adding different response patterns

## 🚀 Next Steps

- Add conversation memory
- Implement user authentication
- Add web interface with Streamlit/Gradio
- Connect to databases
- Add voice capabilities
