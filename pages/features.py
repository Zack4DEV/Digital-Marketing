import streamlit as st

def features_page():
    """Displays the features page."""

    st.title("Our Amazing Features")

    st.markdown("""
    <p>Explore the powerful features that make our application stand out.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Feature 1: Text Rewriting
    st.header("Text Rewriting")
    st.markdown("""
    <p>Our intelligent text rewriting feature helps you improve your writing by providing alternative phrasing and enhancing clarity.</p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Enhance clarity and conciseness</li>
        <li>Generate different writing styles</li>
        <li>Correct grammatical errors</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Feature 2: Personalized Assistance
    st.header("Personalized Assistance")
    st.markdown("""
    <p>Get tailored assistance based on your specific needs and challenges. Our application learns and adapts to provide relevant support.</p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Customized recommendations</li>
        <li>Real-time support and guidance</li>
        <li>Resource suggestions based on your issues</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Feature 3: Token Usage Tracking
    st.header("Token Usage Tracking")
    st.markdown("""
    <p>Keep track of your token usage with detailed insights into the number of tokens consumed by each operation.</p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Detailed token usage reports</li>
        <li>Optimize your usage and costs</li>
        <li>Transparent and easy-to-understand metrics</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Feature 4: Multi-Provider Support
    st.header("Multi-Provider Support")
    st.markdown("""
    <p>Our application supports multiple LLM providers, allowing you to choose the best model for your needs.</p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Flexibility to switch between providers</li>
        <li>Access to a wide range of models</li>
        <li>Compare performance and costs</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Feature 5: User-Friendly Interface
    st.header("User-Friendly Interface")
    st.markdown("""
    <p>Enjoy a seamless and intuitive user experience with our clean and easy-to-navigate interface.</p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Simple and intuitive design</li>
        <li>Easy navigation</li>
        <li>Quick access to all features</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Add more features as needed
    st.markdown("""
    <p>And much more to come!</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    features_page()