import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend import chatbot, retrieve_all_threads
import uuid

#-------------------generate dynamic thread ID-------------------------------#
def genarate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id 

def reset_chat():
    thread_id = genarate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_threads(thread_id, "New Chat")
    st.session_state['message_history'] = []

def add_threads(thread_id, chat_name="New Chat"):
    if not any(t['id'] == thread_id for t in st.session_state['chat_threads']):
        st.session_state['chat_threads'].append({'id': thread_id, 'name': chat_name})

def load_conversations(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    # Check if messages key exists in state values, return empty list if not
    return state.values.get('messages', [])


#----------------------------------------------------------------------------#

# session state is used to have temporary memory in streamlit web
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = genarate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

add_threads(st.session_state['thread_id'])

# ------------------------------SideBar UI--------------------------------------------------#
st.sidebar.title('Chatbot using LangGraph')

if st.sidebar.button('New Conversations'):
    reset_chat()

st.sidebar.header('Conversations')

for thread in st.session_state['chat_threads'][::-1]:
    button_label = thread['name']
    if st.sidebar.button(button_label, key=f"thread_btn_{thread['id']}"):
        st.session_state['thread_id'] = thread['id']
        messages = load_conversations(thread['id'])

        temp_messages = []
        for msg in messages:
            role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages

#--------------------------------------------------------------------------------------------#

#loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



user_input = st.chat_input('Enter your prompt here...')

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    # Rename the chat if it's still "New Chat"
    for chat in st.session_state['chat_threads']:
        if chat['id'] == st.session_state['thread_id'] and chat['name'] == "New Chat":
            short_name = user_input[:10] + "..." if len(user_input) > 10 else user_input
            chat['name'] = short_name
            break

    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    with st.chat_message('assistant'):
        # st.text(ai_message)

        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
