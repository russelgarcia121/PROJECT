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
st.write("How many", A1N, "are you using?")
A1M = st.number_input("")
st.write("What is the wattage of", A1N, "?")
A1W = st.number_input("")
A1B = st.number_input("How many days in a month do you use this?")
while A1B > 31 or A1B < 1:
    A1B = st.number_input("How many days in a month do you use this?")

A1D = st.number_input("How many hours in a day do you use this?")
while A1D > 24 or A1D < 0.00001:
    A1D = st.number_input("How many hours in a day do you use this?")

ask1 = 2
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# if ask1 == 1:  # add app2 (1st line)
#     A2N = str(input("Name of Appliance: "))
#     print("How many", A2N, " are you using?")
#     A2M = int(input("Type here:"))
#     print("What is the wattage of", A2N, "?")
#     A2W = float(input("Type here: "))
#     A2B = float(input("How many days in a month do you use this?"))

#     while A2B > 31 or A2B < 1:
#         A2B = float(input("How many days in a month do you use this?"))

#     A2D = float(input("How many hours in a day do you use this?"))

#     while A2D > 24 or A2D < 0.00001:  # ask for input until A()D is <=24 or >=1
#         A2D = float(input("How many hours in a day do you use this?"))

#     ask2 = int(
#         input("Add 3rd appliance (enter 1), No more appliances (enter 2): "))

#     while ask2 > 2 or ask2 < 1:  # ask for input until ask1 is 1 or 2
#         ask2 = int(
#             input("Add 3rd appliance (enter 1), No more appliances (enter 2): "))
# # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     if ask2 == 1:  # add app3 (2nd line)
#         A3N = str(input("Name of Appliance:"))
#         print("How many", A3N, " are you using?")
#         A3M = int(input("Type here:"))
#         print("What is the wattage of", A3N, "?")
#         A3W = float(input("Type here: "))
#         A3B = float(input("How many days in a month do you use this?"))

#         while A3B > 31 or A3B < 1:
#             A3B = float(input("How many days in a month do you use this?"))

#         A3D = float(input("How many hours in a day do you use this?"))

#         while A3D > 24 or A3D < 0.00001:  # ask for input until A()D is <=24 or >=1
#             A3D = float(input("How many hours in a day do you use this?"))

#         ask3 = int(
#             input("Add 4th appliance (enter 1), No more appliances (enter 2): "))

#         while ask3 > 2 or ask3 < 1:  # ask for input until ask1 is 1 or 2
#             ask3 = int(
#                 input("Add 4th appliance (enter 1), No more appliances (enter 2): "))
# # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         if ask3 == 1:  # add app4 (3rd line)
#             A4N = str(input("Name of Appliance: "))
#             print("How many", A4N, "are you using?")
#             A4M = int(input("Type here: "))
#             print("What is the wattage of", A4N, "?")
#             A4W = float(input("Type here: "))
#             A4B = float(input("How many days in a month do you use this?"))

#             while A4B > 31 or A4B < 1:
#                 A4B = float(input("How many days in a month do you use this?"))

#             A4D = float(input("How many hours in a day do you use this?"))

#             while A4D > 24 or A4D < 0.00001:  # ask for input until A()D is <=24 or >=1
#                 A4D = float(input("How many hours in a day do you use this?"))

#             ask4 = int(
#                 input("Add 5th appliance (enter 1), No more appliances (enter 2): "))

#             while ask4 > 2 or ask4 < 1:  # ask for input until ask1 is 1 or 2
#                 ask4 = int(
#                     input("Add 5th appliance (enter 1), No more appliances (enter 2): "))
# # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#             if ask4 == 1:  # add app5 (4th line)
#                 A5N = str(input("Name of Appliance: "))
#                 print("How many", A5N, "are you using?")
#                 A5M = int(input("Type here: "))
#                 print("What is the wattage of", A5N, "?")
#                 A5W = float(input("Type here: "))
#                 A5B = float(
#                     input("How many days in a month do you use this?"))

#                 while A5B > 31 or A5B < 1:
#                     A5B = float(
#                         input("How many days in a month do you use this?"))

#                 A5D = float(input("How many hours in a day do you use this?"))

#                 while A5D > 24 or A5D < 0.00001:  # ask for input until A()D is <=24 or >=1
#                     A5D = float(
#                         input("How many hours in a day do you use this?"))

#                 ask5 = 2
# # compute app1,2,3,4 and 5 (5th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                 if ask5 == 2:
#                     # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
#                     A1F = (A1B / 30) * A1D
#                     A2F = (A2B / 30) * A2D
#                     A3F = (A3B / 30) * A3D
#                     A4F = (A4B / 30) * A4D
#                     A5F = (A5B / 30) * A5D

#                     # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
#                     A1 = (A1F * (A1W * A1M))
#                     A2 = (A2F * (A2W * A2M))
#                     A3 = (A3F * (A3W * A3M))
#                     A4 = (A4F * (A4W * A4M))
#                     A5 = (A5F * (A5W * A5M))

#                     # TOTAL: watt/hour kada araw.
#                     wh4 = (A1 + A2 + A3 + A4 + A5)

#                     # TOTAL: Kilo-watt/hour kada month.
#                     Kh4 = ((wh4 * 30) / 1000)

#                     # TOTAL: para ma compute ang (cost) kada month.
#                     total4 = cost * Kh4

#                     # INDIVIDUALLY: para ma compute ang (cost) kada month.
#                     A1con = ((A1 * 30) / 1000) * cost
#                     A2con = ((A2 * 30) / 1000) * cost
#                     A3con = ((A3 * 30) / 1000) * cost
#                     A4con = ((A4 * 30) / 1000) * cost
#                     A5con = ((A5 * 30) / 1000) * cost

#                     # OUTPUT
#                     print("Your electricity bill is", total4, "pesos")
#                     print("Your energy consumption is", Kh4, "kWh")
#                     print("(1)The consumption of", A1N, "is:", A1con, "pesos")
#                     print("(2)The consumption of", A2N, "is:", A2con, "pesos")
#                     print("(3)The consumption of", A3N, "is:", A3con, "pesos")
#                     print("(4)The consumption of", A4N, "is:", A4con, "pesos")
#                     print("(5)The consumption of", A5N, "is:", A5con, "pesos")
#                     # print("The largest number in the list is:", max_app)

# # compute app1,2,3 and 4 (4th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#             if ask4 == 2:
#                 # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
#                 A1F = (A1B / 30) * A1D
#                 A2F = (A2B / 30) * A2D
#                 A3F = (A3B / 30) * A3D
#                 A4F = (A4B / 30) * A4D

#                 # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
#                 A1 = (A1F * (A1W * A1M))
#                 A2 = (A2F * (A2W * A2M))
#                 A3 = (A3F * (A3W * A3M))
#                 A4 = (A4F * (A4W * A4M))

#                 # TOTAL: watt/hour kada araw.
#                 wh4 = (A1 + A2 + A3 + A4)

#                 # TOTAL: Kilo-watt/hour kada month.
#                 Kh4 = ((wh4 * 30) / 1000)

#                 # TOTAL: para ma compute ang (cost) kada month.
#                 total4 = cost * Kh4

#                 # INDIVIDUALLY: para ma compute ang (cost) kada month.
#                 A1con = ((A1 * 30) / 1000) * cost
#                 A2con = ((A2 * 30) / 1000) * cost
#                 A3con = ((A3 * 30) / 1000) * cost
#                 A4con = ((A4 * 30) / 1000) * cost

#                 # OUTPUT
#                 print("Your electricity bill is", total4, "pesos")
#                 print("Your energy consumption is", Kh4, "kWh")
#                 print("(1)The consumption of", A1N, "is:", A1con, "pesos")
#                 print("(2)The consumption of", A2N, "is:", A2con, "pesos")
#                 print("(3)The consumption of", A3N, "is:", A3con, "pesos")
#                 print("(4)The consumption of", A4N, "is:", A4con, "pesos")
#                 # print("The largest number in the list is:", max_app)

# # compute app1,2 and 3 (3rd line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         if ask3 == 2:
#             # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
#             A1F = (A1B / 30) * A1D
#             A2F = (A2B / 30) * A2D
#             A3F = (A3B / 30) * A3D

#             # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
#             A1 = (A1F * (A1W * A1M))
#             A2 = (A2F * (A2W * A2M))
#             A3 = (A3F * (A3W * A3M))

#             # TOTAL: watt/hour kada araw.
#             wh3 = (A1 + A2 + A3)

#             # TOTAL: Kilo-watt/hour kada month.
#             Kh3 = ((wh3 * 30)/1000)

#             # TOTAL: para ma compute ang (cost) kada month.
#             total3 = cost * Kh3

#             # INDIVIDUALLY: para ma compute ang (cost) kada month.
#             A1con = ((A1 * 30) / 1000) * cost
#             A2con = ((A2 * 30) / 1000) * cost
#             A3con = ((A3 * 30) / 1000) * cost

#             # OUTPUT
#             print("Your electricity bill is", total3, "pesos")
#             print("Your energy consumption is", Kh3, "kWh")
#             print("(1)The consumption of", A1N, "is:", A1con, "pesos")
#             print("(2)The consumption of", A2N, "is:", A2con, "pesos")
#             print("(3)The consumption of", A3N, "is:", A3con, "pesos")
#             # print("The largest number in the list is:", max_app)

# # compute app1 and 2 (2nd line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#     if ask2 == 2:
#         # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
#         A1F = (A1B / 30) * A1D
#         A2F = (A2B / 30) * A2D

#         # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
#         A1 = (A1F * (A1W * A1M))
#         A2 = (A2F * (A2W * A2M))

#         # TOTAL: watt/hour kada araw.
#         wh1 = A1
#         wh2 = (A1 + A2)

#         # TOTAL: Kilo-watt/hour kada month.
#         Kh1 = (wh1*30) / 1000
#         Kh2 = (wh2 * 30) / 1000

#         # TOTAL: para ma compute ang (cost) kada month.
#         total1 = cost * Kh1
#         total2 = cost * Kh2

#         # INDIVIDUALLY: para ma compute ang (cost) kada month.
#         A1con = ((A1 * 30) / 1000) * cost
#         A2con = ((A2 * 30) / 1000) * cost

#         # Identify the high consumption appliance
#         apps = [A1con, A2con]
#         max_app = apps[0]
#         for app in apps:
#             if app > max_app:
#                 max_app = app
#         if max_app == A1con:
#             print("Ang may pinkamataas na konsumo ay ang", A1N)
#         if max_app == A2con:
#             print("Ang may pinkamataas na konsumo ay ang", A2N)

#         # OUTPUT
#         print("Your electricity bill is", total2, "pesos")
#         print("Your energy consumption is", Kh2, "kWh")
#         print("(1)The consumption of", A1N, "is:", A1con, "pesos")
#         print("(2)The consumption of", A2N, "is:", A2con, "pesos")
#         print("The largest number in the list is:", max_app)

# compute app1 (1st line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

    # Identify the high consumption appliance
    apps = [A1con]
    max_app = apps[0]
    for app in apps:
        if app > max_app:
            max_app = app
    if max_app == A1con:
        st.write("Ang may pinkamataas na konsumo ay ang", A1N)

    # OUTPUT
    st.write("Your electricity bill is", total1, "pesos")
    st.write("Your energy consumption is", Kh1, "kWh")
    st.write("(1)The consumption of", A1N, "is", A1con, "pesos")
