import streamlit as st

# Ask user to select language
language = st.radio("Choose a language / Pumili ng wika", ("English", "Filipino"))

# Check language and ask for name
if language == "English":
    name = st.text_input("What is your name?")
else:
    name = st.text_input("Anong pangalan mo?")

# Display greeting
if name:
    if language == "English":
        st.write(f"Hello {name}!")
    else:
        st.write(f"Kumusta {name}!")
