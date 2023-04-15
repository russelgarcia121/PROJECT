import streamlit as st

st.title("Student Information")

# Ask for the name and age of the first student
name1 = st.text_input("Enter the name of the first student:")
age1 = st.number_input("Enter the age of the first student:", value=0, step=1)

# Ask for the name and age of the second student
name2 = st.text_input("Enter the name of the second student:")
age2 = st.number_input("Enter the age of the second student:", value=0, step=1)

# Print the information
st.write(f"Student 1: Name = {name1}, Age = {age1}")
st.write(f"Student 2: Name = {name2}, Age = {age2}")
