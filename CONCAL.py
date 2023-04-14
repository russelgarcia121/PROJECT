import streamlit as st
st.title("How Great is our God?")
st.text("our God, our Author")
st.markdown("date: 04/14/23")

num1 = st.number_input('Enter the 1st number:')
num2 = st.number_input('Enter the 2nd number:')
ans = num1 + num2
prod= num1 * num2
# Print the name if it's not empty
if num2:
    st.write("The sum:", ans)
    st.write("The product:", prod)
