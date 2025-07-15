import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from filtered_text_input.filtered_text_input import filtered_text_input
from streamlit.components.v1 import html

# --- Page Setup ---
st.set_page_config(page_title="Mini Offline GPT", page_icon="📵")


# --- Sidebar with Scroll and Headers ---
with st.sidebar:
    st.markdown("### 🔧 Controls")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    if st.button("⏹️ Stop"):
        st.stop()
    st.markdown("""
        <div style='height: 90vh; overflow-y: auto; padding-right: 10px;'>
            <h2>📌 Assistant Info</h2>
            <p>This AI remembers the last 5 conversation turns.</p>
            <h2>⚙️ Model Info</h2>
            <p>Running <strong>llama3.2:latest</strong> locally via Ollama.</p>
            <h2>👨‍💻 Developer Info </h2>
            <p>Developed by N. Lokeshraj, an ECE student from MSEC</p>  
        </div>
    """, unsafe_allow_html=True)

# Track if the user has submitted their first prompt
if "has_prompted" not in st.session_state:
    st.session_state.has_prompted = False

# Show intro content only if user hasn't prompted yet
if not st.session_state.has_prompted:
    st.markdown("<h1 style='text-align: center;'>Mini GPT</h1>",unsafe_allow_html=True)
    st.markdown(""" <p style ='text-align: center;'> I remember the last 5 turns of our conversation! Powered by `llama3.2:latest` via Ollama.</p>""",unsafe_allow_html=True)

# --- LLM Chain Setup ---
@st.cache_resource
def initialize_llm_chain():
    
    try:
        llm = Ollama(model="llama3.2:latest")

    except Exception as e:
        st.error(f"❌ Error connecting to Ollama: {e}")
        st.stop()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. You remember the last 5 turns of conversation."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])

    return prompt | llm | StrOutputParser()

chain = initialize_llm_chain()
if not st.session_state.has_prompted:      
    st.success("✅ Connected to Ollama")
# --- Session Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    

    
# --- Chat Display Area ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if st.session_state.has_prompted:
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# --- Custom Text Box (Always Bottom) ---
user_prompt = filtered_text_input("Ask Anything",key="filtered_input")


# --- Process User Input ---
if user_prompt:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.session_state.has_prompted = True

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Prepare 5-turn chat history (10 messages max)
    past = st.session_state.messages[:-1][-10:]
    history = [
        HumanMessage(content=m["content"]) if m["role"] == "user" else AIMessage(content=m["content"])
        for m in past
    ]

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                full_response = chain.invoke({
                    "input": user_prompt,
                    "chat_history": history
                })
                st.markdown(full_response)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
                full_response = "⚠️ Sorry, something went wrong."

   

    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    

