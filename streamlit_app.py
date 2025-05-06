import streamlit as st

# Shared Tailwind CSS classes
PRIMARY_COLOR = "bg-primary"
PRIMARY_TEXT_COLOR = "text-primary"
PRIMARY_FOREGROUND_COLOR = "text-primary-foreground"
BACKGROUND_COLOR = "bg-background"
DARK_MODE_PRIMARY_COLOR = "dark:bg-primary"
DARK_MODE_TEXT_COLOR = "dark:text-primary"
DARK_MODE_TEXT_FOREGROUND_COLOR = "dark:text-primary-foreground"
BUTTON_STYLE = "bg-primary-foreground text-primary px-4 py-2 rounded-lg m-2"

def influencer_dashboard():
    st.markdown(f'<div class="{PRIMARY_COLOR} min-h-screen {PRIMARY_TEXT_COLOR}">', unsafe_allow_html=True)
    st.markdown(f'<div class="{BACKGROUND_COLOR} {DARK_MODE_PRIMARY_COLOR} {DARK_MODE_TEXT_COLOR} {DARK_MODE_TEXT_FOREGROUND_COLOR}">', unsafe_allow_html=True)
    st.markdown('<h1 class="text-2xl font-bold p-4">Influencer Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<div class="flex justify-end mr-4">', unsafe_allow_html=True)
    st.markdown(f'<button class="{BUTTON_STYLE}">Campaigns</button>', unsafe_allow_html=True)
    st.markdown(f'<button class="{BUTTON_STYLE}">Analytics</button>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

influencer_dashboard()
