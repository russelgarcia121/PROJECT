import streamlit as st

# List of fonts to use
fonts = ["Arial", "Times New Roman", "Verdana", "Georgia", "Comic Sans MS"]

# Display "Hi" in each font
st.write(f"<span style='font-family:{fonts[0]}; font-size:36px;'>Hi</span>", unsafe_allow_html=True)
st.write(f"<span style='font-family:{fonts[1]}; font-size:36px;'>Hi</span>", unsafe_allow_html=True)
st.write(f"<span style='font-family:{fonts[2]}; font-size:36px;'>Hi</span>", unsafe_allow_html=True)
st.write(f"<span style='font-family:{fonts[3]}; font-size:36px;'>Hi</span>", unsafe_allow_html=True)
st.write(f"<span style='font-family:{fonts[4]}; font-size:36px;'>Hi</span>", unsafe_allow_html=True)
