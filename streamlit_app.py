import streamlit as st

# st.css Function Only Nightly Builds
with open('assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

# Shared Tailwind classes
TAILWIND_CLASSES = {
    'button_base': 'px-6 py-3 rounded-lg hover:shadow-md transition-all duration-300 ease-in-out',
    'text_alignment': 'text-center',
    'grid_layout': 'grid grid-cols-1 md:grid-cols-2 gap-6'
}

def custom_button(text, color, foreground_color, icon=None):
    """Helper function to create buttons with consistent styling and optional icons"""
    button_content = f"{icon + ' ' if icon else ''}{text}"
    return st.button(
        button_content,
        use_column_width=True,
        key=text,
        style=f"background-color: {color}; color: {foreground_color}; {TAILWIND_CLASSES['button_base']}"
    )

def primary_buttons():
    """Create primary action buttons with icons and vibrant colors"""
    col1, col2 = st.columns(2)
    with col1:
        custom_button("Get Started", "#4CAF50", "#ffffff", icon="🚀")  # Green
    with col2:
        custom_button("Explore Features", "#2196F3", "#ffffff", icon="🔍")  # Blue

def secondary_buttons():
    """Create secondary action buttons with softer tones"""
    col1, col2 = st.columns(2)
    with col1:
        custom_button("Discover Insights", "#9C27B0", "#ffffff", icon="💡")  # Purple
    with col2:
        custom_button("Enterprise Solutions", "#FF9800", "#ffffff", icon="💼")  # Orange

def accent_buttons():
    """Create accent action buttons with bold colors"""
    col1, col2 = st.columns(2)
    with col1:
        custom_button("Join Our Network", "#E91E63", "#ffffff", icon="🤝")  # Pink
    with col2:
        custom_button("Maximize Growth", "#607D8B", "#ffffff", icon="📈") # Blue Grey

def email_form():
    """Create email subscription form with modern styling"""
    with st.form(key="email_form"):
        email = st.text_input(
            "Enter your email",
            placeholder="Your professional email",
            type="email",
            label="Stay Updated",
            value="",
            classes="bg-white p-3 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors",
        )
        st.form_submit_button("Subscribe", type="primary", use_container_width=True)

def main():
    st.markdown(f"<body class='bg-gradient-to-r from-indigo-100 to-purple-100 text-gray-800 p-8 flex flex-col items-center justify-center min-h-screen'>", unsafe_allow_html=True)

    st.markdown("<h1 class='text-4xl font-extrabold mb-6 text-center text-indigo-800'>Elevate Your Marketing Strategy</h1>", unsafe_allow_html=True)

    st.markdown("<p class='text-center mb-8 text-lg text-gray-700'>Unlock strategic insights and propel your business forward with our expert marketing solutions.</p>", unsafe_allow_html=True)

    primary_buttons()

    st.markdown("<div class='my-10 border-t border-gray-300 w-full'></div>", unsafe_allow_html=True)

    st.markdown("<p class='text-center mb-6 text-gray-600'>Drive innovation and creativity with our tailored marketing strategies.</p>", unsafe_allow_html=True)

    secondary_buttons()

    st.markdown("<div class='my-10 border-t border-gray-300 w-full'></div>", unsafe_allow_html=True)

    st.markdown("<p class='text-center mb-6 text-gray-600'>Build your digital empire with our comprehensive marketing tools.</p>", unsafe_allow_html=True)

    accent_buttons()

    st.markdown("<div class='my-10 border-t border-gray-300 w-full'></div>", unsafe_allow_html=True)

    st.markdown("<p class='text-center mb-6 text-gray-600'>Explore our curated content and learn from industry leaders.</p>", unsafe_allow_html=True)

    custom_button("Stay Informed", "#7E57C2", "#ffffff", icon="📧") # Deep Purple

    email_form()

    st.markdown("<div class='mt-12 text-center text-gray-500'>© 2024 All rights reserved.</div>", unsafe_allow_html=True)

    st.markdown("<div class='text-center text-gray-500'>Powered by Innovation</div>", unsafe_allow_html=True)

    st.markdown("</body>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()