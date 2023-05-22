import streamlit as st
from sympy import symbols, diff

def differential_calculator():
    # Getting the function from the user
    function_str = st.text_input("Enter the function:")
    x = symbols('x')
    
    try:
        # Converting the function string to a symbolic expression
        function = eval(function_str)
        
        # Calculating the derivative
        derivative = diff(function, x)
        
        # Printing the result
        st.write("Derivative:", derivative)
    
    except Exception as e:
        st.write("Error:", e)

# Main function to run the Streamlit app
def main():
    st.title("Differential Calculus Calculator")
    differential_calculator()

if __name__ == "__main__":
    main()
