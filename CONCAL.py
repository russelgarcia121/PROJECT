import streamlit as st

# Add a custom font
st.markdown('<style>body {font-family: "Algerian", sans-serif;}</style>', unsafe_allow_html=True)

# Add some text using the custom font
st.header('Hello, world!')
st.write('This is an example of using a custom font in Streamlit.')
