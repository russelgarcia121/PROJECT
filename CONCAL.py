import streamlit as st

# Set title
st.title("Welcome to CONCAL!")

# Ask for cost input
cost = st.number_input("The cost per kilowatt-hour in pesos:")

# Add first appliance
A1N = st.text_input("Name of Appliance:")
A1M = st.number_input(f"How many {A1N} are you using?")
A1W = st.number_input(f"What is the wattage of {A1N}?")
A1B = st.number_input(f"How many days in a month do you use {A1N}? (1-31)", min_value=1, max_value=31)
A1D = st.number_input(f"How many hours per day do you use {A1N}? (0.00001-24)", min_value=0.00001, max_value=24)

# Compute consumption
A1F = (A1B/30) * A1D
A1 = A1F * (A1W * A1M)
wh1 = A1
Kh1 = (wh1 * 30) / 1000
total1 = cost * Kh1
A1con = ((A1 * 30) / 1000) * cost

# Identify high consumption appliance
max_app = A1con
max_app_name = A1N

# Display results
st.write(f"Your electricity bill is {total1} pesos.")
st.write(f"Your energy consumption is {Kh1} kWh.")
st.write(f"The consumption of {A1N} is {A1con} pesos.")

# Add another appliance
add_another = st.button("Add Another Appliance")

while add_another:
    A2N = st.text_input("Name of Appliance:")
    A2M = st.number_input(f"How many {A2N} are you using?")
    A2W = st.number_input(f"What is the wattage of {A2N}?")
    A2B = st.number_input(f"How many days in a month do you use {A2N}? (1-31)", min_value=1, max_value=31)
    A2D = st.number_input(f"How many hours per day do you use {A2N}? (0.00001-24)", min_value=0.00001, max_value=24)

    # Compute consumption
    A2F = (A2B/30) * A2D
    A2 = A2F * (A2W * A2M)
    wh2 = A2
    Kh2 = (wh2 * 30) / 1000
    total2 = cost * Kh2
    A2con = ((A2 * 30) / 1000) * cost

    # Identify high consumption appliance
    if A2con > max_app:
        max_app = A2con
        max_app_name = A2N

    # Display results
    st.write(f"The consumption of {A2N} is {A2con} pesos.")

    # Ask if user wants to add another appliance
    add_another = st.button("Add Another Appliance")

# Display high consumption appliance
st.write(f"The appliance with the highest consumption is {max_app_name}.")
