import streamlit as st
st.title("Welcome to CONCAL!")
st.text("")
st.markdown("## **START!**")

cost = st.number_input("The cost per kilowatt-hour in pesos:")
ask1 = 0
ask2 = 0
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 1st app
st.markdown("## **1st APPLIANCE!**")
A1N = st.text_input("Name of 1st appliance:")
if A1N:
    A1M = st.number_input(f"How many {A1N} are you using?", value=0, step=1)
    ask1 = st.number_input(
        "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)

    while ask1 > 2 or ask1 < 1:  # ask for input until ask1 is 1 or 2
        ask1 = st.number_input(
            "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
        
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if ask1 == 1:  # add app2 (1st line)
    st.markdown("## **2nd APPLIANCE!**")
    A2N = st.text_input("Name of 2nd appliance: ")
    ask1 = st.number_input(
        "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)

    while ask1 > 2 or ask1 < 1:  # ask for input until ask1 is 1 or 2
        ask1 = st.number_input(
            "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
        
    if A2N:
        A2M = st.number_input(f"How many {A2N} are you using?",value=0, step=1)
        ask2 = 2

    if ask2 == 2:

        st.write(A1N)

if ask1 == 2:
    st.write(A2N)
