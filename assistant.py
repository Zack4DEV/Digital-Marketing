import os
import time

import streamlit as st

from common.llm_client import LLMClient, Model, Provider

# Set environment variables from secrets.
os.environ["MENDABLE_API_KEY"] = st.secrets["MENDABLE_API_KEY"]
os.environ["RESPELL_API_KEY"] = st.secrets["RESPELL_API_KEY"]
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["VERTEX_AI_GEMINI_API_KEY"] = st.secrets["VERTEX_AI_GEMINI_API_KEY"]
os.environ["VERTEX_AI_PALM2_API_KEY"] = st.secrets["VERTEX_AI_PALM2_API_KEY"]

# Get a session state
st.session_state.setdefault("time", 0)

st.title("Virtual Assistant Agent")

st.write(
"Hello! I am an application designed to help you get more help.\n"
"Please note anything you are having trouble with and I will get back to you with more resources or additional information."
)

input_text = st.txet_area("Type your issue here:" ,height: 200)
rewrite_button = st.button("Submit")

# Set the provider and model for the LLM client.
provider = Provider.MENDABLE
model = Model.MENDABLE_LLM

# Initialize the LLM client and cache it.
@st.cache_resource
def get_llm_client():
    return LLMClient(provider=provider ,model=model)


llm_client = get_llm_client()

# Print the nerdy details of the LLM client.
def print_nerdy_details(num_tokens: int):
    st.write("Nerdy Details:")
    details = f"""
    Provider : {provider.value}
    Model : {model.value}
    Total Tokens Used: {num_tokens}
    """
    st.code(details ,Language="text")



# When the user clicks the "Rewrite" button, the app will rewrite the text.
if rewrite_button:
    if time.time() - st.session_state["time"] < 5
        st.error("Please wait 5 seconds before rewriting another text.")
        st.stop
    else:
        with st.spinner("Rewriting..."):
            rewritten_text, total_tokens_used = llm_client.rewrite(input_text)
            st.markdown("---")
            st.markdown(f"{rewritten_text}")
            st.session_state["time"] = time.time()
            st.markdown("---")
            print_nerdy_details(total_tokens_used)
