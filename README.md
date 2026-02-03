# 🤖 Conversational Knowledge Bot (Gemini API)

## 📌 Project Overview

The **Conversational Knowledge Bot** is an intelligent, API-driven chatbot application designed to provide contextual, accurate, and interactive responses to user queries. Built using **Google Gemini API** and **Streamlit**, the system supports multi-turn conversations, maintains conversational context, and retrieves external information when required. The project demonstrates the practical application of generative AI for building modern knowledge-based conversational systems.


## 🧠 Key Features

* Context-aware multi-turn conversation handling
* Integration with **Google Gemini API** using secure API keys
* Session-based conversational memory
* External knowledge retrieval using web search
* Interactive and visually enhanced Streamlit chat interface
* Lightweight, modular, and platform-independent design


## 🏗️ System Architecture

The system follows a modular architecture to ensure scalability and maintainability.

### **Architecture Components**

1. **User Interface (Streamlit)**

   * Provides a web-based chat interface
   * Captures user input and displays responses
   * Manages session-based conversation history

2. **Conversation Handler**

   * Constructs prompts using user input and conversation history
   * Passes context to the language model for coherent responses

3. **LLM Integration (Gemini API)**

   * Uses Google Gemini models for natural language understanding and generation
   * Authenticated via API keys stored securely as environment variables

4. **External Knowledge Module**

   * Retrieves relevant information using web search when required
   * Enhances factual accuracy of responses

5. **Error Handling & Rate Control**

   * Gracefully handles API quota limits and runtime errors

### **Architecture Flow**

```
User → Streamlit UI → Prompt Builder (with Context)
     → Gemini API → Response Generation
     → Streamlit UI (Display Output)
```


## 🛠️ Setup Instructions

### **1. Prerequisites**

* Python 3.9 or higher
* Internet connection
* Google Gemini API key


### **2. Clone the Repository**

```bash
cd Soulpage-genai-assignment-saiarchan
```


### **3. Create and Activate Virtual Environment**

bash
python -m venv venv
```

**Windows**

bash
venv\Scripts\activate
```

**Linux / macOS**

bash
source venv/bin/activate


### **4. Install Dependencies**

bash
pip install -r requirements.txt
```


### **5. Set Gemini API Key**

**Windows (CMD – Permanent)**

bash
setx GOOGLE_API_KEY "your_api_key_here"


Restart the terminal after setting the key.

Verify:

bash
echo %GOOGLE_API_KEY%



### **6. Run the Application**

bash
streamlit run app.py


The application will open in your default web browser.



## 💬 Example Usage

### **Sample Conversation**


User: ceo of Google?
Bot: The CEO of Google is Sundar Pichai.



### **Context Awareness**


User: What is Generative AI?
Bot: Generative AI refers to models that can generate text, images, or other data.

User: Suggest a project related to it.
Bot: A conversational knowledge bot with memory and tool integration would be a great project.




## 📂 Project Structure


Soulpage-genai-assignment-saiarchan/
│
├── app.py                # Streamlit UI
├── bot.py                # Gemini API interaction & logic
├── tools.py              # Web search utility
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation


## 🚀 Future Enhancements

* Vector-based long-term memory (FAISS)
* Multi-agent collaboration
* Model fallback and load balancing
* Cloud deployment (Streamlit Cloud / Docker)
* User authentication and personalization



## 📜 Conclusion

This project showcases how modern generative AI models can be effectively integrated into real-world applications using APIs and lightweight frameworks. The Conversational Knowledge Bot serves as a strong foundation for building scalable, intelligent, and user-friendly conversational systems.


