import streamlit as st
from dream_bot import get_multi_book_qa_results

# Set up page configuration
st.set_page_config(page_title="Interpret Your Dream", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://areeba-zafar03.github.io/Dreams/stars.jpg");
    background-size: cover;
    background-position: center;
    font-family: 'Poppins', sans-serif;
    color: white !important;
}

[data-testid="stSidebar"] {
    display: none;
}

h1 {
    text-align: center;
    font-size: 3.5rem;
    font-weight: bold;
    color: white !important;
    margin-top: 3rem;
}

.welcome-container {
    text-align: center;
    color: white;
    padding: 2rem;
}

textarea {
    background-color: #ffffff;
    color: black;
    border: 1px solid #3a7d8c;
    padding: 0.75rem;
    font-size: 16px;
    border-radius: 8px;
    width: 80%;
    margin: 1rem 0;
}

.stButton>button {
    background-color: #6082B6;
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-size: 20px;
    font-weight: bold;
    border: none;
    margin: 1rem auto;
    display: block;
}

.stButton>button:hover {
    background-color: black;
}

.response-box {
    background-color: #4682B4;
    padding: 1.5rem;
    border-radius: 12px;
    margin-top: 2rem;
    color: white;
}

.navbar {
    overflow: hidden;
    font-family: Arial, sans-serif;
    padding: 0.5rem;
    width: 100%;
}

.navbar a {
    float: right;
    display: block;
    color: white;
    text-align: center;
    padding: 14px 20px;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
}

.navbar a:hover {
    background-color: #5a8c92;
    color: white;
}

.stTextArea label {
    color: white !important;
}

/* Alert box text to white for all alert types */
.stAlert[data-testid="stAlert"] {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<div class="navbar">
     <a href="/How_It_Works">How it works</a>
        <a href="/FAQ">FAQ</a>
      <a href="/Dream_History">History</a> 
</div>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1>🌌 Dream Interpretation</h1>", unsafe_allow_html=True)

# Dream input box
st.markdown("### 📝 Describe your dream", unsafe_allow_html=True)
user_input = st.text_area("Enter as much detail as you can remember...", height=150, placeholder="Describe your dream here...")

# Button to trigger dream interpretation
if st.button("🔍 Decode Dream"):
    if not user_input.strip():
        st.warning("Please enter your dream before decoding.")
    else:
        with st.spinner("Interpreting your dream..."):
            try:
                # Get interpretation results from different books
                results = get_multi_book_qa_results(user_input)

                # Book names for better representation
                book_names = {
                    "ibn_sirin": "📜 Ibn Sirin",
                    "ibn_raashid": "📚 Ibn Raashid",
                }

                # Display results in a styled box
                for key, interpretation in results.items():
                    st.markdown(f"""
                    <div class='response-box'>
                        <h4>{book_names.get(key, key)}'s Interpretation:</h4>
                        <p>{interpretation}</p>
                    </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")