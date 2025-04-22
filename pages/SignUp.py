import streamlit as st
import boto3
import time
import uuid

# AWS DynamoDB Configuration
session = boto3.Session(region_name="us-east-1")
dynamodb = session.resource("dynamodb")
TABLE_NAME = "ProjectTable"

# Load Table
try:
    table = dynamodb.Table(TABLE_NAME)
    table.load()
except Exception as e:
    st.error(f"❌ Table {TABLE_NAME} does not exist. Create it first. Error: {e}")
    st.stop()

# Custom CSS for Styling
custom_css = """
<style>
    body {
        background-color: #1a1a1a !important;
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
    }
    /* Top Navigation Bar */
    .top-nav {
        width: 100%;
        background: linear-gradient(90deg, #2C3E50, #1a252f);
        padding: 15px 20px;
        text-align: center;
        border-bottom: 2px solid #ffcc00;
        box-sizing: border-box;
        position: relative;
    }
    .top-nav a {
        color: #ffffff;
        text-decoration: none;
        margin: 0 15px;
        font-weight: bold;
    }
    .top-nav a:hover {
        text-decoration: underline;
    }
    /* Sign Up Card */
    .signup-card {
        padding: 40px;
        max-width: 400px;
        margin: 100px auto 40px;  /* Adjust top margin to account for the nav bar */
        color: #ffffff;
    }
    .signup-card h1 {
        text-align: center;
        margin-bottom: 30px;
    }
    /* Input Styling */
    .signup-card .stTextInput>div>div>input {
        background-color: #2C3E50;
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 8px;
    }
    .signup-card .stTextInput>div>div>input:focus {
        border-color: #ffcc00;
    }
    .signup-card button {
        background-color: #ffcc00;
        color: #1a1a1a;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
        margin-top: 20px;
    }
    .signup-card button:hover {
        background-color: #e6b800;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Top Navigation Bar (Full Width)
st.markdown("""
<div class='top-nav'>
 <a href='/'>Home</a>
        <a href='/About'>About</a>
        <a href='/dashboard'>My Dashboard</a>
        <a href='/Features'>Features</a>
        <a href='/Login'>Login</a>
        <a href='/SignUp'>Sign Up</a>
</div>
""", unsafe_allow_html=True)

# Sign Up Card
st.markdown("<div class='signup-card'>", unsafe_allow_html=True)
st.title("📝 Sign Up")

username = st.text_input("👤 Username")
email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")
confirm_password = st.text_input("🔑 Confirm Password", type="password")

signup_button = st.button("🚀 Sign Up")

# Function to check if a user already exists (by email)
def get_user_by_email(email):
    response = table.query(
        IndexName="EmailIndex",
        KeyConditionExpression="email = :e",
        ExpressionAttributeValues={":e": email}
    )
    return response['Items'][0] if response['Items'] else None

# Sign Up Functionality
if signup_button:
    if password != confirm_password:
        st.error("❌ Passwords do not match!")
    elif get_user_by_email(email) is not None:
        st.error("❌ Email already exists. Please use a different email.")
    else:
        # Create a new user (Note: In production, store a hashed password!)
        user_id = str(uuid.uuid4())
        try:
            table.put_item(Item={
                "ID": user_id,
                "username": username,
                "email": email,
                "password": password
            })
            st.success("✅ Sign up successful! Redirecting to login page...")
            time.sleep(2)
            st.switch_page("login")  # Redirects to the login page
        except Exception as e:
            st.error(f"❌ Error creating account: {e}")

st.markdown("</div>", unsafe_allow_html=True)
