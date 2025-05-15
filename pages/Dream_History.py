# pages/History.py
import streamlit as st
from dream_bot import load_dream_history

st.set_page_config(page_title="Dream History", layout="wide")

st.markdown("""
<style>
           
/* Hide sidebar */
[data-testid="stSidebar"] {
    display: none;
}
                 
[data-testid="stAppViewContainer"] {
    background-image: url("https://areeba-zafar03.github.io/Dreams/faq.jpg");
    background-size: cover;
    background-position: center;
    font-family: 'Poppins', sans-serif;
    color: white;
}
                    
.history-box {
    background-color: #141a2a;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# st.markdown("""
# <div style='background-color: #490F4A; padding: 1rem 2rem; font-size: 1.2rem; color: white;'>
#     <strong>🌙 Dream Interpreter - History</strong>
# </div>
# """, unsafe_allow_html=True)

st.markdown("## 🕰️ Previous Dreams and Interpretations")

history = load_dream_history()
if not history:
    st.info("No previous dreams found.")
else:
    for entry in reversed(history[-20:]):
        st.markdown(f"""
        <div class='history-box'>
            <strong>🗓️ {entry["timestamp"][:19].replace("T", " ")}</strong><br>
            <em>{entry["dream"]}</em>
            <ul>
                {"".join([f"<li><strong>{k.replace('_',' ').title()}</strong>: {v}</li>" for k,v in entry["interpretations"].items()])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
