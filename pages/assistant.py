import time

import streamlit as st

from utils.llm_client import LLMClient

# Get a session state
st.session_state.setdefault("time", 0)

st.title("Virtual Assistant Agent")

st.write(
    "Hello! I am an application designed to help you get more help.\n"
    "Please note anything you are having trouble with and I will get back to you with more resources or additional information."
)

input_text = st.text_area("Type your issue here:", height=200)
rewrite_button = st.button("Submit")

# Initialize the LLM client and cache it.
@st.cache_resource
def get_llm_client():
    return LLMClient()  # No need for Provider and Model here

llm_client = get_llm_client()

# Print the nerdy details of the LLM client.
def print_nerdy_details(response):
    st.write("Nerdy Details:")
    if response:
        details = f"""
        Provider : {llm_client.ai_platform}
        Model : {llm_client.model if hasattr(llm_client, 'model') else 'N/A'}
        """
        st.code(details, language="text")

# When the user clicks the "Rewrite" button, the app will process the input.
if rewrite_button:
    if time.time() - st.session_state["time"] < 5:
        st.error("Please wait 5 seconds before submitting another request.")
        st.stop()
    else:
        with st.spinner("Processing..."):
            response = llm_client.query(input_text)
            if response:
                st.markdown("---")
                st.markdown(response)
                st.session_state["time"] = time.time()
                st.markdown("---")
                print_nerdy_details(response)
            else:
                st.error("Failed to get a response from the AI.")

if __name__ == "__main__":
    pass  # this file will be imported and not run directly.