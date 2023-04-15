import streamlit as st

st.title("Addition of Two Numbers")

# Ask the user for two integer numbers
number1 = st.number_input("Enter the first number:", value=0, step=1)
number2 = st.number_input("Enter the second number:", value=0, step=1)

# Add the two numbers and display the result
result = number1 + number2
st.write(f"The result of {number1} + {number2} is {result}")
