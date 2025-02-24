import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import(
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom Styling for an Appealing Interface

st.markdown("""
<style>
    /* Base styles (kept all original classes and properties, enhanced appearance) */
    
    .main {
        /* Original: background-color: #1a1a1a; */
        /* Updated: subtle gradient for a sleeker look */
        background: linear-gradient(135deg, #1a1a1a 0%, #0F0F0F 100%);
        color: #ffffff;
        font-family: "Segoe UI", "Helvetica Neue", sans-serif;
    }

    .sidebar .sidebar-content {
        /* Original: background-color: #2d2d2d; */
        background: linear-gradient(135deg, #2d2d2d 0%, #232323 100%);
    }

    .stTextInput textarea {
        /* Original: color: #ffffff !important; */
        color: #ffffff !important;
        background-color: #2c2c2c !important;
        border: 1px solid #444444 !important;
        border-radius: 4px;
        font-family: inherit;
    }

    /* Selectbox enhancements */
    .stSelectbox div[data-baseweb="select"] {
        /* Original: color: white !important; background-color: #3d3d3d !important; */
        color: #ffffff !important;
        background-color: #3d3d3d !important;
        border: 1px solid #555555 !important;
        border-radius: 4px !important;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .stSelectbox svg {
        /* Original: fill: white !important; */
        fill: #ffffff !important;
    }

    .stSelectbox option {
        /* Original: background-color: #2d2d2d !important; color: white !important; */
        background-color: #2d2d2d !important;
        color: #ffffff !important;
    }

    /* For dropdown menu items */
    div[role="listbox"] div {
        /* Original: background-color: #2d2d2d !important; color: white !important; */
        background-color: #2d2d2d !important;
        color: #ffffff !important;
    }

</style>
""", unsafe_allow_html=True)

st.title("🔎 DeepSeek CodeXplorer")
st.caption("🚀 Your AI Pair Programmer with Next-Level Debugging Powers")

with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert
    - 🐞 Debugging Assistant
    - 📝 Code Documentation
    - 💡 Solution Design
    """)
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")
    
    
# Main Chat Engine

llm_engine = ChatOllama(
    model=selected_model,
    temperature=0.3,
    base_url="http://localhost:11434"
)

# System Prompt Configuration

system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an Expert AI assistant. Proivde consise, correct solutions"
    "with strategic print statements for debugging. Always respond in English."
)
    
# Session State Management

if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]
    
# Chat Container
chat_container =st.container()

# Display chat messages

with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
# Chat input and processing

user_query = st.chat_input("Type your coding question  here..")

def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate AI response
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Rerun to update chat display
    st.rerun()