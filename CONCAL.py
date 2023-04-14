# A()N ay Name
# A()M ay Quantity
# A()W ay Wattage
# A()B ay ilang Day in a Month ginagamit
# A()D ay ilang Hour in a Day ginagamit
import streamlit as st
st.title("Welcome to CONCAL!")
st.text("")
st.markdown("")

cost = st.number_input("The cost per kilowatt-hour in pesos:")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 1st app
A1N = st.text_input("Name of Appliance:")
A1M = st.number_input(f"How many {A1N} are you using?")
A1W = st.number_input(f"What is the wattage of {A1N} ?")
A1B = st.number_input("How many days in a month do you use this?")
while A1B > 31 or A1B < 1:
    A1B = st.number_input("How many days in a month do you use this?")

A1D = st.number_input("How many hours in a day do you use this?")
while A1D > 24 or A1D < 0.00001:
    A1D = st.number_input("How many hours in a day do you use this?")

ask1 = 2

if ask1 ==2:
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

    # Identify the high consumption appliance
    apps = [A1con]
    max_app = apps[0]
    for app in apps:
        if app > max_app:
            max_app = app
    if max_app == A1con:
        st.write("Ang may pinkamataas na konsumo ay ang(",A1N,")na may consumption na:",A1con)

    # OUTPUT
    st.write("(1)The consumption of", A1N, "is", A1con, "pesos")
    st.write("Your electricity bill is      :", total1, "pesos")
    st.write("Your energy consumption is    :", Kh1, "kWh")
