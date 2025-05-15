import streamlit as st

# Page setup
st.set_page_config(page_title="FAQ", page_icon="❓", layout="wide")

# Custom CSS for dark dreamy look
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://areeba-zafar03.github.io/Dreams/faq.jpg");
    background-size: cover;
    background-position: center;
    font-family: 'Poppins', sans-serif;
    color: black;
}

/* Hide sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Navbar styling */
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
h1{
    color: white !important;
    text-align: center !important;
}
/* FAQ box */
.faq-box {
    background-color: #141a2a;
    padding: 2rem;
    border-radius: 12px;
    margin-top: 2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.faq-item {
    margin-bottom: 1.5rem;
}
.faq-item strong {
    color: #61dafb;
    display: block;
    margin-bottom: 0.3rem;
}
.faq-item p {
    margin: 0;
    color: #e0e0e0;
    font-size: 1.05rem;
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

# Title
st.markdown("<h1>❓ Frequently Asked Questions</h1>", unsafe_allow_html=True)

# FAQ Content
st.markdown("""
<div class="faq-box">
            
    Q: Is this interpretation accurate?
    A: It’s based on Ibn Sirin’s dream interpretations and enhanced with AI. It’s a guide, not a prophecy.

    Q: Can I upload my own dream book?
    A: Not yet — but we're working on this feature for future updates!
    
    Q: Is this free?
    A: Yes, it’s completely free to use — no subscriptions or hidden costs.
   
    Q: Is it private?
    A: 100%. Your dreams are never saved or shared. Privacy is our priority.
    
</div>
""", unsafe_allow_html=True)
