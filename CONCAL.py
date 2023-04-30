import streamlit as st

# Pangalan ng user
name = st.text_input("Ipasok ang iyong pangalan")

# Output ng pangalan ng user
if name:
    st.write("Ang pangalan mo ay", name)

# HTML at CSS para sa pagpapakulay ng background
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: skyblue !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
