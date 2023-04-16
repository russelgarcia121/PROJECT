import streamlit as st

# List of fonts to use
fonts = ["Arial", "Times New Roman", "Verdana", "Georgia", "Comic Sans MS"]

# Loop through the fonts and display "Hi" in each font
for i in range(5):
    font = fonts[i]
    st.write(f"<span style='font-family:{font}; font-size:36px;'>Hi</span>", unsafe_allow_html=True)
