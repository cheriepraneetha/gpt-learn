import streamlit as st
import boto3
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# AWS DynamoDB Configuration
session = boto3.Session(region_name="us-east-1")
dynamodb = session.resource("dynamodb")
TABLE_NAME = "ProjectTable"
EMAIL_INDEX = "EmailIndex"

# Load Table
try:
    table = dynamodb.Table(TABLE_NAME)
    table.load()
except Exception as e:
    st.error(f"❌ Table {TABLE_NAME} does not exist. Create it first. Error: {e}")
    st.stop()

# Wait for Global Secondary Index (GSI)
def wait_for_gsi():
    while True:
        try:
            table.reload()
            indexes = [idx["IndexName"] for idx in table.global_secondary_indexes]
            if EMAIL_INDEX in indexes:
                return
        except:
            pass
        time.sleep(5)

wait_for_gsi()

# User Session Management
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.username = None
    st.session_state.email = None
    st.session_state.preferences_saved = False
    st.session_state.otp = None

# Hardcoded SendGrid API Key (Replace with your actual API key)
SENDGRID_API_KEY = st.secrets["SENDGRID_API_KEY"]
# Send OTP Email using SendGrid
def send_otp_email(recipient_email, otp):
    message = Mail(
        from_email='cheriepraneetha@gmail.com',
        to_emails=recipient_email,
        subject='Your OTP for Password Reset',
        html_content=f'<strong>Your OTP is: {otp}</strong>'
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        if response.status_code in [200, 202]:
            st.success("✅ OTP sent to your email!")
        else:
            st.error("❌ Failed to send OTP email. Please try again later.")
    except Exception as e:
        st.error(f"❌ Error sending OTP: {e}")

# Custom CSS for Styling
custom_css = """
<style>
    body {
        background-color: #1a1a1a !important;
        font-family: 'Arial', sans-serif;
    }
    /* Top Navigation Bar */
    .top-nav {
        background: linear-gradient(90deg, #2C3E50, #1a252f);
        padding: 15px 20px;
        text-align: center;
        border-bottom: 2px solid #ffcc00;
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
    /* Login Card - No background, border, or shadow */
    .login-card {
        padding: 40px;
        max-width: 400px;
        margin: 40px auto;
        color: #ffffff;
    }
    .login-card h1 {
        text-align: center;
        margin-bottom: 30px;
    }
    /* Input Styling */
    .login-card .stTextInput>div>div>input {
        background-color: #2C3E50;
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 8px;
    }
    .login-card .stTextInput>div>div>input:focus {
        border-color: #ffcc00;
    }
    .login-card button {
        background-color: #ffcc00;
        color: #1a1a1a;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
    }
    .login-card button:hover {
        background-color: #e6b800;
    }
    /* Forgot Password Section - Also without extra box styling */
    .forgot-section {
        margin-top: 30px;
        padding: 20px;
        color: #ffffff;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Top Navigation Bar
st.markdown("""
<div class='top-nav'>
 <a href='/'>Home</a>
        <a href='/About'>About</a>
        <a href='/dashboard'>My Dashboard</a>
        <a href='/Features'>Features</a>
        <a href='/Login'>Login</a>
        <a href='/SignUp'>Sign Up</a>
""", unsafe_allow_html=True)

# Login Card
st.markdown("<div class='login-card'>", unsafe_allow_html=True)
st.title("🔐 Login")

email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")

col1, col2 = st.columns(2)
login_button = col1.button("🚀 Login")
forgot_password_button = col2.button("❓ Forgot Password")

# Function to get user data from DynamoDB
def get_user(email):
    response = table.query(
        IndexName=EMAIL_INDEX,
        KeyConditionExpression="email = :e",
        ExpressionAttributeValues={":e": email}
    )
    return response['Items'][0] if response['Items'] else None

# Login Functionality
if login_button:
    user = get_user(email)
    if user and user["password"] == password:
        st.session_state.user_id = user["ID"]
        st.session_state.username = user["username"]
        st.session_state.email = email
        st.success(f"✅ Logged in as {user['username']}")
        # Redirect to Home/Dashboard after login (if using multipage app)
        time.sleep(1)
        st.switch_page("pages/About.py")

    else:
        st.error("❌ Invalid email or password!")

st.markdown("</div>", unsafe_allow_html=True)

# Forgot Password Functionality
if forgot_password_button:
    st.session_state.show_forgot_password = True
    st.rerun()

if st.session_state.get("show_forgot_password", False):
    st.markdown("<div class='login-card forgot-section'>", unsafe_allow_html=True)
    st.subheader("🔑 Forgot Password")
    reset_email = st.text_input("📩 Enter your email", value=st.session_state.get("reset_email", ""))
    
    if st.button("📩 Send OTP"):
        user = get_user(reset_email)
        if user:
            # Generate OTP (for production, generate a random OTP)
            otp = str(123456)
            st.session_state.otp = otp
            st.session_state.reset_email = reset_email
            st.session_state.otp_sent = True
            # Send the OTP email via SendGrid
            send_otp_email(reset_email, otp)
            st.rerun()
        else:
            st.error("❌ Email not found!")
    
    if st.session_state.get("otp_sent", False):
        otp_input = st.text_input("🔢 Enter OTP", type="password")
        new_password = st.text_input("🔑 Enter New Password", type="password")
        confirm_password = st.text_input("🔑 Confirm New Password", type="password")
    
        if st.button("🔄 Reset Password"):
            if new_password != confirm_password:
                st.error("❌ Passwords do not match!")
            elif str(st.session_state.otp) == otp_input:
                st.success("✅ Password reset successfully! Please log in.")
                st.session_state.otp_sent = False
                st.session_state.show_forgot_password = False
                st.rerun()
            else:
                st.error("❌ Invalid OTP!")
    st.markdown("</div>", unsafe_allow_html=True)
