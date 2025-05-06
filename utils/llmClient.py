import streamlit as st

# Shared Tailwind CSS classes
BG_PRIMARY = "bg-primary"
TEXT_PRIMARY = "text-primary-foreground"
BG_SECONDARY = "bg-secondary"
TEXT_SECONDARY = "text-secondary-foreground"
BG_INPUT = "bg-input"
TEXT_INPUT = "text-input"
BG_CARD = "bg-card"
PRIMARY = "primary"
PRIMARY_80 = "primary/80"

def mendable_ai_chat():
    st.markdown(
        f"""
        <div class="bg-background text-foreground min-h-screen flex flex-col items-center justify-center">
            <div class="max-w-md w-full {BG_CARD} shadow-lg rounded-lg overflow-hidden">
                <div class="{BG_PRIMARY} {TEXT_PRIMARY} px-4 py-2">
                    <h1 class="text-lg font-bold">Mendable AI Chat</h1>
                </div>
                <div class="p-4">
                    <div class="flex flex-col space-y-2">
                        <div class="{BG_SECONDARY} {TEXT_SECONDARY} p-2 rounded-lg">
                            <p>Welcome to Mendable AI Chat! How can I assist you today?</p>
                        </div>
                        <div class="{BG_SECONDARY} {TEXT_SECONDARY} p-2 rounded-lg">
                            <p>Ask me anything about user experience, digital marketing, or any other topic.</p>
                        </div>
                    </div>
                </div>
                <div class="p-4">
                    <input type="text" placeholder="Type your message here..." class="w-full {BG_INPUT} {TEXT_INPUT} border border-{PRIMARY} rounded-lg p-2 focus:outline-none focus:ring ring-{PRIMARY}" />
                    <button class="{BG_PRIMARY} {TEXT_PRIMARY} w-full py-2 mt-2 rounded-lg hover:bg-{PRIMARY_80} focus:outline-none focus:ring ring-{PRIMARY}">Send</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

mendable_ai_chat()
