import streamlit as st
import boto3
import pandas as pd
from boto3.dynamodb.conditions import Key
from datetime import datetime, timedelta
import random

# ------------------ Page Config ------------------
st.set_page_config(page_title="📊 Dashboard", layout="wide")
st.title("📊 Personalized Learning Dashboard")

# ------------------ Style ------------------
st.markdown("""
    <style>
        .top-nav {
            background: linear-gradient(90deg, #2C3E50, #1a252f);
            padding: 15px;
            text-align: center;
            border-bottom: 2px solid #ffcc00;
        }
        .top-nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        .top-nav a:hover {
            text-decoration: underline;
        }
    </style>
    <div class='top-nav'>
        <a href='/'>Home</a>
        <a href='/About'>About</a>
        <a href='/Features'>Features</a>
        <a href='/Login'>Login</a>
        <a href='/SignUp'>Sign Up</a>
    </div>
""", unsafe_allow_html=True)

# ------------------ DynamoDB Setup ------------------
session = boto3.Session(region_name="us-east-1")
dynamodb = session.resource("dynamodb")
table = dynamodb.Table("ProjectTable")

# ------------------ Email Input ------------------
st.subheader("🔐 Access Your Personalized Dashboard")
email = st.text_input("Enter your registered email ID:")

if email:
    try:
        # Query using EmailIndex GSI
        response = table.query(
            IndexName="EmailIndex",
            KeyConditionExpression=Key("email").eq(email)
        )
        items = response.get("Items", [])

        if items:
            user_item = items[0]
            username = user_item.get("username", "Learner")
            st.markdown(f"### Welcome, **{username}** 🎓")

            # ------------------ Simulated Time Data ------------------
            st.subheader("📈 Weekly Learning Time")
            dates = [datetime.now() - timedelta(days=i) for i in range(6, -1, -1)]
            time_spent = [random.randint(20, 70) for _ in range(7)]
            df_time = pd.DataFrame({
                "Date": [d.strftime("%Y-%m-%d") for d in dates],
                "Time Spent (minutes)": time_spent
            })
            st.line_chart(df_time.set_index("Date"))

            total_time = sum(time_spent)
            st.success(f"🕒 You've spent a total of **{total_time} minutes** learning this week!")

            # ------------------ Interests Update ------------------
            st.subheader("🎯 Your Learning Interests")
            saved_interests = user_item.get("interests", [])

            # Display interest bar chart
            if isinstance(saved_interests, str):
                interests_list = [i.strip() for i in saved_interests.split(",") if i.strip()]
            elif isinstance(saved_interests, list):
                interests_list = saved_interests
            else:
                interests_list = []

            if interests_list:
                df_interests = pd.DataFrame({
                    "Topic": interests_list,
                    "Recommended Hours": [round(3 + (i * 1.3), 1) for i in range(len(interests_list))]
                })
                st.bar_chart(df_interests.set_index("Topic"))
            else:
                st.info("You haven't selected any interests yet.")

            # Interest update form
            with st.form("update_interests_form"):
                interests_input = st.text_input(
                    "Enter your interests (comma-separated):",
                    value=", ".join(interests_list)
                )
                submit = st.form_submit_button("💾 Save Interests")

            if submit and interests_input.strip():
                try:
                    updated_list = [i.strip() for i in interests_input.split(",") if i.strip()]
                    table.update_item(
                        Key={"user_id": user_item["user_id"]},
                        UpdateExpression="SET interests = :interests",
                        ExpressionAttributeValues={":interests": updated_list}
                    )
                    st.success("✅ Interests updated successfully!")
                    interests_list = updated_list
                    # Refresh chart
                    df_interests = pd.DataFrame({
                        "Topic": interests_list,
                        "Recommended Hours": [round(3 + (i * 1.3), 1) for i in range(len(interests_list))]
                    })
                    st.bar_chart(df_interests.set_index("Topic"))
                except Exception as e:
                    st.error(f"Failed to update interests: {str(e)}")
        else:
            st.warning("⚠️ Email not found in our system. Please sign up first.")

    except Exception as e:
        st.error(f"❌ Error accessing dashboard: {str(e)}")
