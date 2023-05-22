import streamlit as st
from sympy import symbols, diff

def derivative_calculator(expression, variable):
    x = symbols(variable)
    derivative = diff(expression, x)
    return derivative

def main():
    st.title("Derivative Calculator")

    expression = st.text_input("Enter an expression:")
    variable = st.text_input("Enter the variable to differentiate with respect to:")

    if st.button("Calculate"):
        try:
            result = derivative_calculator(expression, variable)
            st.success(f"The derivative of {expression} with respect to {variable} is: {result}")
        except Exception as e:
            st.error("An error occurred during calculation. Please check your input.")

if __name__ == "__main__":
    main()
