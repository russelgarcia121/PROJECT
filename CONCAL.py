import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Main calculator function
def calculator():
    st.title("Simple Calculator")
    
    # Get user input
    num1 = st.number_input("Enter the first number:", step=1.0)
    operator = st.selectbox("Select an operation:", ("+", "-", "*", "/"))
    num2 = st.number_input("Enter the second number:", step=1.0)
    
    # Perform calculation based on operator
    result = 0
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    
    # Display the result
    st.write("Result:", result)

# Run the calculator
calculator()
