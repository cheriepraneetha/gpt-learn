import streamlit as st

# Page Configuration
st.set_page_config(page_title="GPT-Learn", page_icon="📚", layout="wide")

# Hide the sidebar navigation
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Custom CSS for Styling
custom_css = """
<style>
    body {
        background-color: #1a1a1a !important;
        margin: 0;
        font-family: 'Helvetica', sans-serif;
    }
    /* Top Navigation Bar */
    .navbar {
        background: linear-gradient(90deg, #2c3e50, #1a252f);
        padding: 15px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #ffcc00;
    }
    .navbar a {
        color: #ffffff;
        text-decoration: none;
        margin: 0 15px;
        font-weight: bold;
    }
    .navbar a:hover {
        color: #ffcc00;
    }
    .logo {
        color: #ffcc00;
        font-size: 28px;
        font-weight: bold;
    }
    /* Hero Section */
    .hero {
        text-align: center;
        padding: 100px 20px;
        color: 	#4d0000;
    }
    .hero h1 {
        font-size: 48px;
        margin-bottom: 20px;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    }
    .hero p {
        font-size: 20px;
        margin-bottom: 30px;
        color: #3ed7d2;
    }
    .btn-container {
        margin-top: 20px;
    }
    .btn {
        background-color: #007bff;
        color: #ffffff;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        cursor: pointer;
        margin: 10px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .btn:hover {
        background-color: #0056b3;
    }
    /* Feature Card Container */
    .features-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 40px;
    }
    .feature-card {
        background: #2c3e50;
        color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .feature-card h3 {
        font-size: 24px;
        margin-bottom: 15px;
    }
    .feature-card p {
        font-size: 16px;
        color: #cccccc;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class='navbar'>
    <div class='logo'>GPT-Learn</div>
    <div>
        <a href='/'>Home</a>
        <a href='/About'>About</a>
        <a href='/dashboard'>My Dashboard</a>
        <a href='/Features'>Features</a>
        <a href='/Login'>Login</a>
        <a href='/SignUp'>Sign Up</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
# Hero Section
st.markdown("""
<div class='hero'>
    <h1>GPT-Based Personalized Learning Content Generation with Knowledge Adaptation</h1>
    <p>Empowering your education with AI-driven personalized learning paths and real-time knowledge adaptation.</p>
</div>
""", unsafe_allow_html=True)

# Centered Navigation Buttons
# Centered Navigation Buttons using Streamlit's switch_page
# Custom CSS for button styling
st.markdown("""
<style>
    .stButton > button {
        background-color: #007bff;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 6px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin: 10px auto;
        display: block;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
</style>
""", unsafe_allow_html=True)

# Centered Button Layout
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col2:
    if st.button("📄 Chat with PDF"):
        st.switch_page("pages/chat_with_pdf.py")

with col3:
    if st.button("🌐 Wikipedia Search"):
        st.switch_page("pages/wikipedia_search.py")

with col4:
    if st.button("📚 Generate Study Plan"):
        st.switch_page("pages/study_plan.py")




# Advantages of Using GPT-Learn Section
st.markdown("""
<div class='info-section'>
    <h2>Why Choose GPT-Learn?</h2>
    <p>
        GPT-Learn is designed to enhance your learning experience by leveraging the power of AI. Here are just a few of the reasons you should choose our platform:
    </p>
</div>
""", unsafe_allow_html=True)

# Feature Cards with Advantages
st.markdown("""
<div class='features-container'>
    <div class='feature-card'>
        <h3>📚 Personalized Learning Paths</h3>
        <p>GPT-Learn offers AI-powered learning paths tailored to your goals and preferences, making your learning journey more effective.</p>
    </div>
    <div class='feature-card'>
        <h3>🧠 Real-Time Knowledge Adaptation</h3>
        <p>As you progress, GPT-Learn continuously adapts to your learning pace, providing real-time content recommendations for enhanced understanding.</p>
    </div>
    <div class='feature-card'>
        <h3>🎓 Interactive Learning Tools</h3>
        <p>Engage with interactive tools like Chat with PDF, Wikipedia Search, and more to strengthen your learning with personalized, hands-on experiences.</p>
    </div>
    <div class='feature-card'>
        <h3>📊 Progress Tracking & Analytics</h3>
        <p>Track your learning progress over time with detailed analytics that help you stay on track and identify areas for improvement.</p>
    </div>
    <div class='feature-card'>
        <h3>🚀 Accelerated Learning Experience</h3>
        <p>With GPT-Learn, you can learn faster and more efficiently through AI-driven recommendations and personalized study plans.</p>
    </div>
    <div class='feature-card'>
        <h3>🔍 Adaptive Knowledge Integration</h3>
        <p>Our platform helps you integrate new knowledge seamlessly into your learning experience by providing adaptive and up-to-date content.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer Section
st.markdown("""
<div class='footer'>
    <p>&copy; 2025 GPT-Learn. All rights reserved. | <a href='/Privacy'>Privacy Policy</a> | <a href='/Terms'>Terms of Use</a></p>
</div>
""", unsafe_allow_html=True)
