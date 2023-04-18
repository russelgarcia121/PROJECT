import streamlit as st

# Ask the user for their name
name = st.text_input('Enter your name:')

# Create two columns to display the hour and minute inputs side by side for charger usage
st.write("Enter the duration of time you use the charger:")
col1, col2 = st.beta_columns(2)
charger_hours = col1.number_input('Hours:', min_value=0, value=0, key="charger_hours")
charger_minutes = col2.number_input('Minutes:', min_value=0, max_value=59, value=0, key="charger_minutes")

# Create two columns to display the hour and minute inputs side by side for working hours
st.write("Enter your working hours:")
col3, col4 = st.beta_columns(2)
working_hours = col3.number_input('Hours:', min_value=0, value=0, key="working_hours")
working_minutes = col4.number_input('Minutes:', min_value=0, max_value=59, value=0, key="working_minutes")

# Print the user's inputs
st.write(f"{name} uses the charger for {charger_hours} hours and {charger_minutes} minutes.")
st.write(f"{name} works for {working_hours} hours and {working_minutes} minutes.")
