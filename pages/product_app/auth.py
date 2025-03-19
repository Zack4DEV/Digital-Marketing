import streamlit as st
import hashlib
from utils.db_client import DatabaseClient

# Initialize the database client
db_client = DatabaseClient(migrate=True)  # Ensure migrations run

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    """Registers a new user."""
    password_hash = hash_password(password)
    query = "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)"
    try:
        db_client.execute_insert(query, (username, email, password_hash))
        return True
    except Exception as e:
        st.error(f"Registration failed: {e}")
        return False

def authenticate_user(username, password):
    """Authenticates a user."""
    password_hash = hash_password(password)
    query = "SELECT id FROM users WHERE username = ? AND password_hash = ?"
    result = db_client.execute_query(query, (username, password_hash))
    if result is not None and not result.empty:
        return result.iloc[0]['id']  # Return user ID
    else:
        return None

def login_page():
    """Displays the login page."""
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user_id = authenticate_user(username, password)
        if user_id:
            st.session_state['user_id'] = user_id
            st.success("Logged in successfully!")
            st.experimental_rerun() # Rerun the app to show the changes.
        else:
            st.error("Invalid username or password.")

def register_page():
    """Displays the registration page."""
    st.title("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(username, email, password):
            st.success("Registration successful! Please log in.")
            st.experimental_rerun() # Rerun the app to show the changes.

def logout():
    """Logs out the user."""
    if 'user_id' in st.session_state:
        del st.session_state['user_id']
        st.success("Logged out successfully!")
        st.experimental_rerun()

def check_authentication():
    """Checks if the user is authenticated."""
    return 'user_id' in st.session_state

def get_user_id():
    """Gets the current user's ID."""
    if check_authentication():
        return st.session_state['user_id']
    else:
        return None