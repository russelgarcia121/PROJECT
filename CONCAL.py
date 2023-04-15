import streamlit as st
st.title("Welcome to CONCAL!")
st.text("")
st.markdown("## **START!**")

cost = st.number_input("The cost per kilowatt-hour in pesos:")
ask1=0
ask2=0
ask3=0
ask4=0
ask5=0
ask6=0
ask7=0
ask8=0
ask9=0
ask10=0
ask11=0
ask12=0
ask13=0
ask14=0
ask15=0
ask16=0
ask17=0
ask18=0
ask19=0
ask20=0
ask21=0
ask22=0
ask23=0
ask24=0
ask25=0
ask26=0
ask27=0
ask28=0
ask29=0

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 1st app
st.markdown("## **1st APPLIANCE!**")
A1N = st.text_input("Name of 1st appliance:")
if A1N:
    A1M = st.number_input(f"How many {A1N} are you using?", value=0, step=1)
    A1W = st.number_input(f"What is the wattage of {A1N}?(watt)")
    A1B = st.number_input(f"How many days in a month do you use {A1N}?(1-31)", value=0, step=1)
    # while A1B > 31 or A1B < 1:
    #     A1B = st.number_input(
    #         f"How many days in a month do you use {A1N}?(1-31)", value=0, step=1)

    A1D = st.number_input(f"How many hours in a day do you use {A1N}?(1-24)")
    # while A1D > 24 or A1D < 0.00001:
    #     A1D = st.number_input(
    #         f"How many hours in a day do you use {A1N}?(1-24)")

    ask1 = st.number_input(
        "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)

    # while ask1 > 2 or ask1 < 1:  # ask for input until ask1 is 1 or 2
    #     ask1 = st.number_input(
    #         "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
        
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if ask1 == 1:  # add app2 (1st line)
    st.markdown("## **2nd APPLIANCE!**")
    A2N = st.text_input("Name of 2nd appliance: ")
    if A2N:
        A2M = st.number_input(f"How many {A2N} are you using?",value=0, step=1)
        A2W = st.number_input(f"What is the wattage of {A2N}?(watt)")
        A2B = st.number_input(
            f"How many days in a month do you use {A2N}?(1-31)",value=0, step=1)

        while A2B > 31 or A2B < 1:
            A2B = st.number_input(
                f"How many days in a month do you use {A2N}?(1-31)",value=0, step=1)

        A2D = st.number_input(
            f"How many hours in a day do you use {A2N}?(1-24)")

        while A2D > 24 or A2D < 0.00001:  # ask for input until A()D is <=24 or >=1
            A2D = st.number_input(
                f"How many hours in a day do you use {A2N}?(1-24)")

        ask2 = st.number_input(
            "Add 3rd appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

        while ask2 > 2 or ask2 < 1:  # ask for input until ask1 is 1 or 2
            ask2 = st.number_input(
                "Add 3rd appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if ask2 == 1:  # add app3 (2nd line)
        st.markdown("## **3rd APPLIANCE!**")
        A3N = st.text_input("Name of 3rd appliance:")
        if A3N:
            A3M = st.number_input(f"How many {A3N} are you using?",value=0, step=1)
            A3W = st.number_input(f"What is the wattage of {A3N}?(watt)")
            A3B = st.number_input(
                f"How many days in a month do you use {A3N}?(1-31)",value=0, step=1)

            while A3B > 31 or A3B < 1:
                A3B = st.number_input(
                    f"How many days in a month do you use {A3N}?(1-31)",value=0, step=1)

            A3D = st.number_input(
                f"How many hours in a day do you use {A3N}?(1-24)")

            while A3D > 24 or A3D < 0.00001:  # ask for input until A()D is <=24 or >=1
                A3D = st.number_input(
                    f"How many hours in a day do you use {A3N}?(1-24)")

            ask3 = st.number_input(
                "Add 4th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

            while ask3 > 2 or ask3 < 1:  # ask for input until ask1 is 1 or 2
                ask3 = st.number_input(
                    "Add 4th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if ask3 == 1:  # add app4 (3rd line)
            st.markdown("## **4th APPLIANCE!**")
            A4N = st.text_input("Name of 4th appliance: ")
            if A4N:
                A4M = st.number_input(f"How many {A4N} are you using?",value=0, step=1)
                A4W = st.number_input(f"What is the wattage of {A4N}?(watt)")
                A4B = st.number_input(
                    f"How many days in a month do you use {A4N}?(1-31)",value=0, step=1)

                while A4B > 31 or A4B < 1:
                    A4B = st.number_input(
                        f"How many days in a month do you use {A4N}?(1-31)",value=0, step=1)

                A4D = st.number_input(
                    f"How many hours in a day do you use {A4N}?(1-24)")

                while A4D > 24 or A4D < 0.00001:  # ask for input until A()D is <=24 or >=1
                    A4D = st.number_input(
                        f"How many hours in a day do you use {A4N}?(1-24)")

                ask4 = st.number_input(
                    "Add 5th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                while ask4 > 2 or ask4 < 1:  # ask for input until ask1 is 1 or 2
                    ask4 = st.number_input(
                        "Add 5th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if ask4 == 1:  # add app5 (4th line)
                st.markdown("## **5th APPLIANCE!**")
                A5N = st.text_input("Name of 5th appliance: ")
                if A5N:
                    A5M = st.number_input(f"How many {A5N} are you using?",value=0, step=1)
                    A5W = st.number_input(
                        f"What is the wattage of {A5N}?(watt)")
                    A5B = st.number_input(
                        f"How many days in a month do you use {A5N}?(1-31)",value=0, step=1)

                    while A5B > 31 or A5B < 1:
                        A5B = st.number_input(
                            f"How many days in a month do you use {A5N}?(1-31)",value=0, step=1)

                    A5D = st.number_input(
                        f"How many hours in a day do you use {A5N}?(1-24)")

                    while A5D > 24 or A5D < 0.00001:  # ask for input until A()D is <=24 or >=1
                        A5D = st.number_input(
                            f"How many hours in a day do you use {A5N}?(1-24)")

                    ask5 = st.number_input(
                        "Add 6th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                    while ask5 > 2 or ask5 < 1:  # ask for input until ask1 is 1 or 2
                        ask5 = st.number_input(
                            "Add 6th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                if ask5 == 1:  # add app6 (5th line)
                    st.markdown("## **6th APPLIANCE!**")
                    A6N = st.text_input("Name of 6th appliance: ")
                    if A6N:
                        A6M = st.number_input(f"How many {A6N} are you using?",value=0, step=1)
                        A6W = st.number_input(
                            f"What is the wattage of {A6N}?(watt)")
                        A6B = st.number_input(
                            f"How many days in a month do you use {A6N}?(1-31)",value=0, step=1)

                        while A6B > 31 or A6B < 1:
                            A6B = st.number_input(
                                f"How many days in a month do you use {A6N}?(1-31)",value=0, step=1)

                        A6D = st.number_input(
                            f"How many hours in a day do you use {A6N}?(1-24)")

                        while A6D > 24 or A6D < 0.00001:  # ask for input until A()D is <=24 or >=1
                            A6D = st.number_input(
                                f"How many hours in a day do you use {A6N}?(1-24)")

                        ask6 = st.number_input(
                            "Add 7th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                        while ask6 > 2 or ask6 < 1:  # ask for input until ask1 is 1 or 2
                            ask6 = st.number_input(
                                "Add 7th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if ask6 == 1:  # add app7 (6th line)
                        st.markdown("## **7th APPLIANCE!**")
                        A7N = st.text_input("Name of 7th appliance: ")
                        if A7N:
                            A7M = st.number_input(
                                f"How many {A7N} are you using?",value=0, step=1)
                            A7W = st.number_input(
                                f"What is the wattage of {A7N}?(watt)")
                            A7B = st.number_input(
                                f"How many days in a month do you use {A7N}?(1-31)",value=0, step=1)

                            while A7B > 31 or A7B < 1:
                                A7B = st.number_input(
                                    f"How many days in a month do you use {A7N}?(1-31)",value=0, step=1)

                            A7D = st.number_input(
                                f"How many hours in a day do you use {A7N}?(1-24)")

                            while A7D > 24 or A7D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                A7D = st.number_input(
                                    f"How many hours in a day do you use {A7N}?(1-24)")

                            ask7 = st.number_input(
                                "Add 8th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                            while ask7 > 2 or ask7 < 1:  # ask for input until ask1 is 1 or 2
                                ask7 = st.number_input(
                                    "Add 8th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        if ask7 == 1:  # add app8 (7th line)
                            st.markdown("## **8th APPLIANCE!**")
                            A8N = st.text_input("Name of 8th appliance: ")
                            if A8N:
                                A8M = st.number_input(
                                    f"How many {A8N} are you using?",value=0, step=1)
                                A8W = st.number_input(
                                    f"What is the wattage of {A8N}?(watt)")
                                A8B = st.number_input(
                                    f"How many days in a month do you use {A8N}?(1-31)",value=0, step=1)

                                while A8B > 31 or A8B < 1:
                                    A8B = st.number_input(
                                        f"How many days in a month do you use {A8N}?(1-31)",value=0, step=1)

                                A8D = st.number_input(
                                    f"How many hours in a day do you use {A8N}?(1-24)")

                                while A8D > 24 or A8D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                    A8D = st.number_input(
                                        f"How many hours in a day do you use {A8N}?(1-24)")

                                ask8 = st.number_input(
                                    "Add 9th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                                while ask8 > 2 or ask8 < 1:  # ask for input until ask1 is 1 or 2
                                    ask8 = st.number_input(
                                        "Add 9th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                            if ask8 == 1:  # add app9 (8th line)
                                st.markdown("## **9th APPLIANCE!**")
                                A9N = st.text_input("Name of 9th appliance: ")
                                if A9N:
                                    A9M = st.number_input(
                                        f"How many {A9N} are you using?",value=0, step=1)
                                    A9W = st.number_input(
                                        f"What is the wattage of {A9N}?(watt)")
                                    A9B = st.number_input(
                                        f"How many days in a month do you use {A9N}?(1-31)",value=0, step=1)

                                    while A9B > 31 or A9B < 1:
                                        A9B = st.number_input(
                                            f"How many days in a month do you use {A9N}?(1-31)",value=0, step=1)

                                    A9D = st.number_input(
                                        f"How many hours in a day do you use {A9N}?(1-24)")

                                    while A9D > 24 or A9D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                        A9D = st.number_input(
                                            f"How many hours in a day do you use {A9N}?(1-24)")

                                    ask9 = st.number_input(
                                        "Add 10th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                                    while ask9 > 2 or ask9 < 1:  # ask for input until ask1 is 1 or 2
                                        ask9 = st.number_input(
                                            "Add 10th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                if ask9 == 1:  # add app10 (9th line)
                                    st.markdown("## **10th APPLIANCE!**")
                                    A10N = st.text_input(
                                        "Name of 10th appliance: ")
                                    if A10N:
                                        A10M = st.number_input(
                                            f"How many {A10N} are you using?",value=0, step=1)
                                        A10W = st.number_input(
                                            f"What is the wattage of {A10N}?(watt)")
                                        A10B = st.number_input(
                                            f"How many days in a month do you use {A10N}?(1-31)",value=0, step=1)

                                        while A10B > 31 or A10B < 1:
                                            A10B = st.number_input(
                                                f"How many days in a month do you use {A10N}?(1-31)",value=0, step=1)

                                        A10D = st.number_input(
                                            f"How many hours in a day do you use {A10N}?(1-24)")

                                        while A10D > 24 or A10D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                            A10D = st.number_input(
                                                f"How many hours in a day do you use {A10N}?(1-24)")

                                        ask10 = st.number_input(
                                            "Add 11th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                                        while ask10 > 2 or ask10 < 1:  # ask for input until ask1 is 1 or 2
                                            ask2 = st.number_input(
                                                "Add 11th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
         # dito na
                                    if ask10 == 1:  # add app11 (10th line)
                                        st.markdown("## **11th APPLIANCE!**")
                                        A11N = st.text_input(
                                            "Name of 11th appliance:")
                                        if A11N:
                                            A11M = st.number_input(
                                                f"How many {A11N} are you using?",value=0, step=1)
                                            A11W = st.number_input(
                                                f"What is the wattage of {A11N}?(watt)")
                                            A11B = st.number_input(
                                                f"How many days in a month do you use {A11N}?(1-31)",value=0, step=1)

                                            while A11B > 31 or A11B < 1:
                                                A11B = st.number_input(
                                                    f"How many days in a month do you use {A11N}?(1-31)",value=0, step=1)
                                            A11D = st.number_input(
                                                f"How many hours in a day do you use {A11N}?(1-24)")

                                            while A11D > 24 or A11D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                                A3D = st.number_input(
                                                    f"How many hours in a day do you use {A11N}?(1-24)")

                                            ask11 = st.number_input(
                                                "Add 12th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                                            while ask11 > 2 or ask11 < 1:  # ask for input until ask1 is 1 or 2
                                                ask11 = st.number_input(
                                                    "Add 12th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                        if ask11 == 1:  # add app12 (11th line)
                                            st.markdown(
                                                "## **12th APPLIANCE!**")
                                            A12N = st.text_input(
                                                "Name of 12th appliance: ")
                                            if A12N:
                                                A12M = st.number_input(
                                                    f"How many {A12N} are you using?",value=0, step=1)
                                                A12W = st.number_input(
                                                    f"What is the wattage of {A12N}?(watt)")
                                                A12B = st.number_input(
                                                    f"How many days in a month do you use {A12N}?(1-31)",value=0, step=1)

                                                while A12B > 31 or A12B < 1:
                                                    A12B = st.number_input(
                                                        f"How many days in a month do you use {A12N}?(1-31)",value=0, step=1)

                                                A12D = st.number_input(
                                                    f"How many hours in a day do you use {A12N}?(1-24)")

                                                while A12D > 24 or A12D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                                    A12D = st.number_input(
                                                        f"How many hours in a day do you use {A12N}?(1-24)")

                                                ask12 = st.number_input(
                                                    "Add 13th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                                                while ask12 > 2 or ask12 < 1:  # ask for input until ask1 is 1 or 2
                                                    ask12 = st.number_input(
                                                        "Add 13th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
 # add app1 to 13 (12th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                            if ask12 == 1:
                                                st.markdown(
                                                    "## **13th APPLIANCE!**")
                                                A13N = st.text_input(
                                                    "Name of 13th appliance: ")
                                                if A13N:
                                                    A13M = st.number_input(
                                                        f"How many {A13N} are you using?",value=0, step=1)
                                                    A13W = st.number_input(
                                                        f"What is the wattage of {A13N}?(watt)")
                                                    A13B = st.number_input(
                                                        f"How many days in a month do you use {A13N}?(1-31)",value=0, step=1)

                                                    while A13B > 31 or A13B < 1:
                                                        A13B = st.number_input(
                                                            f"How many days in a month do you use {A13N}?(1-31)",value=0, step=1)

                                                    A13D = st.number_input(
                                                        f"How many hours in a day do you use {A13N}?(1-24)")

                                                    while A13D > 24 or A13D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                                        A13D = st.number_input(
                                                            f"How many hours in a day do you use {A13N}?(1-24)")

                                                    ask13 = st.number_input(
                                                        "Add 14th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                                                    while ask13 > 2 or ask13 < 1:  # ask for input until ask1 is 1 or 2
                                                        ask13 = st.number_input(
                                                            "Add 14th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# add app1 to 14 (13th line) ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                if ask13 == 1:
                                                    st.markdown(
                                                        "## **14th APPLIANCE!**")
                                                    A14N = st.text_input(
                                                        "Name of 14th appliance: ")
                                                    if A14N:
                                                        A14M = st.number_input(
                                                            f"How many {A14N} are you using?",value=0, step=1)
                                                        A14W = st.number_input(
                                                            f"What is the wattage of {A14N}?(watt)")
                                                        A14B = st.number_input(
                                                            f"How many days in a month do you use {A14N}?(1-31)",value=0, step=1)

                                                        while A14B > 31 or A14B < 1:
                                                            A14B = st.number_input(
                                                                f"How many days in a month do you use {A14N}?(1-31)",value=0, step=1)

                                                        A14D = st.number_input(
                                                            f"How many hours in a day do you use {A14N}?(1-24)")

                                                        while A14D > 24 or A14D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                                            A14D = st.number_input(
                                                                f"How many hours in a day do you use {A14N}?(1-24)")

                                                        ask14 = st.number_input(
                                                            "Add 15th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)

                                                        while ask14 > 2 or ask14 < 1:  # ask for input until ask1 is 1 or 2
                                                            ask14 = st.number_input(
                                                                "Add 15th appliance (enter 1), No more appliances (enter 2): ",value=0, step=1)
# -----------------------add app1 to 15 (14th line)////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                    # add app7 (6th line)
                                                    if ask14 == 1:
                                                        st.markdown(
                                                            "## **15th APPLIANCE!**")
                                                        A15N = st.text_input(
                                                            "Name of 15th appliance: ")
                                                        if A15N:
                                                            A15M = st.number_input(
                                                                f"How many {A15N} are you using?",value=0, step=1)
                                                            A15W = st.number_input(
                                                                f"What is the wattage of {A15N}?(watt)")
                                                            A15B = st.number_input(
                                                                f"How many days in a month do you use {A15N}?(1-31)",value=0, step=1)

                                                            while A15B > 31 or A15B < 1:
                                                                A15B = st.number_input(
                                                                    f"How many days in a month do you use {A15N}?(1-31)",value=0, step=1)

                                                            A15D = st.number_input(
                                                                f"How many hours in a day do you use {A15N}?(1-24)")

                                                            while A15D > 24 or A15D < 0.00001:  # ask for input until A()D is <=24 or >=1
                                                                A15D = st.number_input(
                                                                    f"How many hours in a day do you use {A15N}?(1-24)")
                                                            ask15 = 2
#                                                             ask15 = st.number_input(
#                                                                 "Add 16th appliance (enter 1), No more appliances (enter 2): ")

#                                                             while ask15 > 2 or ask15 < 1:  # ask for input until ask1 is 1 or 2
#                                                                 ask15 = st.number_input(
#                                                                     "Add 16th appliance (enter 1), No more appliances (enter 2): ")
# # add app1 to 16 (15th line)///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                         if ask15 == 1:
#                                                             st.markdown(
#                                                                 "## **16th APPLIANCE!**")
#                                                             A16N = st.text_input(
#                                                                 "Name of 16th appliance: ")
#                                                             if A16N:
#                                                                 A16M = st.number_input(
#                                                                     f"How many {A16N} are you using?")
#                                                                 A16W = st.number_input(
#                                                                     f"What is the wattage of {A16N}?(watt)")
#                                                                 A16B = st.number_input(
#                                                                     f"How many days in a month do you use {A16N}?(1-31)")

#                                                                 while A16B > 31 or A16B < 1:
#                                                                     A16B = st.number_input(
#                                                                         f"How many days in a month do you use {A16N}?(1-31)")

#                                                                 A16D = st.number_input(
#                                                                     f"How many hours in a day do you use {A16N}?(1-24)")

#                                                                 while A16D > 24 or A16D < 0.00001:  # ask for input until A()D is <=24 or >=1
#                                                                     A16D = st.number_input(
#                                                                         f"How many hours in a day do you use {A16N}?(1-24)")

#                                                                 ask16 = st.number_input(
#                                                                     "Add 17th appliance (enter 1), No more appliances (enter 2): ")

#                                                                 while ask16 > 2 or ask16 < 1:  # ask for input until ask1 is 1 or 2
#                                                                     ask16 = st.number_input(
#                                                                         "Add 17th appliance (enter 1), No more appliances (enter 2): ")

#                                 # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                             # add app9 (8th line)
#                                                             if ask8 == 1:
#                                                                 st.markdown(
#                                                                     "## **9th APPLIANCE!**")
#                                                                 A9N = st.text_input(
#                                                                     "Name of 9th appliance: ")
#                                                                 if A9N:
#                                                                     A9M = st.number_input(
#                                                                         f"How many {A9N} are you using?")
#                                                                     A9W = st.number_input(
#                                                                         f"What is the wattage of {A9N}?(watt)")
#                                                                     A9B = st.number_input(
#                                                                         f"How many days in a month do you use {A9N}?(1-31)")

#                                                                     while A9B > 31 or A9B < 1:
#                                                                         A9B = st.number_input(
#                                                                             f"How many days in a month do you use {A9N}?(1-31)")

#                                                                     A9D = st.number_input(
#                                                                         f"How many hours in a day do you use {A9N}?(1-24)")

#                                                                     while A9D > 24 or A9D < 0.00001:  # ask for input until A()D is <=24 or >=1
#                                                                         A9D = st.number_input(
#                                                                             f"How many hours in a day do you use {A9N}?(1-24)")

#                                                                     ask9 = st.number_input(
#                                                                         "Add 10th appliance (enter 1), No more appliances (enter 2): ")

#                                                                     while ask9 > 2 or ask9 < 1:  # ask for input until ask1 is 1 or 2
#                                                                         ask9 = st.number_input(
#                                                                             "Add 10th appliance (enter 1), No more appliances (enter 2): ")
#                                 # >>

#                                 # compute app1,2,3,4,5,6,7 and 8 (8th line)# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                             if ask8 == 2:
#                                                                 # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
#                                                                 A1F = (
#                                                                     A1B / 30) * A1D
#                                                                 A2F = (
#                                                                     A2B / 30) * A2D
#                                                                 A3F = (
#                                                                     A3B / 30) * A3D
#                                                                 A4F = (
#                                                                     A4B / 30) * A4D
#                                                                 A5F = (
#                                                                     A5B / 30) * A5D
#                                                                 A6F = (
#                                                                     A6B / 30) * A6D
#                                                                 A7F = (
#                                                                     A7B / 30) * A7D
#                                                                 A8F = (
#                                                                     A8B / 30) * A8D

#                                                                 # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
#                                                                 A1 = (
#                                                                     A1F * (A1W * A1M))
#                                                                 A2 = (
#                                                                     A2F * (A2W * A2M))
#                                                                 A3 = (
#                                                                     A3F * (A3W * A3M))
#                                                                 A4 = (
#                                                                     A4F * (A4W * A4M))
#                                                                 A5 = (
#                                                                     A5F * (A5W * A5M))
#                                                                 A6 = (
#                                                                     A6F * (A6W * A6M))
#                                                                 A7 = (
#                                                                     A7F * (A7W * A7M))
#                                                                 A8 = (
#                                                                     A8F * (A8W * A8M))

#                                                                 # TOTAL: watt/hour kada araw.
#                                                                 wh8 = (
#                                                                     A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8)

#                                                                 # TOTAL: Kilo-watt/hour kada month.
#                                                                 Kh8 = (
#                                                                     (wh8 * 30) / 1000)

#                                                                 # TOTAL: para ma compute ang (cost) kada month.
#                                                                 total8 = cost * Kh8

#                                                                 # INDIVIDUALLY: para ma compute ang (cost) kada month.
#                                                                 A1con = (
#                                                                     (A1 * 30) / 1000) * cost
#                                                                 A2con = (
#                                                                     (A2 * 30) / 1000) * cost
#                                                                 A3con = (
#                                                                     (A3 * 30) / 1000) * cost
#                                                                 A4con = (
#                                                                     (A4 * 30) / 1000) * cost
#                                                                 A5con = (
#                                                                     (A5 * 30) / 1000) * cost
#                                                                 A6con = (
#                                                                     (A6 * 30) / 1000) * cost
#                                                                 A7con = (
#                                                                     (A7 * 30) / 1000) * cost
#                                                                 A8con = (
#                                                                     (A8 * 30) / 1000) * cost

#                                                                 # INDIVIDUAL: Kilo-watt/hour
#                                                                 Y1 = (
#                                                                     A1*30)/1000
#                                                                 Y2 = (
#                                                                     A2*30)/1000
#                                                                 Y3 = (
#                                                                     A3*30)/1000
#                                                                 Y4 = (
#                                                                     A4*30)/1000
#                                                                 Y5 = (
#                                                                     A5*30)/1000
#                                                                 Y6 = (
#                                                                     A6*30)/1000
#                                                                 Y7 = (
#                                                                     A7*30)/1000
#                                                                 Y8 = (
#                                                                     A8*30)/1000

#                                                                 # OUTPUT1
#                                                                 st.markdown(
#                                                                     "## **THE RESULTS:**")
#                                                                 # Identify the high consumption appliance
#                                                                 st.write(
#                                                                     "************************************************************************************************************************************************************************")
#                                                                 st.markdown(
#                                                                     "**HIGHEST ENERGY CONSUMPTION**")
#                                                                 apps = [A1con, A2con, A3con,
#                                                                         A4con, A5con, A6con, A7con, A8con]
#                                                                 max_app = apps[0]
#                                                                 for app in apps:
#                                                                     if app > max_app:
#                                                                         max_app = app
#                                                                 if max_app == A1con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A1N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A1con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y1)
#                                                                 if max_app == A2con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A2N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A2con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y2)
#                                                                 if max_app == A3con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A3N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A3con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y3)
#                                                                 if max_app == A4con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A4N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A4con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y4)
#                                                                 if max_app == A5con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A5N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A5con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y5)
#                                                                 if max_app == A6con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A6N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A6con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y6)
#                                                                 if max_app == A7con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A7N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A7con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y7)
#                                                                 if max_app == A8con:
#                                                                     st.write(
#                                                                         "************************************************************************************************************************************************************************")
#                                                                     st.write(
#                                                                         "Name of appliance  :", A8N)
#                                                                     st.write(
#                                                                         "Electricity bill   : PHP", A8con)
#                                                                     st.write(
#                                                                         "Energy consumption :", Y8)
#                                                                 # OUTPUT2
#                                                                 st.write(
#                                                                     "************************************************************************************************************************************************************************")
#                                                                 st.markdown(
#                                                                     "**INDIVIDUAL ELECTRICITY BILL**")
#                                                                 st.write(
#                                                                     A1N, ": PHP", A1con)
#                                                                 st.write(
#                                                                     A2N, ": PHP", A2con)
#                                                                 st.write(
#                                                                     A3N, ": PHP", A3con)
#                                                                 st.write(
#                                                                     A4N, ": PHP", A4con)
#                                                                 st.write(
#                                                                     A5N, ": PHP", A5con)
#                                                                 st.write(
#                                                                     A6N, ": PHP", A6con)
#                                                                 st.write(
#                                                                     A7N, ": PHP", A7con)
#                                                                 st.write(
#                                                                     A8N, ": PHP", A8con)
#                                                                 st.write(
#                                                                     "************************************************************************************************************************************************************************")
#                                                                 st.markdown(
#                                                                     "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
#                                                                 st.write(
#                                                                     "Electricity bill: PHP", total8)
#                                                                 st.write(
#                                                                     "Energy consumption:", Kh8, "kWh")

# compute app1 to 15 (15th line) # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        if ask15 == 2:
                                                            # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                                                            A1F = (
                                                                A1B / 30) * A1D
                                                            A2F = (
                                                                A2B / 30) * A2D
                                                            A3F = (
                                                                A3B / 30) * A3D
                                                            A4F = (
                                                                A4B / 30) * A4D
                                                            A5F = (
                                                                A5B / 30) * A5D
                                                            A6F = (
                                                                A6B / 30) * A6D
                                                            A7F = (
                                                                A7B / 30) * A7D
                                                            A8F = (
                                                                A8B / 30) * A8D
                                                            A9F = (
                                                                A9B / 30) * A9D
                                                            A10F = (
                                                                A10B / 30) * A10D
                                                            A11F = (
                                                                A11B / 30) * A11D
                                                            A12F = (
                                                                A12B / 30) * A12D
                                                            A13F = (
                                                                A13B / 30) * A13D
                                                            A14F = (
                                                                A14B / 30) * A14D
                                                            A15F = (
                                                                A15B / 30) * A15D

                                                            # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                            A1 = (
                                                                A1F * (A1W * A1M))
                                                            A2 = (
                                                                A2F * (A2W * A2M))
                                                            A3 = (
                                                                A3F * (A3W * A3M))
                                                            A4 = (
                                                                A4F * (A4W * A4M))
                                                            A5 = (
                                                                A5F * (A5W * A5M))
                                                            A6 = (
                                                                A6F * (A6W * A6M))
                                                            A7 = (
                                                                A7F * (A7W * A7M))
                                                            A8 = (
                                                                A8F * (A8W * A8M))
                                                            A9 = (
                                                                A9F * (A9W * A9M))
                                                            A10 = (
                                                                A10F * (A10W * A10M))
                                                            A11 = (
                                                                A11F * (A11W * A11M))
                                                            A12 = (
                                                                A12F * (A12W * A12M))
                                                            A13 = (
                                                                A13F * (A13W * A13M))
                                                            A14 = (
                                                                A14F * (A14W * A14M))
                                                            A15 = (
                                                                A15F * (A15W * A15M))

                                                            # TOTAL: watt/hour kada araw.
                                                            wh15 = (A1 + A2 + A3 + A4 +
                                                                    A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15)

                                                            # TOTAL: Kilo-watt/hour kada month.
                                                            Kh15 = (
                                                                (wh15 * 30) / 1000)

                                                            # TOTAL: para ma compute ang (cost) kada month.
                                                            total15 = cost * Kh15

                                                            # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                            A1con = (
                                                                (A1 * 30) / 1000) * cost
                                                            A2con = (
                                                                (A2 * 30) / 1000) * cost
                                                            A3con = (
                                                                (A3 * 30) / 1000) * cost
                                                            A4con = (
                                                                (A4 * 30) / 1000) * cost
                                                            A5con = (
                                                                (A5 * 30) / 1000) * cost
                                                            A6con = (
                                                                (A6 * 30) / 1000) * cost
                                                            A7con = (
                                                                (A7 * 30) / 1000) * cost
                                                            A8con = (
                                                                (A8 * 30) / 1000) * cost
                                                            A9con = (
                                                                (A9 * 30) / 1000) * cost
                                                            A10con = (
                                                                (A10 * 30) / 1000) * cost
                                                            A11con = (
                                                                (A11 * 30) / 1000) * cost
                                                            A12con = (
                                                                (A12 * 30) / 1000) * cost
                                                            A13con = (
                                                                (A13 * 30) / 1000) * cost
                                                            A14con = (
                                                                (A14 * 30) / 1000) * cost
                                                            A15con = (
                                                                (A15 * 30) / 1000) * cost

                                                            # INDIVIDUAL: Kilo-watt/hour
                                                            Y1 = (A1*30)/1000
                                                            Y2 = (A2*30)/1000
                                                            Y3 = (A3*30)/1000
                                                            Y4 = (A4*30)/1000
                                                            Y5 = (A5*30)/1000
                                                            Y6 = (A6*30)/1000
                                                            Y7 = (A7*30)/1000
                                                            Y8 = (A8*30)/1000
                                                            Y9 = (A8*30)/1000
                                                            Y10 = (A10*30)/1000
                                                            Y11 = (A11*30)/1000
                                                            Y12 = (A12*30)/1000
                                                            Y13 = (A13*30)/1000
                                                            Y14 = (A14*30)/1000
                                                            Y15 = (A15*30)/1000

                                                            # OUTPUT1
                                                            st.markdown(
                                                                "## **THE RESULTS:**")
                                                            # Identify the high consumption appliance
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.markdown(
                                                                "**HIGHEST ENERGY CONSUMPTION**")
                                                            apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15]
                                                            max_app = apps[0]
                                                            for app in apps:
                                                                if app > max_app:
                                                                    max_app = app
                                                            if max_app == Y1:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A1N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A1con)
                                                                st.write(
                                                                    "Energy consumption :", Y1)
                                                            if max_app == Y2:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A2N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A2con)
                                                                st.write(
                                                                    "Energy consumption :", Y2)
                                                            if max_app == Y3:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A3N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A3con)
                                                                st.write(
                                                                    "Energy consumption :", Y3)
                                                            if max_app == Y4:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A4N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A4con)
                                                                st.write(
                                                                    "Energy consumption :", Y4)
                                                            if max_app == Y5:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A5N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A5con)
                                                                st.write(
                                                                    "Energy consumption :", Y5)
                                                            if max_app == Y6:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A6N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A6con)
                                                                st.write(
                                                                    "Energy consumption :", Y6)
                                                            if max_app == Y7:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A7N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A7con)
                                                                st.write(
                                                                    "Energy consumption :", Y7)
                                                            if max_app == Y8:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A8N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A8con)
                                                                st.write(
                                                                    "Energy consumption :", Y8)
                                                            if max_app == Y9:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A9N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A9con)
                                                                st.write(
                                                                    "Energy consumption :", Y9)
                                                            if max_app == Y10:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A10N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A10con)
                                                                st.write(
                                                                    "Energy consumption :", Y10)
                                                            if max_app == Y11:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A11N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A11con)
                                                                st.write(
                                                                    "Energy consumption :", Y11)
                                                            if max_app == Y12:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A12N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A12con)
                                                                st.write(
                                                                    "Energy consumption :", Y12)
                                                            if max_app == Y13:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A13N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A13con)
                                                                st.write(
                                                                    "Energy consumption :", Y13)
                                                            if max_app == Y14:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A14N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A14con)
                                                                st.write(
                                                                    "Energy consumption :", Y14)
                                                            if max_app == Y15:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A15N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A15con)
                                                                st.write(
                                                                    "Energy consumption :", Y15)
                                                            # OUTPUT2
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.markdown(
                                                                "**INDIVIDUAL ELECTRICITY BILL**")
                                                            st.write(
                                                                A1N, ": PHP", A1con)
                                                            st.write(
                                                                A2N, ": PHP", A2con)
                                                            st.write(
                                                                A3N, ": PHP", A3con)
                                                            st.write(
                                                                A4N, ": PHP", A4con)
                                                            st.write(
                                                                A5N, ": PHP", A5con)
                                                            st.write(
                                                                A6N, ": PHP", A6con)
                                                            st.write(
                                                                A7N, ": PHP", A7con)
                                                            st.write(
                                                                A8N, ": PHP", A8con)
                                                            st.write(
                                                                A9N, ": PHP", A9con)
                                                            st.write(
                                                                A10N, ": PHP", A10con)
                                                            st.write(
                                                                A11N, ": PHP", A11con)
                                                            st.write(
                                                                A12N, ": PHP", A12con)
                                                            st.write(
                                                                A13N, ": PHP", A13con)
                                                            st.write(
                                                                A14N, ": PHP", A14con)
                                                            st.write(
                                                                A15N, ": PHP", A15con)
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.markdown(
                                                                "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                            st.write(
                                                                "Electricity bill: PHP", total15)
                                                            st.write(
                                                                "Energy consumption:", Kh15, "kWh")
# compute app1 to 14 (14th line) ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                    if ask14 == 2:
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
                                                        A10F = (
                                                            A10B / 30) * A10D
                                                        A11F = (
                                                            A11B / 30) * A11D
                                                        A12F = (
                                                            A12B / 30) * A12D
                                                        A13F = (
                                                            A13B / 30) * A13D
                                                        A14F = (
                                                            A14B / 30) * A14D

                                                        # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                        A1 = (
                                                            A1F * (A1W * A1M))
                                                        A2 = (
                                                            A2F * (A2W * A2M))
                                                        A3 = (
                                                            A3F * (A3W * A3M))
                                                        A4 = (
                                                            A4F * (A4W * A4M))
                                                        A5 = (
                                                            A5F * (A5W * A5M))
                                                        A6 = (
                                                            A6F * (A6W * A6M))
                                                        A7 = (
                                                            A7F * (A7W * A7M))
                                                        A8 = (
                                                            A8F * (A8W * A8M))
                                                        A9 = (
                                                            A9F * (A9W * A9M))
                                                        A10 = (
                                                            A10F * (A10W * A10M))
                                                        A11 = (
                                                            A11F * (A11W * A11M))
                                                        A12 = (
                                                            A12F * (A12W * A12M))
                                                        A13 = (
                                                            A13F * (A13W * A13M))
                                                        A14 = (
                                                            A14F * (A14W * A14M))

                                                        # TOTAL: watt/hour kada araw.
                                                        wh14 = (A1 + A2 + A3 + A4 +
                                                                A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14)

                                                        # TOTAL: Kilo-watt/hour kada month.
                                                        Kh14 = (
                                                            (wh14 * 30) / 1000)

                                                        # TOTAL: para ma compute ang (cost) kada month.
                                                        total14 = cost * Kh14

                                                        # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                        A1con = (
                                                            (A1 * 30) / 1000) * cost
                                                        A2con = (
                                                            (A2 * 30) / 1000) * cost
                                                        A3con = (
                                                            (A3 * 30) / 1000) * cost
                                                        A4con = (
                                                            (A4 * 30) / 1000) * cost
                                                        A5con = (
                                                            (A5 * 30) / 1000) * cost
                                                        A6con = (
                                                            (A6 * 30) / 1000) * cost
                                                        A7con = (
                                                            (A7 * 30) / 1000) * cost
                                                        A8con = (
                                                            (A8 * 30) / 1000) * cost
                                                        A9con = (
                                                            (A9 * 30) / 1000) * cost
                                                        A10con = (
                                                            (A10 * 30) / 1000) * cost
                                                        A11con = (
                                                            (A11 * 30) / 1000) * cost
                                                        A12con = (
                                                            (A12 * 30) / 1000) * cost
                                                        A13con = (
                                                            (A13 * 30) / 1000) * cost
                                                        A14con = (
                                                            (A14 * 30) / 1000) * cost

                                                        # INDIVIDUAL: Kilo-watt/hour
                                                        Y1 = (A1*30)/1000
                                                        Y2 = (A2*30)/1000
                                                        Y3 = (A3*30)/1000
                                                        Y4 = (A4*30)/1000
                                                        Y5 = (A5*30)/1000
                                                        Y6 = (A6*30)/1000
                                                        Y7 = (A7*30)/1000
                                                        Y8 = (A8*30)/1000
                                                        Y9 = (A8*30)/1000
                                                        Y10 = (A10*30)/1000
                                                        Y11 = (A11*30)/1000
                                                        Y12 = (A12*30)/1000
                                                        Y13 = (A13*30)/1000
                                                        Y14 = (A14*30)/1000

                                                        # OUTPUT1
                                                        st.markdown(
                                                            "## **THE RESULTS:**")
                                                        # Identify the high consumption appliance
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.markdown(
                                                            "**HIGHEST ENERGY CONSUMPTION**")
                                                        apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14]
                                                        max_app = apps[0]
                                                        for app in apps:
                                                            if app > max_app:
                                                                max_app = app
                                                        if max_app == Y1:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A1N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A1con)
                                                            st.write(
                                                                "Energy consumption :", Y1)
                                                        if max_app == Y2:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A2N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A2con)
                                                            st.write(
                                                                "Energy consumption :", Y2)
                                                        if max_app == Y3:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A3N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A3con)
                                                            st.write(
                                                                "Energy consumption :", Y3)
                                                        if max_app == Y4:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A4N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A4con)
                                                            st.write(
                                                                "Energy consumption :", Y4)
                                                        if max_app == Y5:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A5N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A5con)
                                                            st.write(
                                                                "Energy consumption :", Y5)
                                                        if max_app == Y6:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A6N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A6con)
                                                            st.write(
                                                                "Energy consumption :", Y6)
                                                        if max_app == Y7:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A7N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A7con)
                                                            st.write(
                                                                "Energy consumption :", Y7)
                                                        if max_app == Y8:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A8N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A8con)
                                                            st.write(
                                                                "Energy consumption :", Y8)
                                                        if max_app == Y9:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A9N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A9con)
                                                            st.write(
                                                                "Energy consumption :", Y9)
                                                        if max_app == Y10:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A10N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A10con)
                                                            st.write(
                                                                "Energy consumption :", Y10)
                                                        if max_app == Y11:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A11N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A11con)
                                                            st.write(
                                                                "Energy consumption :", Y11)
                                                        if max_app == Y12:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A12N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A12con)
                                                            st.write(
                                                                "Energy consumption :", Y12)
                                                        if max_app == Y13:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A13N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A13con)
                                                            st.write(
                                                                "Energy consumption :", Y13)
                                                        if max_app == Y14:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A14N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A14con)
                                                            st.write(
                                                                "Energy consumption :", Y14)
                                                        # OUTPUT2
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.markdown(
                                                            "**INDIVIDUAL ELECTRICITY BILL**")
                                                        st.write(
                                                            A1N, ": PHP", A1con)
                                                        st.write(
                                                            A2N, ": PHP", A2con)
                                                        st.write(
                                                            A3N, ": PHP", A3con)
                                                        st.write(
                                                            A4N, ": PHP", A4con)
                                                        st.write(
                                                            A5N, ": PHP", A5con)
                                                        st.write(
                                                            A6N, ": PHP", A6con)
                                                        st.write(
                                                            A7N, ": PHP", A7con)
                                                        st.write(
                                                            A8N, ": PHP", A8con)
                                                        st.write(
                                                            A9N, ": PHP", A9con)
                                                        st.write(
                                                            A10N, ": PHP", A10con)
                                                        st.write(
                                                            A11N, ": PHP", A11con)
                                                        st.write(
                                                            A12N, ": PHP", A12con)
                                                        st.write(
                                                            A13N, ": PHP", A13con)
                                                        st.write(
                                                            A14N, ": PHP", A14con)
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.markdown(
                                                            "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                        st.write(
                                                            "Electricity bill: PHP", total14)
                                                        st.write(
                                                            "Energy consumption:", Kh14, "kWh")

# compute app1 to 13 (13th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                if ask13 == 2:
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
                                                    A10F = (A10B / 30) * A10D
                                                    A11F = (A11B / 30) * A11D
                                                    A12F = (A12B / 30) * A12D
                                                    A13F = (A13B / 30) * A13D

                                                    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                    A1 = (A1F * (A1W * A1M))
                                                    A2 = (A2F * (A2W * A2M))
                                                    A3 = (A3F * (A3W * A3M))
                                                    A4 = (A4F * (A4W * A4M))
                                                    A5 = (A5F * (A5W * A5M))
                                                    A6 = (A6F * (A6W * A6M))
                                                    A7 = (A7F * (A7W * A7M))
                                                    A8 = (A8F * (A8W * A8M))
                                                    A9 = (A9F * (A9W * A9M))
                                                    A10 = (
                                                        A10F * (A10W * A10M))
                                                    A11 = (
                                                        A11F * (A11W * A11M))
                                                    A12 = (
                                                        A12F * (A12W * A12M))
                                                    A13 = (
                                                        A13F * (A13W * A13M))

                                                    # TOTAL: watt/hour kada araw.
                                                    wh13 = (A1 + A2 + A3 + A4 +
                                                            A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13)

                                                    # TOTAL: Kilo-watt/hour kada month.
                                                    Kh13 = ((wh13 * 30) / 1000)

                                                    # TOTAL: para ma compute ang (cost) kada month.
                                                    total13 = cost * Kh13

                                                    # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                    A1con = (
                                                        (A1 * 30) / 1000) * cost
                                                    A2con = (
                                                        (A2 * 30) / 1000) * cost
                                                    A3con = (
                                                        (A3 * 30) / 1000) * cost
                                                    A4con = (
                                                        (A4 * 30) / 1000) * cost
                                                    A5con = (
                                                        (A5 * 30) / 1000) * cost
                                                    A6con = (
                                                        (A6 * 30) / 1000) * cost
                                                    A7con = (
                                                        (A7 * 30) / 1000) * cost
                                                    A8con = (
                                                        (A8 * 30) / 1000) * cost
                                                    A9con = (
                                                        (A9 * 30) / 1000) * cost
                                                    A10con = (
                                                        (A10 * 30) / 1000) * cost
                                                    A11con = (
                                                        (A11 * 30) / 1000) * cost
                                                    A12con = (
                                                        (A12 * 30) / 1000) * cost
                                                    A13con = (
                                                        (A13 * 30) / 1000) * cost

                                                    # INDIVIDUAL: Kilo-watt/hour
                                                    Y1 = (A1*30)/1000
                                                    Y2 = (A2*30)/1000
                                                    Y3 = (A3*30)/1000
                                                    Y4 = (A4*30)/1000
                                                    Y5 = (A5*30)/1000
                                                    Y6 = (A6*30)/1000
                                                    Y7 = (A7*30)/1000
                                                    Y8 = (A8*30)/1000
                                                    Y9 = (A8*30)/1000
                                                    Y10 = (A10*30)/1000
                                                    Y11 = (A11*30)/1000
                                                    Y12 = (A12*30)/1000
                                                    Y13 = (A13*30)/1000

                                                    # OUTPUT1
                                                    st.markdown(
                                                        "## **THE RESULTS:**")
                                                    # Identify the high consumption appliance
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.markdown(
                                                        "**HIGHEST ENERGY CONSUMPTION**")
                                                    apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13]
                                                    max_app = apps[0]
                                                    for app in apps:
                                                        if app > max_app:
                                                            max_app = app
                                                    if max_app == Y1:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A1N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A1con)
                                                        st.write(
                                                            "Energy consumption :", Y1)
                                                    if max_app == Y2:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A2N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A2con)
                                                        st.write(
                                                            "Energy consumption :", Y2)
                                                    if max_app == Y3:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A3N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A3con)
                                                        st.write(
                                                            "Energy consumption :", Y3)
                                                    if max_app == Y4:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A4N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A4con)
                                                        st.write(
                                                            "Energy consumption :", Y4)
                                                    if max_app == Y5:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A5N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A5con)
                                                        st.write(
                                                            "Energy consumption :", Y5)
                                                    if max_app == Y6:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A6N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A6con)
                                                        st.write(
                                                            "Energy consumption :", Y6)
                                                    if max_app == A7con:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A7N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A7con)
                                                        st.write(
                                                            "Energy consumption :", Y7)
                                                    if max_app == Y8:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A8N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A8con)
                                                        st.write(
                                                            "Energy consumption :", Y8)
                                                    if max_app == Y9:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A9N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A9con)
                                                        st.write(
                                                            "Energy consumption :", Y9)
                                                    if max_app == Y10:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A10N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A10con)
                                                        st.write(
                                                            "Energy consumption :", Y10)
                                                    if max_app == Y11:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A11N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A11con)
                                                        st.write(
                                                            "Energy consumption :", Y11)
                                                    if max_app == Y12:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A12N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A12con)
                                                        st.write(
                                                            "Energy consumption :", Y12)
                                                    if max_app == Y13:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A13N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A13con)
                                                        st.write(
                                                            "Energy consumption :", Y13)
                                                    # OUTPUT2
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.markdown(
                                                        "**INDIVIDUAL ELECTRICITY BILL**")
                                                    st.write(
                                                        A1N, ": PHP", A1con)
                                                    st.write(
                                                        A2N, ": PHP", A2con)
                                                    st.write(
                                                        A3N, ": PHP", A3con)
                                                    st.write(
                                                        A4N, ": PHP", A4con)
                                                    st.write(
                                                        A5N, ": PHP", A5con)
                                                    st.write(
                                                        A6N, ": PHP", A6con)
                                                    st.write(
                                                        A7N, ": PHP", A7con)
                                                    st.write(
                                                        A8N, ": PHP", A8con)
                                                    st.write(
                                                        A9N, ": PHP", A9con)
                                                    st.write(
                                                        A10N, ": PHP", A10con)
                                                    st.write(
                                                        A11N, ": PHP", A11con)
                                                    st.write(
                                                        A12N, ": PHP", A12con)
                                                    st.write(
                                                        A13N, ": PHP", A13con)
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.markdown(
                                                        "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                    st.write(
                                                        "Electricity bill: PHP", total13)
                                                    st.write(
                                                        "Energy consumption:", Kh13, "kWh")

# compute app1 to 12 (12th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                            if ask12 == 2:
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
                                                A10F = (A10B / 30) * A10D
                                                A11F = (A11B / 30) * A11D
                                                A12F = (A12B / 30) * A12D

                                                # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                A1 = (A1F * (A1W * A1M))
                                                A2 = (A2F * (A2W * A2M))
                                                A3 = (A3F * (A3W * A3M))
                                                A4 = (A4F * (A4W * A4M))
                                                A5 = (A5F * (A5W * A5M))
                                                A6 = (A6F * (A6W * A6M))
                                                A7 = (A7F * (A7W * A7M))
                                                A8 = (A8F * (A8W * A8M))
                                                A9 = (A9F * (A9W * A9M))
                                                A10 = (A10F * (A10W * A10M))
                                                A11 = (A11F * (A11W * A11M))
                                                A12 = (A12F * (A12W * A12M))

                                                # TOTAL: watt/hour kada araw.
                                                wh12 = (A1 + A2 + A3 + A4 +
                                                        A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12)

                                                # TOTAL: Kilo-watt/hour kada month.
                                                Kh12 = ((wh12 * 30) / 1000)

                                                # TOTAL: para ma compute ang (cost) kada month.
                                                total12 = cost * Kh12

                                                # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                A1con = (
                                                    (A1 * 30) / 1000) * cost
                                                A2con = (
                                                    (A2 * 30) / 1000) * cost
                                                A3con = (
                                                    (A3 * 30) / 1000) * cost
                                                A4con = (
                                                    (A4 * 30) / 1000) * cost
                                                A5con = (
                                                    (A5 * 30) / 1000) * cost
                                                A6con = (
                                                    (A6 * 30) / 1000) * cost
                                                A7con = (
                                                    (A7 * 30) / 1000) * cost
                                                A8con = (
                                                    (A8 * 30) / 1000) * cost
                                                A9con = (
                                                    (A9 * 30) / 1000) * cost
                                                A10con = (
                                                    (A10 * 30) / 1000) * cost
                                                A11con = (
                                                    (A11 * 30) / 1000) * cost
                                                A12con = (
                                                    (A12 * 30) / 1000) * cost

                                                # INDIVIDUAL: Kilo-watt/hour
                                                Y1 = (A1*30)/1000
                                                Y2 = (A2*30)/1000
                                                Y3 = (A3*30)/1000
                                                Y4 = (A4*30)/1000
                                                Y5 = (A5*30)/1000
                                                Y6 = (A6*30)/1000
                                                Y7 = (A7*30)/1000
                                                Y8 = (A8*30)/1000
                                                Y9 = (A8*30)/1000
                                                Y10 = (A10*30)/1000
                                                Y11 = (A11*30)/1000
                                                Y12 = (A12*30)/1000

                                                # OUTPUT1
                                                st.markdown(
                                                    "## **THE RESULTS:**")
                                                # Identify the high consumption appliance
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.markdown(
                                                    "**HIGHEST ENERGY CONSUMPTION**")
                                                apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12]
                                                max_app = apps[0]
                                                for app in apps:
                                                    if app > max_app:
                                                        max_app = app
                                                if max_app == Y1:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A1N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A1con)
                                                    st.write(
                                                        "Energy consumption :", Y1)
                                                if max_app == Y2:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A2N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A2con)
                                                    st.write(
                                                        "Energy consumption :", Y2)
                                                if max_app == Y3:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A3N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A3con)
                                                    st.write(
                                                        "Energy consumption :", Y3)
                                                if max_app == Y4:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A4N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A4con)
                                                    st.write(
                                                        "Energy consumption :", Y4)
                                                if max_app == Y5:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A5N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A5con)
                                                    st.write(
                                                        "Energy consumption :", Y5)
                                                if max_app == Y6:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A6N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A6con)
                                                    st.write(
                                                        "Energy consumption :", Y6)
                                                if max_app == A7con:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A7N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A7con)
                                                    st.write(
                                                        "Energy consumption :", Y7)
                                                if max_app == Y8:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A8N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A8con)
                                                    st.write(
                                                        "Energy consumption :", Y8)
                                                if max_app == Y9:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A9N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A9con)
                                                    st.write(
                                                        "Energy consumption :", Y9)
                                                if max_app == Y10:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A10N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A10con)
                                                    st.write(
                                                        "Energy consumption :", Y10)
                                                if max_app == Y11:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A11N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A11con)
                                                    st.write(
                                                        "Energy consumption :", Y11)
                                                if max_app == Y12:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A12N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A12con)
                                                    st.write(
                                                        "Energy consumption :", Y12)
                                                # OUTPUT2
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.markdown(
                                                    "**INDIVIDUAL ELECTRICITY BILL**")
                                                st.write(A1N, ": PHP", A1con)
                                                st.write(A2N, ": PHP", A2con)
                                                st.write(A3N, ": PHP", A3con)
                                                st.write(A4N, ": PHP", A4con)
                                                st.write(A5N, ": PHP", A5con)
                                                st.write(A6N, ": PHP", A6con)
                                                st.write(A7N, ": PHP", A7con)
                                                st.write(A8N, ": PHP", A8con)
                                                st.write(A9N, ": PHP", A9con)
                                                st.write(A10N, ": PHP", A10con)
                                                st.write(A11N, ": PHP", A11con)
                                                st.write(A12N, ": PHP", A12con)
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.markdown(
                                                    "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                st.write(
                                                    "Electricity bill: PHP", total12)
                                                st.write(
                                                    "Energy consumption:", Kh12, "kWh")

# compute app1 to 11 (11th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                        if ask11 == 2:
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
                                            A10F = (A10B / 30) * A10D
                                            A11F = (A11B / 30) * A11D

                                            # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                            A1 = (A1F * (A1W * A1M))
                                            A2 = (A2F * (A2W * A2M))
                                            A3 = (A3F * (A3W * A3M))
                                            A4 = (A4F * (A4W * A4M))
                                            A5 = (A5F * (A5W * A5M))
                                            A6 = (A6F * (A6W * A6M))
                                            A7 = (A7F * (A7W * A7M))
                                            A8 = (A8F * (A8W * A8M))
                                            A9 = (A9F * (A9W * A9M))
                                            A10 = (A10F * (A10W * A10M))
                                            A11 = (A11F * (A11W * A11M))

                                            # TOTAL: watt/hour kada araw.
                                            wh11 = (A1 + A2 + A3 + A4 +
                                                    A5 + A6 + A7 + A8 + A9 + A10 + A11)

                                            # TOTAL: Kilo-watt/hour kada month.
                                            Kh11 = ((wh11 * 30) / 1000)

                                            # TOTAL: para ma compute ang (cost) kada month.
                                            total11 = cost * Kh11

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
                                            A10con = ((A10 * 30) / 1000) * cost
                                            A11con = ((A11 * 30) / 1000) * cost

                                            # INDIVIDUAL: Kilo-watt/hour
                                            Y1 = (A1*30)/1000
                                            Y2 = (A2*30)/1000
                                            Y3 = (A3*30)/1000
                                            Y4 = (A4*30)/1000
                                            Y5 = (A5*30)/1000
                                            Y6 = (A6*30)/1000
                                            Y7 = (A7*30)/1000
                                            Y8 = (A8*30)/1000
                                            Y9 = (A8*30)/1000
                                            Y10 = (A10*30)/1000
                                            Y11 = (A11*30)/1000

                                            # OUTPUT1
                                            st.markdown("## **THE RESULTS:**")
                                            # Identify the high consumption appliance
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.markdown(
                                                "**HIGHEST ENERGY CONSUMPTION**")
                                            apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11]
                                            max_app = apps[0]
                                            for app in apps:
                                                if app > max_app:
                                                    max_app = app
                                            if max_app == Y1:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A1N)
                                                st.write(
                                                    "Electricity bill   : PHP", A1con)
                                                st.write(
                                                    "Energy consumption :", Y1)
                                            if max_app == Y2:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A2N)
                                                st.write(
                                                    "Electricity bill   : PHP", A2con)
                                                st.write(
                                                    "Energy consumption :", Y2)
                                            if max_app == Y3:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A3N)
                                                st.write(
                                                    "Electricity bill   : PHP", A3con)
                                                st.write(
                                                    "Energy consumption :", Y3)
                                            if max_app == Y4:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A4N)
                                                st.write(
                                                    "Electricity bill   : PHP", A4con)
                                                st.write(
                                                    "Energy consumption :", Y4)
                                            if max_app == Y5:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A5N)
                                                st.write(
                                                    "Electricity bill   : PHP", A5con)
                                                st.write(
                                                    "Energy consumption :", Y5)
                                            if max_app == Y6:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A6N)
                                                st.write(
                                                    "Electricity bill   : PHP", A6con)
                                                st.write(
                                                    "Energy consumption :", Y6)
                                            if max_app == Y7:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A7N)
                                                st.write(
                                                    "Electricity bill   : PHP", A7con)
                                                st.write(
                                                    "Energy consumption :", Y7)
                                            if max_app == Y8:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A8N)
                                                st.write(
                                                    "Electricity bill   : PHP", A8con)
                                                st.write(
                                                    "Energy consumption :", Y8)
                                            if max_app == Y9:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A9N)
                                                st.write(
                                                    "Electricity bill   : PHP", A9con)
                                                st.write(
                                                    "Energy consumption :", Y9)
                                            if max_app == Y10:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A10N)
                                                st.write(
                                                    "Electricity bill   : PHP", A10con)
                                                st.write(
                                                    "Energy consumption :", Y10)
                                            if max_app == Y11:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A11N)
                                                st.write(
                                                    "Electricity bill   : PHP", A11con)
                                                st.write(
                                                    "Energy consumption :", Y11)
                                            # OUTPUT2
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.markdown(
                                                "**INDIVIDUAL ELECTRICITY BILL**")
                                            st.write(A1N, ": PHP", A1con)
                                            st.write(A2N, ": PHP", A2con)
                                            st.write(A3N, ": PHP", A3con)
                                            st.write(A4N, ": PHP", A4con)
                                            st.write(A5N, ": PHP", A5con)
                                            st.write(A6N, ": PHP", A6con)
                                            st.write(A7N, ": PHP", A7con)
                                            st.write(A8N, ": PHP", A8con)
                                            st.write(A9N, ": PHP", A9con)
                                            st.write(A10N, ": PHP", A10con)
                                            st.write(A11N, ": PHP", A11con)
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.markdown(
                                                "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                            st.write(
                                                "Electricity bill: PHP", total11)
                                            st.write(
                                                "Energy consumption:", Kh11, "kWh")
# compute app1 to 10 (10th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                    if ask10 == 2:
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
                                        A10F = (A10B / 30) * A10D

                                        # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                        A1 = (A1F * (A1W * A1M))
                                        A2 = (A2F * (A2W * A2M))
                                        A3 = (A3F * (A3W * A3M))
                                        A4 = (A4F * (A4W * A4M))
                                        A5 = (A5F * (A5W * A5M))
                                        A6 = (A6F * (A6W * A6M))
                                        A7 = (A7F * (A7W * A7M))
                                        A8 = (A8F * (A8W * A8M))
                                        A9 = (A9F * (A9W * A9M))
                                        A10 = (A10F * (A10W * A10M))

                                        # TOTAL: watt/hour kada araw.
                                        wh10 = (A1 + A2 + A3 + A4 +
                                                A5 + A6 + A7 + A8 + A9 + A10)

                                        # TOTAL: Kilo-watt/hour kada month.
                                        Kh10 = ((wh10 * 30) / 1000)

                                        # TOTAL: para ma compute ang (cost) kada month.
                                        total10 = cost * Kh10

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
                                        A10con = ((A10 * 30) / 1000) * cost

                                        # INDIVIDUAL: Kilo-watt/hour
                                        Y1 = (A1*30)/1000
                                        Y2 = (A2*30)/1000
                                        Y3 = (A3*30)/1000
                                        Y4 = (A4*30)/1000
                                        Y5 = (A5*30)/1000
                                        Y6 = (A6*30)/1000
                                        Y7 = (A7*30)/1000
                                        Y8 = (A8*30)/1000
                                        Y9 = (A8*30)/1000
                                        Y10 = (A10*30)/1000

                                        # OUTPUT1
                                        st.markdown("## **THE RESULTS:**")
                                        # Identify the high consumption appliance
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.markdown(
                                            "**HIGHEST ENERGY CONSUMPTION**")
                                        apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10]
                                        max_app = apps[0]
                                        for app in apps:
                                            if app > max_app:
                                                max_app = app
                                        if max_app == Y1:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A1N)
                                            st.write(
                                                "Electricity bill   : PHP", A1con)
                                            st.write(
                                                "Energy consumption :", Y1)
                                        if max_app == Y2:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A2N)
                                            st.write(
                                                "Electricity bill   : PHP", A2con)
                                            st.write(
                                                "Energy consumption :", Y2)
                                        if max_app == Y3:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A3N)
                                            st.write(
                                                "Electricity bill   : PHP", A3con)
                                            st.write(
                                                "Energy consumption :", Y3)
                                        if max_app == Y4:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A4N)
                                            st.write(
                                                "Electricity bill   : PHP", A4con)
                                            st.write(
                                                "Energy consumption :", Y4)
                                        if max_app == Y5:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A5N)
                                            st.write(
                                                "Electricity bill   : PHP", A5con)
                                            st.write(
                                                "Energy consumption :", Y5)
                                        if max_app == Y6:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A6N)
                                            st.write(
                                                "Electricity bill   : PHP", A6con)
                                            st.write(
                                                "Energy consumption :", Y6)
                                        if max_app == Y7:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A7N)
                                            st.write(
                                                "Electricity bill   : PHP", A7con)
                                            st.write(
                                                "Energy consumption :", Y7)
                                        if max_app == Y8:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A8N)
                                            st.write(
                                                "Electricity bill   : PHP", A8con)
                                            st.write(
                                                "Energy consumption :", Y8)
                                        if max_app == Y9:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A9N)
                                            st.write(
                                                "Electricity bill   : PHP", A9con)
                                            st.write(
                                                "Energy consumption :", Y9)
                                        if max_app == Y10:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A10N)
                                            st.write(
                                                "Electricity bill   : PHP", A10con)
                                            st.write(
                                                "Energy consumption :", Y10)
                                        # OUTPUT2
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.markdown(
                                            "**INDIVIDUAL ELECTRICITY BILL**")
                                        st.write(A1N, ": PHP", A1con)
                                        st.write(A2N, ": PHP", A2con)
                                        st.write(A3N, ": PHP", A3con)
                                        st.write(A4N, ": PHP", A4con)
                                        st.write(A5N, ": PHP", A5con)
                                        st.write(A6N, ": PHP", A6con)
                                        st.write(A7N, ": PHP", A7con)
                                        st.write(A8N, ": PHP", A8con)
                                        st.write(A9N, ": PHP", A9con)
                                        st.write(A10N, ": PHP", A10con)
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.markdown(
                                            "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                        st.write(
                                            "Electricity bill: PHP", total10)
                                        st.write(
                                            "Energy consumption:", Kh10, "kWh")

# compute app1 to 9 (9th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
                                    A9 = (A9F * (A9W * A9M))

                                    # TOTAL: watt/hour kada araw.
                                    wh9 = (A1 + A2 + A3 + A4 +
                                           A5 + A6 + A7 + A8 + A9)

                                    # TOTAL: Kilo-watt/hour kada month.
                                    Kh9 = ((wh9 * 30) / 1000)

                                    # TOTAL: para ma compute ang (cost) kada month.
                                    total9 = cost * Kh9

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

                                    # INDIVIDUAL: Kilo-watt/hour
                                    Y1 = (A1*30)/1000
                                    Y2 = (A2*30)/1000
                                    Y3 = (A3*30)/1000
                                    Y4 = (A4*30)/1000
                                    Y5 = (A5*30)/1000
                                    Y6 = (A6*30)/1000
                                    Y7 = (A7*30)/1000
                                    Y8 = (A8*30)/1000
                                    Y9 = (A8*30)/1000

                                    # OUTPUT1
                                    st.markdown("## **THE RESULTS:**")
                                    # Identify the high consumption appliance
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.markdown(
                                        "**HIGHEST ENERGY CONSUMPTION**")
                                    apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9]
                                    max_app = apps[0]
                                    for app in apps:
                                        if app > max_app:
                                            max_app = app
                                    if max_app == Y1:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A1N)
                                        st.write(
                                            "Electricity bill   : PHP", A1con)
                                        st.write("Energy consumption :", Y1)
                                    if max_app == Y2:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A2N)
                                        st.write(
                                            "Electricity bill   : PHP", A2con)
                                        st.write("Energy consumption :", Y2)
                                    if max_app == Y3:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A3N)
                                        st.write(
                                            "Electricity bill   : PHP", A3con)
                                        st.write("Energy consumption :", Y3)
                                    if max_app == Y4:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A4N)
                                        st.write(
                                            "Electricity bill   : PHP", A4con)
                                        st.write("Energy consumption :", Y4)
                                    if max_app == Y5:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A5N)
                                        st.write(
                                            "Electricity bill   : PHP", A5con)
                                        st.write("Energy consumption :", Y5)
                                    if max_app == Y6:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A6N)
                                        st.write(
                                            "Electricity bill   : PHP", A6con)
                                        st.write("Energy consumption :", Y6)
                                    if max_app == Y7:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A7N)
                                        st.write(
                                            "Electricity bill   : PHP", A7con)
                                        st.write("Energy consumption :", Y7)
                                    if max_app == Y8:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A8N)
                                        st.write(
                                            "Electricity bill   : PHP", A8con)
                                        st.write("Energy consumption :", Y8)
                                    if max_app == Y9:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A9N)
                                        st.write(
                                            "Electricity bill   : PHP", A9con)
                                        st.write("Energy consumption :", Y9)
                                    # OUTPUT2
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.markdown(
                                        "**INDIVIDUAL ELECTRICITY BILL**")
                                    st.write(A1N, ": PHP", A1con)
                                    st.write(A2N, ": PHP", A2con)
                                    st.write(A3N, ": PHP", A3con)
                                    st.write(A4N, ": PHP", A4con)
                                    st.write(A5N, ": PHP", A5con)
                                    st.write(A6N, ": PHP", A6con)
                                    st.write(A7N, ": PHP", A7con)
                                    st.write(A8N, ": PHP", A8con)
                                    st.write(A9N, ": PHP", A9con)
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.markdown(
                                        "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                    st.write("Electricity bill: PHP", total9)
                                    st.write("Energy consumption:", Kh9, "kWh")


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
                                wh8 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8)

                                # TOTAL: Kilo-watt/hour kada month.
                                Kh8 = ((wh8 * 30) / 1000)

                                # TOTAL: para ma compute ang (cost) kada month.
                                total8 = cost * Kh8

                                # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                A1con = ((A1 * 30) / 1000) * cost
                                A2con = ((A2 * 30) / 1000) * cost
                                A3con = ((A3 * 30) / 1000) * cost
                                A4con = ((A4 * 30) / 1000) * cost
                                A5con = ((A5 * 30) / 1000) * cost
                                A6con = ((A6 * 30) / 1000) * cost
                                A7con = ((A7 * 30) / 1000) * cost
                                A8con = ((A8 * 30) / 1000) * cost

                                # INDIVIDUAL: Kilo-watt/hour
                                Y1 = (A1*30)/1000
                                Y2 = (A2*30)/1000
                                Y3 = (A3*30)/1000
                                Y4 = (A4*30)/1000
                                Y5 = (A5*30)/1000
                                Y6 = (A6*30)/1000
                                Y7 = (A7*30)/1000
                                Y8 = (A8*30)/1000

                                # OUTPUT1
                                st.markdown("## **THE RESULTS:**")
                                # Identify the high consumption appliance
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.markdown("**HIGHEST ENERGY CONSUMPTION**")
                                apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8]
                                max_app = apps[0]
                                for app in apps:
                                    if app > max_app:
                                        max_app = app
                                if max_app == Y1:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A1N)
                                    st.write("Electricity bill   : PHP", A1con)
                                    st.write("Energy consumption :", Y1)
                                if max_app == Y2:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A2N)
                                    st.write("Electricity bill   : PHP", A2con)
                                    st.write("Energy consumption :", Y2)
                                if max_app == Y3:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A3N)
                                    st.write("Electricity bill   : PHP", A3con)
                                    st.write("Energy consumption :", Y3)
                                if max_app == Y4:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A4N)
                                    st.write("Electricity bill   : PHP", A4con)
                                    st.write("Energy consumption :", Y4)
                                if max_app == Y5:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A5N)
                                    st.write("Electricity bill   : PHP", A5con)
                                    st.write("Energy consumption :", Y5)
                                if max_app == Y6:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A6N)
                                    st.write("Electricity bill   : PHP", A6con)
                                    st.write("Energy consumption :", Y6)
                                if max_app == Y7:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A7N)
                                    st.write("Electricity bill   : PHP", A7con)
                                    st.write("Energy consumption :", Y7)
                                if max_app == Y8:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A8N)
                                    st.write("Electricity bill   : PHP", A8con)
                                    st.write("Energy consumption :", Y8)
                                # OUTPUT2
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
                                st.write(A1N, ": PHP", A1con)
                                st.write(A2N, ": PHP", A2con)
                                st.write(A3N, ": PHP", A3con)
                                st.write(A4N, ": PHP", A4con)
                                st.write(A5N, ": PHP", A5con)
                                st.write(A6N, ": PHP", A6con)
                                st.write(A7N, ": PHP", A7con)
                                st.write(A8N, ": PHP", A8con)
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.markdown(
                                    "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                st.write("Electricity bill: PHP", total8)
                                st.write("Energy consumption:", Kh8, "kWh")

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
                            wh7 = (A1 + A2 + A3 + A4 + A5 + A6 + A7)

                            # TOTAL: Kilo-watt/hour kada month.
                            Kh7 = ((wh7 * 30) / 1000)

                            # TOTAL: para ma compute ang (cost) kada month.
                            total7 = cost * Kh7

                            # INDIVIDUALLY: para ma compute ang (cost) kada month.
                            A1con = ((A1 * 30) / 1000) * cost
                            A2con = ((A2 * 30) / 1000) * cost
                            A3con = ((A3 * 30) / 1000) * cost
                            A4con = ((A4 * 30) / 1000) * cost
                            A5con = ((A5 * 30) / 1000) * cost
                            A6con = ((A6 * 30) / 1000) * cost
                            A7con = ((A7 * 30) / 1000) * cost
                            # INDIVIDUAL: Kilo-watt/hour
                            Y1 = (A1*30)/1000
                            Y2 = (A2*30)/1000
                            Y3 = (A3*30)/1000
                            Y4 = (A4*30)/1000
                            Y5 = (A5*30)/1000
                            Y6 = (A6*30)/1000
                            Y7 = (A7*30)/1000

                            # OUTPUT1
                            st.markdown("## **THE RESULTS:**")
                            # Identify the high consumption appliance
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.markdown("**HIGHEST ENERGY CONSUMPTION**")
                            apps = [Y1,Y2,Y3,Y4,Y5,Y6,Y7]
                            max_app = apps[0]
                            for app in apps:
                                if app > max_app:
                                    max_app = app
                            if max_app == Y1:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A1N)
                                st.write("Electricity bill   : PHP", A1con)
                                st.write("Energy consumption :", Y1)
                            if max_app == Y2:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A2N)
                                st.write("Electricity bill   : PHP", A2con)
                                st.write("Energy consumption :", Y2)
                            if max_app == Y3:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A3N)
                                st.write("Electricity bill   : PHP", A3con)
                                st.write("Energy consumption :", Y3)
                            if max_app == Y4:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A4N)
                                st.write("Electricity bill   : PHP", A4con)
                                st.write("Energy consumption :", Y4)
                            if max_app == Y5:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A5N)
                                st.write("Electricity bill   : PHP", A5con)
                                st.write("Energy consumption :", Y5)
                            if max_app == Y6:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A6N)
                                st.write("Electricity bill   : PHP", A6con)
                                st.write("Energy consumption :", Y6)
                            if max_app == Y7:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A7N)
                                st.write("Electricity bill   : PHP", A7con)
                                st.write("Energy consumption :", Y7)
                            # OUTPUT2
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
                            st.write(A1N, ": PHP", A1con)
                            st.write(A2N, ": PHP", A2con)
                            st.write(A3N, ": PHP", A3con)
                            st.write(A4N, ": PHP", A4con)
                            st.write(A5N, ": PHP", A5con)
                            st.write(A6N, ": PHP", A6con)
                            st.write(A7N, ": PHP", A7con)
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.markdown(
                                "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                            st.write("Electricity bill: PHP", total7)
                            st.write("Energy consumption:", Kh7, "kWh")

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
                        wh6 = (A1 + A2 + A3 + A4 + A5 + A6)

                        # TOTAL: Kilo-watt/hour kada month.
                        Kh6 = ((wh6 * 30) / 1000)

                        # TOTAL: para ma compute ang (cost) kada month.
                        total6 = cost * Kh6

                        # INDIVIDUALLY: para ma compute ang (cost) kada month.
                        A1con = ((A1 * 30) / 1000) * cost
                        A2con = ((A2 * 30) / 1000) * cost
                        A3con = ((A3 * 30) / 1000) * cost
                        A4con = ((A4 * 30) / 1000) * cost
                        A5con = ((A5 * 30) / 1000) * cost
                        A6con = ((A6 * 30) / 1000) * cost

                        # INDIVIDUAL: Kilo-watt/hour
                        Y1 = (A1*30)/1000
                        Y2 = (A2*30)/1000
                        Y3 = (A3*30)/1000
                        Y4 = (A4*30)/1000
                        Y5 = (A5*30)/1000
                        Y6 = (A6*30)/1000

                        # OUTPUT1
                        st.markdown("## **THE RESULTS:**")
                        # Identify the high consumption appliance
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.markdown("**HIGHEST ENERGY CONSUMPTION**")
                        apps = [Y1, Y2, Y3, Y4, Y5, Y6]
                        max_app = apps[0]
                        for app in apps:
                            if app > max_app:
                                max_app = app
                        if max_app == Y1:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A1N)
                            st.write("Electricity bill   : PHP", A1con)
                            st.write("Energy consumption :", Y1)
                        if max_app == Y2:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A2N)
                            st.write("Electricity bill   : PHP", A2con)
                            st.write("Energy consumption :", Y2)
                        if max_app == Y3:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A3N)
                            st.write("Electricity bill   : PHP", A3con)
                            st.write("Energy consumption :", Y3)
                        if max_app == Y4:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A4N)
                            st.write("Electricity bill   : PHP", A4con)
                            st.write("Energy consumption :", Y4)
                        if max_app == Y5:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A5N)
                            st.write("Electricity bill   : PHP", A5con)
                            st.write("Energy consumption :", Y5)
                        if max_app == Y6:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A6N)
                            st.write("Electricity bill   : PHP", A6con)
                            st.write("Energy consumption :", Y6)
                        # OUTPUT2
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
                        st.write(A1N, ": PHP", A1con)
                        st.write(A2N, ": PHP", A2con)
                        st.write(A3N, ": PHP", A3con)
                        st.write(A4N, ": PHP", A4con)
                        st.write(A5N, ": PHP", A5con)
                        st.write(A6N, ": PHP", A6con)
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.markdown(
                            "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                        st.write("Electricity bill: PHP", total6)
                        st.write("Energy consumption:", Kh6, "kWh")

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
                    wh5 = (A1 + A2 + A3 + A4 + A5)

                    # TOTAL: Kilo-watt/hour kada month.
                    Kh5 = ((wh5 * 30) / 1000)

                    # TOTAL: para ma compute ang (cost) kada month.
                    total5 = cost * Kh5

                    # INDIVIDUALLY: para ma compute ang (cost) kada month.
                    A1con = ((A1 * 30) / 1000) * cost
                    A2con = ((A2 * 30) / 1000) * cost
                    A3con = ((A3 * 30) / 1000) * cost
                    A4con = ((A4 * 30) / 1000) * cost
                    A5con = ((A5 * 30) / 1000) * cost

                    # INDIVIDUAL: Kilo-watt/hour
                    Y1 = (A1*30)/1000
                    Y2 = (A2*30)/1000
                    Y3 = (A3*30)/1000
                    Y4 = (A4*30)/1000
                    Y5 = (A5*30)/1000

                    # OUTPUT1
                    st.markdown("## **THE RESULTS:**")
                    # Identify the high consumption appliance
                    st.write("************************************************************************************************************************************************************************")
                    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
                    apps = [Y1, Y2, Y3, Y4, Y5]
                    max_app = apps[0]
                    for app in apps:
                        if app > max_app:
                            max_app = app
                    if max_app == Y1:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A1N)
                        st.write("Electricity bill   : PHP", A1con)
                        st.write("Energy consumption :", Y1)
                    if max_app == Y2:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A2N)
                        st.write("Electricity bill   : PHP", A2con)
                        st.write("Energy consumption :", Y2)
                    if max_app == Y3:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A3N)
                        st.write("Electricity bill   : PHP", A3con)
                        st.write("Energy consumption :", Y3)
                    if max_app == Y4:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A4N)
                        st.write("Electricity bill   : PHP", A4con)
                        st.write("Energy consumption :", Y4)
                    if max_app == Y5:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A5N)
                        st.write("Electricity bill   : PHP", A5con)
                        st.write("Energy consumption :", Y5)
                    # OUTPUT2
                    st.write("************************************************************************************************************************************************************************")
                    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
                    st.write(A1N, ": PHP", A1con)
                    st.write(A2N, ": PHP", A2con)
                    st.write(A3N, ": PHP", A3con)
                    st.write(A4N, ": PHP", A4con)
                    st.write(A5N, ": PHP", A5con)
                    st.write("************************************************************************************************************************************************************************")
                    st.markdown(
                        "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                    st.write("Electricity bill: PHP", total5)
                    st.write("Energy consumption:", Kh5, "kWh")

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
                # INDIVIDUAL: Kilo-watt/hour
                Y1 = (A1*30)/1000
                Y2 = (A2*30)/1000
                Y3 = (A3*30)/1000
                Y4 = (A4*30)/1000

                # OUTPUT1
                st.markdown("## **THE RESULTS:**")
                # Identify the high consumption appliance
                st.write("************************************************************************************************************************************************************************")
                st.markdown("**HIGHEST ENERGY CONSUMPTION**")
                apps = [Y1, Y2, Y3, Y4]
                max_app = apps[0]
                for app in apps:
                    if app > max_app:
                        max_app = app
                if max_app == Y1:
                    st.write("************************************************************************************************************************************************************************")
                    st.write("Name of appliance  :", A1N)
                    st.write("Electricity bill   : PHP", A1con)
                    st.write("Energy consumption :", Y1)
                if max_app == Y2:
                    st.write("************************************************************************************************************************************************************************")
                    st.write("Name of appliance  :", A2N)
                    st.write("Electricity bill   : PHP", A2con)
                    st.write("Energy consumption :", Y2)
                if max_app == Y3:
                    st.write("************************************************************************************************************************************************************************")
                    st.write("Name of appliance  :", A3N)
                    st.write("Electricity bill   : PHP", A3con)
                    st.write("Energy consumption :", Y3)
                if max_app == Y4:
                    st.write("************************************************************************************************************************************************************************")
                    st.write("Name of appliance  :", A4N)
                    st.write("Electricity bill   : PHP", A4con)
                    st.write("Energy consumption :", Y4)
                # OUTPUT2
                st.write("************************************************************************************************************************************************************************")
                st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
                st.write(A1N, ": PHP", A1con,)
                st.write(A2N, ": PHP", A2con,)
                st.write(A3N, ": PHP", A3con,)
                st.write(A4N, ": PHP", A4con,)
                st.write("************************************************************************************************************************************************************************")
                st.markdown(
                    "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                st.write("Electricity bill: PHP", total4)
                st.write("Energy consumption:", Kh4, "kWh")

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

            # INDIVIDUAL: Kilo-watt/hour
            Y1 = (A1*30)/1000
            Y2 = (A2*30)/1000
            Y3 = (A3*30)/1000

            # OUTPUT1
            st.markdown("## **THE RESULTS:**")
            # Identify the high consumption appliance
            st.write("************************************************************************************************************************************************************************")
            st.markdown("**HIGHEST ENERGY CONSUMPTION**")
            apps = [Y1, Y2, Y3]
            max_app = apps[0]
            for app in apps:
                if app > max_app:
                    max_app = app
            if max_app == Y1:
                st.write("************************************************************************************************************************************************************************")
                st.write("Name of appliance  :", A1N)
                st.write("Electricity bill   : PHP", A1con)
                st.write("Energy consumption :", Y1)
            if max_app == Y2:
                st.write("************************************************************************************************************************************************************************")
                st.write("Name of appliance  :", A2N)
                st.write("Electricity bill   : PHP", A2con)
                st.write("Energy consumption :", Y2)
            if max_app == Y3:
                st.write("************************************************************************************************************************************************************************")
                st.write("Name of appliance  :", A3N)
                st.write("Electricity bill   : PHP", A3con)
                st.write("Energy consumption :", Y3)
            # OUTPUT2
            st.write("************************************************************************************************************************************************************************")
            st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
            st.write(A1N, ": PHP", A1con)
            st.write(A2N, ": PHP", A2con)
            st.write(A3N, ": PHP", A3con)
            st.write("************************************************************************************************************************************************************************")
            st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
            st.write("Electricity bill: PHP", total3)
            st.write("Energy consumption:", Kh3, "kWh")

# compute app1 and 2 (2nd line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
        Kh2 = (wh2*30) / 1000

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
        st.write("************************************************************************************************************************************************************************")
        st.markdown("**HIGHEST ENERGY CONSUMPTION**")
        apps = [Y1, Y2]
        max_app = apps[0]
        for app in apps:
            if app > max_app:
                max_app = app
        if max_app == Y2:
            st.write("************************************************************************************************************************************************************************")
            st.write("Name of appliance  :", A1N)
            st.write("Electricity bill   : PHP", A1con)
            st.write("Energy consumption :", Y1)
        if max_app == Y2:
            st.write("************************************************************************************************************************************************************************")
            st.write("Name of appliance  :", A2N)
            st.write("Electricity bill   : PHP", A2con)
            st.write("Energy consumption :", Y2)
        # OUTPUT2
        st.write("************************************************************************************************************************************************************************")
        st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
        st.write(A1N, ": PHP", A1con)
        st.write(A2N, ": PHP", A2con)
        st.write("************************************************************************************************************************************************************************")
        st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
        st.write("Electricity bill: PHP", total2)
        st.write("Energy consumption:", Kh2, "kWh")

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
