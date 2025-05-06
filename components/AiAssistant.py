import streamlit as st

# Shared Tailwind CSS classes
TW_BG = "bg-background"
TW_TEXT_PRIMARY = "text-primary-foreground"
TW_TEXT_SECONDARY = "text-secondary-foreground"
TW_CARD = "max-w-md w-full p-6 bg-card rounded-lg shadow-lg"
TW_INPUT = "w-full p-2 border border-input rounded-md mb-6 h-32 resize-none"
TW_BUTTON = "w-full py-2 bg-primary text-primary-foreground rounded-md mb-6 hover:bg-primary/80"
TW_SPINNER = "animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-primary"
TW_RESPONSE = "max-h-48 overflow-y-auto border border-input rounded-md p-2"

def virtual_assistant_component():
    st.markdown('<div class="{} text-primary-foreground min-h-screen flex items-center justify-center">'.format(TW_BG), unsafe_allow_html=True)
    with st.markdown('<div class="{}">'.format(TW_CARD), unsafe_allow_html=True):
        st.markdown('<h1 class="text-3xl font-bold mb-4">Virtual Assistant</h1>', unsafe_allow_html=True)
        st.markdown('<p class="{} mb-6">Hello! I am your digital marketing assistant. How can I help you today?</p>'.format(TW_TEXT_SECONDARY), unsafe_allow_html=True)
        st.text_area("", class_=TW_INPUT, placeholder="Type your question here...")
        st.button("Submit", class_=TW_BUTTON, disabled=True)
        with st.markdown('<div class="flex items-center justify-center mb-6">', unsafe_allow_html=True):
            st.markdown('<div class="{}"></div>'.format(TW_SPINNER), unsafe_allow_html=True)
        with st.markdown('<div class="{}">'.format(TW_RESPONSE), unsafe_allow_html=True):
            st.markdown('<p class="{}">Response text goes here...</p>'.format(TW_TEXT_PRIMARY), unsafe_allow_html=True)

virtual_assistant_component()
