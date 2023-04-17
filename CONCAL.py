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
ask3 = 0
ask4 = 0
ask5 = 0
ask6 = 0
ask7 = 0
ask8 = 0
ask9 = 0
ask10 = 0
ask11 = 0
ask12 = 0
ask13 = 0
ask14 = 0
ask15 = 0
ask16 = 0
ask17 = 0
ask18 = 0
ask19 = 0
ask20 = 0
ask21 = 0
ask22 = 0
ask23 = 0
ask24 = 0
ask25 = 0
ask26 = 0
ask27 = 0
ask28 = 0
ask29 = 0
ask30 = 0
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
        if 31 >= A1D >= 1:
            ask1 = st.number_input(
                "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if ask1 == 1:  # add app2 (1st line)
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 2nd appliance.</span>", unsafe_allow_html=True)
    A2N = st.text_input("Name of 2nd appliance: ")
    if A2N:
        A2M = st.number_input(
            f"How many {A2N} are you using?", value=0, step=1)
        A2W = st.number_input(f"What is the wattage of {A2N}?(watt)")
        A2B = st.number_input(
            f"How many days in a month do you use {A2N}?(1-31)", value=0, step=1)
        if 31 >= A2B >= 1:
            A2D = st.number_input(
                f"How many hours in a day do you use {A2N}?(1-24)")
            if 31 >= A2D >= 1:
                ask2 = st.number_input(
                    "Add 3rd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if ask2 == 1:  # add app3 (2nd line)
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 3rd appliance.</span>", unsafe_allow_html=True)
    A3N = st.text_input("Name of 3rd appliance:")
    if A3N:
        A3M = st.number_input(f"How many {A3N} are you using?", value=0, step=1)
        A3W = st.number_input(f"What is the wattage of {A3N}?(watt)")
        A3B = st.number_input(f"How many days in a month do you use {A3N}?(1-31)", value=0, step=1)
        if 31 >= A3B >= 1:
            A3D = st.number_input(f"How many hours in a day do you use {A3N}?(1-24)")
            if 31 >= A3D >= 1:
                ask3 = st.number_input("Add 4th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if ask3 == 1:  # add app4 (3rd line)
            st.write("***")
            st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 4th appliance.</span>", unsafe_allow_html=True)
            A4N = st.text_input("Name of 4th appliance: ")
            if A4N:
                A4M = st.number_input(
                    f"How many {A4N} are you using?", value=0, step=1)
                A4W = st.number_input(f"What is the wattage of {A4N}?(watt)")
                A4B = st.number_input(
                    f"How many days in a month do you use {A4N}?(1-31)", value=0, step=1)
                if 31 >= A4B >= 1:
                    A4D = st.number_input(
                        f"How many hours in a day do you use {A4N}?(1-24)")
                    if 31 >= A4D >= 1:
                        ask4 = st.number_input(
                            "Add 5th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if ask4 == 1:  # add app5 (4th line)
                st.write("***")
                st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 5th appliance.</span>", unsafe_allow_html=True)
                A5N = st.text_input("Name of 5th appliance: ")
                if A5N:
                    A5M = st.number_input(
                        f"How many {A5N} are you using?", value=0, step=1)
                    A5W = st.number_input(
                        f"What is the wattage of {A5N}?(watt)")
                    A5B = st.number_input(
                        f"How many days in a month do you use {A5N}?(1-31)", value=0, step=1)
                    if 31 >= A5B >= 1:
                        A5D = st.number_input(
                            f"How many hours in a day do you use {A5N}?(1-24)")
                        if 31 >= A5D >= 1:
                            ask5 = st.number_input(
                                "Add 6th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                if ask5 == 1:  # add app6 (5th line)
                    st.write("***")
                    st.write(
                        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 6th appliance.</span>", unsafe_allow_html=True)
                    A6N = st.text_input("Name of 6th appliance: ")
                    if A6N:
                        A6M = st.number_input(
                            f"How many {A6N} are you using?", value=0, step=1)
                        A6W = st.number_input(
                            f"What is the wattage of {A6N}?(watt)")
                        A6B = st.number_input(
                            f"How many days in a month do you use {A6N}?(1-31)", value=0, step=1)
                        if 31 >= A6B >= 1:
                            A6D = st.number_input(
                                f"How many hours in a day do you use {A6N}?(1-24)")
                            if 31 >= A6D >= 1:
                                ask6 = st.number_input(
                                    "Add 7th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if ask6 == 1:  # add app7 (6th line)
                        st.write("***")
                        st.write(
                            "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 7th appliance.</span>", unsafe_allow_html=True)
                        A7N = st.text_input("Name of 7th appliance: ")
                        if A7N:
                            A7M = st.number_input(
                                f"How many {A7N} are you using?", value=0, step=1)
                            A7W = st.number_input(
                                f"What is the wattage of {A7N}?(watt)")
                            A7B = st.number_input(
                                f"How many days in a month do you use {A7N}?(1-31)", value=0, step=1)
                            if 31 >= A7B >= 1:
                                A7D = st.number_input(
                                    f"How many hours in a day do you use {A7N}?(1-24)")
                                if 31 >= A7D >= 1:
                                    ask7 = st.number_input(
                                        "Add 8th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        if ask7 == 1:  # add app8 (7th line)
                            st.write("***")
                            st.write(
                                "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 8th appliance.</span>", unsafe_allow_html=True)
                            A8N = st.text_input("Name of 8th appliance: ")
                            if A8N:
                                A8M = st.number_input(
                                    f"How many {A8N} are you using?", value=0, step=1)
                                A8W = st.number_input(
                                    f"What is the wattage of {A8N}?(watt)")
                                A8B = st.number_input(
                                    f"How many days in a month do you use {A8N}?(1-31)", value=0, step=1)
                                if 31 >= A8B >= 1:
                                    A8D = st.number_input(
                                        f"How many hours in a day do you use {A8N}?(1-24)")
                                    if 31 >= A8D >= 1:
                                        ask8 = st.number_input(
                                            "Add 9th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                            if ask8 == 1:  # add app9 (8th line)
                                st.write("***")
                                st.write(
                                    "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 9th appliance.</span>", unsafe_allow_html=True)
                                A9N = st.text_input("Name of 9th appliance: ")
                                if A9N:
                                    A9M = st.number_input(
                                        f"How many {A9N} are you using?", value=0, step=1)
                                    A9W = st.number_input(
                                        f"What is the wattage of {A9N}?(watt)")
                                    A9B = st.number_input(
                                        f"How many days in a month do you use {A9N}?(1-31)", value=0, step=1)
                                    if 31 >= A9B >= 1:
                                        A9D = st.number_input(
                                            f"How many hours in a day do you use {A9N}?(1-24)")
                                        if 31 >= A9D >= 1:
                                            ask9 = st.number_input(
                                                "Add 10th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                if ask9 == 1:  # add app10 (9th line)
                                    st.write("***")
                                    st.write(
                                        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 10th appliance.</span>", unsafe_allow_html=True)
                                    A10N = st.text_input(
                                        "Name of 10th appliance: ")
                                    if A10N:
                                        A10M = st.number_input(
                                            f"How many {A10N} are you using?", value=0, step=1)
                                        A10W = st.number_input(
                                            f"What is the wattage of {A10N}?(watt)")
                                        A10B = st.number_input(
                                            f"How many days in a month do you use {A10N}?(1-31)", value=0, step=1)
                                        if 31 >= A10B >= 1:
                                            A10D = st.number_input(
                                                f"How many hours in a day do you use {A10N}?(1-24)")
                                            if 31 >= A10D >= 1:
                                                ask10 = st.number_input(
                                                    "Add 11th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                    if ask10 == 1:  # add app11 (10th line)
                                        st.write("***")
                                        st.write(
                                            "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 11th appliance.</span>", unsafe_allow_html=True)
                                        A11N = st.text_input(
                                            "Name of 11th appliance:")
                                        if A11N:
                                            A11M = st.number_input(
                                                f"How many {A11N} are you using?", value=0, step=1)
                                            A11W = st.number_input(
                                                f"What is the wattage of {A11N}?(watt)")
                                            A11B = st.number_input(
                                                f"How many days in a month do you use {A11N}?(1-31)", value=0, step=1)
                                            if 31 >= A11B >= 1:
                                                A11D = st.number_input(
                                                    f"How many hours in a day do you use {A11N}?(1-24)")
                                                if 31 >= A11D >= 1:
                                                    ask11 = st.number_input(
                                                        "Add 12th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                        if ask11 == 1:  # add app12 (11th line)
                                            st.write("***")
                                            st.write(
                                                "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 12th appliance.</span>", unsafe_allow_html=True)
                                            A12N = st.text_input(
                                                "Name of 12th appliance: ")
                                            if A12N:
                                                A12M = st.number_input(
                                                    f"How many {A12N} are you using?", value=0, step=1)
                                                A12W = st.number_input(
                                                    f"What is the wattage of {A12N}?(watt)")
                                                A12B = st.number_input(
                                                    f"How many days in a month do you use {A12N}?(1-31)", value=0, step=1)
                                                if 31 >= A12B >= 1:
                                                    A12D = st.number_input(
                                                        f"How many hours in a day do you use {A12N}?(1-24)")
                                                    if 31 >= A12D >= 1:
                                                        ask12 = st.number_input(
                                                            "Add 13th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
 # add app1 to 13 (12th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                            if ask12 == 1:
                                                st.write("***")
                                                st.write(
                                                    "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 13th appliance.</span>", unsafe_allow_html=True)
                                                A13N = st.text_input(
                                                    "Name of 13th appliance: ")
                                                if A13N:
                                                    A13M = st.number_input(
                                                        f"How many {A13N} are you using?", value=0, step=1)
                                                    A13W = st.number_input(
                                                        f"What is the wattage of {A13N}?(watt)")
                                                    A13B = st.number_input(
                                                        f"How many days in a month do you use {A13N}?(1-31)", value=0, step=1)
                                                    if 31 >= A13B >= 1:
                                                        A13D = st.number_input(
                                                            f"How many hours in a day do you use {A13N}?(1-24)")
                                                        if 31 >= A13D >= 1:
                                                            ask13 = st.number_input(
                                                                "Add 14th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# add app1 to 14 (13th line) ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                if ask13 == 1:
                                                    st.write("***")
                                                    st.write(
                                                        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 14th appliance.</span>", unsafe_allow_html=True)
                                                    A14N = st.text_input(
                                                        "Name of 14th appliance: ")
                                                    if A14N:
                                                        A14M = st.number_input(
                                                            f"How many {A14N} are you using?", value=0, step=1)
                                                        A14W = st.number_input(
                                                            f"What is the wattage of {A14N}?(watt)")
                                                        A14B = st.number_input(
                                                            f"How many days in a month do you use {A14N}?(1-31)", value=0, step=1)
                                                        if 31 >= A14B >= 1:
                                                            A14D = st.number_input(
                                                                f"How many hours in a day do you use {A14N}?(1-24)")
                                                            if 31 >= A14D >= 1:
                                                                ask14 = st.number_input(
                                                                    "Add 15th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# -----------------------add app1 to 15 (14th line)////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                    # add app7 (6th line)
                                                    if ask14 == 1:
                                                        st.write("***")
                                                        st.write(
                                                            "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 16th appliance.</span>", unsafe_allow_html=True)
                                                        A15N = st.text_input(
                                                            "Name of 15th appliance: ")
                                                        if A15N:
                                                            A15M = st.number_input(
                                                                f"How many {A15N} are you using?", value=0, step=1)
                                                            A15W = st.number_input(
                                                                f"What is the wattage of {A15N}?(watt)")
                                                            A15B = st.number_input(
                                                                f"How many days in a month do you use {A15N}?(1-31)", value=0, step=1)
                                                            if 31 >= A15B >= 1:
                                                                A15D = st.number_input(
                                                                    f"How many hours in a day do you use {A15N}?(1-24)")
                                                                if 31 >= A15D >= 1:
                                                                    ask15 = st.number_input(
                                                                        "Add 16th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# -----------------------add app1 to 16 (15th line)////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                    # add app7 (6th line)
                                                        if ask15 == 1:
                                                            st.write("***")
                                                            st.write(
                                                                "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 16th appliance.</span>", unsafe_allow_html=True)
                                                            A16N = st.text_input(
                                                                "Name of 16th appliance: ")
                                                            if A16N:
                                                                A16M = st.number_input(
                                                                    f"How many {A16N} are you using?", value=0, step=1)
                                                                A16W = st.number_input(
                                                                    f"What is the wattage of {A16N}?(watt)")
                                                                A16B = st.number_input(
                                                                    f"How many days in a month do you use {A16N}?(1-31)", value=0, step=1)
                                                                if 31 >= A16B >= 1:
                                                                    A16D = st.number_input(
                                                                        f"How many hours in a day do you use {A16N}?(1-24)")
                                                                    if 31 >= A16D >= 1:
                                                                        ask16 = st.number_input(
                                                                            "Add 17th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# -----------------------add app1 to 16 (15th line)////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                            # add app2 (1st line)
                                                            if ask16 == 1:
                                                                st.write("***")
                                                                st.write(
                                                                    "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 17th appliance.</span>", unsafe_allow_html=True)
                                                                A17N = st.text_input(
                                                                    "Name of 17th appliance: ")
                                                                if A17N:
                                                                    A17M = st.number_input(
                                                                        f"How many {A17N} are you using?", value=0, step=1)
                                                                    A17W = st.number_input(
                                                                        f"What is the wattage of {A17N}?(watt)")
                                                                    A17B = st.number_input(
                                                                        f"How many days in a month do you use {A17N}?(1-31)", value=0, step=1)
                                                                    if 31 >= A17B >= 1:
                                                                        A17D = st.number_input(
                                                                            f"How many hours in a day do you use {A17N}?(1-24)")
                                                                        if 31 >= A17D >= 1:
                                                                            ask17 = st.number_input(
                                                                                "Add 18th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                # add app3 (2nd line)
                                                                if ask17 == 1:
                                                                    st.write(
                                                                        "***")
                                                                    st.write(
                                                                        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 18th appliance.</span>", unsafe_allow_html=True)
                                                                    A18N = st.text_input(
                                                                        "Name of 18th appliance:")
                                                                    if A18N:
                                                                        A18M = st.number_input(
                                                                            f"How many {A18N} are you using?", value=0, step=1)
                                                                        A18W = st.number_input(
                                                                            f"What is the wattage of {A18N}?(watt)")
                                                                        A18B = st.number_input(
                                                                            f"How many days in a month do you use {A18N}?(1-31)", value=0, step=1)
                                                                        if 31 >= A18B >= 1:
                                                                            A18D = st.number_input(
                                                                                f"How many hours in a day do you use {A18N}?(1-24)")
                                                                            if 31 >= A18D >= 1:
                                                                                ask18 = st.number_input(
                                                                                    "Add 19th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                    # add app4 (3rd line)
                                                                    if ask18 == 1:
                                                                        st.write(
                                                                            "***")
                                                                        st.write(
                                                                            "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 19th appliance.</span>", unsafe_allow_html=True)
                                                                        A19N = st.text_input(
                                                                            "Name of 19th appliance: ")
                                                                        if A19N:
                                                                            A19M = st.number_input(
                                                                                f"How many {A19N} are you using?", value=0, step=1)
                                                                            A19W = st.number_input(
                                                                                f"What is the wattage of {A19N}?(watt)")
                                                                            A19B = st.number_input(
                                                                                f"How many days in a month do you use {A19N}?(1-31)", value=0, step=1)
                                                                            if 31 >= A19B >= 1:
                                                                                A19D = st.number_input(
                                                                                    f"How many hours in a day do you use {A19N}?(1-24)")
                                                                                if 31 >= A19D >= 1:
                                                                                    ask19 = st.number_input(
                                                                                        "Add 20th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                        # add app5 (4th line)
                                                                        if ask19 == 1:
                                                                            st.write(
                                                                                "***")
                                                                            st.write(
                                                                                "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 20th appliance.</span>", unsafe_allow_html=True)
                                                                            A20N = st.text_input(
                                                                                "Name of 20th appliance: ")
                                                                            if A20N:
                                                                                A20M = st.number_input(
                                                                                    f"How many {A20N} are you using?", value=0, step=1)
                                                                                A20W = st.number_input(
                                                                                    f"What is the wattage of {A20N}?(watt)")
                                                                                A20B = st.number_input(
                                                                                    f"How many days in a month do you use {A20N}?(1-31)", value=0, step=1)
                                                                                if 31 >= A20B >= 1:
                                                                                    A20D = st.number_input(
                                                                                        f"How many hours in a day do you use {A20N}?(1-24)")
                                                                                    if 31 >= A20D >= 1:
                                                                                        ask20 = st.number_input(
                                                                                            "Add 21st appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                            # add app6 (5th line)
                                                                            if ask20 == 1:
                                                                                st.write(
                                                                                    "***")
                                                                                st.write(
                                                                                    "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 21st appliance.</span>", unsafe_allow_html=True)
                                                                                A21N = st.text_input(
                                                                                    "Name of 21st appliance: ")
                                                                                if A21N:
                                                                                    A21M = st.number_input(
                                                                                        f"How many {A21N} are you using?", value=0, step=1)
                                                                                    A21W = st.number_input(
                                                                                        f"What is the wattage of {A21N}?(watt)")
                                                                                    A21B = st.number_input(
                                                                                        f"How many days in a month do you use {A21N}?(1-31)", value=0, step=1)
                                                                                    if 31 >= A21B >= 1:
                                                                                        A21D = st.number_input(
                                                                                            f"How many hours in a day do you use {A21N}?(1-24)")
                                                                                        if 31 >= A21D >= 1:
                                                                                            ask21 = st.number_input(
                                                                                                "Add 22nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                # add app7 (6th line)
                                                                                if ask21 == 1:
                                                                                    st.write(
                                                                                        "***")
                                                                                    st.write(
                                                                                        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 22nd appliance.</span>", unsafe_allow_html=True)
                                                                                    A22N = st.text_input(
                                                                                        "Name of 22nd appliance: ")
                                                                                    if A22N:
                                                                                        A22M = st.number_input(
                                                                                            f"How many {A22N} are you using?", value=0, step=1)
                                                                                        A22W = st.number_input(
                                                                                            f"What is the wattage of {A22N}?(watt)")
                                                                                        A22B = st.number_input(
                                                                                            f"How many days in a month do you use {A22N}?(1-31)", value=0, step=1)
                                                                                        if 31 >= A22B >= 1:
                                                                                            A22D = st.number_input(
                                                                                                f"How many hours in a day do you use {A22N}?(1-24)")
                                                                                            if 31 >= A22D >= 1:
                                                                                                ask22 = st.number_input(
                                                                                                    "Add 23rd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                    # add app8 (7th line)
                                                                                    if ask22 == 1:
                                                                                        st.write(
                                                                                            "***")
                                                                                        st.write(
                                                                                            "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 23rd appliance.</span>", unsafe_allow_html=True)
                                                                                        A23N = st.text_input(
                                                                                            "Name of 23rd appliance: ")
                                                                                        if A23N:
                                                                                            A23M = st.number_input(
                                                                                                f"How many {A23N} are you using?", value=0, step=1)
                                                                                            A23W = st.number_input(
                                                                                                f"What is the wattage of {A23N}?(watt)")
                                                                                            A23B = st.number_input(
                                                                                                f"How many days in a month do you use {A23N}?(1-31)", value=0, step=1)
                                                                                            if 31 >= A23B >= 1:
                                                                                                A23D = st.number_input(
                                                                                                    f"How many hours in a day do you use {A23N}?(1-24)")
                                                                                                if 31 >= A23D >= 1:
                                                                                                    ask23 = st.number_input(
                                                                                                        "Add 24th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                        # add app9 (8th line)
                                                                                        if ask23 == 1:
                                                                                            st.write(
                                                                                                "***")
                                                                                            st.write(
                                                                                                "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 24th appliance.</span>", unsafe_allow_html=True)
                                                                                            A24N = st.text_input(
                                                                                                "Name of 24th appliance: ")
                                                                                            if A24N:
                                                                                                A24M = st.number_input(
                                                                                                    f"How many {A24N} are you using?", value=0, step=1)
                                                                                                A24W = st.number_input(
                                                                                                    f"What is the wattage of {A24N}?(watt)")
                                                                                                A24B = st.number_input(
                                                                                                    f"How many days in a month do you use {A24N}?(1-31)", value=0, step=1)
                                                                                                if 31 >= A24B >= 1:
                                                                                                    A24D = st.number_input(
                                                                                                        f"How many hours in a day do you use {A24N}?(1-24)")
                                                                                                    if 31 >= A24D >= 1:
                                                                                                        ask24 = st.number_input(
                                                                                                            "Add 25th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                            # add app10 (9th line)
                                                                                            if ask24 == 1:
                                                                                                st.write(
                                                                                                    "***")
                                                                                                st.write(
                                                                                                    "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 25th appliance.</span>", unsafe_allow_html=True)
                                                                                                A25N = st.text_input(
                                                                                                    "Name of 25th appliance: ")
                                                                                                if A25N:
                                                                                                    A25M = st.number_input(
                                                                                                        f"How many {A25N} are you using?", value=0, step=1)
                                                                                                    A25W = st.number_input(
                                                                                                        f"What is the wattage of {A25N}?(watt)")
                                                                                                    A25B = st.number_input(
                                                                                                        f"How many days in a month do you use {A25N}?(1-31)", value=0, step=1)
                                                                                                    if 31 >= A25B >= 1:
                                                                                                        A25D = st.number_input(
                                                                                                            f"How many hours in a day do you use {A25N}?(1-24)")
                                                                                                        if 31 >= A25D >= 1:
                                                                                                            ask25 = st.number_input(
                                                                                                                "Add 26th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                # add app11 (10th line)
                                                                                                if ask25 == 1:
                                                                                                    st.write(
                                                                                                        "***")
                                                                                                    st.write(
                                                                                                        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 26th appliance.</span>", unsafe_allow_html=True)
                                                                                                    A26N = st.text_input(
                                                                                                        "Name of 26th appliance:")
                                                                                                    if A26N:
                                                                                                        A26M = st.number_input(
                                                                                                            f"How many {A26N} are you using?", value=0, step=1)
                                                                                                        A26W = st.number_input(
                                                                                                            f"What is the wattage of {A26N}?(watt)")
                                                                                                        A26B = st.number_input(
                                                                                                            f"How many days in a month do you use {A26N}?(1-31)", value=0, step=1)
                                                                                                        if 31 >= A26B >= 1:
                                                                                                            A26D = st.number_input(
                                                                                                                f"How many hours in a day do you use {A26N}?(1-24)")
                                                                                                            if 31 >= A26D >= 1:
                                                                                                                ask26 = st.number_input(
                                                                                                                    "Add 27th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                    # add app12 (11th line)
                                                                                                    if ask26 == 1:
                                                                                                        st.write(
                                                                                                            "***")
                                                                                                        st.write(
                                                                                                            "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 27th appliance.</span>", unsafe_allow_html=True)
                                                                                                        A27N = st.text_input(
                                                                                                            "Name of 27th appliance: ")
                                                                                                        if A27N:
                                                                                                            A27M = st.number_input(
                                                                                                                f"How many {A27N} are you using?", value=0, step=1)
                                                                                                            A27W = st.number_input(
                                                                                                                f"What is the wattage of {A27N}?(watt)")
                                                                                                            A27B = st.number_input(
                                                                                                                f"How many days in a month do you use {A27N}?(1-31)", value=0, step=1)
                                                                                                            if 31 >= A27B >= 1:
                                                                                                                A27D = st.number_input(
                                                                                                                    f"How many hours in a day do you use {A27N}?(1-24)")
                                                                                                                if 31 >= A27D >= 1:
                                                                                                                    ask27 = st.number_input(
                                                                                                                        "Add 28th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # add app1 to 13 (12th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                        if ask27 == 1:
                                                                                                            st.write(
                                                                                                                "***")
                                                                                                            st.write(
                                                                                                                "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 28th appliance.</span>", unsafe_allow_html=True)
                                                                                                            A28N = st.text_input(
                                                                                                                "Name of 28th appliance: ")
                                                                                                            if A28N:
                                                                                                                A28M = st.number_input(
                                                                                                                    f"How many {A28N} are you using?", value=0, step=1)
                                                                                                                A28W = st.number_input(
                                                                                                                    f"What is the wattage of {A28N}?(watt)")
                                                                                                                A28B = st.number_input(
                                                                                                                    f"How many days in a month do you use {A28N}?(1-31)", value=0, step=1)
                                                                                                                if 31 >= A28B >= 1:
                                                                                                                    A28D = st.number_input(
                                                                                                                        f"How many hours in a day do you use {A28N}?(1-24)")
                                                                                                                    if 31 >= A28D >= 1:
                                                                                                                        ask28 = st.number_input(
                                                                                                                            "Add 29th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # add app1 to 14 (13th line) ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                            if ask28 == 1:
                                                                                                                st.write(
                                                                                                                    "***")
                                                                                                                st.write(
                                                                                                                    "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 29th appliance.</span>", unsafe_allow_html=True)
                                                                                                                A29N = st.text_input(
                                                                                                                    "Name of 29th appliance: ")
                                                                                                                if A29N:
                                                                                                                    A29M = st.number_input(
                                                                                                                        f"How many {A29N} are you using?", value=0, step=1)
                                                                                                                    A29W = st.number_input(
                                                                                                                        f"What is the wattage of {A29N}?(watt)")
                                                                                                                    A29B = st.number_input(
                                                                                                                        f"How many days in a month do you use {A29N}?(1-31)", value=0, step=1)
                                                                                                                    if 31 >= A29B >= 1:
                                                                                                                        A29D = st.number_input(
                                                                                                                            f"How many hours in a day do you use {A29N}?(1-24)")
                                                                                                                        if 31 >= A29D >= 1:
                                                                                                                            ask29 = st.number_input(
                                                                                                                                "Add 30th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
                                                            # -----------------------add app1 to 15 (14th line)////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                # add app7 (6th line)
                                                                                                                if ask29 == 1:
                                                                                                                    st.write(
                                                                                                                        "***")
                                                                                                                    st.write(
                                                                                                                        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 30th appliance.</span>", unsafe_allow_html=True)
                                                                                                                    A30N = st.text_input(
                                                                                                                        "Name of 30th appliance: ")
                                                                                                                    if A30N:
                                                                                                                        A30M = st.number_input(
                                                                                                                            f"How many {A30N} are you using?", value=0, step=1)
                                                                                                                        A30W = st.number_input(
                                                                                                                            f"What is the wattage of {A30N}?(watt)")
                                                                                                                        A30B = st.number_input(
                                                                                                                            f"How many days in a month do you use {A30N}?(1-31)", value=0, step=1)
                                                                                                                        if 31 >= A30B >= 1:
                                                                                                                            A30D = st.number_input(
                                                                                                                                f"How many hours in a day do you use {A30N}?(1-24)")
                                                                                                                            if 31 >= A30D >= 1:
                                                                                                                                ask30 = 2

                                                            # compute app1 to 15 (15th line) # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                    if ask30 == 2:
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
                                                                                                                        Y1 = (
                                                                                                                            A1*30)/1000
                                                                                                                        Y2 = (
                                                                                                                            A2*30)/1000
                                                                                                                        Y3 = (
                                                                                                                            A3*30)/1000
                                                                                                                        Y4 = (
                                                                                                                            A4*30)/1000
                                                                                                                        Y5 = (
                                                                                                                            A5*30)/1000
                                                                                                                        Y6 = (
                                                                                                                            A6*30)/1000
                                                                                                                        Y7 = (
                                                                                                                            A7*30)/1000
                                                                                                                        Y8 = (
                                                                                                                            A8*30)/1000
                                                                                                                        Y9 = (
                                                                                                                            A8*30)/1000
                                                                                                                        Y10 = (
                                                                                                                            A10*30)/1000
                                                                                                                        Y11 = (
                                                                                                                            A11*30)/1000
                                                                                                                        Y12 = (
                                                                                                                            A12*30)/1000
                                                                                                                        Y13 = (
                                                                                                                            A13*30)/1000
                                                                                                                        Y14 = (
                                                                                                                            A14*30)/1000
                                                                                                                        Y15 = (
                                                                                                                            A15*30)/1000

                                                                                                                        # OUTPUT1
                                                                                                                        st.markdown(
                                                                                                                            "## **THE RESULTS:**")
                                                                                                                        # Identify the high consumption appliance
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.markdown(
                                                                                                                            "**HIGHEST ENERGY CONSUMPTION**")
                                                                                                                        apps = [
                                                                                                                            Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15]
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
                                                                                                                                "Energy consumption :", Y1, "kWh")
                                                                                                                        if max_app == Y2:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A2N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A2con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y2, "kWh")
                                                                                                                        if max_app == Y3:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A3N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A3con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y3, "kWh")
                                                                                                                        if max_app == Y4:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A4N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A4con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y4, "kWh")
                                                                                                                        if max_app == Y5:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A5N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A5con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y5, "kWh")
                                                                                                                        if max_app == Y6:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A6N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A6con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y6, "kWh")
                                                                                                                        if max_app == Y7:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A7N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A7con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y7, "kWh")
                                                                                                                        if max_app == Y8:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A8N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A8con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y8, "kWh")
                                                                                                                        if max_app == Y9:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A9N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A9con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y9, "kWh")
                                                                                                                        if max_app == Y10:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A10N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A10con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y10, "kWh")
                                                                                                                        if max_app == Y11:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A11N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A11con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y11, "kWh")
                                                                                                                        if max_app == Y12:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A12N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A12con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y12, "kWh")
                                                                                                                        if max_app == Y13:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A13N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A13con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y13, "kWh")
                                                                                                                        if max_app == Y14:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A14N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A14con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y14, "kWh")
                                                                                                                        if max_app == Y15:
                                                                                                                            st.write(
                                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                                            st.write(
                                                                                                                                "Name of appliance  :", A15N)
                                                                                                                            st.write(
                                                                                                                                "Electricity bill   : PHP", A15con)
                                                                                                                            st.write(
                                                                                                                                "Energy consumption :", Y15, "kWh")
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
                                                                                                                if ask29 == 2:
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
                                                                                                                    Y1 = (
                                                                                                                        A1*30)/1000
                                                                                                                    Y2 = (
                                                                                                                        A2*30)/1000
                                                                                                                    Y3 = (
                                                                                                                        A3*30)/1000
                                                                                                                    Y4 = (
                                                                                                                        A4*30)/1000
                                                                                                                    Y5 = (
                                                                                                                        A5*30)/1000
                                                                                                                    Y6 = (
                                                                                                                        A6*30)/1000
                                                                                                                    Y7 = (
                                                                                                                        A7*30)/1000
                                                                                                                    Y8 = (
                                                                                                                        A8*30)/1000
                                                                                                                    Y9 = (
                                                                                                                        A8*30)/1000
                                                                                                                    Y10 = (
                                                                                                                        A10*30)/1000
                                                                                                                    Y11 = (
                                                                                                                        A11*30)/1000
                                                                                                                    Y12 = (
                                                                                                                        A12*30)/1000
                                                                                                                    Y13 = (
                                                                                                                        A13*30)/1000
                                                                                                                    Y14 = (
                                                                                                                        A14*30)/1000

                                                                                                                    # OUTPUT1
                                                                                                                    st.markdown(
                                                                                                                        "## **THE RESULTS:**")
                                                                                                                    # Identify the high consumption appliance
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.markdown(
                                                                                                                        "**HIGHEST ENERGY CONSUMPTION**")
                                                                                                                    apps = [
                                                                                                                        Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14]
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
                                                                                                                            "Energy consumption :", Y1, "kWh")
                                                                                                                    if max_app == Y2:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A2N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A2con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y2, "kWh")
                                                                                                                    if max_app == Y3:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A3N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A3con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y3, "kWh")
                                                                                                                    if max_app == Y4:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A4N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A4con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y4, "kWh")
                                                                                                                    if max_app == Y5:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A5N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A5con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y5, "kWh")
                                                                                                                    if max_app == Y6:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A6N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A6con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y6, "kWh")
                                                                                                                    if max_app == Y7:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A7N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A7con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y7, "kWh")
                                                                                                                    if max_app == Y8:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A8N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A8con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y8, "kWh")
                                                                                                                    if max_app == Y9:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A9N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A9con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y9, "kWh")
                                                                                                                    if max_app == Y10:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A10N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A10con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y10, "kWh")
                                                                                                                    if max_app == Y11:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A11N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A11con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y11, "kWh")
                                                                                                                    if max_app == Y12:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A12N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A12con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y12, "kWh")
                                                                                                                    if max_app == Y13:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A13N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A13con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y13, "kWh")
                                                                                                                    if max_app == Y14:
                                                                                                                        st.write(
                                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                                        st.write(
                                                                                                                            "Name of appliance  :", A14N)
                                                                                                                        st.write(
                                                                                                                            "Electricity bill   : PHP", A14con)
                                                                                                                        st.write(
                                                                                                                            "Energy consumption :", Y14, "kWh")
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
                                                                                                            if ask28 == 2:
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

                                                                                                                # TOTAL: watt/hour kada araw.
                                                                                                                wh13 = (A1 + A2 + A3 + A4 +
                                                                                                                        A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13)

                                                                                                                # TOTAL: Kilo-watt/hour kada month.
                                                                                                                Kh13 = (
                                                                                                                    (wh13 * 30) / 1000)

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
                                                                                                                Y1 = (
                                                                                                                    A1*30)/1000
                                                                                                                Y2 = (
                                                                                                                    A2*30)/1000
                                                                                                                Y3 = (
                                                                                                                    A3*30)/1000
                                                                                                                Y4 = (
                                                                                                                    A4*30)/1000
                                                                                                                Y5 = (
                                                                                                                    A5*30)/1000
                                                                                                                Y6 = (
                                                                                                                    A6*30)/1000
                                                                                                                Y7 = (
                                                                                                                    A7*30)/1000
                                                                                                                Y8 = (
                                                                                                                    A8*30)/1000
                                                                                                                Y9 = (
                                                                                                                    A8*30)/1000
                                                                                                                Y10 = (
                                                                                                                    A10*30)/1000
                                                                                                                Y11 = (
                                                                                                                    A11*30)/1000
                                                                                                                Y12 = (
                                                                                                                    A12*30)/1000
                                                                                                                Y13 = (
                                                                                                                    A13*30)/1000

                                                                                                                # OUTPUT1
                                                                                                                st.markdown(
                                                                                                                    "## **THE RESULTS:**")
                                                                                                                # Identify the high consumption appliance
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.markdown(
                                                                                                                    "**HIGHEST ENERGY CONSUMPTION**")
                                                                                                                apps = [
                                                                                                                    Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13]
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
                                                                                                                        "Energy consumption :", Y1, "kWh")
                                                                                                                if max_app == Y2:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A2N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A2con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y2, "kWh")
                                                                                                                if max_app == Y3:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A3N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A3con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y3, "kWh")
                                                                                                                if max_app == Y4:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A4N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A4con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y4, "kWh")
                                                                                                                if max_app == Y5:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A5N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A5con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y5, "kWh")
                                                                                                                if max_app == Y6:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A6N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A6con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y6, "kWh")
                                                                                                                if max_app == A7con:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A7N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A7con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y7, "kWh")
                                                                                                                if max_app == Y8:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A8N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A8con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y8, "kWh")
                                                                                                                if max_app == Y9:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A9N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A9con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y9, "kWh")
                                                                                                                if max_app == Y10:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A10N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A10con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y10, "kWh")
                                                                                                                if max_app == Y11:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A11N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A11con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y11, "kWh")
                                                                                                                if max_app == Y12:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A12N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A12con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y12, "kWh")
                                                                                                                if max_app == Y13:
                                                                                                                    st.write(
                                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                                    st.write(
                                                                                                                        "Name of appliance  :", A13N)
                                                                                                                    st.write(
                                                                                                                        "Electricity bill   : PHP", A13con)
                                                                                                                    st.write(
                                                                                                                        "Energy consumption :", Y13, "kWh")
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
                                                                                                        if ask27 == 2:
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

                                                                                                            # TOTAL: watt/hour kada araw.
                                                                                                            wh12 = (A1 + A2 + A3 + A4 +
                                                                                                                    A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12)

                                                                                                            # TOTAL: Kilo-watt/hour kada month.
                                                                                                            Kh12 = (
                                                                                                                (wh12 * 30) / 1000)

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
                                                                                                            Y1 = (
                                                                                                                A1*30)/1000
                                                                                                            Y2 = (
                                                                                                                A2*30)/1000
                                                                                                            Y3 = (
                                                                                                                A3*30)/1000
                                                                                                            Y4 = (
                                                                                                                A4*30)/1000
                                                                                                            Y5 = (
                                                                                                                A5*30)/1000
                                                                                                            Y6 = (
                                                                                                                A6*30)/1000
                                                                                                            Y7 = (
                                                                                                                A7*30)/1000
                                                                                                            Y8 = (
                                                                                                                A8*30)/1000
                                                                                                            Y9 = (
                                                                                                                A8*30)/1000
                                                                                                            Y10 = (
                                                                                                                A10*30)/1000
                                                                                                            Y11 = (
                                                                                                                A11*30)/1000
                                                                                                            Y12 = (
                                                                                                                A12*30)/1000

                                                                                                            # OUTPUT1
                                                                                                            st.markdown(
                                                                                                                "## **THE RESULTS:**")
                                                                                                            # Identify the high consumption appliance
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.markdown(
                                                                                                                "**HIGHEST ENERGY CONSUMPTION**")
                                                                                                            apps = [
                                                                                                                Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12]
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
                                                                                                                    "Energy consumption :", Y1, "kWh")
                                                                                                            if max_app == Y2:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A2N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A2con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y2, "kWh")
                                                                                                            if max_app == Y3:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A3N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A3con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y3, "kWh")
                                                                                                            if max_app == Y4:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A4N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A4con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y4, "kWh")
                                                                                                            if max_app == Y5:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A5N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A5con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y5, "kWh")
                                                                                                            if max_app == Y6:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A6N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A6con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y6, "kWh")
                                                                                                            if max_app == A7con:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A7N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A7con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y7, "kWh")
                                                                                                            if max_app == Y8:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A8N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A8con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y8, "kWh")
                                                                                                            if max_app == Y9:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A9N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A9con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y9, "kWh")
                                                                                                            if max_app == Y10:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A10N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A10con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y10, "kWh")
                                                                                                            if max_app == Y11:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A11N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A11con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y11, "kWh")
                                                                                                            if max_app == Y12:
                                                                                                                st.write(
                                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                                st.write(
                                                                                                                    "Name of appliance  :", A12N)
                                                                                                                st.write(
                                                                                                                    "Electricity bill   : PHP", A12con)
                                                                                                                st.write(
                                                                                                                    "Energy consumption :", Y12, "kWh")
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
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.markdown(
                                                                                                                "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                                            st.write(
                                                                                                                "Electricity bill: PHP", total12)
                                                                                                            st.write(
                                                                                                                "Energy consumption:", Kh12, "kWh")

                                                            # compute app1 to 11 (11th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                    if ask26 == 2:
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

                                                                                                        # TOTAL: watt/hour kada araw.
                                                                                                        wh11 = (A1 + A2 + A3 + A4 +
                                                                                                                A5 + A6 + A7 + A8 + A9 + A10 + A11)

                                                                                                        # TOTAL: Kilo-watt/hour kada month.
                                                                                                        Kh11 = (
                                                                                                            (wh11 * 30) / 1000)

                                                                                                        # TOTAL: para ma compute ang (cost) kada month.
                                                                                                        total11 = cost * Kh11

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

                                                                                                        # INDIVIDUAL: Kilo-watt/hour
                                                                                                        Y1 = (
                                                                                                            A1*30)/1000
                                                                                                        Y2 = (
                                                                                                            A2*30)/1000
                                                                                                        Y3 = (
                                                                                                            A3*30)/1000
                                                                                                        Y4 = (
                                                                                                            A4*30)/1000
                                                                                                        Y5 = (
                                                                                                            A5*30)/1000
                                                                                                        Y6 = (
                                                                                                            A6*30)/1000
                                                                                                        Y7 = (
                                                                                                            A7*30)/1000
                                                                                                        Y8 = (
                                                                                                            A8*30)/1000
                                                                                                        Y9 = (
                                                                                                            A8*30)/1000
                                                                                                        Y10 = (
                                                                                                            A10*30)/1000
                                                                                                        Y11 = (
                                                                                                            A11*30)/1000

                                                                                                        # OUTPUT1
                                                                                                        st.markdown(
                                                                                                            "## **THE RESULTS:**")
                                                                                                        # Identify the high consumption appliance
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.markdown(
                                                                                                            "**HIGHEST ENERGY CONSUMPTION**")
                                                                                                        apps = [Y1, Y2, Y3, Y4, Y5,
                                                                                                                Y6, Y7, Y8, Y9, Y10, Y11]
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
                                                                                                                "Energy consumption :", Y2, "kWh", "kWh")
                                                                                                        if max_app == Y3:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A3N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A3con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y3, "kWh")
                                                                                                        if max_app == Y4:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A4N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A4con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y4, "kWh")
                                                                                                        if max_app == Y5:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A5N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A5con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y5, "kWh")
                                                                                                        if max_app == Y6:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A6N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A6con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y6, "kWh")
                                                                                                        if max_app == Y7:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A7N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A7con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y7, "kWh")
                                                                                                        if max_app == Y8:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A8N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A8con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y8, "kWh")
                                                                                                        if max_app == Y9:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A9N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A9con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y9, "kWh")
                                                                                                        if max_app == Y10:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A10N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A10con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y10, "kWh")
                                                                                                        if max_app == Y11:
                                                                                                            st.write(
                                                                                                                "************************************************************************************************************************************************************************")
                                                                                                            st.write(
                                                                                                                "Name of appliance  :", A11N)
                                                                                                            st.write(
                                                                                                                "Electricity bill   : PHP", A11con)
                                                                                                            st.write(
                                                                                                                "Energy consumption :", Y11, "kWh")
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
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.markdown(
                                                                                                            "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                                        st.write(
                                                                                                            "Electricity bill: PHP", total11)
                                                                                                        st.write(
                                                                                                            "Energy consumption:", Kh11, "kWh")
                                                            # compute app1 to 10 (10th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                if ask25 == 2:
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

                                                                                                    # TOTAL: watt/hour kada araw.
                                                                                                    wh10 = (A1 + A2 + A3 + A4 +
                                                                                                            A5 + A6 + A7 + A8 + A9 + A10)

                                                                                                    # TOTAL: Kilo-watt/hour kada month.
                                                                                                    Kh10 = (
                                                                                                        (wh10 * 30) / 1000)

                                                                                                    # TOTAL: para ma compute ang (cost) kada month.
                                                                                                    total10 = cost * Kh10

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

                                                                                                    # INDIVIDUAL: Kilo-watt/hour
                                                                                                    Y1 = (
                                                                                                        A1*30)/1000
                                                                                                    Y2 = (
                                                                                                        A2*30)/1000
                                                                                                    Y3 = (
                                                                                                        A3*30)/1000
                                                                                                    Y4 = (
                                                                                                        A4*30)/1000
                                                                                                    Y5 = (
                                                                                                        A5*30)/1000
                                                                                                    Y6 = (
                                                                                                        A6*30)/1000
                                                                                                    Y7 = (
                                                                                                        A7*30)/1000
                                                                                                    Y8 = (
                                                                                                        A8*30)/1000
                                                                                                    Y9 = (
                                                                                                        A8*30)/1000
                                                                                                    Y10 = (
                                                                                                        A10*30)/1000

                                                                                                    # OUTPUT1
                                                                                                    st.markdown(
                                                                                                        "## **THE RESULTS:**")
                                                                                                    # Identify the high consumption appliance
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.markdown(
                                                                                                        "**HIGHEST ENERGY CONSUMPTION**")
                                                                                                    apps = [Y1, Y2, Y3, Y4, Y5,
                                                                                                            Y6, Y7, Y8, Y9, Y10]
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
                                                                                                            "Energy consumption :", Y1, "kWh")
                                                                                                    if max_app == Y2:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A2N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A2con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y2, "kWh")
                                                                                                    if max_app == Y3:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A3N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A3con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y3, "kWh")
                                                                                                    if max_app == Y4:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A4N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A4con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y4, "kWh")
                                                                                                    if max_app == Y5:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A5N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A5con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y5, "kWh")
                                                                                                    if max_app == Y6:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A6N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A6con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y6, "kWh")
                                                                                                    if max_app == Y7:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A7N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A7con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y7, "kWh")
                                                                                                    if max_app == Y8:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A8N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A8con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y8, "kWh")
                                                                                                    if max_app == Y9:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A9N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A9con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y9, "kWh")
                                                                                                    if max_app == Y10:
                                                                                                        st.write(
                                                                                                            "************************************************************************************************************************************************************************")
                                                                                                        st.write(
                                                                                                            "Name of appliance  :", A10N)
                                                                                                        st.write(
                                                                                                            "Electricity bill   : PHP", A10con)
                                                                                                        st.write(
                                                                                                            "Energy consumption :", Y10, "kWh")
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
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.markdown(
                                                                                                        "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                                    st.write(
                                                                                                        "Electricity bill: PHP", total10)
                                                                                                    st.write(
                                                                                                        "Energy consumption:", Kh10, "kWh")

                                                            # compute app1 to 9 (9th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                            if ask24 == 2:
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

                                                                                                # TOTAL: watt/hour kada araw.
                                                                                                wh9 = (A1 + A2 + A3 + A4 +
                                                                                                       A5 + A6 + A7 + A8 + A9)

                                                                                                # TOTAL: Kilo-watt/hour kada month.
                                                                                                Kh9 = (
                                                                                                    (wh9 * 30) / 1000)

                                                                                                # TOTAL: para ma compute ang (cost) kada month.
                                                                                                total9 = cost * Kh9

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

                                                                                                # INDIVIDUAL: Kilo-watt/hour
                                                                                                Y1 = (
                                                                                                    A1*30)/1000
                                                                                                Y2 = (
                                                                                                    A2*30)/1000
                                                                                                Y3 = (
                                                                                                    A3*30)/1000
                                                                                                Y4 = (
                                                                                                    A4*30)/1000
                                                                                                Y5 = (
                                                                                                    A5*30)/1000
                                                                                                Y6 = (
                                                                                                    A6*30)/1000
                                                                                                Y7 = (
                                                                                                    A7*30)/1000
                                                                                                Y8 = (
                                                                                                    A8*30)/1000
                                                                                                Y9 = (
                                                                                                    A8*30)/1000

                                                                                                # OUTPUT1
                                                                                                st.markdown(
                                                                                                    "## **THE RESULTS:**")
                                                                                                # Identify the high consumption appliance
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.markdown(
                                                                                                    "**HIGHEST ENERGY CONSUMPTION**")
                                                                                                apps = [
                                                                                                    Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9]
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
                                                                                                        "Energy consumption :", Y1, "kWh")
                                                                                                if max_app == Y2:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A2N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A2con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y2, "kWh")
                                                                                                if max_app == Y3:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A3N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A3con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y3, "kWh")
                                                                                                if max_app == Y4:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A4N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A4con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y4, "kWh")
                                                                                                if max_app == Y5:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A5N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A5con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y5, "kWh")
                                                                                                if max_app == Y6:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A6N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A6con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y6, "kWh")
                                                                                                if max_app == Y7:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A7N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A7con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y7, "kWh")
                                                                                                if max_app == Y8:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A8N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A8con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y8, "kWh")
                                                                                                if max_app == Y9:
                                                                                                    st.write(
                                                                                                        "************************************************************************************************************************************************************************")
                                                                                                    st.write(
                                                                                                        "Name of appliance  :", A9N)
                                                                                                    st.write(
                                                                                                        "Electricity bill   : PHP", A9con)
                                                                                                    st.write(
                                                                                                        "Energy consumption :", Y9, "kWh")
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
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.markdown(
                                                                                                    "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                                st.write(
                                                                                                    "Electricity bill: PHP", total9)
                                                                                                st.write(
                                                                                                    "Energy consumption:", Kh9, "kWh")

                                                            # compute app1,2,3,4,5,6,7 and 8 (8th line)# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                        if ask23 == 2:
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

                                                                                            # TOTAL: watt/hour kada araw.
                                                                                            wh8 = (
                                                                                                A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8)

                                                                                            # TOTAL: Kilo-watt/hour kada month.
                                                                                            Kh8 = (
                                                                                                (wh8 * 30) / 1000)

                                                                                            # TOTAL: para ma compute ang (cost) kada month.
                                                                                            total8 = cost * Kh8

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

                                                                                            # INDIVIDUAL: Kilo-watt/hour
                                                                                            Y1 = (
                                                                                                A1*30)/1000
                                                                                            Y2 = (
                                                                                                A2*30)/1000
                                                                                            Y3 = (
                                                                                                A3*30)/1000
                                                                                            Y4 = (
                                                                                                A4*30)/1000
                                                                                            Y5 = (
                                                                                                A5*30)/1000
                                                                                            Y6 = (
                                                                                                A6*30)/1000
                                                                                            Y7 = (
                                                                                                A7*30)/1000
                                                                                            Y8 = (
                                                                                                A8*30)/1000

                                                                                            # OUTPUT1
                                                                                            st.markdown(
                                                                                                "## **THE RESULTS:**")
                                                                                            # Identify the high consumption appliance
                                                                                            st.write(
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.markdown(
                                                                                                "**HIGHEST ENERGY CONSUMPTION**")
                                                                                            apps = [
                                                                                                Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8]
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
                                                                                                    "Energy consumption :", Y1, "kWh")
                                                                                            if max_app == Y2:
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.write(
                                                                                                    "Name of appliance  :", A2N)
                                                                                                st.write(
                                                                                                    "Electricity bill   : PHP", A2con)
                                                                                                st.write(
                                                                                                    "Energy consumption :", Y2, "kWh")
                                                                                            if max_app == Y3:
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.write(
                                                                                                    "Name of appliance  :", A3N)
                                                                                                st.write(
                                                                                                    "Electricity bill   : PHP", A3con)
                                                                                                st.write(
                                                                                                    "Energy consumption :", Y3, "kWh")
                                                                                            if max_app == Y4:
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.write(
                                                                                                    "Name of appliance  :", A4N)
                                                                                                st.write(
                                                                                                    "Electricity bill   : PHP", A4con)
                                                                                                st.write(
                                                                                                    "Energy consumption :", Y4, "kWh")
                                                                                            if max_app == Y5:
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.write(
                                                                                                    "Name of appliance  :", A5N)
                                                                                                st.write(
                                                                                                    "Electricity bill   : PHP", A5con)
                                                                                                st.write(
                                                                                                    "Energy consumption :", Y5, "kWh")
                                                                                            if max_app == Y6:
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.write(
                                                                                                    "Name of appliance  :", A6N)
                                                                                                st.write(
                                                                                                    "Electricity bill   : PHP", A6con)
                                                                                                st.write(
                                                                                                    "Energy consumption :", Y6, "kWh")
                                                                                            if max_app == Y7:
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.write(
                                                                                                    "Name of appliance  :", A7N)
                                                                                                st.write(
                                                                                                    "Electricity bill   : PHP", A7con)
                                                                                                st.write(
                                                                                                    "Energy consumption :", Y7, "kWh")
                                                                                            if max_app == Y8:
                                                                                                st.write(
                                                                                                    "************************************************************************************************************************************************************************")
                                                                                                st.write(
                                                                                                    "Name of appliance  :", A8N)
                                                                                                st.write(
                                                                                                    "Electricity bill   : PHP", A8con)
                                                                                                st.write(
                                                                                                    "Energy consumption :", Y8, "kWh")
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
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.markdown(
                                                                                                "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                            st.write(
                                                                                                "Electricity bill: PHP", total8)
                                                                                            st.write(
                                                                                                "Energy consumption:", Kh8, "kWh")

                                                            # compute app1,2,3,4,5,6 and 7 (7th line) # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                    if ask22 == 2:
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

                                                                                        # TOTAL: watt/hour kada araw.
                                                                                        wh7 = (
                                                                                            A1 + A2 + A3 + A4 + A5 + A6 + A7)

                                                                                        # TOTAL: Kilo-watt/hour kada month.
                                                                                        Kh7 = (
                                                                                            (wh7 * 30) / 1000)

                                                                                        # TOTAL: para ma compute ang (cost) kada month.
                                                                                        total7 = cost * Kh7

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
                                                                                        # INDIVIDUAL: Kilo-watt/hour
                                                                                        Y1 = (
                                                                                            A1*30)/1000
                                                                                        Y2 = (
                                                                                            A2*30)/1000
                                                                                        Y3 = (
                                                                                            A3*30)/1000
                                                                                        Y4 = (
                                                                                            A4*30)/1000
                                                                                        Y5 = (
                                                                                            A5*30)/1000
                                                                                        Y6 = (
                                                                                            A6*30)/1000
                                                                                        Y7 = (
                                                                                            A7*30)/1000

                                                                                        # OUTPUT1
                                                                                        st.markdown(
                                                                                            "## **THE RESULTS:**")
                                                                                        # Identify the high consumption appliance
                                                                                        st.write(
                                                                                            "************************************************************************************************************************************************************************")
                                                                                        st.markdown(
                                                                                            "**HIGHEST ENERGY CONSUMPTION**")
                                                                                        apps = [
                                                                                            Y1, Y2, Y3, Y4, Y5, Y6, Y7]
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
                                                                                                "Energy consumption :", Y1, "kWh")
                                                                                        if max_app == Y2:
                                                                                            st.write(
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.write(
                                                                                                "Name of appliance  :", A2N)
                                                                                            st.write(
                                                                                                "Electricity bill   : PHP", A2con)
                                                                                            st.write(
                                                                                                "Energy consumption :", Y2, "kWh")
                                                                                        if max_app == Y3:
                                                                                            st.write(
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.write(
                                                                                                "Name of appliance  :", A3N)
                                                                                            st.write(
                                                                                                "Electricity bill   : PHP", A3con)
                                                                                            st.write(
                                                                                                "Energy consumption :", Y3, "kWh")
                                                                                        if max_app == Y4:
                                                                                            st.write(
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.write(
                                                                                                "Name of appliance  :", A4N)
                                                                                            st.write(
                                                                                                "Electricity bill   : PHP", A4con)
                                                                                            st.write(
                                                                                                "Energy consumption :", Y4, "kWh")
                                                                                        if max_app == Y5:
                                                                                            st.write(
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.write(
                                                                                                "Name of appliance  :", A5N)
                                                                                            st.write(
                                                                                                "Electricity bill   : PHP", A5con)
                                                                                            st.write(
                                                                                                "Energy consumption :", Y5, "kWh")
                                                                                        if max_app == Y6:
                                                                                            st.write(
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.write(
                                                                                                "Name of appliance  :", A6N)
                                                                                            st.write(
                                                                                                "Electricity bill   : PHP", A6con)
                                                                                            st.write(
                                                                                                "Energy consumption :", Y6, "kWh")
                                                                                        if max_app == Y7:
                                                                                            st.write(
                                                                                                "************************************************************************************************************************************************************************")
                                                                                            st.write(
                                                                                                "Name of appliance  :", A7N)
                                                                                            st.write(
                                                                                                "Electricity bill   : PHP", A7con)
                                                                                            st.write(
                                                                                                "Energy consumption :", Y7, "kWh")
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
                                                                                            "************************************************************************************************************************************************************************")
                                                                                        st.markdown(
                                                                                            "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                        st.write(
                                                                                            "Electricity bill: PHP", total7)
                                                                                        st.write(
                                                                                            "Energy consumption:", Kh7, "kWh")

                                                            # compute app1,2,3,4,5 and 6 (6th line) ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                if ask21 == 2:
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

                                                                                    # TOTAL: watt/hour kada araw.
                                                                                    wh6 = (
                                                                                        A1 + A2 + A3 + A4 + A5 + A6)

                                                                                    # TOTAL: Kilo-watt/hour kada month.
                                                                                    Kh6 = (
                                                                                        (wh6 * 30) / 1000)

                                                                                    # TOTAL: para ma compute ang (cost) kada month.
                                                                                    total6 = cost * Kh6

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

                                                                                    # INDIVIDUAL: Kilo-watt/hour
                                                                                    Y1 = (
                                                                                        A1*30)/1000
                                                                                    Y2 = (
                                                                                        A2*30)/1000
                                                                                    Y3 = (
                                                                                        A3*30)/1000
                                                                                    Y4 = (
                                                                                        A4*30)/1000
                                                                                    Y5 = (
                                                                                        A5*30)/1000
                                                                                    Y6 = (
                                                                                        A6*30)/1000

                                                                                    # OUTPUT1
                                                                                    st.markdown(
                                                                                        "## **THE RESULTS:**")
                                                                                    # Identify the high consumption appliance
                                                                                    st.write(
                                                                                        "************************************************************************************************************************************************************************")
                                                                                    st.markdown(
                                                                                        "**HIGHEST ENERGY CONSUMPTION**")
                                                                                    apps = [
                                                                                        Y1, Y2, Y3, Y4, Y5, Y6]
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
                                                                                            "Energy consumption :", Y1, "kWh")
                                                                                    if max_app == Y2:
                                                                                        st.write(
                                                                                            "************************************************************************************************************************************************************************")
                                                                                        st.write(
                                                                                            "Name of appliance  :", A2N)
                                                                                        st.write(
                                                                                            "Electricity bill   : PHP", A2con)
                                                                                        st.write(
                                                                                            "Energy consumption :", Y2, "kWh")
                                                                                    if max_app == Y3:
                                                                                        st.write(
                                                                                            "************************************************************************************************************************************************************************")
                                                                                        st.write(
                                                                                            "Name of appliance  :", A3N)
                                                                                        st.write(
                                                                                            "Electricity bill   : PHP", A3con)
                                                                                        st.write(
                                                                                            "Energy consumption :", Y3, "kWh")
                                                                                    if max_app == Y4:
                                                                                        st.write(
                                                                                            "************************************************************************************************************************************************************************")
                                                                                        st.write(
                                                                                            "Name of appliance  :", A4N)
                                                                                        st.write(
                                                                                            "Electricity bill   : PHP", A4con)
                                                                                        st.write(
                                                                                            "Energy consumption :", Y4, "kWh")
                                                                                    if max_app == Y5:
                                                                                        st.write(
                                                                                            "************************************************************************************************************************************************************************")
                                                                                        st.write(
                                                                                            "Name of appliance  :", A5N)
                                                                                        st.write(
                                                                                            "Electricity bill   : PHP", A5con)
                                                                                        st.write(
                                                                                            "Energy consumption :", Y5, "kWh")
                                                                                    if max_app == Y6:
                                                                                        st.write(
                                                                                            "************************************************************************************************************************************************************************")
                                                                                        st.write(
                                                                                            "Name of appliance  :", A6N)
                                                                                        st.write(
                                                                                            "Electricity bill   : PHP", A6con)
                                                                                        st.write(
                                                                                            "Energy consumption :", Y6, "kWh")
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
                                                                                        "************************************************************************************************************************************************************************")
                                                                                    st.markdown(
                                                                                        "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                    st.write(
                                                                                        "Electricity bill: PHP", total6)
                                                                                    st.write(
                                                                                        "Energy consumption:", Kh6, "kWh")

                                                            # compute app1,2,3,4 and 5 (5th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                            if ask20 == 2:
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

                                                                                # TOTAL: watt/hour kada araw.
                                                                                wh5 = (
                                                                                    A1 + A2 + A3 + A4 + A5)

                                                                                # TOTAL: Kilo-watt/hour kada month.
                                                                                Kh5 = (
                                                                                    (wh5 * 30) / 1000)

                                                                                # TOTAL: para ma compute ang (cost) kada month.
                                                                                total5 = cost * Kh5

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

                                                                                # INDIVIDUAL: Kilo-watt/hour
                                                                                Y1 = (
                                                                                    A1*30)/1000
                                                                                Y2 = (
                                                                                    A2*30)/1000
                                                                                Y3 = (
                                                                                    A3*30)/1000
                                                                                Y4 = (
                                                                                    A4*30)/1000
                                                                                Y5 = (
                                                                                    A5*30)/1000

                                                                                # OUTPUT1
                                                                                st.markdown(
                                                                                    "## **THE RESULTS:**")
                                                                                # Identify the high consumption appliance
                                                                                st.write(
                                                                                    "************************************************************************************************************************************************************************")
                                                                                st.markdown(
                                                                                    "**HIGHEST ENERGY CONSUMPTION**")
                                                                                apps = [
                                                                                    Y1, Y2, Y3, Y4, Y5]
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
                                                                                        "Energy consumption :", Y1, "kWh")
                                                                                if max_app == Y2:
                                                                                    st.write(
                                                                                        "************************************************************************************************************************************************************************")
                                                                                    st.write(
                                                                                        "Name of appliance  :", A2N)
                                                                                    st.write(
                                                                                        "Electricity bill   : PHP", A2con)
                                                                                    st.write(
                                                                                        "Energy consumption :", Y2, "kWh")
                                                                                if max_app == Y3:
                                                                                    st.write(
                                                                                        "************************************************************************************************************************************************************************")
                                                                                    st.write(
                                                                                        "Name of appliance  :", A3N)
                                                                                    st.write(
                                                                                        "Electricity bill   : PHP", A3con)
                                                                                    st.write(
                                                                                        "Energy consumption :", Y3, "kWh")
                                                                                if max_app == Y4:
                                                                                    st.write(
                                                                                        "************************************************************************************************************************************************************************")
                                                                                    st.write(
                                                                                        "Name of appliance  :", A4N)
                                                                                    st.write(
                                                                                        "Electricity bill   : PHP", A4con)
                                                                                    st.write(
                                                                                        "Energy consumption :", Y4, "kWh")
                                                                                if max_app == Y5:
                                                                                    st.write(
                                                                                        "************************************************************************************************************************************************************************")
                                                                                    st.write(
                                                                                        "Name of appliance  :", A5N)
                                                                                    st.write(
                                                                                        "Electricity bill   : PHP", A5con)
                                                                                    st.write(
                                                                                        "Energy consumption :", Y5, "kWh")
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
                                                                                    "************************************************************************************************************************************************************************")
                                                                                st.markdown(
                                                                                    "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                                st.write(
                                                                                    "Electricity bill: PHP", total5)
                                                                                st.write(
                                                                                    "Energy consumption:", Kh5, "kWh")

                                                            # compute app1,2,3 and 4 (4th line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                        if ask19 == 2:
                                                                            # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                                                                            A1F = (
                                                                                A1B / 30) * A1D
                                                                            A2F = (
                                                                                A2B / 30) * A2D
                                                                            A3F = (
                                                                                A3B / 30) * A3D
                                                                            A4F = (
                                                                                A4B / 30) * A4D

                                                                            # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                                            A1 = (
                                                                                A1F * (A1W * A1M))
                                                                            A2 = (
                                                                                A2F * (A2W * A2M))
                                                                            A3 = (
                                                                                A3F * (A3W * A3M))
                                                                            A4 = (
                                                                                A4F * (A4W * A4M))

                                                                            # TOTAL: watt/hour kada araw.
                                                                            wh4 = (
                                                                                A1 + A2 + A3 + A4)

                                                                            # TOTAL: Kilo-watt/hour kada month.
                                                                            Kh4 = (
                                                                                (wh4 * 30) / 1000)

                                                                            # TOTAL: para ma compute ang (cost) kada month.
                                                                            total4 = cost * Kh4

                                                                            # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                                            A1con = (
                                                                                (A1 * 30) / 1000) * cost
                                                                            A2con = (
                                                                                (A2 * 30) / 1000) * cost
                                                                            A3con = (
                                                                                (A3 * 30) / 1000) * cost
                                                                            A4con = (
                                                                                (A4 * 30) / 1000) * cost
                                                                            # INDIVIDUAL: Kilo-watt/hour
                                                                            Y1 = (
                                                                                A1*30)/1000
                                                                            Y2 = (
                                                                                A2*30)/1000
                                                                            Y3 = (
                                                                                A3*30)/1000
                                                                            Y4 = (
                                                                                A4*30)/1000

                                                                            # OUTPUT1
                                                                            st.markdown(
                                                                                "## **THE RESULTS:**")
                                                                            # Identify the high consumption appliance
                                                                            st.write(
                                                                                "************************************************************************************************************************************************************************")
                                                                            st.markdown(
                                                                                "**HIGHEST ENERGY CONSUMPTION**")
                                                                            apps = [
                                                                                Y1, Y2, Y3, Y4]
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
                                                                                    "Energy consumption :", Y1, "kWh")
                                                                            if max_app == Y2:
                                                                                st.write(
                                                                                    "************************************************************************************************************************************************************************")
                                                                                st.write(
                                                                                    "Name of appliance  :", A2N)
                                                                                st.write(
                                                                                    "Electricity bill   : PHP", A2con)
                                                                                st.write(
                                                                                    "Energy consumption :", Y2, "kWh")
                                                                            if max_app == Y3:
                                                                                st.write(
                                                                                    "************************************************************************************************************************************************************************")
                                                                                st.write(
                                                                                    "Name of appliance  :", A3N)
                                                                                st.write(
                                                                                    "Electricity bill   : PHP", A3con)
                                                                                st.write(
                                                                                    "Energy consumption :", Y3, "kWh")
                                                                            if max_app == Y4:
                                                                                st.write(
                                                                                    "************************************************************************************************************************************************************************")
                                                                                st.write(
                                                                                    "Name of appliance  :", A4N)
                                                                                st.write(
                                                                                    "Electricity bill   : PHP", A4con)
                                                                                st.write(
                                                                                    "Energy consumption :", Y4, "kWh")
                                                                            # OUTPUT2
                                                                            st.write(
                                                                                "************************************************************************************************************************************************************************")
                                                                            st.markdown(
                                                                                "**INDIVIDUAL ELECTRICITY BILL**")
                                                                            st.write(
                                                                                A1N, ": PHP", A1con,)
                                                                            st.write(
                                                                                A2N, ": PHP", A2con,)
                                                                            st.write(
                                                                                A3N, ": PHP", A3con,)
                                                                            st.write(
                                                                                A4N, ": PHP", A4con,)
                                                                            st.write(
                                                                                "************************************************************************************************************************************************************************")
                                                                            st.markdown(
                                                                                "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                            st.write(
                                                                                "Electricity bill: PHP", total4)
                                                                            st.write(
                                                                                "Energy consumption:", Kh4, "kWh")

                                                            # compute app1,2 and 3 (3rd line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                    if ask18 == 2:
                                                                        # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                                                                        A1F = (
                                                                            A1B / 30) * A1D
                                                                        A2F = (
                                                                            A2B / 30) * A2D
                                                                        A3F = (
                                                                            A3B / 30) * A3D

                                                                        # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                                        A1 = (
                                                                            A1F * (A1W * A1M))
                                                                        A2 = (
                                                                            A2F * (A2W * A2M))
                                                                        A3 = (
                                                                            A3F * (A3W * A3M))

                                                                        # TOTAL: watt/hour kada araw.
                                                                        wh3 = (
                                                                            A1 + A2 + A3)

                                                                        # TOTAL: Kilo-watt/hour kada month.
                                                                        Kh3 = (
                                                                            (wh3 * 30)/1000)

                                                                        # TOTAL: para ma compute ang (cost) kada month.
                                                                        total3 = cost * Kh3

                                                                        # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                                        A1con = (
                                                                            (A1 * 30) / 1000) * cost
                                                                        A2con = (
                                                                            (A2 * 30) / 1000) * cost
                                                                        A3con = (
                                                                            (A3 * 30) / 1000) * cost

                                                                        # INDIVIDUAL: Kilo-watt/hour
                                                                        Y1 = (
                                                                            A1*30)/1000
                                                                        Y2 = (
                                                                            A2*30)/1000
                                                                        Y3 = (
                                                                            A3*30)/1000

                                                                        # OUTPUT1
                                                                        st.markdown(
                                                                            "## **THE RESULTS:**")
                                                                        # Identify the high consumption appliance
                                                                        st.write(
                                                                            "************************************************************************************************************************************************************************")
                                                                        st.markdown(
                                                                            "**HIGHEST ENERGY CONSUMPTION**")
                                                                        apps = [
                                                                            Y1, Y2, Y3]
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
                                                                                "Energy consumption :", Y1, "kWh")
                                                                        if max_app == Y2:
                                                                            st.write(
                                                                                "************************************************************************************************************************************************************************")
                                                                            st.write(
                                                                                "Name of appliance  :", A2N)
                                                                            st.write(
                                                                                "Electricity bill   : PHP", A2con)
                                                                            st.write(
                                                                                "Energy consumption :", Y2, "kWh")
                                                                        if max_app == Y3:
                                                                            st.write(
                                                                                "************************************************************************************************************************************************************************")
                                                                            st.write(
                                                                                "Name of appliance  :", A3N)
                                                                            st.write(
                                                                                "Electricity bill   : PHP", A3con)
                                                                            st.write(
                                                                                "Energy consumption :", Y3, "kWh")
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
                                                                            "************************************************************************************************************************************************************************")
                                                                        st.markdown(
                                                                            "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                        st.write(
                                                                            "Electricity bill: PHP", total3)
                                                                        st.write(
                                                                            "Energy consumption:", Kh3, "kWh")

                                                            # compute app1 and 2 (2nd line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                if ask17 == 2:
                                                                    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                                                                    A1F = (
                                                                        A1B / 30) * A1D
                                                                    A2F = (
                                                                        A2B / 30) * A2D

                                                                    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                                    A1 = (
                                                                        A1F * (A1W * A1M))
                                                                    A2 = (
                                                                        A2F * (A2W * A2M))

                                                                    # TOTAL: watt/hour kada araw.
                                                                    wh2 = (
                                                                        A1 + A2)

                                                                    # TOTAL: Kilo-watt/hour kada month.
                                                                    Kh2 = (
                                                                        wh2*30) / 1000

                                                                    # TOTAL: para ma compute ang (cost) kada month.
                                                                    total2 = cost * Kh2

                                                                    # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                                    A1con = (
                                                                        (A1 * 30) / 1000) * cost
                                                                    A2con = (
                                                                        (A2 * 30) / 1000) * cost

                                                                    # INDIVIDUAL: Kilo-watt/hour
                                                                    Y1 = (
                                                                        A1*30)/1000
                                                                    Y2 = (
                                                                        A2*30)/1000

                                                                    # OUTPUT1
                                                                    st.markdown(
                                                                        "## **THE RESULTS:**")
                                                                    # Identify the high consumption appliance
                                                                    st.write(
                                                                        "************************************************************************************************************************************************************************")
                                                                    st.markdown(
                                                                        "**HIGHEST ENERGY CONSUMPTION**")
                                                                    apps = [
                                                                        Y1, Y2]
                                                                    max_app = apps[0]
                                                                    for app in apps:
                                                                        if app > max_app:
                                                                            max_app = app
                                                                    if max_app == Y2:
                                                                        st.write(
                                                                            "************************************************************************************************************************************************************************")
                                                                        st.write(
                                                                            "Name of appliance  :", A1N)
                                                                        st.write(
                                                                            "Electricity bill   : PHP", A1con)
                                                                        st.write(
                                                                            "Energy consumption :", Y1, "kWh")
                                                                    if max_app == Y2:
                                                                        st.write(
                                                                            "************************************************************************************************************************************************************************")
                                                                        st.write(
                                                                            "Name of appliance  :", A2N)
                                                                        st.write(
                                                                            "Electricity bill   : PHP", A2con)
                                                                        st.write(
                                                                            "Energy consumption :", Y2, "kWh")
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
                                                                        "************************************************************************************************************************************************************************")
                                                                    st.markdown(
                                                                        "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                    st.write(
                                                                        "Electricity bill: PHP", total2)
                                                                    st.write(
                                                                        "Energy consumption:", Kh2, "kWh")

                                                            # compute app1 (1st line)//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                            if ask16 == 2:
                                                                # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
                                                                A1F = (
                                                                    A1B/30) * A1D

                                                                # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
                                                                A1 = (
                                                                    A1F * (A1W * A1M))

                                                                # TOTAL: watt/hour kada araw.
                                                                wh1 = A1

                                                                # TOTAL: Kilo-watt/hour kada month.
                                                                Kh1 = (
                                                                    wh1*30) / 1000

                                                                # TOTAL: para ma compute ang (cost) kada month.
                                                                total1 = cost * Kh1

                                                                # INDIVIDUALLY: para ma compute ang (cost) kada month.
                                                                A1con = (
                                                                    (A1*30)/1000)*cost

                                                                # INDIVIDUAL: Kilo-watt/hour
                                                                Y1 = (
                                                                    A1*30)/1000

                                                                # OUTPUT1
                                                                st.markdown(
                                                                    "## **THE RESULTS:**")
                                                                # Identify the high consumption appliance
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.markdown(
                                                                    "**HIGHEST ENERGY CONSUMPTION**")
                                                                apps = [Y1]
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
                                                                        "Energy consumption :", Y1, "kWh")
                                                                # OUTPUT2
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.markdown(
                                                                    "**INDIVIDUAL ELECTRICITY BILL**")
                                                                st.write(
                                                                    A1N, ": PHP", A1con,)
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.markdown(
                                                                    "**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
                                                                st.write(
                                                                    "Electricity bill: PHP", total1)
                                                                st.write(
                                                                    "Energy consumption:", Kh1, "kWh")


# compute app1 to 15 (15th line) # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                            # //
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
                                                            apps = [
                                                                Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15]
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
                                                                    "Energy consumption :", Y1, "kWh")
                                                            if max_app == Y2:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A2N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A2con)
                                                                st.write(
                                                                    "Energy consumption :", Y2, "kWh")
                                                            if max_app == Y3:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A3N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A3con)
                                                                st.write(
                                                                    "Energy consumption :", Y3, "kWh")
                                                            if max_app == Y4:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A4N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A4con)
                                                                st.write(
                                                                    "Energy consumption :", Y4, "kWh")
                                                            if max_app == Y5:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A5N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A5con)
                                                                st.write(
                                                                    "Energy consumption :", Y5, "kWh")
                                                            if max_app == Y6:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A6N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A6con)
                                                                st.write(
                                                                    "Energy consumption :", Y6, "kWh")
                                                            if max_app == Y7:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A7N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A7con)
                                                                st.write(
                                                                    "Energy consumption :", Y7, "kWh")
                                                            if max_app == Y8:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A8N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A8con)
                                                                st.write(
                                                                    "Energy consumption :", Y8, "kWh")
                                                            if max_app == Y9:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A9N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A9con)
                                                                st.write(
                                                                    "Energy consumption :", Y9, "kWh")
                                                            if max_app == Y10:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A10N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A10con)
                                                                st.write(
                                                                    "Energy consumption :", Y10, "kWh")
                                                            if max_app == Y11:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A11N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A11con)
                                                                st.write(
                                                                    "Energy consumption :", Y11, "kWh")
                                                            if max_app == Y12:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A12N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A12con)
                                                                st.write(
                                                                    "Energy consumption :", Y12, "kWh")
                                                            if max_app == Y13:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A13N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A13con)
                                                                st.write(
                                                                    "Energy consumption :", Y13, "kWh")
                                                            if max_app == Y14:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A14N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A14con)
                                                                st.write(
                                                                    "Energy consumption :", Y14, "kWh")
                                                            if max_app == Y15:
                                                                st.write(
                                                                    "************************************************************************************************************************************************************************")
                                                                st.write(
                                                                    "Name of appliance  :", A15N)
                                                                st.write(
                                                                    "Electricity bill   : PHP", A15con)
                                                                st.write(
                                                                    "Energy consumption :", Y15, "kWh")
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
                                                        apps = [
                                                            Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14]
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
                                                                "Energy consumption :", Y1, "kWh")
                                                        if max_app == Y2:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A2N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A2con)
                                                            st.write(
                                                                "Energy consumption :", Y2, "kWh")
                                                        if max_app == Y3:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A3N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A3con)
                                                            st.write(
                                                                "Energy consumption :", Y3, "kWh")
                                                        if max_app == Y4:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A4N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A4con)
                                                            st.write(
                                                                "Energy consumption :", Y4, "kWh")
                                                        if max_app == Y5:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A5N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A5con)
                                                            st.write(
                                                                "Energy consumption :", Y5, "kWh")
                                                        if max_app == Y6:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A6N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A6con)
                                                            st.write(
                                                                "Energy consumption :", Y6, "kWh")
                                                        if max_app == Y7:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A7N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A7con)
                                                            st.write(
                                                                "Energy consumption :", Y7, "kWh")
                                                        if max_app == Y8:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A8N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A8con)
                                                            st.write(
                                                                "Energy consumption :", Y8, "kWh")
                                                        if max_app == Y9:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A9N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A9con)
                                                            st.write(
                                                                "Energy consumption :", Y9, "kWh")
                                                        if max_app == Y10:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A10N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A10con)
                                                            st.write(
                                                                "Energy consumption :", Y10, "kWh")
                                                        if max_app == Y11:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A11N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A11con)
                                                            st.write(
                                                                "Energy consumption :", Y11, "kWh")
                                                        if max_app == Y12:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A12N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A12con)
                                                            st.write(
                                                                "Energy consumption :", Y12, "kWh")
                                                        if max_app == Y13:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A13N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A13con)
                                                            st.write(
                                                                "Energy consumption :", Y13, "kWh")
                                                        if max_app == Y14:
                                                            st.write(
                                                                "************************************************************************************************************************************************************************")
                                                            st.write(
                                                                "Name of appliance  :", A14N)
                                                            st.write(
                                                                "Electricity bill   : PHP", A14con)
                                                            st.write(
                                                                "Energy consumption :", Y14, "kWh")
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
                                                    apps = [
                                                        Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13]
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
                                                            "Energy consumption :", Y1, "kWh")
                                                    if max_app == Y2:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A2N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A2con)
                                                        st.write(
                                                            "Energy consumption :", Y2, "kWh")
                                                    if max_app == Y3:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A3N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A3con)
                                                        st.write(
                                                            "Energy consumption :", Y3, "kWh")
                                                    if max_app == Y4:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A4N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A4con)
                                                        st.write(
                                                            "Energy consumption :", Y4, "kWh")
                                                    if max_app == Y5:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A5N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A5con)
                                                        st.write(
                                                            "Energy consumption :", Y5, "kWh")
                                                    if max_app == Y6:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A6N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A6con)
                                                        st.write(
                                                            "Energy consumption :", Y6, "kWh")
                                                    if max_app == A7con:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A7N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A7con)
                                                        st.write(
                                                            "Energy consumption :", Y7, "kWh")
                                                    if max_app == Y8:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A8N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A8con)
                                                        st.write(
                                                            "Energy consumption :", Y8, "kWh")
                                                    if max_app == Y9:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A9N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A9con)
                                                        st.write(
                                                            "Energy consumption :", Y9, "kWh")
                                                    if max_app == Y10:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A10N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A10con)
                                                        st.write(
                                                            "Energy consumption :", Y10, "kWh")
                                                    if max_app == Y11:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A11N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A11con)
                                                        st.write(
                                                            "Energy consumption :", Y11, "kWh")
                                                    if max_app == Y12:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A12N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A12con)
                                                        st.write(
                                                            "Energy consumption :", Y12, "kWh")
                                                    if max_app == Y13:
                                                        st.write(
                                                            "************************************************************************************************************************************************************************")
                                                        st.write(
                                                            "Name of appliance  :", A13N)
                                                        st.write(
                                                            "Electricity bill   : PHP", A13con)
                                                        st.write(
                                                            "Energy consumption :", Y13, "kWh")
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
                                                apps = [
                                                    Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12]
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
                                                        "Energy consumption :", Y1, "kWh")
                                                if max_app == Y2:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A2N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A2con)
                                                    st.write(
                                                        "Energy consumption :", Y2, "kWh")
                                                if max_app == Y3:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A3N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A3con)
                                                    st.write(
                                                        "Energy consumption :", Y3, "kWh")
                                                if max_app == Y4:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A4N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A4con)
                                                    st.write(
                                                        "Energy consumption :", Y4, "kWh")
                                                if max_app == Y5:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A5N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A5con)
                                                    st.write(
                                                        "Energy consumption :", Y5, "kWh")
                                                if max_app == Y6:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A6N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A6con)
                                                    st.write(
                                                        "Energy consumption :", Y6, "kWh")
                                                if max_app == A7con:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A7N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A7con)
                                                    st.write(
                                                        "Energy consumption :", Y7, "kWh")
                                                if max_app == Y8:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A8N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A8con)
                                                    st.write(
                                                        "Energy consumption :", Y8, "kWh")
                                                if max_app == Y9:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A9N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A9con)
                                                    st.write(
                                                        "Energy consumption :", Y9, "kWh")
                                                if max_app == Y10:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A10N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A10con)
                                                    st.write(
                                                        "Energy consumption :", Y10, "kWh")
                                                if max_app == Y11:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A11N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A11con)
                                                    st.write(
                                                        "Energy consumption :", Y11, "kWh")
                                                if max_app == Y12:
                                                    st.write(
                                                        "************************************************************************************************************************************************************************")
                                                    st.write(
                                                        "Name of appliance  :", A12N)
                                                    st.write(
                                                        "Electricity bill   : PHP", A12con)
                                                    st.write(
                                                        "Energy consumption :", Y12, "kWh")
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
                                            apps = [Y1, Y2, Y3, Y4, Y5,
                                                    Y6, Y7, Y8, Y9, Y10, Y11]
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
                                                    "Energy consumption :", Y2, "kWh", "kWh")
                                            if max_app == Y3:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A3N)
                                                st.write(
                                                    "Electricity bill   : PHP", A3con)
                                                st.write(
                                                    "Energy consumption :", Y3, "kWh")
                                            if max_app == Y4:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A4N)
                                                st.write(
                                                    "Electricity bill   : PHP", A4con)
                                                st.write(
                                                    "Energy consumption :", Y4, "kWh")
                                            if max_app == Y5:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A5N)
                                                st.write(
                                                    "Electricity bill   : PHP", A5con)
                                                st.write(
                                                    "Energy consumption :", Y5, "kWh")
                                            if max_app == Y6:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A6N)
                                                st.write(
                                                    "Electricity bill   : PHP", A6con)
                                                st.write(
                                                    "Energy consumption :", Y6, "kWh")
                                            if max_app == Y7:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A7N)
                                                st.write(
                                                    "Electricity bill   : PHP", A7con)
                                                st.write(
                                                    "Energy consumption :", Y7, "kWh")
                                            if max_app == Y8:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A8N)
                                                st.write(
                                                    "Electricity bill   : PHP", A8con)
                                                st.write(
                                                    "Energy consumption :", Y8, "kWh")
                                            if max_app == Y9:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A9N)
                                                st.write(
                                                    "Electricity bill   : PHP", A9con)
                                                st.write(
                                                    "Energy consumption :", Y9, "kWh")
                                            if max_app == Y10:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A10N)
                                                st.write(
                                                    "Electricity bill   : PHP", A10con)
                                                st.write(
                                                    "Energy consumption :", Y10, "kWh")
                                            if max_app == Y11:
                                                st.write(
                                                    "************************************************************************************************************************************************************************")
                                                st.write(
                                                    "Name of appliance  :", A11N)
                                                st.write(
                                                    "Electricity bill   : PHP", A11con)
                                                st.write(
                                                    "Energy consumption :", Y11, "kWh")
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
                                        apps = [Y1, Y2, Y3, Y4, Y5,
                                                Y6, Y7, Y8, Y9, Y10]
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
                                                "Energy consumption :", Y1, "kWh")
                                        if max_app == Y2:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A2N)
                                            st.write(
                                                "Electricity bill   : PHP", A2con)
                                            st.write(
                                                "Energy consumption :", Y2, "kWh")
                                        if max_app == Y3:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A3N)
                                            st.write(
                                                "Electricity bill   : PHP", A3con)
                                            st.write(
                                                "Energy consumption :", Y3, "kWh")
                                        if max_app == Y4:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A4N)
                                            st.write(
                                                "Electricity bill   : PHP", A4con)
                                            st.write(
                                                "Energy consumption :", Y4, "kWh")
                                        if max_app == Y5:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A5N)
                                            st.write(
                                                "Electricity bill   : PHP", A5con)
                                            st.write(
                                                "Energy consumption :", Y5, "kWh")
                                        if max_app == Y6:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A6N)
                                            st.write(
                                                "Electricity bill   : PHP", A6con)
                                            st.write(
                                                "Energy consumption :", Y6, "kWh")
                                        if max_app == Y7:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A7N)
                                            st.write(
                                                "Electricity bill   : PHP", A7con)
                                            st.write(
                                                "Energy consumption :", Y7, "kWh")
                                        if max_app == Y8:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A8N)
                                            st.write(
                                                "Electricity bill   : PHP", A8con)
                                            st.write(
                                                "Energy consumption :", Y8, "kWh")
                                        if max_app == Y9:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A9N)
                                            st.write(
                                                "Electricity bill   : PHP", A9con)
                                            st.write(
                                                "Energy consumption :", Y9, "kWh")
                                        if max_app == Y10:
                                            st.write(
                                                "************************************************************************************************************************************************************************")
                                            st.write(
                                                "Name of appliance  :", A10N)
                                            st.write(
                                                "Electricity bill   : PHP", A10con)
                                            st.write(
                                                "Energy consumption :", Y10, "kWh")
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
                                    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9]
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
                                        st.write(
                                            "Energy consumption :", Y1, "kWh")
                                    if max_app == Y2:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A2N)
                                        st.write(
                                            "Electricity bill   : PHP", A2con)
                                        st.write(
                                            "Energy consumption :", Y2, "kWh")
                                    if max_app == Y3:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A3N)
                                        st.write(
                                            "Electricity bill   : PHP", A3con)
                                        st.write(
                                            "Energy consumption :", Y3, "kWh")
                                    if max_app == Y4:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A4N)
                                        st.write(
                                            "Electricity bill   : PHP", A4con)
                                        st.write(
                                            "Energy consumption :", Y4, "kWh")
                                    if max_app == Y5:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A5N)
                                        st.write(
                                            "Electricity bill   : PHP", A5con)
                                        st.write(
                                            "Energy consumption :", Y5, "kWh")
                                    if max_app == Y6:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A6N)
                                        st.write(
                                            "Electricity bill   : PHP", A6con)
                                        st.write(
                                            "Energy consumption :", Y6, "kWh")
                                    if max_app == Y7:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A7N)
                                        st.write(
                                            "Electricity bill   : PHP", A7con)
                                        st.write(
                                            "Energy consumption :", Y7, "kWh")
                                    if max_app == Y8:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A8N)
                                        st.write(
                                            "Electricity bill   : PHP", A8con)
                                        st.write(
                                            "Energy consumption :", Y8, "kWh")
                                    if max_app == Y9:
                                        st.write(
                                            "************************************************************************************************************************************************************************")
                                        st.write("Name of appliance  :", A9N)
                                        st.write(
                                            "Electricity bill   : PHP", A9con)
                                        st.write(
                                            "Energy consumption :", Y9, "kWh")
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
                                apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8]
                                max_app = apps[0]
                                for app in apps:
                                    if app > max_app:
                                        max_app = app
                                if max_app == Y1:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A1N)
                                    st.write("Electricity bill   : PHP", A1con)
                                    st.write("Energy consumption :", Y1, "kWh")
                                if max_app == Y2:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A2N)
                                    st.write("Electricity bill   : PHP", A2con)
                                    st.write("Energy consumption :", Y2, "kWh")
                                if max_app == Y3:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A3N)
                                    st.write("Electricity bill   : PHP", A3con)
                                    st.write("Energy consumption :", Y3, "kWh")
                                if max_app == Y4:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A4N)
                                    st.write("Electricity bill   : PHP", A4con)
                                    st.write("Energy consumption :", Y4, "kWh")
                                if max_app == Y5:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A5N)
                                    st.write("Electricity bill   : PHP", A5con)
                                    st.write("Energy consumption :", Y5, "kWh")
                                if max_app == Y6:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A6N)
                                    st.write("Electricity bill   : PHP", A6con)
                                    st.write("Energy consumption :", Y6, "kWh")
                                if max_app == Y7:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A7N)
                                    st.write("Electricity bill   : PHP", A7con)
                                    st.write("Energy consumption :", Y7, "kWh")
                                if max_app == Y8:
                                    st.write(
                                        "************************************************************************************************************************************************************************")
                                    st.write("Name of appliance  :", A8N)
                                    st.write("Electricity bill   : PHP", A8con)
                                    st.write("Energy consumption :", Y8, "kWh")
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
                            apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7]
                            max_app = apps[0]
                            for app in apps:
                                if app > max_app:
                                    max_app = app
                            if max_app == Y1:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A1N)
                                st.write("Electricity bill   : PHP", A1con)
                                st.write("Energy consumption :", Y1, "kWh")
                            if max_app == Y2:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A2N)
                                st.write("Electricity bill   : PHP", A2con)
                                st.write("Energy consumption :", Y2, "kWh")
                            if max_app == Y3:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A3N)
                                st.write("Electricity bill   : PHP", A3con)
                                st.write("Energy consumption :", Y3, "kWh")
                            if max_app == Y4:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A4N)
                                st.write("Electricity bill   : PHP", A4con)
                                st.write("Energy consumption :", Y4, "kWh")
                            if max_app == Y5:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A5N)
                                st.write("Electricity bill   : PHP", A5con)
                                st.write("Energy consumption :", Y5, "kWh")
                            if max_app == Y6:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A6N)
                                st.write("Electricity bill   : PHP", A6con)
                                st.write("Energy consumption :", Y6, "kWh")
                            if max_app == Y7:
                                st.write(
                                    "************************************************************************************************************************************************************************")
                                st.write("Name of appliance  :", A7N)
                                st.write("Electricity bill   : PHP", A7con)
                                st.write("Energy consumption :", Y7, "kWh")
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
                            st.write("Energy consumption :", Y1, "kWh")
                        if max_app == Y2:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A2N)
                            st.write("Electricity bill   : PHP", A2con)
                            st.write("Energy consumption :", Y2, "kWh")
                        if max_app == Y3:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A3N)
                            st.write("Electricity bill   : PHP", A3con)
                            st.write("Energy consumption :", Y3, "kWh")
                        if max_app == Y4:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A4N)
                            st.write("Electricity bill   : PHP", A4con)
                            st.write("Energy consumption :", Y4, "kWh")
                        if max_app == Y5:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A5N)
                            st.write("Electricity bill   : PHP", A5con)
                            st.write("Energy consumption :", Y5, "kWh")
                        if max_app == Y6:
                            st.write(
                                "************************************************************************************************************************************************************************")
                            st.write("Name of appliance  :", A6N)
                            st.write("Electricity bill   : PHP", A6con)
                            st.write("Energy consumption :", Y6, "kWh")
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
                        st.write("Energy consumption :", Y1, "kWh")
                    if max_app == Y2:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A2N)
                        st.write("Electricity bill   : PHP", A2con)
                        st.write("Energy consumption :", Y2, "kWh")
                    if max_app == Y3:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A3N)
                        st.write("Electricity bill   : PHP", A3con)
                        st.write("Energy consumption :", Y3, "kWh")
                    if max_app == Y4:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A4N)
                        st.write("Electricity bill   : PHP", A4con)
                        st.write("Energy consumption :", Y4, "kWh")
                    if max_app == Y5:
                        st.write(
                            "************************************************************************************************************************************************************************")
                        st.write("Name of appliance  :", A5N)
                        st.write("Electricity bill   : PHP", A5con)
                        st.write("Energy consumption :", Y5, "kWh")
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
                    st.write("Energy consumption :", Y1, "kWh")
                if max_app == Y2:
                    st.write("************************************************************************************************************************************************************************")
                    st.write("Name of appliance  :", A2N)
                    st.write("Electricity bill   : PHP", A2con)
                    st.write("Energy consumption :", Y2, "kWh")
                if max_app == Y3:
                    st.write("************************************************************************************************************************************************************************")
                    st.write("Name of appliance  :", A3N)
                    st.write("Electricity bill   : PHP", A3con)
                    st.write("Energy consumption :", Y3, "kWh")
                if max_app == Y4:
                    st.write("************************************************************************************************************************************************************************")
                    st.write("Name of appliance  :", A4N)
                    st.write("Electricity bill   : PHP", A4con)
                    st.write("Energy consumption :", Y4, "kWh")
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
                st.write("Energy consumption :", Y1, "kWh")
            if max_app == Y2:
                st.write("************************************************************************************************************************************************************************")
                st.write("Name of appliance  :", A2N)
                st.write("Electricity bill   : PHP", A2con)
                st.write("Energy consumption :", Y2, "kWh")
            if max_app == Y3:
                st.write("************************************************************************************************************************************************************************")
                st.write("Name of appliance  :", A3N)
                st.write("Electricity bill   : PHP", A3con)
                st.write("Energy consumption :", Y3, "kWh")
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
        st.write("Energy consumption :", Y1, "kWh")
    if max_app == Y2:
        st.write("************************************************************************************************************************************************************************")
        st.write("Name of appliance  :", A2N)
        st.write("Electricity bill   : PHP", A2con)
        st.write("Energy consumption :", Y2, "kWh")
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
        st.write("Energy consumption :", Y1, "kWh")
    # OUTPUT2
    st.write("************************************************************************************************************************************************************************")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con,)
    st.write("************************************************************************************************************************************************************************")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total1)
    st.write("Energy consumption:", Kh1, "kWh")
