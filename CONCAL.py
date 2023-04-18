import streamlit as st

# Ask the user for their name
name = st.text_input('Enter your name:')

# Create two columns to display the hour and minute inputs side by side
col1, col2 = st.beta_columns(2)

# Ask the user for the number of hours and minutes they use the charger
hours = col1.number_input('Enter the number of hours you use the charger:', min_value=0, value=0)
minutes = col2.number_input('Enter the number of minutes you use the charger:', min_value=0, max_value=59, value=0)

# Print the user's name and the number of hours and minutes
st.write(f"{name} uses the charger for {hours} hours and {minutes} minutes.")
