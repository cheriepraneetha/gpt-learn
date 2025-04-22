import streamlit as st

# Set page config
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Navbar Styles */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #007bff;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            padding: 8px 15px;
            font-size: 16px;
        }
        .navbar a:hover {
            background-color: #0056b3;
            border-radius: 5px;
        }
        .logo {
            font-size: 20px;
            font-weight: bold;
            color: white;
        }
        /* Hide Sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        /* Feature Cards */
        .feature-card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

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
""", unsafe_allow_html=True)

# Features Section
st.markdown("## 🚀 Features")

features = [
    {
        "title": "Chat with PDF",
        "description": "Interact with PDFs using AI-powered Q&A.",
        "icon": "📄",
        "button_text": "Explore Chat with PDF",
        "switch_page": "pages/chat_with_pdf.py",
    },
    {
        "title": "Wikipedia Search",
        "description": "Search Wikipedia directly from the platform.",
        "icon": "🌐",
        "button_text": "Explore Wikipedia",
        "switch_page": "pages/wikipedia_search.py",
    },
    {
        "title": "Personalized Study Plan",
        "description": "Get a customized study plan based on your learning goals.",
        "icon": "📚",
        "button_text": "Create Study Plan",
        "switch_page": "pages/study_plan.py",
    },
    {
        "title": "Gamification & Badges",
        "description": "Earn badges and track progress with gamification.",
        "icon": "🏆",
        "button_text": "View Badges",
        "switch_page": "pages/badges.py",
    },
]

# Display features in two columns
col1, col2 = st.columns(2)

for index, feature in enumerate(features):
    with col1 if index % 2 == 0 else col2:
        st.markdown(f"""
            <div class="feature-card">
                <h3>{feature['icon']} {feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(feature["button_text"], key=feature["title"]):
            st.switch_page(feature["switch_page"])
