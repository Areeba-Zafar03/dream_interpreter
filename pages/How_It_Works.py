import streamlit as st

# Page setup
st.set_page_config(page_title="How It Works", page_icon="🔎", layout="wide")

# Custom CSS styling
st.markdown("""
<style>
            
[data-testid="stAppViewContainer"] {
    background-image: url("https://areeba-zafar03.github.io/Dreams/faq.jpg");
    background-size: cover;
    background-position: center;
    color: white;
}
                        
body {
    background-color: #0b0f1a;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stSidebar"] {
    display: none;
}
.navbar {
    background-color: #490F4A;
    padding: 1rem 2rem;
    font-size: 1.1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    border-bottom: 1px solid #2a2f45;
}
.nav-links a {
    margin-left: 25px;
    color: #ccc;
    text-decoration: none;
    transition: color 0.3s ease;
}
.nav-links a:hover {
    color: #ffffff;
}
h1 {
    color: #ffffff;
    font-size: 2.5rem;
    margin-top: 2rem;
    text-align: center !important;
            
}
.step-box {
    # background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    margin-top: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.step-box h3 {
    margin-bottom: 0.5rem;
    color: #61dafb;
}
.step-box p {
    font-size: 1.1rem;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Navbar
# st.markdown("""
# <div class='navbar'>
#     <div><a href="/" style="color: white; text-decoration: none;"><strong>🌙 Dream Interpreter</strong></a></div>
#     <div class='nav-links'>
#         <a href="/How_It_Works">How it works</a>
#         <a href="/FAQ">FAQ</a>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# Page Title
st.markdown("<h1>🔎 How It Works</h1>", unsafe_allow_html=True)

# Steps
st.markdown("""
<div class="step-box">
    <h3>🧠 Step 1: Vectorize the Vision</h3>
    <p>Your dream is transformed into rich vector embeddings, capturing the essence of your experience.</p>
</div>
<div class="step-box">
    <h3>📚 Step 2: Match with Ancient Wisdom</h3>
    <p>These vectors are compared with classical interpretations — inspired by Ibn Sirin’s legendary dream dictionary.</p>
</div>
<div class="step-box">
    <h3>🤖 Step 3: AI-Powered Insight</h3>
    <p>Gemini Pro dives deep to reveal symbolic meanings and personal insights, fusing tradition with technology.</p>
</div>
<div class="step-box">
    <h3>✨ The Result</h3>
    <p>You receive a beautifully crafted interpretation — thoughtful, intuitive, and often eye-opening.</p>
</div>
""", unsafe_allow_html=True)
