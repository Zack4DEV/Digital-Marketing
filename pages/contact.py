import streamlit as st

def contact_page():
    """Displays the contact page with a contact form."""

    st.title("Contact Us")

    st.markdown("""
    <p>We'd love to hear from you! Please fill out the form below to get in touch.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    with st.form(key="contact_form"):
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email")
        subject = st.text_input("Subject", placeholder="Enter the subject")
        message = st.text_area("Message", placeholder="Enter your message", height=200)

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Here, you would typically add code to send the email.
            # For demonstration purposes, we'll just display a success message.
            if name and email and message :
                st.success("Thank you for your message! We will get back to you soon.")
                # You can add code to send the form data via email or store it in a database.
                # Example (replace with your actual email sending logic):
                # send_email(name, email, subject, message)
            else:
                st.error("Please fill in all fields.")

    st.markdown("---")

    st.header("Our Address")
    st.markdown("""
    <p>123 Main Street<br>
    Anytown, State, 12345<br>
    Country</p>
    """, unsafe_allow_html=True)

    st.header("Email")
    st.markdown("""
    <p><a href="mailto:contact@example.com">contact@example.com</a></p>
    """, unsafe_allow_html=True)

    st.header("Phone")
    st.markdown("""
    <p>+1 (123) 456-7890</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.header("Follow Us")
    st.markdown("""
    <p>
        <a href="https://www.facebook.com/example" target="_blank">Facebook</a> |
        <a href="https://twitter.com/example" target="_blank">Twitter</a> |
        <a href="https://www.linkedin.com/company/example" target="_blank">LinkedIn</a>
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    contact_page()