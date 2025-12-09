import streamlit as st
import google.generativeai as genai
from datetime import datetime
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="ProductiBot - Your AI Productivity Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (same as before)
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1F618D;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #566573;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #E8F8F5;
        border-left: 4px solid #1ABC9C;
    }
    .bot-message {
        background-color: #EBF5FB;
        border-left: 4px solid #3498DB;
    }
    .stats-box {
        background-color: #1F618D;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #D5D8DC;
    }
    .task-item {
        background-color: #FDFEFE;
        padding: 0.8rem;
        border-radius: 8px;
        border-left: 3px solid #F39C12;
        margin-bottom: 0.5rem;
    }
    .task-completed {
        background-color: #D5F4E6;
        border-left: 3px solid #27AE60;
        text-decoration: line-through;
        opacity: 0.7;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'conversation_count' not in st.session_state:
    st.session_state.conversation_count = 0
if 'api_configured' not in st.session_state:
    st.session_state.api_configured = False

# Try to load API key from environment
env_api_key = os.getenv('GEMINI_API_KEY')

# System Prompt for ProductiBot
SYSTEM_PROMPT = """You are ProductiBot, an enthusiastic and helpful AI productivity assistant. Your personality:

- Friendly, motivational, and encouraging
- Use emojis occasionally to make conversations engaging (but not excessively)
- Provide actionable, practical advice
- Be concise but comprehensive
- Remember context from previous messages in the conversation

Your core capabilities:
1. 📝 Task Management: Help users organize, prioritize, and track tasks
2. ⏰ Time Management: Provide tips on time blocking, Pomodoro technique, deep work, etc.
3. 🎯 Goal Setting: Use SMART goals framework (Specific, Measurable, Achievable, Relevant, Time-bound)
4. 💡 Productivity Tips: Share best practices, techniques, and productivity hacks
5. 🌟 Motivation: Encourage users, celebrate their progress, and help overcome procrastination

Guidelines for responses:
- Ask clarifying questions when needed to understand the user's situation better
- Provide structured responses for complex topics (but use prose, not bullet points unless asked)
- Suggest specific, actionable steps the user can take immediately
- Be empathetic and understanding of challenges
- Reference established productivity frameworks when relevant (GTD, Eisenhower Matrix, etc.)
- Adapt your tone based on the user's needs (more serious for work, lighter for personal tasks)

Current date and time: {datetime}
"""

def configure_gemini(api_key):
    """Configure Gemini API with the provided key"""
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"❌ Error configuring API: {str(e)}")
        return False

def generate_response(messages, temperature, max_tokens, top_p):
    """Generate response from Gemini"""
    try:
        model = genai.GenerativeModel(
            'gemini-pro',
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
                top_p=top_p,
            )
        )
        
        # Prepare conversation history
        context_messages = []
        for msg in messages[-10:]:  # Last 10 messages for context
            context_messages.append(f"{msg['role'].capitalize()}: {msg['content']}")
        
        conversation_context = "\n".join(context_messages)
        
        # Create full prompt
        full_prompt = SYSTEM_PROMPT.format(
            datetime=datetime.now().strftime("%A, %B %d, %Y at %H:%M")
        )
        full_prompt += f"\n\nConversation History:\n{conversation_context}\n\nRespond naturally to the user's latest message."
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")

# Sidebar Configuration
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    
    # API Key input (with fallback to env variable)
    if env_api_key:
        api_key = env_api_key
        st.success("✅ API Key loaded from .env file")
        st.session_state.api_configured = True
    else:
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            help="Enter your Google Gemini API key or set it in .env file"
        )
        
        if api_key:
            if configure_gemini(api_key):
                st.session_state.api_configured = True
                st.success("✅ API Key configured!")
    
    if st.session_state.api_configured and not env_api_key:
        genai.configure(api_key=api_key)
    
    st.markdown("---")
    
    # Model Configuration
    st.markdown("### 🎛️ Model Settings")
    
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher = more creative, Lower = more focused"
    )
    
    max_tokens = st.slider(
        "Max Tokens",
        min_value=256,
        max_value=2048,
        value=1024,
        step=256,
        help="Maximum length of response"
    )
    
    top_p = st.slider(
        "Top P",
        min_value=0.1,
        max_value=1.0,
        value=0.95,
        step=0.05,
        help="Diversity of word choice"
    )
    
    st.markdown("---")
    
    # Statistics
    st.markdown("### 📊 Session Statistics")
    st.markdown(f"""
    <div class="stats-box">
        <p>💬 <strong>Conversations:</strong> {st.session_state.conversation_count}</p>
        <p>✅ <strong>Tasks Created:</strong> {len(st.session_state.tasks)}</p>
        <p>📝 <strong>Messages:</strong> {len(st.session_state.messages)}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Actions
    st.markdown("### 🎯 Quick Actions")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Tasks", use_container_width=True):
            st.session_state.show_tasks = not st.session_state.get('show_tasks', False)
    
    with col2:
        if st.button("🗑️ Clear", use_container_width=True):
            if st.session_state.messages:
                st.session_state.messages = []
                st.session_state.conversation_count = 0
                st.rerun()
    
    if st.button("💾 Export Chat", use_container_width=True):
        if st.session_state.messages:
            chat_export = {
                "export_date": datetime.now().isoformat(),
                "messages": st.session_state.messages,
                "tasks": st.session_state.tasks,
                "stats": {
                    "conversation_count": st.session_state.conversation_count,
                    "total_messages": len(st.session_state.messages)
                }
            }
            
            # Create exports directory if not exists
            os.makedirs('exports', exist_ok=True)
            
            filename = f"productibot_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            st.download_button(
                label="📥 Download JSON",
                data=json.dumps(chat_export, indent=2),
                file_name=filename,
                mime="application/json",
                use_container_width=True
            )
        else:
            st.warning("No chat to export!")
    
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.8rem; color: #7F8C8D;">
    <p><strong>💡 Tips:</strong></p>
    <ul>
        <li>Be specific in your questions</li>
        <li>Provide context for better advice</li>
        <li>Use follow-up questions</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Main Content
st.markdown('<p class="main-header">🚀 ProductiBot</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your AI-Powered Productivity Assistant</p>', unsafe_allow_html=True)

# Check API configuration
if not st.session_state.api_configured:
    st.warning("⚠️ Please configure your Gemini API Key to start chatting!")
    
    st.info("""
    ### How to get started:
    
    1. Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
    2. Either:
       - Enter it in the sidebar, OR
       - Create a `.env` file with `GEMINI_API_KEY=your_key_here`
    3. Start chatting!
    """)
    
    # Feature showcase
    st.markdown("### ✨ What I Can Help You With:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📝 Task Management
        - Organize your to-dos
        - Prioritize tasks
        - Break down complex projects
        - Track progress
        """)
    
    with col2:
        st.markdown("""
        #### ⏰ Time Management
        - Pomodoro technique
        - Time blocking
        - Schedule optimization
        - Avoid procrastination
        """)
    
    with col3:
        st.markdown("""
        #### 🎯 Goal Setting
        - SMART goals framework
        - Action planning
        - Milestone tracking
        - Motivation & accountability
        """)
    
    st.markdown("---")
    st.markdown("### 💬 Example Questions:")
    
    example_col1, example_col2 = st.columns(2)
    with example_col1:
        st.markdown("""
        - "Help me organize my tasks for this week"
        - "How can I stop procrastinating?"
        - "What's the Pomodoro technique?"
        """)
    with example_col2:
        st.markdown("""
        - "Create a SMART goal for learning Python"
        - "I have 5 deadlines, help me prioritize"
        - "Tips for staying focused while working from home"
        """)

else:
    # Chat Interface
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        if not st.session_state.messages:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #7F8C8D;">
                <h3>👋 Hi! I'm ProductiBot</h3>
                <p>Ask me anything about productivity, tasks, time management, or goals!</p>
            </div>
            """, unsafe_allow_html=True)
        
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]
            timestamp = message.get("timestamp", "")
            
            if role == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>You</strong> <span style="color: #95A5A6; font-size: 0.85rem;">{timestamp}</span><br>
                    {content}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message bot-message">
                    <strong>🤖 ProductiBot</strong> <span style="color: #95A5A6; font-size: 0.85rem;">{timestamp}</span><br>
                    {content}
                </div>
                """, unsafe_allow_html=True)
    
    # Task Viewer
    if st.session_state.get('show_tasks', False):
        st.markdown("---")
        st.markdown("### 📋 Your Tasks")
        
        if st.session_state.tasks:
            for idx, task in enumerate(st.session_state.tasks):
                task_class = "task-completed" if task.get('status') == 'completed' else ""
                
                col1, col2, col3 = st.columns([0.5, 5, 1])
                
                with col1:
                    st.markdown(f"**#{task['id']}**")
                
                with col2:
                    st.markdown(f"""
                    <div class="task-item {task_class}">
                        {task['description'][:150]}{'...' if len(task['description']) > 150 else ''}
                        <br><span style="font-size: 0.8rem; color: #7F8C8D;">
                        Created: {datetime.fromisoformat(task['created_at']).strftime('%Y-%m-%d %H:%M')}
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    if task.get('status') != 'completed':
                        if st.button("✓", key=f"complete_{idx}"):
                            st.session_state.tasks[idx]['status'] = 'completed'
                            st.rerun()
                    else:
                        st.markdown("✅")
        else:
            st.info("📝 No tasks yet! Mention tasks in your conversation and I'll track them for you.")
    
    # Chat Input
    user_input = st.chat_input("💬 Type your message here...")
    
    if user_input:
        timestamp = datetime.now().strftime("%H:%M")
        
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": timestamp
        })
        st.session_state.conversation_count += 1
        
        # Generate response
        with st.spinner("🤔 Thinking..."):
            try:
                bot_response = generate_response(
                    st.session_state.messages,
                    temperature,
                    max_tokens,
                    top_p
                )
                
                # Extract tasks (simple keyword detection)
                task_keywords = ['task', 'todo', 'remind', 'need to', 'have to', 'must', 'deadline']
                if any(keyword in user_input.lower() for keyword in task_keywords):
                    task = {
                        "id": len(st.session_state.tasks) + 1,
                        "description": user_input,
                        "created_at": datetime.now().isoformat(),
                        "status": "pending"
                    }
                    st.session_state.tasks.append(task)
                
                # Add bot response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_response,
                    "timestamp": datetime.now().strftime("%H:%M")
                })
                
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Try rephrasing your question or check your API key.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7F8C8D; font-size: 0.85rem; padding: 1rem;">
    <p><strong>ProductiBot v1.0</strong> | Built with Streamlit & Google Gemini AI</p>
    <p>🎓 Final Project - LLM-Based Tools and Gemini API Integration</p>
</div>
""", unsafe_allow_html=True)