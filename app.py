import streamlit as st

# Page setup
st.set_page_config(page_title="AI Dream Interpreter", layout="wide")

# Custom CSS styling with your hosted image
page_styles = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stAppViewContainer"] {
    background-image: url("https://areeba-zafar03.github.io/Dreams/dreamimage.jpg");
    background-size: cover;
    background-position: center;
    font-family: 'Poppins', sans-serif;
    color: black;
}

h1, p, div, span, .stText, .stMarkdown {
    color: white !important;
    text-align: center !important;
}

h1 {
    font-size: 3em;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    margin-top: -40px;
}

p {
    margin-bottom: -10px;
    font-size: 1.2em;
    font-weight: 500;
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

.stButton > button {
    background-color: #7393B3 !important;
    color: white !important;
    border: none !important;
    padding: 1em 3em !important;
    border-radius: 12px !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    transition: all 0.3s ease !important;
    margin: 30px auto !important;
    display: block !important;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2) !important;
}

.stButton > button:hover {
    background-color: #0047AB !important;
    transform: scale(1.05) !important;
}
</style>
"""

st.markdown(page_styles, unsafe_allow_html=True)

# Lottie animation (centered)
st.components.v1.html("""
    <div style="display: flex; justify-content: center; align-items: center; transform: translateY(-40px);">
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player 
            src="https://lottie.host/0741b903-b3fb-4d6b-a581-2568897620c9/QSdd9vlD7X.json"  
            background="transparent"  
            speed="1"  
            style="height: 300px;"  
            loop  
            autoplay>
        </lottie-player>
    </div>
""", height=250)

# Main title and subtitle
st.markdown("<h1>🌙 Welcome to AI Dream Interpreter</h1>", unsafe_allow_html=True)
st.markdown("<p>Discover what your dreams mean using classical texts and AI insights.</p>", unsafe_allow_html=True)

# Start button
if st.button("START INTERPRETING"):
    st.switch_page("pages/DREAM.py")  # Make sure DREAM.py exists in /pages
