import streamlit as st
from sympy import symbols, diff

def differential_calculator():
    st.title("Differential Calculus Calculator")
    
    # Getting the function from the user
    function_str = st.text_input("Enter the function:")
    x = symbols('x')
    
    try:
        # Converting the function string to a symbolic expression
        function = eval(function_str)
        
        # Calculating the derivative
        derivative = diff(function, x)
        
        # Displaying the result
        st.write("Derivative:", derivative)
    
    except Exception as e:
        st.write("Error:", e)

# Running the Streamlit app
if __name__ == "__main__":
    differential_calculator()
