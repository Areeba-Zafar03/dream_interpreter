import streamlit as st
from dream_bot import get_qa_chain

# Hide Streamlit's default UI elements (like sidebar)
st.set_page_config(page_title="Dream Interpreter", layout="wide")

# Custom CSS for dark dreamy theme with lilac background
st.markdown("""
<style>
/* Set lilac background for the entire page */
html, body, .css-1v3fvcr {
    background-color: #C8A2D4 !important;  /* Lilac color */
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

/* Remove Streamlit's top padding */
main > div:first-child {
    padding-top: 0rem;
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
}

.nav-links a {
    margin-left: 25px;
    color: #fff;
    text-decoration: none;
}

.banner {
    background: url('https://png.pngtree.com/background/20210709/original/pngtree-full-purple-beautiful-starry-banner-background-picture-image_961976.jpg') no-repeat center center;
    background-size: cover;
    padding: 5rem 2rem;
    text-align: center;
    border-radius: 10px;
    margin-top: 1rem;
}

.banner h1 {
    font-size: 3rem;
    color: #fff;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
}

.input-area {
    background-color: #1c2331;
    padding: 2rem;
    border-radius: 12px;
    margin-top: 2rem;
}

textarea {
    background-color: #141a2a;
    color: white;
}

.button {
    background-color: #141a2a;
    margin-top: 1rem;
}

.response-box {
    background-color: #202d44;
    padding: 1.5rem;
    border-radius: 12px;
    margin-top: 2rem;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class='navbar'>
    <div><a href="/" style="color: white; text-decoration: none;"><strong>🌙 Dream Interpreter</strong></a></div>
    <div class='nav-links'>
        <a href="/How_It_Works">How it works</a>
        <a href="/FAQ">FAQ</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Banner
st.markdown("""
<div class='banner'>
    <h1>AI Dream Interpreter: <br> Unlock the Mysteries of Your Dreams</h1>
</div>
""", unsafe_allow_html=True)

# Dream Input Section
st.markdown("### 📝 Describe your dream")
user_input = st.text_area("", height=150, placeholder="Enter as much detail about your dream as you can remember...")

submit = st.button("🔍 Decode Dream")

# Response Section
if submit:
    if user_input.strip() == "":
        st.warning("Please enter your dream before decoding.")
    else:
        with st.spinner("Analyzing your dream..."):
            try:
                chain = get_qa_chain()
                result = chain.run(user_input)
                st.markdown(f"<div class='response-box'><h4>🔮 Interpretation:</h4><p>{result}</p></div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
