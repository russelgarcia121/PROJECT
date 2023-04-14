import streamlit as st
st.title("How Great is our God?")
st.text("my God, my Author")
st.markdown("date: 04/13/23")

import streamlit as st

num1 = st.number_input('Enter the 1st number')
num2 = st.number_input('Enter the 2st number')
ans = num1 + num2
prod= num1 * num2
# Print the name if it's not empty
if num2:
    st.write("The sum:", ans)
    st.write("The product:", prod)
