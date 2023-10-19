import streamlit as st
import investmate_lib as glib

st.set_page_config(layout="wide", page_title="Invest Mate")
st.title("Upload a document and ask me anything about it")

if 'memory' not in st.session_state: #see if the memory hasn't been created yet
    st.session_state.memory = glib.get_memory() #initialize the memory

if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
    st.session_state.chat_history = [] #initialize the chat history
    

uploaded_file = st.file_uploader("Select a PDF", type=['pdf'])

upload_button = st.button("Upload", type="primary")

if upload_button:
    with st.spinner("Uploading..."):
        upload_response = glib.save_file(file_bytes=uploaded_file.getvalue())
        st.success(upload_response)        
        st.session_state.has_document = True
    with st.spinner("Indexing document..."): #show a spinner while the code in this with block runs
        st.session_state.vector_index = glib.get_index() #retrieve the index through the supporting library and store in the app's session cache
    st.session_state.chat_history = []

if 'has_document' in st.session_state: #see if document has been uploaded
    # if 'vector_index' not in st.session_state: #see if the vector index hasn't been created yet
    #     with st.spinner("Indexing document..."): #show a spinner while the code in this with block runs
    #         st.session_state.vector_index = glib.get_index() #retrieve the index through the supporting library and store in the app's session cache
        
    #Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
    for message in st.session_state.chat_history: #loop through the chat history
        with st.chat_message(message["role"]): #renders a chat line for the given role, containing everything in the with block
            st.markdown(message["text"]) #display the chat content



    input_text = st.chat_input("Chat with your bot here") #display a chat input box

    if input_text: #run the code in this if block after the user submits a chat message
        
        with st.chat_message("user"): #display a user chat message
            st.markdown(input_text) #renders the user's latest message
        
        st.session_state.chat_history.append({"role":"user", "text":input_text}) #append the user's latest message to the chat history
        
        chat_response = glib.get_rag_chat_response(input_text=input_text, memory=st.session_state.memory, index=st.session_state.vector_index,) #call the model through the supporting library
        
        with st.chat_message("assistant"): #display a bot chat message
            st.markdown(chat_response) #display bot's latest response
        
        st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) #append the bot's latest message to the chat history

