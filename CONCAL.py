import streamlit as st
st.title("Welcome to CONCAL!")
st.text("")
st.markdown("## **START!**")

cost = st.number_input("The cost per kilowatt-hour in pesos:")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 1st app
st.markdown("## **1st APPLIANCE!**")
A1N = st.text_input("Name of 1st appliance:")
if A1N:
    A1M = st.number_input(f"How many {A1N} are you using?")
    A1W = st.number_input(f"What is the wattage of {A1N} ?")
    A1B = st.number_input(f"How many days in a month do you use {A1N}?(1-31)")
    while A1B > 31 or A1B < 1:
        A1B = st.number_input(
            f"How many days in a month do you use {A1N}?(1-31)")

    A1D = st.number_input(f"How many hours in a day do you use {A1N}?(1-24)")
    while A1D > 24 or A1D < 0.00001:
        A1D = st.number_input(
            f"How many hours in a day do you use {A1N}?(1-24)")

    ask1 = st.number_input(
        "Add 2nd appliance (enter 1), No more appliances (enter 2): ")

    while ask1 > 2 or ask1 < 1:  # ask for input until ask1 is 1 or 2
        ask1 = st.number_input(
            "Add 2nd appliance (enter 1), No more appliances (enter 2): ")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if ask1 == 1:  # add app2 (1st line)
    st.markdown("## **2nd APPLIANCE!**")
    A2N = st.text_input("Name of 2nd appliance: ")
    if A2N:
        A2M = st.number_input(f"How many {A2N} are you using?")
        A2W = st.number_input(f"What is the wattage of {A2N} ?")
        A2B = st.number_input(
            f"How many days in a month do you use {A2N}?(1-31)")

        while A2B > 31 or A2B < 1:
            A2B = st.number_input(
                f"How many days in a month do you use {A2N}?(1-31)")

        A2D = st.number_input(
            f"How many hours in a day do you use {A2N}?(1-24)")

        while A2D > 24 or A2D < 0.00001:  # ask for input until A()D is <=24 or >=1
            A2D = st.number_input(
                f"How many hours in a day do you use {A2N}?(1-24)")

        ask2 = st.number_input(
            "Add 3rd appliance (enter 1), No more appliances (enter 2): ")

        while ask2 > 2 or ask2 < 1:  # ask for input until ask1 is 1 or 2
            ask2 = st.number_input(
                "Add 3rd appliance (enter 1), No more appliances (enter 2): ")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if ask2 == 1:  # add app3 (2nd line)
        st.markdown("## **3rd APPLIANCE!**")
        A3N = st.text_input("Name of 3rd appliance:")
        if A3N:
            A3M = st.number_input(f"How many {A3N} are you using?")
            A3W = st.number_input(f"What is the wattage of {A3N} ?")
            A3B = st.number_input(
                f"How many days in a month do you use {A3N}?(1-31)")

            while A3B > 31 or A3B < 1:
                A3B = st.number_input(
                    f"How many days in a month do you use {A3N}?(1-31)")

            A3D = st.number_input(
                f"How many hours in a day do you use {A3N}?(1-24)")

            while A3D > 24 or A3D < 0.00001:  # ask for input until A()D is <=24 or >=1
                A3D = st.number_input(
                    f"How many hours in a day do you use {A3N}?(1-24)")

            ask3 = st.number_input(
                "Add 4th appliance (enter 1), No more appliances (enter 2): ")

            while ask3 > 2 or ask3 < 1:  # ask for input until ask1 is 1 or 2
                ask3 = st.number_input(
                    "Add 4th appliance (enter 1), No more appliances (enter 2): ")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if ask3 == 1:  # add app4 (3rd line)
            st.markdown("## **4th APPLIANCE!**")
            A4N = st.text_input("Name of 4th appliance: ")
            if A4N:
                A4M = st.number_input(f"How many {A4N} are you using?")
                A4W = st.number_input(f"What is the wattage of {A4N} ?")
                A4B = st.number_input(
                    f"How many days in a month do you use {A4N}?(1-31)")

                while A4B > 31 or A4B < 1:
                    A4B = st.number_input(
                        f"How many days in a month do you use {A4N}?(1-31)")

                A4D = st.number_input(
                    f"How many hours in a day do you use {A4N}?(1-24)")

                while A4D > 24 or A4D < 0.00001:  # ask for input until A()D is <=24 or >=1
                    A4D = st.number_input(
                        f"How many hours in a day do you use {A4N}?(1-24)")

                ask4 = st.number_input(
                    "Add 5th appliance (enter 1), No more appliances (enter 2): ")

                while ask4 > 2 or ask4 < 1:  # ask for input until ask1 is 1 or 2
                    ask4 = st.number_input(
                        "Add 5th appliance (enter 1), No more appliances (enter 2): ")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if ask4 == 1:  # add app5 (4th line)
                st.markdown("## **5th APPLIANCE!**")
                A5N = st.text_input("Name of 5th appliance: ")
                if A5N:
                    A5M = st.number_input(f"How many {A5N} are you using?")
                    A5W = st.number_input(f"What is the wattage of {A5N} ?")
                    A5B = st.number_input(
                        f"How many days in a month do you use {A5N}?(1-31)")

                    while A5B > 31 or A5B < 1:
                        A5B = st.number_input(
                            f"How many days in a month do you use {A5N}?(1-31)")

                    A5D = st.number_input(
                        f"How many hours in a day do you use {A5N}?(1-24)")

                    while A5D > 24 or A5D < 0.00001:  # ask for input until A()D is <=24 or >=1
                        A5D = st.number_input(
                            f"How many hours in a day do you use {A5N}?(1-24)")

                    ask5 = st.number_input(
                        "Add 6th appliance (enter 1), No more appliances (enter 2): ")

                    while ask5 > 2 or ask5 < 1:  # ask for input until ask1 is 1 or 2
                        ask5 = st.number_input(
                            "Add 6th appliance (enter 1), No more appliances (enter 2): ")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                if ask5 == 1:  # add app6 (5th line)
                    st.markdown("## **6th APPLIANCE!**")
                    A6N = st.text_input("Name of 6th appliance: ")
                    if A6N:
                        A6M = st.number_input(f"How many {A6N} are you using?")
                        A6W = st.number_input(
                            f"What is the wattage of {A6N} ?")
                        A6B = st.number_input(
                            f"How many days in a month do you use {A6N}?(1-31)")

                        while A6B > 31 or A6B < 1:
                            A6B = st.number_input(
                                f"How many days in a month do you use {A6N}?(1-31)")

                        A6D = st.number_input(
                            f"How many hours in a day do you use {A6N}?(1-24)")

                        while A6D > 24 or A6D < 0.00001:  # ask for input until A()D is <=24 or >=1
                            A6D = st.number_input(
                                f"How many hours in a day do you use {A6N}?(1-24)")

                        ask6 = st.number_input(
                            "Add 7th appliance (enter 1), No more appliances (enter 2): ")

                        while ask6 > 2 or ask6 < 1:  # ask for input until ask1 is 1 or 2
                            ask6 = st.number_input(
                                "Add 7th appliance (enter 1), No more appliances (enter 2): ")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if ask6 == 1:  # add app7 (6th line)
                        st.markdown("## **7th APPLIANCE!**")
                        A7N = st.text_input("Name of 7th appliance: ")
                        if A7N:
                            A7M = st.number_input(
                                f"How many {A7N} are you using?")
                            A7W = st.number_input(
                                f"What is the wattage of {A7N} ?")
                            A7B = st.number_input(
                                f"How many days in a month do you use {A7N}?(1-31)")

                            while A7B > 31 or A7B < 1:
                                A7B = st.number_input(
                                    f"How many days in a month do you use {A7N}?(1-31)")

                            A7D = st.number_input(
                                f"How many hours in a day do you use {A7N}?(1-24)")

                            while A7D > 24 or A7D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                A7D = st.number_input(
                                    f"How many hours in a day do you use {A7N}?(1-24)")

                            ask7 = st.number_input(
                                "Add 8th appliance (enter 1), No more appliances (enter 2): ")

                            while ask7 > 2 or ask7 < 1:  # ask for input until ask1 is 1 or 2
                                ask7 = st.number_input(
                                    "Add 8th appliance (enter 1), No more appliances (enter 2): ")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        if ask7 == 1:  # add app8 (7th line)
                            st.markdown("## **8th APPLIANCE!**")
                            A8N = st.text_input("Name of 8th appliance: ")
                            if A8N:
                                A8M = st.number_input(
                                    f"How many {A8N} are you using?")
                                A8W = st.number_input(
                                    f"What is the wattage of {A8N} ?")
                                A8B = st.number_input(
                                    f"How many days in a month do you use {A8N}?(1-31)")

                                while A8B > 31 or A8B < 1:
                                    A8B = st.number_input(
                                        f"How many days in a month do you use {A8N}?(1-31)")

                                A8D = st.number_input(
                                    f"How many hours in a day do you use {A8N}?(1-24)")

                                while A8D > 24 or A8D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                    A8D = st.number_input(
                                        f"How many hours in a day do you use {A8N}?(1-24)")

                                ask8 = st.number_input(
                                    "Add 9th appliance (enter 1), No more appliances (enter 2): ")

                                while ask8 > 2 or ask8 < 1:  # ask for input until ask1 is 1 or 2
                                    ask8 = st.number_input(
                                        "Add 9th appliance (enter 1), No more appliances (enter 2): ")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                            if ask8 == 1:  # add app9 (8th line)
                                st.markdown("## **9th APPLIANCE!**")
                                A9N = st.text_input("Name of 9th appliance: ")
                                if A9N:
                                    A9M = st.number_input(
                                        f"How many {A9N} are you using?")
                                    A9W = st.number_input(
                                        f"What is the wattage of {A9N} ?")
                                    A9B = st.number_input(
                                        f"How many days in a month do you use {A9N}?(1-31)")

                                    while A9B > 31 or A9B < 1:
                                        A9B = st.number_input(
                                            f"How many days in a month do you use {A9N}?(1-31)")

                                    A9D = st.number_input(
                                        f"How many hours in a day do you use {A9N}?(1-24)")

                                    while A9D > 24 or A9D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                        A9D = st.number_input(
                                            f"How many hours in a day do you use {A9N}?(1-24)")

                                    ask9 = 2
                                # ask9 = st.number_input("Add 10th appliance (enter 1), No more appliances (enter 2): ")

                                # while ask9 > 2 or ask9 < 1:  # ask for input until ask1 is 1 or 2
                                #     ask9 = st.number_input("Add 10th appliance (enter 1), No more appliances (enter 2): ")

# The Great Wall of Code HAHAHAHAHAHAHA /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# The Great Wall of Code HAHAHAHAHAHAHA /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# The Great Wall of Code HAHAHAHAHAHAHA /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                            # compute app1,2,3,4,5,6,7,8,9 and 10 (10th line)
                            # if ask10 == 2:
                            #     # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                            #     A1F = (A1B / 30) * A1D
                            #     A2F = (A2B / 30) * A2D
                            #     A3F = (A3B / 30) * A3D
                            #     A4F = (A4B / 30) * A4D
                            #     A5F = (A5B / 30) * A5D
                            #     A6F = (A6B / 30) * A6D
                            #     A7F = (A7B / 30) * A7D
                            #     A8F = (A8B / 30) * A8D
                            #     A9F = (A9B / 30) * A9D
                            #     A10F = (A10B / 30) * A10D

                            #     # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                            #     A1 = (A1F * (A1W * A1M))
                            #     A2 = (A2F * (A2W * A2M))
                            #     A3 = (A3F * (A3W * A3M))
                            #     A4 = (A4F * (A4W * A4M))
                            #     A5 = (A5F * (A5W * A5M))
                            #     A6 = (A6F * (A6W * A6M))
                            #     A7 = (A7F * (A7W * A7M))
                            #     A8 = (A8F * (A8W * A8M))
                            #     A9 = (A9F * (A9W * A9M))
                            #     A10 = (A10F * (A10W * A10M))

                            #     # TOTAL: watt/hour kada araw.
                            #     wh4 = (A1 + A2 + A3 + A4 +
                            #            A5 + A6 + A7 + A8 + A9)

                            #     # TOTAL: Kilo-watt/hour kada month.
                            #     Kh4 = ((wh4 * 30) / 1000)

                            #     # TOTAL: para ma compute ang (cost) kada month.
                            #     total4 = cost * Kh4

                            #     # INDIVIDUALLY: para ma compute ang (cost) kada month.
                            #     A1con = ((A1 * 30) / 1000) * cost
                            #     A2con = ((A2 * 30) / 1000) * cost
                            #     A3con = ((A3 * 30) / 1000) * cost
                            #     A4con = ((A4 * 30) / 1000) * cost
                            #     A5con = ((A5 * 30) / 1000) * cost
                            #     A6con = ((A6 * 30) / 1000) * cost
                            #     A7con = ((A7 * 30) / 1000) * cost
                            #     A8con = ((A8 * 30) / 1000) * cost
                            #     A9con = ((A9 * 30) / 1000) * cost

                            #     # OUTPUT
                            #     print("Your electricity bill is",
                            #           total4, "pesos")
                            #     print("Your energy consumption is",
                            #           Kh4, "kWh")
                            #     print("(1)The consumption of",
                            #           A1N, "is:", A1con, "pesos")
                            #     print("(2)The consumption of", A2N,
                            #           "is:", A2con, "pesos")
                            #     print("(3)The consumption of", A3N,
                            #           "is:", A3con, "pesos")
                            #     print("(4)The consumption of", A4N,
                            #           "is:", A4con, "pesos")
                            #     print("(5)The consumption of", A5N,
                            #           "is:", A5con, "pesos")
                            #     print("(6)The consumption of", A6N,
                            #           "is:", A6con, "pesos")
                            #     print("(7)The consumption of", A7N,
                            #           "is:", A7con, "pesos")
                            #     print("(8)The consumption of", A8N,
                            #           "is:", A8con, "pesos")
                            #     print("(9)The consumption of", A9N,
                            #           "is:", A9con, "pesos")
                                # print("The largest number in the list is:", max_app)
# compute app1,2,3,4,5,6,7,8 and 9 (9th line)# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                if ask9 == 2:
                                    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                                    A1F = (A1B / 30) * A1D
                                    A2F = (A2B / 30) * A2D
                                    A3F = (A3B / 30) * A3D
                                    A4F = (A4B / 30) * A4D
                                    A5F = (A5B / 30) * A5D
                                    A6F = (A6B / 30) * A6D
                                    A7F = (A7B / 30) * A7D
                                    A8F = (A8B / 30) * A8D
                                    A9F = (A9B / 30) * A9D

                                    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                    A1 = (A1F * (A1W * A1M))
                                    A2 = (A2F * (A2W * A2M))
                                    A3 = (A3F * (A3W * A3M))
                                    A4 = (A4F * (A4W * A4M))
                                    A5 = (A5F * (A5W * A5M))
                                    A6 = (A6F * (A6W * A6M))
                                    A7 = (A7F * (A7W * A7M))
                                    A8 = (A8F * (A8W * A8M))
                                    # ///////////////////////////////////////////////////
                                    A9 = (A9F * (A9W * A9M))

                                    # TOTAL: watt/hour kada araw.
                                    wh4 = (A1 + A2 + A3 + A4 +
                                           A5 + A6 + A7 + A8 + A9)

                                    # TOTAL: Kilo-watt/hour kada month.
                                    Kh4 = ((wh4 * 30) / 1000)

                                    # TOTAL: para ma compute ang (cost) kada month.
                                    total4 = cost * Kh4

                                    # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                    A1con = ((A1 * 30) / 1000) * cost
                                    A2con = ((A2 * 30) / 1000) * cost
                                    A3con = ((A3 * 30) / 1000) * cost
                                    A4con = ((A4 * 30) / 1000) * cost
                                    A5con = ((A5 * 30) / 1000) * cost
                                    A6con = ((A6 * 30) / 1000) * cost
                                    A7con = ((A7 * 30) / 1000) * cost
                                    A8con = ((A8 * 30) / 1000) * cost
                                    A9con = ((A9 * 30) / 1000) * cost

                                    # OUTPUT1
                                    st.markdown("## **THE RESULTS:**")
                                    # OUTPUT2

                                    st.write("(1)The consumption of",
                                             A1N, "is:", A1con, "pesos")
                                    st.write("(2)The consumption of", A2N,
                                             "is:", A2con, "pesos")
                                    st.write("(3)The consumption of", A3N,
                                             "is:", A3con, "pesos")
                                    st.write("(4)The consumption of", A4N,
                                             "is:", A4con, "pesos")
                                    st.write("(5)The consumption of", A5N,
                                             "is:", A5con, "pesos")
                                    st.write("(6)The consumption of", A6N,
                                             "is:", A6con, "pesos")
                                    st.write("(7)The consumption of", A7N,
                                             "is:", A7con, "pesos")
                                    st.write("(8)The consumption of", A8N,
                                             "is:", A8con, "pesos")
                                    st.write("(9)The consumption of", A9N,
                                             "is:", A9con, "pesos")
                                    st.write("Your electricity bill is",
                                             total4, "pesos")
                                    st.write("Your energy consumption is",
                                             Kh4, "kWh")
                                    # print("The largest number in the list is:", max_app)
# compute app1,2,3,4,5,6,7 and 8 (8th line)# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                            if ask8 == 2:
                                # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                                A1F = (A1B / 30) * A1D
                                A2F = (A2B / 30) * A2D
                                A3F = (A3B / 30) * A3D
                                A4F = (A4B / 30) * A4D
                                A5F = (A5B / 30) * A5D
                                A6F = (A6B / 30) * A6D
                                A7F = (A7B / 30) * A7D
                                A8F = (A8B / 30) * A8D

                                # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                A1 = (A1F * (A1W * A1M))
                                A2 = (A2F * (A2W * A2M))
                                A3 = (A3F * (A3W * A3M))
                                A4 = (A4F * (A4W * A4M))
                                A5 = (A5F * (A5W * A5M))
                                A6 = (A6F * (A6W * A6M))
                                A7 = (A7F * (A7W * A7M))
                                A8 = (A8F * (A8W * A8M))

                                # TOTAL: watt/hour kada araw.
                                wh4 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8)

                                # TOTAL: Kilo-watt/hour kada month.
                                Kh4 = ((wh4 * 30) / 1000)

                                # TOTAL: para ma compute ang (cost) kada month.
                                total4 = cost * Kh4

                                # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                A1con = ((A1 * 30) / 1000) * cost
                                A2con = ((A2 * 30) / 1000) * cost
                                A3con = ((A3 * 30) / 1000) * cost
                                A4con = ((A4 * 30) / 1000) * cost
                                A5con = ((A5 * 30) / 1000) * cost
                                A6con = ((A6 * 30) / 1000) * cost
                                A7con = ((A7 * 30) / 1000) * cost
                                A8con = ((A8 * 30) / 1000) * cost

                                # OUTPUT1
                                st.markdown("## **THE RESULTS:**")
                                # OUTPUT2
                                st.write("(1)The consumption of",
                                         A1N, "is:", A1con, "pesos")
                                st.write("(2)The consumption of", A2N,
                                         "is:", A2con, "pesos")
                                st.write("(3)The consumption of", A3N,
                                         "is:", A3con, "pesos")
                                st.write("(4)The consumption of", A4N,
                                         "is:", A4con, "pesos")
                                st.write("(5)The consumption of", A5N,
                                         "is:", A5con, "pesos")
                                st.write("(6)The consumption of", A6N,
                                         "is:", A6con, "pesos")
                                st.write("(7)The consumption of", A7N,
                                         "is:", A7con, "pesos")
                                st.write("(8)The consumption of", A8N,
                                         "is:", A8con, "pesos")
                                st.write("Your electricity bill is",
                                         total4, "pesos")
                                st.write(
                                    "Your energy consumption is", Kh4, "kWh")
                                # print("The largest number in the list is:", max_app)

# compute app1,2,3,4,5,6 and 7 (7th line) # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        if ask7 == 2:
                            # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                            A1F = (A1B / 30) * A1D
                            A2F = (A2B / 30) * A2D
                            A3F = (A3B / 30) * A3D
                            A4F = (A4B / 30) * A4D
                            A5F = (A5B / 30) * A5D
                            A6F = (A6B / 30) * A6D
                            A7F = (A7B / 30) * A7D

                            # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                            A1 = (A1F * (A1W * A1M))
                            A2 = (A2F * (A2W * A2M))
                            A3 = (A3F * (A3W * A3M))
                            A4 = (A4F * (A4W * A4M))
                            A5 = (A5F * (A5W * A5M))
                            A6 = (A6F * (A6W * A6M))
                            A7 = (A7F * (A7W * A7M))

                            # TOTAL: watt/hour kada araw.
                            wh4 = (A1 + A2 + A3 + A4 + A5 + A6 + A7)

                            # TOTAL: Kilo-watt/hour kada month.
                            Kh4 = ((wh4 * 30) / 1000)

                            # TOTAL: para ma compute ang (cost) kada month.
                            total4 = cost * Kh4

                            # INDIVIDUALLY: para ma compute ang (cost) kada month.
                            A1con = ((A1 * 30) / 1000) * cost
                            A2con = ((A2 * 30) / 1000) * cost
                            A3con = ((A3 * 30) / 1000) * cost
                            A4con = ((A4 * 30) / 1000) * cost
                            A5con = ((A5 * 30) / 1000) * cost
                            A6con = ((A6 * 30) / 1000) * cost
                            A7con = ((A7 * 30) / 1000) * cost

                            # OUTPUT1
                            st.markdown("## **THE RESULTS:**")
                            # OUTPUT2
                            st.write("(1)The consumption of",
                                     A1N, "is:", A1con, "pesos")
                            st.write("(2)The consumption of", A2N,
                                     "is:", A2con, "pesos")
                            st.write("(3)The consumption of", A3N,
                                     "is:", A3con, "pesos")
                            st.write("(4)The consumption of", A4N,
                                     "is:", A4con, "pesos")
                            st.write("(5)The consumption of", A5N,
                                     "is:", A5con, "pesos")
                            st.write("(6)The consumption of", A6N,
                                     "is:", A6con, "pesos")
                            st.write("(7)The consumption of", A7N,
                                     "is:", A7con, "pesos")
                            st.write("Your electricity bill is",
                                     total4, "pesos")
                            st.write("Your energy consumption is", Kh4, "kWh")
                            # print("The largest number in the list is:", max_app)

# compute app1,2,3,4,5 and 6 (6th line) ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if ask6 == 2:
                        # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                        A1F = (A1B / 30) * A1D
                        A2F = (A2B / 30) * A2D
                        A3F = (A3B / 30) * A3D
                        A4F = (A4B / 30) * A4D
                        A5F = (A5B / 30) * A5D
                        A6F = (A6B / 30) * A6D

                        # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                        A1 = (A1F * (A1W * A1M))
                        A2 = (A2F * (A2W * A2M))
                        A3 = (A3F * (A3W * A3M))
                        A4 = (A4F * (A4W * A4M))
                        A5 = (A5F * (A5W * A5M))
                        A6 = (A6F * (A6W * A6M))

                        # TOTAL: watt/hour kada araw.
                        wh4 = (A1 + A2 + A3 + A4 + A5 + A6)

                        # TOTAL: Kilo-watt/hour kada month.
                        Kh4 = ((wh4 * 30) / 1000)

                        # TOTAL: para ma compute ang (cost) kada month.
                        total4 = cost * Kh4

                        # INDIVIDUALLY: para ma compute ang (cost) kada month.
                        A1con = ((A1 * 30) / 1000) * cost
                        A2con = ((A2 * 30) / 1000) * cost
                        A3con = ((A3 * 30) / 1000) * cost
                        A4con = ((A4 * 30) / 1000) * cost
                        A5con = ((A5 * 30) / 1000) * cost
                        A6con = ((A6 * 30) / 1000) * cost

                        # OUTPUT1
                        st.markdown("## **THE RESULTS:**")
                        # OUTPUT2
                        st.write("(1)The consumption of",
                                 A1N, "is:", A1con, "pesos")
                        st.write("(2)The consumption of",
                                 A2N, "is:", A2con, "pesos")
                        st.write("(3)The consumption of",
                                 A3N, "is:", A3con, "pesos")
                        st.write("(4)The consumption of",
                                 A4N, "is:", A4con, "pesos")
                        st.write("(5)The consumption of",
                                 A5N, "is:", A5con, "pesos")
                        st.write("(6)The consumption of",
                                 A6N, "is:", A6con, "pesos")
                        st.write("Your electricity bill is", total4, "pesos")
                        st.write("Your energy consumption is", Kh4, "kWh")
                        # print("The largest number in the list is:", max_app)

# compute app1,2,3,4 and 5 (5th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                if ask5 == 2:
                    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                    A1F = (A1B / 30) * A1D
                    A2F = (A2B / 30) * A2D
                    A3F = (A3B / 30) * A3D
                    A4F = (A4B / 30) * A4D
                    A5F = (A5B / 30) * A5D

                    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                    A1 = (A1F * (A1W * A1M))
                    A2 = (A2F * (A2W * A2M))
                    A3 = (A3F * (A3W * A3M))
                    A4 = (A4F * (A4W * A4M))
                    A5 = (A5F * (A5W * A5M))

                    # TOTAL: watt/hour kada araw.
                    wh4 = (A1 + A2 + A3 + A4 + A5)

                    # TOTAL: Kilo-watt/hour kada month.
                    Kh4 = ((wh4 * 30) / 1000)

                    # TOTAL: para ma compute ang (cost) kada month.
                    total4 = cost * Kh4

                    # INDIVIDUALLY: para ma compute ang (cost) kada month.
                    A1con = ((A1 * 30) / 1000) * cost
                    A2con = ((A2 * 30) / 1000) * cost
                    A3con = ((A3 * 30) / 1000) * cost
                    A4con = ((A4 * 30) / 1000) * cost
                    A5con = ((A5 * 30) / 1000) * cost

                    # OUTPUT1
                    st.markdown("## **THE RESULTS:**")
                    # OUTPUT2
                    st.write("(1)The consumption of",
                             A1N, "is:", A1con, "pesos")
                    st.write("(2)The consumption of",
                             A2N, "is:", A2con, "pesos")
                    st.write("(3)The consumption of",
                             A3N, "is:", A3con, "pesos")
                    st.write("(4)The consumption of",
                             A4N, "is:", A4con, "pesos")
                    st.write("(5)The consumption of",
                             A5N, "is:", A5con, "pesos")
                    st.write("Your electricity bill is", total4, "pesos")
                    st.write("Your energy consumption is", Kh4, "kWh")
                    # print("The largest number in the list is:", max_app)

# compute app1,2,3 and 4 (4th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if ask4 == 2:
                # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                A1F = (A1B / 30) * A1D
                A2F = (A2B / 30) * A2D
                A3F = (A3B / 30) * A3D
                A4F = (A4B / 30) * A4D

                # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                A1 = (A1F * (A1W * A1M))
                A2 = (A2F * (A2W * A2M))
                A3 = (A3F * (A3W * A3M))
                A4 = (A4F * (A4W * A4M))

                # TOTAL: watt/hour kada araw.
                wh4 = (A1 + A2 + A3 + A4)

                # TOTAL: Kilo-watt/hour kada month.
                Kh4 = ((wh4 * 30) / 1000)

                # TOTAL: para ma compute ang (cost) kada month.
                total4 = cost * Kh4

                # INDIVIDUALLY: para ma compute ang (cost) kada month.
                A1con = ((A1 * 30) / 1000) * cost
                A2con = ((A2 * 30) / 1000) * cost
                A3con = ((A3 * 30) / 1000) * cost
                A4con = ((A4 * 30) / 1000) * cost

                # OUTPUT1
                st.markdown("## **THE RESULTS:**")
                # OUTPUT2
                st.write("(1)The consumption of", A1N, "is:", A1con, "pesos")
                st.write("(2)The consumption of", A2N, "is:", A2con, "pesos")
                st.write("(3)The consumption of", A3N, "is:", A3con, "pesos")
                st.write("(4)The consumption of", A4N, "is:", A4con, "pesos")
                st.write("Your electricity bill is", total4, "pesos")
                st.write("Your energy consumption is", Kh4, "kWh")
                # print("The largest number in the list is:", max_app)

# compute app1,2 and 3 (3rd line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if ask3 == 2:
            # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
            A1F = (A1B / 30) * A1D
            A2F = (A2B / 30) * A2D
            A3F = (A3B / 30) * A3D

            # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
            A1 = (A1F * (A1W * A1M))
            A2 = (A2F * (A2W * A2M))
            A3 = (A3F * (A3W * A3M))

            # TOTAL: watt/hour kada araw.
            wh3 = (A1 + A2 + A3)

            # TOTAL: Kilo-watt/hour kada month.
            Kh3 = ((wh3 * 30)/1000)

            # TOTAL: para ma compute ang (cost) kada month.
            total3 = cost * Kh3

            # INDIVIDUALLY: para ma compute ang (cost) kada month.
            A1con = ((A1 * 30) / 1000) * cost
            A2con = ((A2 * 30) / 1000) * cost
            A3con = ((A3 * 30) / 1000) * cost

            # OUTPUT1
            st.markdown("## **THE RESULTS:**")
            # OUTPUT2
            st.write("(1)The consumption of", A1N, "is:", A1con, "pesos")
            st.write("(2)The consumption of", A2N, "is:", A2con, "pesos")
            st.write("(3)The consumption of", A3N, "is:", A3con, "pesos")
            st.write("Your electricity bill is", total3, "pesos")
            st.write("Your energy consumption is", Kh3, "kWh")
            # print("The largest number in the list is:", max_app)

# compute app1 and 2 (2nd line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if ask2 == 2:
        # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
        A1F = (A1B / 30) * A1D
        A2F = (A2B / 30) * A2D

        # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
        A1 = (A1F * (A1W * A1M))
        A2 = (A2F * (A2W * A2M))

        # TOTAL: watt/hour kada araw.
        wh1 = A1
        wh2 = (A1 + A2)

        # TOTAL: Kilo-watt/hour kada month.
        Kh1 = (wh1*30) / 1000
        Kh2 = (wh2 * 30) / 1000

        # TOTAL: para ma compute ang (cost) kada month.
        total1 = cost * Kh1
        total2 = cost * Kh2

        # INDIVIDUALLY: para ma compute ang (cost) kada month.
        A1con = ((A1 * 30) / 1000) * cost
        A2con = ((A2 * 30) / 1000) * cost

        # Identify the high consumption appliance
        apps = [A1con, A2con]
        max_app = apps[0]
        for app in apps:
            if app > max_app:
                max_app = app
        if max_app == A1con:
            st.write("Ang may pinkamataas na konsumo ay ang", A1N)
        if max_app == A2con:
            st.write("Ang may pinkamataas na konsumo ay ang", A2N)

        # OUTPUT1
        st.markdown("## **THE RESULTS:**")
        # OUTPUT2
        st.write("(1)The consumption of", A1N, "is:", A1con, "pesos")
        st.write("(2)The consumption of", A2N, "is:", A2con, "pesos")
        st.write("The largest number in the list is:", max_app)
        st.write("Your electricity bill is", total2, "pesos")
        st.write("Your energy consumption is", Kh2, "kWh")

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
        st.write("The appliance with the highest consumption is the (",
                 A1N, ") with a consumption of:", A1con, "kWh")

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # OUTPUT2
    st.write("(1)The consumption of", A1N, "is", A1con, "pesos")
    st.write("Your electricity bill is      :", total1, "pesos")
    st.write("Your energy consumption is    :", Kh1, "kWh")
