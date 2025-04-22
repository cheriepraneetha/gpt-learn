import streamlit as st
from langchain_community.utilities import WikipediaAPIWrapper

# Set page to wide layout
st.set_page_config(layout="wide")

# Custom CSS for fixed navbar
st.markdown("""
    <style>
        /* Make navbar cover full width */
        .navbar {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #4A90E2;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
            font-size: 18px;
            font-weight: bold;
            z-index: 9999;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            padding-left: 20px;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-weight: 500;
        }
        .navbar a:hover {
            text-decoration: underline;
        }
        /* Push content down to avoid navbar overlap */
        .content {
            margin-top: 70px; /* Adjust height */
        }
    </style>

    <div class='navbar'>
        <div class='logo'>GPT-Learn</div>
        <div>
            <a href='/' >Home</a>
            <a href='/About' >About</a>
            <a href='/dashboard' >My Dashboard</a>
            <a href='/Features' >Features</a>
            <a href='/Login' >Login</a>
            <a href='/SignUp' >Sign Up</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Add a spacer to push content below navbar
st.markdown("<div class='content'></div>", unsafe_allow_html=True)

# Wikipedia Search Function
def search_wikipedia(query, num_results=3):
    """Search Wikipedia using LangChain API."""
    wikipedia = WikipediaAPIWrapper(top_k_results=num_results)
    try:
        results = wikipedia.run(query)
        return results
    except Exception as e:
        return f"Error: {e}"

# UI for Wikipedia Search
st.title("🔍 Search Wikipedia with LangChain")
query = st.text_input("Enter your search query:", "")

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching Wikipedia..."):
            results = search_wikipedia(query)
        st.subheader("📜 Search Results:")
        st.write(results)
    else:
        st.warning("Please enter a search term!")
