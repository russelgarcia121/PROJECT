import streamlit as st
st.title("Welcome to CONCAL!")
st.text("")
st.markdown("## **START!**")

cost = st.number_input("The cost per kilowatt-hour in pesos:")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 1st app
st.markdown("## **1st APPLIANCE!**")
ask1=0
A1N = st.text_input("Name of 1st appliance:")
if A1N:
    A1M = st.number_input(f"How many {A1N} are you using?", value=0, step=1)
    A1W = st.number_input(f"What is the wattage of {A1N}?(watt)")
    A1B = st.number_input(f"How many days in a month do you use {A1N}?(1-31)", value=0, step=1)
    while A1B > 31 or A1B < 1:
        A1B = st.number_input(
            f"How many days in a month do you use {A1N}?(1-31)", value=0, step=1)

    A1D = st.number_input(f"How many hours in a day do you use {A1N}?(1-24)")
    while A1D > 24 or A1D < 0.00001:
        A1D = st.number_input(
            f"How many hours in a day do you use {A1N}?(1-24)")

    ask1 = 2
    
if ask1 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B/30) * A1D

    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
    A1 = (A1F * (A1W * A1M))

    # TOTAL: watt/hour kada araw.
    wh1 = A1

    # TOTAL: Kilo-watt/hour kada month.
    Kh1 = (wh1*30) / 1000

    # TOTAL: para ma compute ang (cost) kada month.
    total1 = cost * Kh1

    # INDIVIDUALLY: para ma compute ang (cost) kada month.
    A1con = ((A1*30)/1000)*cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("************************************************************************************************************************************************************************")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1]
    max_app = apps[0]
    for app in apps:
        if app > max_app:
            max_app = app
    if max_app == Y1:
        st.write("************************************************************************************************************************************************************************")
        st.write("Name of appliance  :", A1N)
        st.write("Electricity bill   : PHP", A1con)
        st.write("Energy consumption :", Y1)
    # OUTPUT2
    st.write("************************************************************************************************************************************************************************")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con,)
    st.write("************************************************************************************************************************************************************************")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total1)
    st.write("Energy consumption:", Kh1, "kWh")
