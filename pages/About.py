import streamlit as st

# Page Configuration
st.set_page_config(page_title="About - GPT-Learn", page_icon="📘", layout="wide")

# Custom CSS for Navigation Bar & Styling
custom_css = """
    <style>
        /* Hide default sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }

        /* Top Navigation Bar */
        .topnav {
            background-color: #4A90E2;
            overflow: hidden;
            padding: 10px 0;
            text-align: center;
            font-family: Arial, sans-serif;
        }

        .topnav a {
            display: inline-block;
            color: white;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
        }

        .topnav a:hover {
            background-color: #357ABD;
            border-radius: 5px;
        }

        /* Main Content Styling */
        .container {
            text-align: center;
            padding: 40px 20px;
        }

        h1, h2, h3 {
            color: #222;
        }

        p {
            color: #555;
            font-size: 18px;
        }

        .feature-box {
            background: #F1F1F1;
            padding: 20px;
            border-radius: 10px;
            width: 300px;
            text-align: center;
            margin: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }

        .features-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 30px;
        }

        .highlight {
            color: #ff5733;
            font-weight: bold;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Top Navigation Bar
st.markdown(
    """
    <div class='topnav'>
        <a href="/">🏠 Home</a>
        <a href="/About">📘 About</a>
        <a href="/dashboard">📊 My Dashboard</a>
        <a href="/Features">🚀 Features</a>
        <a href="/Login">🔑 Login</a>
        <a href="/SignUp">📝 Sign Up</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<div class='container'><h1>📘 About GPT-Learn</h1></div>", unsafe_allow_html=True)

st.markdown("""
    <div class='container'>
        <p>GPT-Learn is an advanced AI-powered educational platform designed to provide personalized learning experiences. 
        Using state-of-the-art GPT-based models, this platform dynamically adapts to users' knowledge levels, helping them learn more effectively.</p>
    </div>
""", unsafe_allow_html=True)

# What GPT-Learn Does
st.markdown("<h2>🎯 What Does GPT-Learn Do?</h2>", unsafe_allow_html=True)
st.markdown("<p>GPT-Learn leverages Artificial Intelligence to enhance learning in multiple ways:</p>", unsafe_allow_html=True)

# Feature Section
st.markdown("""
    <div class='features-container'>
        <div class='feature-box'>
            <h3>📄 Chat with PDF</h3>
            <p>Upload PDFs and interact with their content through AI-driven question-answering.</p>
        </div>
        <div class='feature-box'>
            <h3>🌐 Wikipedia Search</h3>
            <p>Get quick and reliable information from Wikipedia without leaving the platform.</p>
        </div>
        <div class='feature-box'>
            <h3>📚 Study Plan Generator</h3>
            <p>Receive a personalized study plan based on your interests, strengths, and weaknesses.</p>
        </div>
        <div class='feature-box'>
            <h3>📊 Learning Progress Tracking</h3>
            <p>Monitor and analyze your learning journey with AI-powered insights.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Why GPT-Learn?
st.markdown("<h2>💡 Why GPT-Learn?</h2>", unsafe_allow_html=True)
st.markdown("""
    <p>Traditional education methods often fail to cater to individual needs. <span class='highlight'>GPT-Learn</span> addresses this gap by offering:</p>
    <ul>
        <li>✔ Adaptive learning paths</li>
        <li>✔ AI-generated explanations</li>
        <li>✔ Instant Q&A with smart responses</li>
        <li>✔ Simplified research through integrated Wikipedia search</li>
        <li>✔ A structured approach to knowledge retention</li>
    </ul>
""", unsafe_allow_html=True)

# How It Works
st.markdown("<h2>🚀 How It Works</h2>", unsafe_allow_html=True)
st.markdown("""
    <p>
    1️⃣ <strong>User Profiles</strong>: Users create a profile to customize their learning experience. <br>
    2️⃣ <strong>AI-Powered Learning</strong>: Based on user preferences, AI recommends study materials and generates interactive content. <br>
    3️⃣ <strong>Gamification</strong>: Earn badges and track progress through an intuitive dashboard. <br>
    4️⃣ <strong>Personalized Insights</strong>: AI continuously analyzes learning patterns and suggests improvements.
    </p>
""", unsafe_allow_html=True)

# Who Can Use GPT-Learn?
st.markdown("<h2>🌍 Who Can Use GPT-Learn?</h2>", unsafe_allow_html=True)
st.markdown("""
    <p>GPT-Learn is built for <span class='highlight'>students, professionals, and lifelong learners</span> who want to enhance their knowledge using AI-driven tools. 
    Whether you're preparing for exams, researching a new topic, or simply curious about something, GPT-Learn is your go-to platform!</p>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("<h2>🎓 Start Your AI-Powered Learning Journey Today!</h2>", unsafe_allow_html=True)
st.markdown("""
    <p>Join GPT-Learn and experience the future of education! Whether you're a student looking for personalized study plans 
    or a researcher seeking quick answers, GPT-Learn is here to help.</p>
""", unsafe_allow_html=True)
