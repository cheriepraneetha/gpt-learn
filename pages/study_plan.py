import streamlit as st
from groq import Groq
from fpdf import FPDF

# Initialize the LLM with API Key

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

def generate_study_plan(topic, duration, difficulty):
    prompt = f"""
    Generate a structured study plan for learning {topic}.
    - Duration: {duration} weeks
    - Difficulty: {difficulty} level
    - Include key topics, resources, and a weekly breakdown.
    """
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are an AI that generates structured study plans."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def clean_text(text):
    return text.replace("\u2013", "-")  # Replace en dash with hyphen

def create_pdf(text, filename="study_plan.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    cleaned_text = clean_text(text)
    pdf.multi_cell(0, 10, cleaned_text.encode("latin-1", "replace").decode("latin-1"))  
    pdf.output(filename)
    return filename

# Streamlit UI
st.title("Study Plan Generator")

# User Inputs
topic = st.text_input("Enter your topic of study:")
duration = st.slider("Select study duration (weeks):", 1, 24, 8)
difficulty = st.selectbox("Select difficulty level:", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Study Plan"):
    if topic:
        study_plan = generate_study_plan(topic, duration, difficulty)
        st.subheader("Your Study Plan")
        st.write(study_plan)
        
        # Generate the PDF file
        pdf_filename = "study_plan.pdf"
        create_pdf(study_plan, pdf_filename)
        
        # Provide a download button for the PDF
        with open(pdf_filename, "rb") as f:
            st.download_button(
                label="Download Study Plan as PDF",
                data=f,
                file_name="study_plan.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Please enter a topic to generate a study plan.")
