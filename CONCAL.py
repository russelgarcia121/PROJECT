import streamlit as st
st.write("<span style='font-family:Times New Roman; font-size:32px;font-weight:bold;'>Welcome to CONCAL!</span>", unsafe_allow_html=True)
st.write("<span style='font-family:Times New Roman; font-size:14px;'>An advanced technology for managing household energy consumption.</span>", unsafe_allow_html=True)
st.write("***")
st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>CONCAL can do the following:</span>", unsafe_allow_html=True)
st.write("<span style='font-family:Times New Roman; font-size:14px;'>&#10003; Identifies appliance with highest bill and power consumption.</span></li></ul>", unsafe_allow_html=True)
st.write("<span style='font-family:Times New Roman; font-size:14px;'>&#10003; Calculates consumption and bill for each appliance.</span></li></ul>", unsafe_allow_html=True)
st.write("<span style='font-family:Times New Roman; font-size:14px;'>&#10003;Computes total bill and power consumption.</span></li></ul>", unsafe_allow_html=True)
st.write("***")
st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Let's start!</span>",
         unsafe_allow_html=True)
cost = st.number_input("# The cost per kilowatt-hour in pesos:")
ask1 = 0
ask2 = 0

Appliances = []

# Get the item to add from the user

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 1st app
st.write("***")
st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 1st appliance.</span>", unsafe_allow_html=True)
A1N = st.text_input("Name of 1st appliance:")
if A1N:
    A1M = st.number_input(f"How many {A1N} are you using?", value=0, step=1)
    A1W = st.number_input(f"What is the wattage of {A1N}?(watt)")
    A1B = st.number_input(
        f"How many days in a month do you use {A1N}?(1-31)", value=0, step=1)
    if 31 >= A1B >= 1:
        A1D = st.number_input(
            f"How many hours in a day do you use {A1N}?(1-24)")
        if 24 >= A1D >= 1:
            ask1 = st.number_input(
                "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 2nd app
if ask1 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 2nd appliance.</span>", unsafe_allow_html=True)
    A2N = st.text_input("Name of 2nd appliance: ")
    if A2N in Appliances:
        st.write("Use an alternative name aside from", A2N)
    else:
        Appliances.append(A2N)
        if A2N:
            A2M = st.number_input(
                f"How many {A2N} are you using?", value=0, step=1)
            A2W = st.number_input(f"What is the wattage of {A2N}?(watt)")
            A2B = st.number_input(
                f"How many days in a month do you use {A2N}?(1-31)", value=0, step=1)
            if 31 >= A2B >= 1:
                A2D = st.number_input(
                    f"How many hours in a day do you use {A2N}?(1-24)")
                if 24 >= A2D >= 1:
                    ask2 = 2

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-2nd app
if ask2 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * A1D
    A2F = (A2B / 30) * A2D

    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
    A1 = (A1F * (A1W * A1M))
    A2 = (A2F * (A2W * A2M))

    # TOTAL: watt/hour kada araw.
    wh2 = (A1 + A2)

    # TOTAL: Kilo-watt/hour kada month.
    Kh2 = ((wh2 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total2 = cost * Kh2

    # INDIVIDUALLY: para ma compute ang (cost) kada month.
    A1con = ((A1 * 30) / 1000) * cost
    A2con = ((A2 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2]
    max_app = apps[0]
    for app in apps:
        if app > max_app:
            max_app = app
    if max_app == Y1:
        st.write("***")
        st.write("Name of appliance  :", A1N)
        st.write("Electricity bill   : PHP", A1con)
        st.write("Energy consumption :", Y1, "kWh")
    if max_app == Y2:
        st.write("***")
        st.write("Name of appliance  :", A2N)
        st.write("Electricity bill   : PHP", A2con)
        st.write("Energy consumption :", Y2, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total2)
    st.write("Energy consumption:", Kh2, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1st app
if ask1 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * A1D

    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
    A1 = (A1F * (A1W * A1M))

    # TOTAL: watt/hour kada araw.
    wh1 = (A1)

    # TOTAL: Kilo-watt/hour kada month.
    Kh1 = ((wh1 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total1 = cost * Kh1

    # INDIVIDUALLY: para ma compute ang (cost) kada month.
    A1con = ((A1 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1]
    max_app = apps[0]
    for app in apps:
        if app > max_app:
            max_app = app
    if max_app == Y1:
        st.write("***")
        st.write("Name of appliance  :", A1N)
        st.write("Electricity bill   : PHP", A1con)
        st.write("Energy consumption :", Y1, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total1)
    st.write("Energy consumption:", Kh1, "kWh")
