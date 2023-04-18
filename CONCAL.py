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
cost=0
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
ask31 = 0
ask32 = 0
ask33 = 0
ask34 = 0
ask35 = 0
ask36 = 0
ask37 = 0
ask38 = 0
ask39 = 0
ask40 = 0
Appliances = []
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 1st app
if cost>0:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 1st appliance.</span>", unsafe_allow_html=True)
    A1N = st.text_input("Name of 1st appliance:")
    if A1N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                A1N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A1N)
        if A1N:
            A1M = st.number_input(
                f"How many {A1N} are you using?", value=0, step=1)
            if A1M== 0:
                 st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Before you proceed to the next step, please type the quantity value. Thank you.</span>", unsafe_allow_html=True)
            if A1M<0:
                st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>To proceed, please enter a non-negative value for quantity. Thank you.</span>", unsafe_allow_html=True)
            if A1M>=0:
                A1W = st.number_input(f"What is the wattage of {A1N}?(watt)")
                A1B = st.number_input(
                    f"How many days in a month do you use {A1N}?(1-31)", value=0, step=1)
                if 31 >= A1B >= 1:
                    st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A1N + ".</span>", unsafe_allow_html=True)
                    col1, col2 = st.beta_columns(2)
                    A1D = col1.number_input(f"Hours: (0-24)", value=0, step=1,key="A1D")
                    A1E = col2.number_input(f"Minutes: (0-59)", value=0, step=1,key="A1E")
                    if (((24 == A1D) and (A1E==0))and((A1D>0.1)or(A1E>0.1))) or (((24>A1D>=0)and(59>=A1E>=0))and((A1D>0.1)or(A1E>0.1))):
                        ask1 = st.number_input(
                            "Add 2nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
if cost<=0:
    st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>To proceed to the next step, please type the cost value. Thank you.</span>", unsafe_allow_html=True)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 2nd app
if ask1 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 2nd appliance.</span>", unsafe_allow_html=True)
    A2N = st.text_input("Name of 2nd appliance: ")
    if A2N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A2N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A2N)
        if A2N:
            A2M = st.number_input(
                f"How many {A2N} are you using?", value=0, step=1)
            A2W = st.number_input(f"What is the wattage of {A2N}?(watt)")
            A2B = st.number_input(
                f"How many days in a month do you use {A2N}?(1-31)", value=0, step=1)
            if 31 >= A2B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A2N + ".</span>", unsafe_allow_html=True)
                col3, col4 = st.beta_columns(2)
                A2D = col3.number_input(f"Hours: (0-24)", value=0, step=1,key="A2D")
                A2E = col4.number_input(f"Minutes: (0-59)", value=0, step=1,key="A2E")
                if (((24 == A2D) and (A2E==0))and((A2D>0.1)or(A2E>0.1))) or (((24>A2D>=0)and(59>=A2E>=0))and((A2D>0.1)or(A2E>0.1))):
                    ask2 = st.number_input(
                        "Add 3rd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 3rd app
if ask2 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 3rd appliance.</span>", unsafe_allow_html=True)
    A3N = st.text_input("Name of 3rd appliance:")
    if A3N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A3N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A3N)
        if A3N:
            A3M = st.number_input(
                f"How many {A3N} are you using?", value=0, step=1)
            A3W = st.number_input(f"What is the wattage of {A3N}?(watt)")
            A3B = st.number_input(
                f"How many days in a month do you use {A3N}?(1-31)", value=0, step=1)
            if 31 >= A3B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A3N + ".</span>", unsafe_allow_html=True)
                col5, col6 = st.beta_columns(2)
                A3D = col5.number_input(f"Hours: (0-24)", value=0, step=1,key="A3D")
                A3E = col6.number_input(f"Minutes: (0-59)", value=0, step=1,key="A3E")
                if (((24 == A3D) and (A3E==0))and((A3D>0.1)or(A3E>0.1))) or (((24>A3D>=0)and(59>=A3E>=0))and((A3D>0.1)or(A3E>0.1))):
                    ask3 = st.number_input(
                        "Add 4th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 4th app
if ask3 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 4th appliance.</span>", unsafe_allow_html=True)
    A4N = st.text_input("Name of 4th appliance: ")
    if A4N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A4N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A4N)
        if A4N:
            A4M = st.number_input(
                f"How many {A4N} are you using?", value=0, step=1)
            A4W = st.number_input(f"What is the wattage of {A4N}?(watt)")
            A4B = st.number_input(
                f"How many days in a month do you use {A4N}?(1-31)", value=0, step=1)
            if 31 >= A4B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A4N + ".</span>", unsafe_allow_html=True)
                col7, col8 = st.beta_columns(2)
                A4D = col7.number_input(f"Hours: (0-24)", value=0, step=1,key="A4D")
                A4E = col8.number_input(f"Minutes: (0-59)", value=0, step=1,key="A4E")
                if (((24 == A4D) and (A4E==0))and((A4D>0.1)or(A4E>0.1))) or (((24>A4D>=0)and(59>=A4E>=0))and((A4D>0.1)or(A4E>0.1))):
                    ask4 = st.number_input(
                        "Add 5th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 5th app
if ask4 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 5th appliance.</span>", unsafe_allow_html=True)
    A5N = st.text_input("Name of 5th appliance: ")
    if A5N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A5N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A5N)
        if A5N:
            A5M = st.number_input(
                f"How many {A5N} are you using?", value=0, step=1)
            A5W = st.number_input(
                f"What is the wattage of {A5N}?(watt)")
            A5B = st.number_input(
                f"How many days in a month do you use {A5N}?(1-31)", value=0, step=1)
            if 31 >= A5B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A5N + ".</span>", unsafe_allow_html=True)
                col9, col10 = st.beta_columns(2)
                A5D = col9.number_input(f"Hours: (0-24)", value=0, step=1,key="A5D")
                A5E = col10.number_input(f"Minutes: (0-59)", value=0, step=1,key="A5E")
                if (((24 == A5D) and (A5E==0))and((A5D>0.1)or(A5E>0.1))) or (((24>A5D>=0)and(59>=A5E>=0))and((A5D>0.1)or(A5E>0.1))):
                    ask5 = st.number_input(
                        "Add 6th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 6th app
if ask5 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 6th appliance.</span>", unsafe_allow_html=True)
    A6N = st.text_input("Name of 6th appliance: ")
    if A6N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A6N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A6N)
        if A6N:
            A6M = st.number_input(
                f"How many {A6N} are you using?", value=0, step=1)
            A6W = st.number_input(
                f"What is the wattage of {A6N}?(watt)")
            A6B = st.number_input(
                f"How many days in a month do you use {A6N}?(1-31)", value=0, step=1)
            if 31 >= A6B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A6N + ".</span>", unsafe_allow_html=True)
                col11, col12 = st.beta_columns(2)
                A6D = col11.number_input(f"Hours: (0-24)", value=0, step=1,key="A6D")
                A6E = col12.number_input(f"Minutes: (0-59)", value=0, step=1,key="A6E")
                if (((24 == A6D) and (A6E==0))and((A6D>0.1)or(A1E>0.1))) or (((24>A6D>=0)and(59>=A6E>=0))and((A6D>0.1)or(A6E>0.1))):
                    ask6 = st.number_input(
                        "Add 7th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 7th app
if ask6 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 7th appliance.</span>", unsafe_allow_html=True)
    A7N = st.text_input("Name of 7th appliance: ")
    if A7N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A7N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A7N)
        if A7N:
            A7M = st.number_input(
                f"How many {A7N} are you using?", value=0, step=1)
            A7W = st.number_input(
                f"What is the wattage of {A7N}?(watt)")
            A7B = st.number_input(
                f"How many days in a month do you use {A7N}?(1-31)", value=0, step=1)
            if 31 >= A7B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A7N + ".</span>", unsafe_allow_html=True)
                col13, col14 = st.beta_columns(2)
                A7D = col13.number_input(f"Hours: (0-24)", value=0, step=1,key="A7D")
                A7E = col14.number_input(f"Minutes: (0-59)", value=0, step=1,key="A7E")
                if (((24 == A7D) and (A7E==0))and((A7D>0.1)or(A7E>0.1))) or (((24>A7D>=0)and(59>=A7E>=0))and((A7D>0.1)or(A7E>0.1))):
                    ask7 = st.number_input(
                        "Add 8th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 8th app
if ask7 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 8th appliance.</span>", unsafe_allow_html=True)
    A8N = st.text_input("Name of 8th appliance: ")
    if A8N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A8N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A8N)
        if A8N:
            A8M = st.number_input(
                f"How many {A8N} are you using?", value=0, step=1)
            A8W = st.number_input(
                f"What is the wattage of {A8N}?(watt)")
            A8B = st.number_input(
                f"How many days in a month do you use {A8N}?(1-31)", value=0, step=1)
            if 31 >= A8B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A8N + ".</span>", unsafe_allow_html=True)
                col15, col16 = st.beta_columns(2)
                A8D = col15.number_input(f"Hours: (0-24)", value=0, step=1,key="A8D")
                A8E = col16.number_input(f"Minutes: (0-59)", value=0, step=1,key="A8E")
                if (((24 == A8D) and (A8E==0))and((A8D>0.1)or(A8E>0.1))) or (((24>A8D>=0)and(59>=A8E>=0))and((A8D>0.1)or(A8E>0.1))):
                    ask8 = st.number_input(
                        "Add 9th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 9th app
if ask8 == 1:
    st.write("***")
    st.write(
        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 9th appliance.</span>", unsafe_allow_html=True)
    A9N = st.text_input("Name of 9th appliance: ")
    if A9N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A9N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A9N)
        if A9N:
            A9M = st.number_input(
                f"How many {A9N} are you using?", value=0, step=1)
            A9W = st.number_input(
                f"What is the wattage of {A9N}?(watt)")
            A9B = st.number_input(
                f"How many days in a month do you use {A9N}?(1-31)", value=0, step=1)
            if 31 >= A9B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A9N + ".</span>", unsafe_allow_html=True)
                col17, col18 = st.beta_columns(2)
                A9D = col17.number_input(f"Hours: (0-24)", value=0, step=1,key="A9D")
                A9E = col18.number_input(f"Minutes: (0-59)", value=0, step=1,key="A9E")
                if (((24 == A9D) and (A9E==0))and((A9D>0.1)or(A9E>0.1))) or (((24>A9D>=0)and(59>=A9E>=0))and((A9D>0.1)or(A9E>0.1))):
                    ask9 = st.number_input(
                        "Add 10th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 10th app
if ask9 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 10th appliance.</span>", unsafe_allow_html=True)
    A10N = st.text_input("Name of 10th appliance: ")
    if A10N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A10N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A10N)
        if A10N:
            A10M = st.number_input(
                f"How many {A10N} are you using?", value=0, step=1)
            A10W = st.number_input(
                f"What is the wattage of {A10N}?(watt)")
            A10B = st.number_input(
                f"How many days in a month do you use {A10N}?(1-31)", value=0, step=1)
            if 31 >= A10B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A10N + ".</span>", unsafe_allow_html=True)
                col19, col20 = st.beta_columns(2)
                A10D = col19.number_input(f"Hours: (0-24)", value=0, step=1,key="A10D")
                A10E = col20.number_input(f"Minutes: (0-59)", value=0, step=1,key="A10E")
                if (((24 == A10D) and (A10E==0))and((A10D>0.1)or(A10E>0.1))) or (((24>A10D>=0)and(59>=A10E>=0))and((A10D>0.1)or(A10E>0.1))):
                    ask10 = st.number_input(
                        "Add 11th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 11th app
if ask10 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 11th appliance.</span>", unsafe_allow_html=True)
    A11N = st.text_input("Name of 11th appliance:")
    if A11N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A11N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A11N)
        if A11N:
            A11M = st.number_input(
                f"How many {A11N} are you using?", value=0, step=1)
            A11W = st.number_input(
                f"What is the wattage of {A11N}?(watt)")
            A11B = st.number_input(
                f"How many days in a month do you use {A11N}?(1-31)", value=0, step=1)
            if 31 >= A11B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A11N + ".</span>", unsafe_allow_html=True)
                col21, col22 = st.beta_columns(2)
                A11D = col21.number_input(f"Hours: (0-24)", value=0, step=1,key="A11D")
                A11E = col22.number_input(f"Minutes: (0-59)", value=0, step=1,key="A11E")
                if (((24 == A11D) and (A11E==0))and((A11D>0.1)or(A11E>0.1))) or (((24>A11D>=0)and(59>=A11E>=0))and((A11D>0.1)or(A11E>0.1))):
                    ask11 = st.number_input(
                        "Add 12th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 12th app
if ask11 == 1:
    st.write("***")
    st.write(
        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 12th appliance.</span>", unsafe_allow_html=True)
    A12N = st.text_input(
        "Name of 12th appliance: ")
    if A12N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A12N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A12N)
        if A12N:
            A12M = st.number_input(
                f"How many {A12N} are you using?", value=0, step=1)
            A12W = st.number_input(
                f"What is the wattage of {A12N}?(watt)")
            A12B = st.number_input(
                f"How many days in a month do you use {A12N}?(1-31)", value=0, step=1)
            if 31 >= A12B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A12N + ".</span>", unsafe_allow_html=True)
                col23, col24 = st.beta_columns(2)
                A12D = col23.number_input(f"Hours: (0-24)", value=0, step=1,key="A12D")
                A12E = col24.number_input(f"Minutes: (0-59)", value=0, step=1,key="A12E")
                if (((24 == A12D) and (A12E==0))and((A12D>0.1)or(A12E>0.1))) or (((24>A12D>=0)and(59>=A12E>=0))and((A12D>0.1)or(A12E>0.1))):
                    ask12 = st.number_input(
                        "Add 13th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 13th app
if ask12 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 13th appliance.</span>", unsafe_allow_html=True)
    A13N = st.text_input("Name of 13th appliance: ")
    if A13N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A13N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A13N)
        if A13N:
            A13M = st.number_input(
                f"How many {A13N} are you using?", value=0, step=1)
            A13W = st.number_input(
                f"What is the wattage of {A13N}?(watt)")
            A13B = st.number_input(
                f"How many days in a month do you use {A13N}?(1-31)", value=0, step=1)
            if 31 >= A13B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A13N + ".</span>", unsafe_allow_html=True)
                col25, col26 = st.beta_columns(2)
                A13D = col25.number_input(f"Hours: (0-24)", value=0, step=1,key="A13D")
                A13E = col26.number_input(f"Minutes: (0-59)", value=0, step=1,key="A13E")
                if (((24 == A13D) and (A13E==0))and((A13D>0.1)or(A13E>0.1))) or (((24>A13D>=0)and(59>=A13E>=0))and((A13D>0.1)or(A13E>0.1))):
                    ask13 = st.number_input(
                        "Add 14th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 14th app
if ask13 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 14th appliance.</span>", unsafe_allow_html=True)
    A14N = st.text_input("Name of 14th appliance: ")
    if A14N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A14N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A14N)
        if A14N:
            A14M = st.number_input(
                f"How many {A14N} are you using?", value=0, step=1)
            A14W = st.number_input(
                f"What is the wattage of {A14N}?(watt)")
            A14B = st.number_input(
                f"How many days in a month do you use {A14N}?(1-31)", value=0, step=1)
            if 31 >= A14B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A14N + ".</span>", unsafe_allow_html=True)
                col27, col28 = st.beta_columns(2)
                A14D = col27.number_input(f"Hours: (0-24)", value=0, step=1,key="A14D")
                A14E = col28.number_input(f"Minutes: (0-59)", value=0, step=1,key="A14E")
                if (((24 == A14D) and (A14E==0))and((A14D>0.1)or(A14E>0.1))) or (((24>A14D>=0)and(59>=A14E>=0))and((A14D>0.1)or(A14E>0.1))):
                    ask14 = st.number_input(
                        "Add 15th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 15th app
if ask14 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 15th appliance.</span>", unsafe_allow_html=True)
    A15N = st.text_input("Name of 15th appliance: ")
    if A15N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A15N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A15N)
        if A15N:
            A15M = st.number_input(
                f"How many {A15N} are you using?", value=0, step=1)
            A15W = st.number_input(
                f"What is the wattage of {A15N}?(watt)")
            A15B = st.number_input(
                f"How many days in a month do you use {A15N}?(1-31)", value=0, step=1)
            if 31 >= A15B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A15N + ".</span>", unsafe_allow_html=True)
                col29, col30 = st.beta_columns(2)
                A15D = col29.number_input(f"Hours: (0-24)", value=0, step=1,key="A15D")
                A15E = col30.number_input(f"Minutes: (0-59)", value=0, step=1,key="A15E")
                if (((24 == A15D) and (A15E==0))and((A15D>0.1)or(A15E>0.1))) or (((24>A15D>=0)and(59>=A15E>=0))and((A15D>0.1)or(A15E>0.1))):
                    ask15 = st.number_input(
                        "Add 16th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 16th app
if ask15 == 1:
    st.write("***")
    st.write(
        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 16th appliance.</span>", unsafe_allow_html=True)
    A16N = st.text_input("Name of 16th appliance: ")
    if A16N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A16N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A16N)
        if A16N:
            A16M = st.number_input(
                f"How many {A16N} are you using?", value=0, step=1)
            A16W = st.number_input(
                f"What is the wattage of {A16N}?(watt)")
            A16B = st.number_input(
                f"How many days in a month do you use {A16N}?(1-31)", value=0, step=1)
            if 31 >= A16B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A16N + ".</span>", unsafe_allow_html=True)
                col31, col32 = st.beta_columns(2)
                A16D = col31.number_input(f"Hours: (0-24)", value=0, step=1,key="A16D")
                A16E = col32.number_input(f"Minutes: (0-59)", value=0, step=1,key="A16E")
                if (((24 == A16D) and (A16E==0))and((A16D>0.1)or(A16E>0.1))) or (((24>A16D>=0)and(59>=A16E>=0))and((A16D>0.1)or(A16E>0.1))):
                    ask16 = st.number_input(
                        "Add 17th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 17th app
if ask16 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 17th appliance.</span>", unsafe_allow_html=True)
    A17N = st.text_input("Name of 17th appliance: ")
    if A17N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A17N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A17N)
        if A17N:
            A17M = st.number_input(
                f"How many {A17N} are you using?", value=0, step=1)
            A17W = st.number_input(
                f"What is the wattage of {A17N}?(watt)")
            A17B = st.number_input(
                f"How many days in a month do you use {A17N}?(1-31)", value=0, step=1)
            if 31 >= A17B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A17N + ".</span>", unsafe_allow_html=True)
                col33, col34 = st.beta_columns(2)
                A17D = col33.number_input(f"Hours: (0-24)", value=0, step=1,key="A17D")
                A17E = col34.number_input(f"Minutes: (0-59)", value=0, step=1,key="A17E")
                if (((24 == A17D) and (A17E==0))and((A17D>0.1)or(A17E>0.1))) or (((24>A17D>=0)and(59>=A17E>=0))and((A17D>0.1)or(A17E>0.1))):
                    ask17 = st.number_input(
                        "Add 18th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 18th app
if ask17 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 18th appliance.</span>", unsafe_allow_html=True)
    A18N = st.text_input("Name of 18th appliance:")
    if A18N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A18N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A18N)
        if A18N:
            A18M = st.number_input(
                f"How many {A18N} are you using?", value=0, step=1)
            A18W = st.number_input(
                f"What is the wattage of {A18N}?(watt)")
            A18B = st.number_input(
                f"How many days in a month do you use {A18N}?(1-31)", value=0, step=1)
            if 31 >= A18B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A18N + ".</span>", unsafe_allow_html=True)
                col35, col36 = st.beta_columns(2)
                A18D = col35.number_input(f"Hours: (0-24)", value=0, step=1,key="A18D")
                A18E = col36.number_input(f"Minutes: (0-59)", value=0, step=1,key="A18E")
                if (((24 == A18D) and (A18E==0))and((A18D>0.1)or(A18E>0.1))) or (((24>A18D>=0)and(59>=A18E>=0))and((A18D>0.1)or(A18E>0.1))):
                    ask18 = st.number_input(
                        "Add 19th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 19th app
if ask18 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 19th appliance.</span>", unsafe_allow_html=True)
    A19N = st.text_input("Name of 19th appliance: ")
    if A19N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A19N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A19N)
        if A19N:
            A19M = st.number_input(
                f"How many {A19N} are you using?", value=0, step=1)
            A19W = st.number_input(
                f"What is the wattage of {A19N}?(watt)")
            A19B = st.number_input(
                f"How many days in a month do you use {A19N}?(1-31)", value=0, step=1)
            if 31 >= A19B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A19N + ".</span>", unsafe_allow_html=True)
                col37, col38 = st.beta_columns(2)
                A19D = col37.number_input(f"Hours: (0-24)", value=0, step=1,key="A19D")
                A19E = col38.number_input(f"Minutes: (0-59)", value=0, step=1,key="A19E")
                if (((24 == A19D) and (A19E==0))and((A19D>0.1)or(A19E>0.1))) or (((24>A19D>=0)and(59>=A19E>=0))and((A19D>0.1)or(A19E>0.1))):
                    ask19 = st.number_input(
                        "Add 20th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 20th app
if ask19 == 1:
    st.write(
        "***")
    st.write(
        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 20th appliance.</span>", unsafe_allow_html=True)
    A20N = st.text_input("Name of 20th appliance: ")
    if A20N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A20N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A20N)
        if A20N:
            A20M = st.number_input(
                f"How many {A20N} are you using?", value=0, step=1)
            A20W = st.number_input(
                f"What is the wattage of {A20N}?(watt)")
            A20B = st.number_input(
                f"How many days in a month do you use {A20N}?(1-31)", value=0, step=1)
            if 31 >= A20B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A20N + ".</span>", unsafe_allow_html=True)
                col39, col40 = st.beta_columns(2)
                A20D = col39.number_input(f"Hours: (0-24)", value=0, step=1,key="A20D")
                A20E = col40.number_input(f"Minutes: (0-59)", value=0, step=1,key="A20E")
                if (((24 == A20D) and (A20E==0))and((A20D>0.1)or(A20E>0.1))) or (((24>A20D>=0)and(59>=A20E>=0))and((A20D>0.1)or(A20E>0.1))):
                    ask20 = st.number_input(
                        "Add 21st appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 21st app
if ask20 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 21st appliance.</span>", unsafe_allow_html=True)
    A21N = st.text_input("Name of 21st appliance: ")
    if A21N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A21N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A21N)
        if A21N:
            A21M = st.number_input(
                f"How many {A21N} are you using?", value=0, step=1)
            A21W = st.number_input(
                f"What is the wattage of {A21N}?(watt)")
            A21B = st.number_input(
                f"How many days in a month do you use {A21N}?(1-31)", value=0, step=1)
            if 31 >= A21B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A21N + ".</span>", unsafe_allow_html=True)
                col41, col42 = st.beta_columns(2)
                A21D = col41.number_input(f"Hours: (0-24)", value=0, step=1,key="A21D")
                A21E = col42.number_input(f"Minutes: (0-59)", value=0, step=1,key="A21E")
                if (((24 == A21D) and (A21E==0))and((A21D>0.1)or(A21E>0.1))) or (((24>A21D>=0)and(59>=A21E>=0))and((A21D>0.1)or(A21E>0.1))):
                    ask21 = st.number_input(
                        "Add 22nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 22nd app
if ask21 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 22nd appliance.</span>", unsafe_allow_html=True)
    A22N = st.text_input("Name of 22nd appliance: ")
    if A22N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A22N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A22N)
        if A22N:
            A22M = st.number_input(
                f"How many {A22N} are you using?", value=0, step=1)
            A22W = st.number_input(
                f"What is the wattage of {A22N}?(watt)")
            A22B = st.number_input(
                f"How many days in a month do you use {A22N}?(1-31)", value=0, step=1)
            if 31 >= A22B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A22N + ".</span>", unsafe_allow_html=True)
                col43, col44 = st.beta_columns(2)
                A22D = col43.number_input(f"Hours: (0-24)", value=0, step=1,key="A22D")
                A22E = col44.number_input(f"Minutes: (0-59)", value=0, step=1,key="A22E")
                if (((24 == A22D) and (A22E==0))and((A22D>0.1)or(A22E>0.1))) or (((24>A22D>=0)and(59>=A22E>=0))and((A22D>0.1)or(A22E>0.1))):
                    ask22 = st.number_input(
                        "Add 23rd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 23rd app
if ask22 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 23rd appliance.</span>", unsafe_allow_html=True)
    A23N = st.text_input("Name of 23rd appliance: ")
    if A23N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A23N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A23N)
        if A23N:
            A23M = st.number_input(
                f"How many {A23N} are you using?", value=0, step=1)
            A23W = st.number_input(
                f"What is the wattage of {A23N}?(watt)")
            A23B = st.number_input(
                f"How many days in a month do you use {A23N}?(1-31)", value=0, step=1)
            if 31 >= A23B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A23N + ".</span>", unsafe_allow_html=True)
                col45, col46 = st.beta_columns(2)
                A23D = col45.number_input(f"Hours: (0-24)", value=0, step=1,key="A23D")
                A23E = col46.number_input(f"Minutes: (0-59)", value=0, step=1,key="A23E")
                if (((24 == A23D) and (A23E==0))and((A23D>0.1)or(A23E>0.1))) or (((24>A23D>=0)and(59>=A23E>=0))and((A23D>0.1)or(A23E>0.1))):
                    ask23 = st.number_input(
                        "Add 24th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 24th app
if ask23 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 24th appliance.</span>", unsafe_allow_html=True)
    A24N = st.text_input("Name of 24th appliance: ")
    if A24N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A24N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A24N)
        if A24N:
            A24M = st.number_input(
                f"How many {A24N} are you using?", value=0, step=1)
            A24W = st.number_input(
                f"What is the wattage of {A24N}?(watt)")
            A24B = st.number_input(
                f"How many days in a month do you use {A24N}?(1-31)", value=0, step=1)
            if 31 >= A24B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A24N + ".</span>", unsafe_allow_html=True)
                col47, col48 = st.beta_columns(2)
                A24D = col39.number_input(f"Hours: (0-24)", value=0, step=1,key="A24D")
                A24E = col40.number_input(f"Minutes: (0-59)", value=0, step=1,key="A24E")
                if (((24 == A24D) and (A24E==0))and((A24D>0.1)or(A24E>0.1))) or (((24>A24D>=0)and(59>=A24E>=0))and((A24D>0.1)or(A24E>0.1))):
                    ask24 = st.number_input(
                        "Add 25th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 25th app
if ask24 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 25th appliance.</span>", unsafe_allow_html=True)
    A25N = st.text_input("Name of 25th appliance: ")
    if A25N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A25N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A25N)
        if A25N:
            A25M = st.number_input(
                f"How many {A25N} are you using?", value=0, step=1)
            A25W = st.number_input(
                f"What is the wattage of {A25N}?(watt)")
            A25B = st.number_input(
                f"How many days in a month do you use {A25N}?(1-31)", value=0, step=1)
            if 31 >= A25B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A25N + ".</span>", unsafe_allow_html=True)
                col49, col50 = st.beta_columns(2)
                A25D = col49.number_input(f"Hours: (0-24)", value=0, step=1,key="A25D")
                A25E = col50.number_input(f"Minutes: (0-59)", value=0, step=1,key="A25E")
                if (((24 == A25D) and (A25E==0))and((A25D>0.1)or(A25E>0.1))) or (((24>A25D>=0)and(59>=A25E>=0))and((A25D>0.1)or(A25E>0.1))):
                    ask25 = st.number_input(
                        "Add 26th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 26th app
if ask25 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 26th appliance.</span>", unsafe_allow_html=True)
    A26N = st.text_input("Name of 26th appliance:")
    if A26N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A26N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A26N)
        if A26N:
            A26M = st.number_input(
                f"How many {A26N} are you using?", value=0, step=1)
            A26W = st.number_input(
                f"What is the wattage of {A26N}?(watt)")
            A26B = st.number_input(
                f"How many days in a month do you use {A26N}?(1-31)", value=0, step=1)
            if 31 >= A26B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A26N + ".</span>", unsafe_allow_html=True)
                col51, col52 = st.beta_columns(2)
                A26D = col51.number_input(f"Hours: (0-24)", value=0, step=1,key="A26D")
                A26E = col52.number_input(f"Minutes: (0-59)", value=0, step=1,key="A26E")
                if (((24 == A26D) and (A26E==0))and((A26D>0.1)or(A26E>0.1))) or (((24>A26D>=0)and(59>=A26E>=0))and((A26D>0.1)or(A26E>0.1))):
                    ask26 = st.number_input(
                        "Add 27th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 27th app
if ask26 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 27th appliance.</span>", unsafe_allow_html=True)
    A27N = st.text_input("Name of 27th appliance: ")
    if A27N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A27N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A27N)
        if A27N:
            A27M = st.number_input(
                f"How many {A27N} are you using?", value=0, step=1)
            A27W = st.number_input(f"What is the wattage of {A27N}?(watt)")
            A27B = st.number_input(
                f"How many days in a month do you use {A27N}?(1-31)", value=0, step=1)
            if 31 >= A27B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A27N + ".</span>", unsafe_allow_html=True)
                col53, col54 = st.beta_columns(2)
                A27D = col53.number_input(f"Hours: (0-24)", value=0, step=1,key="A27D")
                A27E = col54.number_input(f"Minutes: (0-59)", value=0, step=1,key="A27E")
                if (((24 == A27D) and (A27E==0))and((A27D>0.1)or(A27E>0.1))) or (((24>A27D>=0)and(59>=A27E>=0))and((A27D>0.1)or(A27E>0.1))):
                    ask27 = st.number_input(
                        "Add 28th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 28th app
if ask27 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 28th appliance.</span>", unsafe_allow_html=True)
    A28N = st.text_input("Name of 28th appliance: ")
    if A28N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A28N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A28N)
        if A28N:
            A28M = st.number_input(
                f"How many {A28N} are you using?", value=0, step=1)
            A28W = st.number_input(f"What is the wattage of {A28N}?(watt)")
            A28B = st.number_input(
                f"How many days in a month do you use {A28N}?(1-31)", value=0, step=1)
            if 31 >= A28B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A28N + ".</span>", unsafe_allow_html=True)
                col55, col56 = st.beta_columns(2)
                A28D = col55.number_input(f"Hours: (0-24)", value=0, step=1,key="A28D")
                A28E = col56.number_input(f"Minutes: (0-59)", value=0, step=1,key="A28E")
                if (((24 == A28D) and (A28E==0))and((A28D>0.1)or(A28E>0.1))) or (((24>A28D>=0)and(59>=A28E>=0))and((A28D>0.1)or(A28E>0.1))):
                    ask28 = st.number_input(
                        "Add 29th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 29th app
if ask28 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 29th appliance.</span>", unsafe_allow_html=True)
    A29N = st.text_input("Name of 29th appliance: ")
    if A29N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A29N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A29N)
        if A29N:
            A29M = st.number_input(
                f"How many {A29N} are you using?", value=0, step=1)
            A29W = st.number_input(f"What is the wattage of {A29N}?(watt)")
            A29B = st.number_input(
                f"How many days in a month do you use {A29N}?(1-31)", value=0, step=1)
            if 31 >= A29B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A29N + ".</span>", unsafe_allow_html=True)
                col57, col58 = st.beta_columns(2)
                A29D = col57.number_input(f"Hours: (0-24)", value=0, step=1,key="A29D")
                A29E = col58.number_input(f"Minutes: (0-59)", value=0, step=1,key="A29E")
                if (((24 == A29D) and (A29E==0))and((A29D>0.1)or(A29E>0.1))) or (((24>A29D>=0)and(59>=A29E>=0))and((A29D>0.1)or(A29E>0.1))):
                    ask29 = st.number_input(
                        "Add 30th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 30th app
if ask29 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 30th appliance.</span>", unsafe_allow_html=True)
    A30N = st.text_input("Name of 30th appliance: ")
    if A30N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A30N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A30N)
        if A30N:
            A30M = st.number_input(
                f"How many {A30N} are you using?", value=0, step=1)
            A30W = st.number_input(f"What is the wattage of {A30N}?(watt)")
            A30B = st.number_input(
                f"How many days in a month do you use {A30N}?(1-31)", value=0, step=1)
            if 31 >= A30B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A30N + ".</span>", unsafe_allow_html=True)
                col59, col60 = st.beta_columns(2)
                A30D = col59.number_input(f"Hours: (0-24)", value=0, step=1,key="A30D")
                A30E = col60.number_input(f"Minutes: (0-59)", value=0, step=1,key="A30E")
                if (((24 == A30D) and (A30E==0))and((A30D>0.1)or(A30E>0.1))) or (((24>A30D>=0)and(59>=A30E>=0))and((A30D>0.1)or(A30E>0.1))):
                    ask30 = st.number_input(
                        "Add 31st appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 31st app
if ask30 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 31st appliance.</span>", unsafe_allow_html=True)
    A31N = st.text_input("Name of 31st appliance: ")
    if A31N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A31N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A31N)
        if A31N:
            A31M = st.number_input(
                f"How many {A31N} are you using?", value=0, step=1)
            A31W = st.number_input(
                f"What is the wattage of {A31N}?(watt)")
            A31B = st.number_input(
                f"How many days in a month do you use {A31N}?(1-31)", value=0, step=1)
            if 31 >= A31B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A31N + ".</span>", unsafe_allow_html=True)
                col61, col62 = st.beta_columns(2)
                A31D = col61.number_input(f"Hours: (0-24)", value=0, step=1,key="A31D")
                A31E = col62.number_input(f"Minutes: (0-59)", value=0, step=1,key="A31E")
                if (((24 == A31D) and (A31E==0))and((A31D>0.1)or(A31E>0.1))) or (((24>A31D>=0)and(59>=A31E>=0))and((A31D>0.1)or(A31E>0.1))):
                    ask31 = st.number_input(
                        "Add 32nd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 32nd app
if ask31 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 32nd appliance.</span>", unsafe_allow_html=True)
    A32N = st.text_input("Name of 32nd appliance:")
    if A32N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A32N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A32N)
        if A32N:
            A32M = st.number_input(
                f"How many {A32N} are you using?", value=0, step=1)
            A32W = st.number_input(
                f"What is the wattage of {A32N}?(watt)")
            A32B = st.number_input(
                f"How many days in a month do you use {A32N}?(1-31)", value=0, step=1)
            if 31 >= A32B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A32N + ".</span>", unsafe_allow_html=True)
                col63, col64 = st.beta_columns(2)
                A32D = col63.number_input(f"Hours: (0-24)", value=0, step=1,key="A32D")
                A32E = col64.number_input(f"Minutes: (0-59)", value=0, step=1,key="A32E")
                if (((24 == A32D) and (A32E==0))and((A32D>0.1)or(A32E>0.1))) or (((24>A32D>=0)and(59>=A32E>=0))and((A32D>0.1)or(A32E>0.1))):
                    ask32 = st.number_input(
                        "Add 33rd appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 33rd app

if ask32 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 33rd appliance.</span>", unsafe_allow_html=True)
    A33N = st.text_input("Name of 33rd appliance: ")
    if A33N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A33N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A33N)
        if A33N:
            A33M = st.number_input(
                f"How many {A33N} are you using?", value=0, step=1)
            A33W = st.number_input(f"What is the wattage of {A33N}?(watt)")
            A33B = st.number_input(
                f"How many days in a month do you use {A33N}?(1-31)", value=0, step=1)
            if 31 >= A33B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A33N + ".</span>", unsafe_allow_html=True)
                col65, col66 = st.beta_columns(2)
                A33D = col65.number_input(f"Hours: (0-24)", value=0, step=1,key="A33D")
                A33E = col66.number_input(f"Minutes: (0-59)", value=0, step=1,key="A33E")
                if (((24 == A33D) and (A33E==0))and((A33D>0.1)or(A33E>0.1))) or (((24>A33D>=0)and(59>=A33E>=0))and((A33D>0.1)or(A33E>0.1))):
                    ask33 = st.number_input(
                        "Add 34th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 34th app
if ask33 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 34th appliance.</span>", unsafe_allow_html=True)
    A34N = st.text_input("Name of 34th appliance: ")
    if A34N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A34N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A34N)
        if A34N:
            A34M = st.number_input(
                f"How many {A34N} are you using?", value=0, step=1)
            A34W = st.number_input(f"What is the wattage of {A34N}?(watt)")
            A34B = st.number_input(
                f"How many days in a month do you use {A34N}?(1-31)", value=0, step=1)
            if 31 >= A34B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A34N + ".</span>", unsafe_allow_html=True)
                col67, col68 = st.beta_columns(2)
                A34D = col67.number_input(f"Hours: (0-24)", value=0, step=1,key="A34D")
                A34E = col68.number_input(f"Minutes: (0-59)", value=0, step=1,key="A34E")
                if (((24 == A34D) and (A34E==0))and((A34D>0.1)or(A34E>0.1))) or (((24>A34D>=0)and(59>=A34E>=0))and((A34D>0.1)or(A34E>0.1))):
                    ask34 = st.number_input(
                        "Add 35th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 35th app
if ask34 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 35th appliance.</span>", unsafe_allow_html=True)
    A35N = st.text_input("Name of 35th appliance: ")
    if A35N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A35N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A35N)
        if A35N:
            A35M = st.number_input(
                f"How many {A35N} are you using?", value=0, step=1)
            A35W = st.number_input(f"What is the wattage of {A35N}?(watt)")
            A35B = st.number_input(
                f"How many days in a month do you use {A35N}?(1-31)", value=0, step=1)
            if 31 >= A35B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A35N + ".</span>", unsafe_allow_html=True)
                col69, col70 = st.beta_columns(2)
                A35D = col69.number_input(f"Hours: (0-24)", value=0, step=1,key="A35D")
                A35E = col70.number_input(f"Minutes: (0-59)", value=0, step=1,key="A35E")
                if (((24 == A35D) and (A35E==0))and((A35D>0.1)or(A35E>0.1))) or (((24>A35D>=0)and(59>=A35E>=0))and((A35D>0.1)or(A35E>0.1))):
                    ask35 = st.number_input(
                        "Add 36th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 36th app
if ask35 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 36th appliance.</span>", unsafe_allow_html=True)
    A36N = st.text_input("Name of 36th appliance: ")
    if A36N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A36N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A36N)
        if A36N:
            A36M = st.number_input(
                f"How many {A36N} are you using?", value=0, step=1)
            A36W = st.number_input(f"What is the wattage of {A36N}?(watt)")
            A36B = st.number_input(
                f"How many days in a month do you use {A36N}?(1-31)", value=0, step=1)
            if 31 >= A36B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A36N + ".</span>", unsafe_allow_html=True)
                col71, col72 = st.beta_columns(2)
                A36D = col71.number_input(f"Hours: (0-24)", value=0, step=1,key="A36D")
                A36E = col72.number_input(f"Minutes: (0-59)", value=0, step=1,key="A36E")
                if (((24 == A36D) and (A36E==0))and((A36D>0.1)or(A36E>0.1))) or (((24>A36D>=0)and(59>=A36E>=0))and((A36D>0.1)or(A36E>0.1))):
                    ask36 = st.number_input(
                        "Add 37th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 37th app
if ask36 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 37th appliance.</span>", unsafe_allow_html=True)
    A37N = st.text_input("Name of 37th appliance: ")
    if A37N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A37N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A37N)
        if A37N:
            A37M = st.number_input(
                f"How many {A37N} are you using?", value=0, step=1)
            A37W = st.number_input(
                f"What is the wattage of {A37N}?(watt)")
            A37B = st.number_input(
                f"How many days in a month do you use {A37N}?(1-31)", value=0, step=1)
            if 31 >= A37B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A37N + ".</span>", unsafe_allow_html=True)
                col73, col74 = st.beta_columns(2)
                A37D = col73.number_input(f"Hours: (0-24)", value=0, step=1,key="A37D")
                A37E = col74.number_input(f"Minutes: (0-59)", value=0, step=1,key="A37E")
                if (((24 == A37D) and (A37E==0))and((A37D>0.1)or(A37E>0.1))) or (((24>A37D>=0)and(59>=A37E>=0))and((A37D>0.1)or(A37E>0.1))):
                    ask37 = st.number_input(
                        "Add 38th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 38th app
if ask37 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 38th appliance.</span>", unsafe_allow_html=True)
    A38N = st.text_input("Name of 38th appliance: ")
    if A38N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A38N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A38N)
        if A38N:
            A38M = st.number_input(
                f"How many {A38N} are you using?", value=0, step=1)
            A38W = st.number_input(
                f"What is the wattage of {A38N}?(watt)")
            A38B = st.number_input(
                f"How many days in a month do you use {A38N}?(1-31)", value=0, step=1)
            if 31 >= A38B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A38N + ".</span>", unsafe_allow_html=True)
                col75, col76 = st.beta_columns(2)
                A38D = col75.number_input(f"Hours: (0-24)", value=0, step=1,key="A38D")
                A38E = col76.number_input(f"Minutes: (0-59)", value=0, step=1,key="A38E")
                if (((24 == A38D) and (A38E==0))and((A38D>0.1)or(A38E>0.1))) or (((24>A38D>=0)and(59>=A38E>=0))and((A38D>0.1)or(A38E>0.1))):
                    ask38 = st.number_input(
                        "Add 39th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 39th app
if ask38 == 1:
    st.write("***")
    st.write(
        "<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 39th appliance.</span>", unsafe_allow_html=True)
    A39N = st.text_input("Name of 39th appliance: ")
    if A39N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A39N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A39N)
        if A39N:
            A39M = st.number_input(
                f"How many {A39N} are you using?", value=0, step=1)
            A39W = st.number_input(
                f"What is the wattage of {A39N}?(watt)")
            A39B = st.number_input(
                f"How many days in a month do you use {A39N}?(1-31)", value=0, step=1)
            if 31 >= A39B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A39N + ".</span>", unsafe_allow_html=True)
                col77, col78 = st.beta_columns(2)
                A39D = col77.number_input(f"Hours: (0-24)", value=0, step=1,key="A39D")
                A39E = col78.number_input(f"Minutes: (0-59)", value=0, step=1,key="A39E")
                if (((24 == A39D) and (A39E==0))and((A39D>0.1)or(A39E>0.1))) or (((24>A39D>=0)and(59>=A39E>=0))and((A39D>0.1)or(A39E>0.1))):
                    ask39 = st.number_input(
                        "Add 40th appliance (enter 1), No more appliances (enter 2): ", value=0, step=1)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# add 40th app
if ask39 == 1:
    st.write("***")
    st.write("<span style='font-family:Times New Roman; font-size:18px;font-weight:bold;'>Information about the 40th appliance.</span>", unsafe_allow_html=True)
    A40N = st.text_input("Name of 40th appliance: ")
    if A40N in Appliances:
        st.write("<span style='font-family:Times New Roman; font-size:14px;font-style:italic;font-weight:bold;'>Please kindly use an alternative name for the appliance, other than " +
                 A40N + ".</span>", unsafe_allow_html=True)
    else:
        Appliances.append(A40N)
        if A40N:
            A40M = st.number_input(
                f"How many {A40N} are you using?", value=0, step=1)
            A40W = st.number_input(
                f"What is the wattage of {A40N}?(watt)")
            A40B = st.number_input(
                f"How many days in a month do you use {A40N}?(1-31)", value=0, step=1)
            if 31 >= A40B >= 1:
                st.write("<span style='font-family:Source Sans Pro; font-size:14px;'>Set the amount of time that you use the " + A40N + ".</span>", unsafe_allow_html=True)
                col79, col80 = st.beta_columns(2)
                A40D = col79.number_input(f"Hours: (0-24)", value=0, step=1,key="A40D")
                A40E = col80.number_input(f"Minutes: (0-59)", value=0, step=1,key="A40E")
                if (((24 == A40D) and (A40E==0))and((A40D>0.1)or(A40E>0.1))) or (((24>A40D>=0)and(59>=A40E>=0))and((A40D>0.1)or(A40E>0.1))):
                    ask40 = 2

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-40th app
if ask40 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))
    A34F = (A34B / 30) * (A34D+(A34E/60))
    A35F = (A35B / 30) * (A35D+(A35E/60))
    A36F = (A36B / 30) * (A36D+(A36E/60))
    A37F = (A37B / 30) * (A37D+(A37E/60))
    A38F = (A38B / 30) * (A38D+(A38E/60))
    A39F = (A39B / 30) * (A39D+(A39E/60))
    A40F = (A40B / 30) * (A40D+(A40E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))
    A34 = (A34F * (A34W * A34M))
    A35 = (A35F * (A35W * A35M))
    A36 = (A36F * (A36W * A36M))
    A37 = (A37F * (A37W * A37M))
    A38 = (A38F * (A38W * A38M))
    A39 = (A39F * (A39W * A39M))
    A40 = (A40F * (A40W * A40M))

    # TOTAL: watt/hour kada araw.
    wh40 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33 + A34 + A35 + A36 + A37 + A38 + A39 + A40)

    # TOTAL: Kilo-watt/hour kada month.
    Kh40 = ((wh40 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total40 = cost * Kh40

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost
    A34con = ((A34 * 30) / 1000) * cost
    A35con = ((A35 * 30) / 1000) * cost
    A36con = ((A36 * 30) / 1000) * cost
    A37con = ((A37 * 30) / 1000) * cost
    A38con = ((A38 * 30) / 1000) * cost
    A39con = ((A39 * 30) / 1000) * cost
    A40con = ((A40 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000
    Y34 = (A34*30)/1000
    Y35 = (A35*30)/1000
    Y36 = (A36*30)/1000
    Y37 = (A37*30)/1000
    Y38 = (A38*30)/1000
    Y39 = (A39*30)/1000
    Y40 = (A40*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33, Y34, Y35, Y36, Y37, Y38, Y39, Y40]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")
    if max_app == Y34:
        st.write("***")
        st.write("Name of appliance  :", A34N)
        st.write("Electricity bill   : PHP", A34con)
        st.write("Energy consumption :", Y34, "kWh")
    if max_app == Y35:
        st.write("***")
        st.write("Name of appliance  :", A35N)
        st.write("Electricity bill   : PHP", A35con)
        st.write("Energy consumption :", Y35, "kWh")
    if max_app == Y36:
        st.write("***")
        st.write("Name of appliance  :", A36N)
        st.write("Electricity bill   : PHP", A36con)
        st.write("Energy consumption :", Y36, "kWh")
    if max_app == Y37:
        st.write("***")
        st.write("Name of appliance  :", A37N)
        st.write("Electricity bill   : PHP", A37con)
        st.write("Energy consumption :", Y37, "kWh")
    if max_app == Y38:
        st.write("***")
        st.write("Name of appliance  :", A38N)
        st.write("Electricity bill   : PHP", A38con)
        st.write("Energy consumption :", Y38, "kWh")
    if max_app == Y39:
        st.write("***")
        st.write("Name of appliance  :", A39N)
        st.write("Electricity bill   : PHP", A39con)
        st.write("Energy consumption :", Y39, "kWh")
    if max_app == Y40:
        st.write("***")
        st.write("Name of appliance  :", A40N)
        st.write("Electricity bill   : PHP", A40con)
        st.write("Energy consumption :", Y40, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write(A34N, ": PHP", A34con)
    st.write(A35N, ": PHP", A35con)
    st.write(A36N, ": PHP", A36con)
    st.write(A37N, ": PHP", A37con)
    st.write(A38N, ": PHP", A38con)
    st.write(A39N, ": PHP", A39con)
    st.write(A40N, ": PHP", A40con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total40)
    st.write("Energy consumption:", Kh40, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-39th app
if ask39 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))
    A34F = (A34B / 30) * (A34D+(A34E/60))
    A35F = (A35B / 30) * (A35D+(A35E/60))
    A36F = (A36B / 30) * (A36D+(A36E/60))
    A37F = (A37B / 30) * (A37D+(A37E/60))
    A38F = (A38B / 30) * (A38D+(A38E/60))
    A39F = (A39B / 30) * (A39D+(A39E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))
    A34 = (A34F * (A34W * A34M))
    A35 = (A35F * (A35W * A35M))
    A36 = (A36F * (A36W * A36M))
    A37 = (A37F * (A37W * A37M))
    A38 = (A38F * (A38W * A38M))
    A39 = (A39F * (A39W * A39M))

    # TOTAL: watt/hour kada araw.
    wh39 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33 + A34 + A35 + A36 + A37 + A38 + A39)

    # TOTAL: Kilo-watt/hour kada month.
    Kh39 = ((wh39 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total39 = cost * Kh39

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost
    A34con = ((A34 * 30) / 1000) * cost
    A35con = ((A35 * 30) / 1000) * cost
    A36con = ((A36 * 30) / 1000) * cost
    A37con = ((A37 * 30) / 1000) * cost
    A38con = ((A38 * 30) / 1000) * cost
    A39con = ((A39 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000
    Y34 = (A34*30)/1000
    Y35 = (A35*30)/1000
    Y36 = (A36*30)/1000
    Y37 = (A37*30)/1000
    Y38 = (A38*30)/1000
    Y39 = (A39*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33, Y34, Y35, Y36, Y37, Y38, Y39]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")
    if max_app == Y34:
        st.write("***")
        st.write("Name of appliance  :", A34N)
        st.write("Electricity bill   : PHP", A34con)
        st.write("Energy consumption :", Y34, "kWh")
    if max_app == Y35:
        st.write("***")
        st.write("Name of appliance  :", A35N)
        st.write("Electricity bill   : PHP", A35con)
        st.write("Energy consumption :", Y35, "kWh")
    if max_app == Y36:
        st.write("***")
        st.write("Name of appliance  :", A36N)
        st.write("Electricity bill   : PHP", A36con)
        st.write("Energy consumption :", Y36, "kWh")
    if max_app == Y37:
        st.write("***")
        st.write("Name of appliance  :", A37N)
        st.write("Electricity bill   : PHP", A37con)
        st.write("Energy consumption :", Y37, "kWh")
    if max_app == Y38:
        st.write("***")
        st.write("Name of appliance  :", A38N)
        st.write("Electricity bill   : PHP", A38con)
        st.write("Energy consumption :", Y38, "kWh")
    if max_app == Y39:
        st.write("***")
        st.write("Name of appliance  :", A39N)
        st.write("Electricity bill   : PHP", A39con)
        st.write("Energy consumption :", Y39, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write(A34N, ": PHP", A34con)
    st.write(A35N, ": PHP", A35con)
    st.write(A36N, ": PHP", A36con)
    st.write(A37N, ": PHP", A37con)
    st.write(A38N, ": PHP", A38con)
    st.write(A39N, ": PHP", A39con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total39)
    st.write("Energy consumption:", Kh39, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-38th app
if ask38 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))
    A34F = (A34B / 30) * (A34D+(A34E/60))
    A35F = (A35B / 30) * (A35D+(A35E/60))
    A36F = (A36B / 30) * (A36D+(A36E/60))
    A37F = (A37B / 30) * (A37D+(A37E/60))
    A38F = (A38B / 30) * (A38D+(A38E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))
    A34 = (A34F * (A34W * A34M))
    A35 = (A35F * (A35W * A35M))
    A36 = (A36F * (A36W * A36M))
    A37 = (A37F * (A37W * A37M))
    A38 = (A38F * (A38W * A38M))

    # TOTAL: watt/hour kada araw.
    wh38 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33 + A34 + A35 + A36 + A37 + A38)

    # TOTAL: Kilo-watt/hour kada month.
    Kh38 = ((wh38 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total38 = cost * Kh38

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost
    A34con = ((A34 * 30) / 1000) * cost
    A35con = ((A35 * 30) / 1000) * cost
    A36con = ((A36 * 30) / 1000) * cost
    A37con = ((A37 * 30) / 1000) * cost
    A38con = ((A38 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000
    Y34 = (A34*30)/1000
    Y35 = (A35*30)/1000
    Y36 = (A36*30)/1000
    Y37 = (A37*30)/1000
    Y38 = (A38*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33, Y34, Y35, Y36, Y37, Y38]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")
    if max_app == Y34:
        st.write("***")
        st.write("Name of appliance  :", A34N)
        st.write("Electricity bill   : PHP", A34con)
        st.write("Energy consumption :", Y34, "kWh")
    if max_app == Y35:
        st.write("***")
        st.write("Name of appliance  :", A35N)
        st.write("Electricity bill   : PHP", A35con)
        st.write("Energy consumption :", Y35, "kWh")
    if max_app == Y36:
        st.write("***")
        st.write("Name of appliance  :", A36N)
        st.write("Electricity bill   : PHP", A36con)
        st.write("Energy consumption :", Y36, "kWh")
    if max_app == Y37:
        st.write("***")
        st.write("Name of appliance  :", A37N)
        st.write("Electricity bill   : PHP", A37con)
        st.write("Energy consumption :", Y37, "kWh")
    if max_app == Y38:
        st.write("***")
        st.write("Name of appliance  :", A38N)
        st.write("Electricity bill   : PHP", A38con)
        st.write("Energy consumption :", Y38, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write(A34N, ": PHP", A34con)
    st.write(A35N, ": PHP", A35con)
    st.write(A36N, ": PHP", A36con)
    st.write(A37N, ": PHP", A37con)
    st.write(A38N, ": PHP", A38con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total38)
    st.write("Energy consumption:", Kh38, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-37th app
if ask37 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))
    A34F = (A34B / 30) * (A34D+(A34E/60))
    A35F = (A35B / 30) * (A35D+(A35E/60))
    A36F = (A36B / 30) * (A36D+(A36E/60))
    A37F = (A37B / 30) * (A37D+(A37E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))
    A34 = (A34F * (A34W * A34M))
    A35 = (A35F * (A35W * A35M))
    A36 = (A36F * (A36W * A36M))
    A37 = (A37F * (A37W * A37M))

    # TOTAL: watt/hour kada araw.
    wh37 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33 + A34 + A35 + A36 + A37)

    # TOTAL: Kilo-watt/hour kada month.
    Kh37 = ((wh37 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total37 = cost * Kh37

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost
    A34con = ((A34 * 30) / 1000) * cost
    A35con = ((A35 * 30) / 1000) * cost
    A36con = ((A36 * 30) / 1000) * cost
    A37con = ((A37 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000
    Y34 = (A34*30)/1000
    Y35 = (A35*30)/1000
    Y36 = (A36*30)/1000
    Y37 = (A37*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33, Y34, Y35, Y36, Y37]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")
    if max_app == Y34:
        st.write("***")
        st.write("Name of appliance  :", A34N)
        st.write("Electricity bill   : PHP", A34con)
        st.write("Energy consumption :", Y34, "kWh")
    if max_app == Y35:
        st.write("***")
        st.write("Name of appliance  :", A35N)
        st.write("Electricity bill   : PHP", A35con)
        st.write("Energy consumption :", Y35, "kWh")
    if max_app == Y36:
        st.write("***")
        st.write("Name of appliance  :", A36N)
        st.write("Electricity bill   : PHP", A36con)
        st.write("Energy consumption :", Y36, "kWh")
    if max_app == Y37:
        st.write("***")
        st.write("Name of appliance  :", A37N)
        st.write("Electricity bill   : PHP", A37con)
        st.write("Energy consumption :", Y37, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write(A34N, ": PHP", A34con)
    st.write(A35N, ": PHP", A35con)
    st.write(A36N, ": PHP", A36con)
    st.write(A37N, ": PHP", A37con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total37)
    st.write("Energy consumption:", Kh37, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-36th app
if ask36 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))
    A34F = (A34B / 30) * (A34D+(A34E/60))
    A35F = (A35B / 30) * (A35D+(A35E/60))
    A36F = (A36B / 30) * (A36D+(A36E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))
    A34 = (A34F * (A34W * A34M))
    A35 = (A35F * (A35W * A35M))
    A36 = (A36F * (A36W * A36M))

    # TOTAL: watt/hour kada araw.
    wh36 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33 + A34 + A35 + A36)

    # TOTAL: Kilo-watt/hour kada month.
    Kh36 = ((wh36 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total36 = cost * Kh36

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost
    A34con = ((A34 * 30) / 1000) * cost
    A35con = ((A35 * 30) / 1000) * cost
    A36con = ((A36 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000
    Y34 = (A34*30)/1000
    Y35 = (A35*30)/1000
    Y36 = (A36*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33, Y34, Y35, Y36]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")
    if max_app == Y34:
        st.write("***")
        st.write("Name of appliance  :", A34N)
        st.write("Electricity bill   : PHP", A34con)
        st.write("Energy consumption :", Y34, "kWh")
    if max_app == Y35:
        st.write("***")
        st.write("Name of appliance  :", A35N)
        st.write("Electricity bill   : PHP", A35con)
        st.write("Energy consumption :", Y35, "kWh")
    if max_app == Y36:
        st.write("***")
        st.write("Name of appliance  :", A36N)
        st.write("Electricity bill   : PHP", A36con)
        st.write("Energy consumption :", Y36, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write(A34N, ": PHP", A34con)
    st.write(A35N, ": PHP", A35con)
    st.write(A36N, ": PHP", A36con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total36)
    st.write("Energy consumption:", Kh36, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-35th app
if ask35 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))
    A34F = (A34B / 30) * (A34D+(A34E/60))
    A35F = (A35B / 30) * (A35D+(A35E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))
    A34 = (A34F * (A34W * A34M))
    A35 = (A35F * (A35W * A35M))

    # TOTAL: watt/hour kada araw.
    wh35 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33 + A34 + A35)

    # TOTAL: Kilo-watt/hour kada month.
    Kh35 = ((wh35 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total35 = cost * Kh35

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost
    A34con = ((A34 * 30) / 1000) * cost
    A35con = ((A35 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000
    Y34 = (A34*30)/1000
    Y35 = (A35*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33, Y34, Y35]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")
    if max_app == Y34:
        st.write("***")
        st.write("Name of appliance  :", A34N)
        st.write("Electricity bill   : PHP", A34con)
        st.write("Energy consumption :", Y34, "kWh")
    if max_app == Y35:
        st.write("***")
        st.write("Name of appliance  :", A35N)
        st.write("Electricity bill   : PHP", A35con)
        st.write("Energy consumption :", Y35, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write(A34N, ": PHP", A34con)
    st.write(A35N, ": PHP", A35con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total35)
    st.write("Energy consumption:", Kh35, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-34th app
if ask34 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))
    A34F = (A34B / 30) * (A34D+(A34E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))
    A34 = (A34F * (A34W * A34M))

    # TOTAL: watt/hour kada araw.
    wh34 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33 + A34)

    # TOTAL: Kilo-watt/hour kada month.
    Kh34 = ((wh34 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total34 = cost * Kh34

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost
    A34con = ((A34 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000
    Y34 = (A34*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33, Y34]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")
    if max_app == Y34:
        st.write("***")
        st.write("Name of appliance  :", A34N)
        st.write("Electricity bill   : PHP", A34con)
        st.write("Energy consumption :", Y34, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write(A34N, ": PHP", A34con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total34)
    st.write("Energy consumption:", Kh34, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-33th app
if ask33 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))
    A33F = (A33B / 30) * (A33D+(A33E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))
    A33 = (A33F * (A33W * A33M))

    # TOTAL: watt/hour kada araw.
    wh33 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 +
            A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32 + A33)

    # TOTAL: Kilo-watt/hour kada month.
    Kh33 = ((wh33 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total33 = cost * Kh33

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost
    A33con = ((A33 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000
    Y33 = (A33*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y19, Y20, Y21,
            Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32, Y33]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    if max_app == Y33:
        st.write("***")
        st.write("Name of appliance  :", A33N)
        st.write("Electricity bill   : PHP", A33con)
        st.write("Energy consumption :", Y33, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write(A33N, ": PHP", A33con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total33)
    st.write("Energy consumption:", Kh33, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-32nd app
if ask32 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))
    A32F = (A32B / 30) * (A32D+(A32E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))
    A32 = (A32F * (A32W * A32M))

    # TOTAL: watt/hour kada araw.
    wh32 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31 + A32)

    # TOTAL: Kilo-watt/hour kada month.
    Kh32 = ((wh32 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total32 = cost * Kh32

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost
    A32con = ((A32 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000
    Y32 = (A32*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31, Y32]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    if max_app == Y32:
        st.write("***")
        st.write("Name of appliance  :", A32N)
        st.write("Electricity bill   : PHP", A32con)
        st.write("Energy consumption :", Y32, "kWh")
    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write(A32N, ": PHP", A32con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total32)
    st.write("Energy consumption:", Kh32, "kWh")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-31th app
if ask31 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))
    A31F = (A31B / 30) * (A31D+(A31E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))
    A31 = (A31F * (A31W * A31M))

    # TOTAL: watt/hour kada araw.
    wh31 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30 + A31)

    # TOTAL: Kilo-watt/hour kada month.
    Kh31 = ((wh31 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total31 = cost * Kh31

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost
    A31con = ((A31 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000
    Y31 = (A31*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30, Y31]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    if max_app == Y31:
        st.write("***")
        st.write("Name of appliance  :", A31N)
        st.write("Electricity bill   : PHP", A31con)
        st.write("Energy consumption :", Y31, "kWh")
    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write(A31N, ": PHP", A31con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total31)
    st.write("Energy consumption:", Kh31, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-30th app
if ask30 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))
    A30F = (A30B / 30) * (A30D+(A30E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))
    A30 = (A30F * (A30W * A30M))

    # TOTAL: watt/hour kada araw.
    wh30 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30)

    # TOTAL: Kilo-watt/hour kada month.
    Kh30 = ((wh30 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total30 = cost * Kh30

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost
    A30con = ((A30 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000
    Y30 = (A30*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29, Y30]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")
    if max_app == Y30:
        st.write("***")
        st.write("Name of appliance  :", A30N)
        st.write("Electricity bill   : PHP", A30con)
        st.write("Energy consumption :", Y30, "kWh")
    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write(A30N, ": PHP", A30con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total30)
    st.write("Energy consumption:", Kh30, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-29th app
if ask29 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))
    A29F = (A29B / 30) * (A29D+(A29E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))
    A29 = (A29F * (A29W * A29M))

    # TOTAL: watt/hour kada araw.
    wh29 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29)

    # TOTAL: Kilo-watt/hour kada month.
    Kh29 = ((wh29 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total29 = cost * Kh29

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost
    A29con = ((A29 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000
    Y29 = (A29*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28, Y29]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")
    if max_app == Y29:
        st.write("***")
        st.write("Name of appliance  :", A29N)
        st.write("Electricity bill   : PHP", A29con)
        st.write("Energy consumption :", Y29, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write(A29N, ": PHP", A29con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total29)
    st.write("Energy consumption:", Kh29, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-28th app
if ask28 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))
    A28F = (A28B / 30) * (A28D+(A28E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))
    A28 = (A28F * (A28W * A28M))

    # TOTAL: watt/hour kada araw.
    wh28 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28)

    # TOTAL: Kilo-watt/hour kada month.
    Kh28 = ((wh28 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total28 = cost * Kh28

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost
    A28con = ((A28 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000
    Y28 = (A28*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25, Y26, Y27, Y28]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")
    if max_app == Y28:
        st.write("***")
        st.write("Name of appliance  :", A28N)
        st.write("Electricity bill   : PHP", A28con)
        st.write("Energy consumption :", Y28, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write(A28N, ": PHP", A28con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total28)
    st.write("Energy consumption:", Kh28, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-27th app
if ask27 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))
    A27F = (A27B / 30) * (A27D+(A27E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))
    A27 = (A27F * (A27W * A27M))

    # TOTAL: watt/hour kada araw.
    wh27 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26 + A27)

    # TOTAL: Kilo-watt/hour kada month.
    Kh27 = ((wh27 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total27 = cost * Kh27

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost
    A27con = ((A27 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000
    Y27 = (A27*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25, Y26, Y27]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")
    if max_app == Y27:
        st.write("***")
        st.write("Name of appliance  :", A27N)
        st.write("Electricity bill   : PHP", A27con)
        st.write("Energy consumption :", Y27, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write(A27N, ": PHP", A27con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total27)
    st.write("Energy consumption:", Kh27, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-26th app
if ask26 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))
    A26F = (A26B / 30) * (A26D+(A26E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))
    A26 = (A26F * (A26W * A26M))

    # TOTAL: watt/hour kada araw.
    wh26 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26)

    # TOTAL: Kilo-watt/hour kada month.
    Kh26 = ((wh26 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total26 = cost * Kh26

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost
    A26con = ((A26 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000
    Y26 = (A26*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25, Y26]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")
    if max_app == Y26:
        st.write("***")
        st.write("Name of appliance  :", A26N)
        st.write("Electricity bill   : PHP", A26con)
        st.write("Energy consumption :", Y26, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write(A26N, ": PHP", A26con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total26)
    st.write("Energy consumption:", Kh26, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-25th app
if ask25 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))
    A25F = (A25B / 30) * (A25D+(A25E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))
    A25 = (A25F * (A25W * A25M))

    # TOTAL: watt/hour kada araw.
    wh25 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25)

    # TOTAL: Kilo-watt/hour kada month.
    Kh25 = ((wh25 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total25 = cost * Kh25

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost
    A25con = ((A25 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000
    Y25 = (A25*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24, Y24, Y25]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")
    if max_app == Y25:
        st.write("***")
        st.write("Name of appliance  :", A25N)
        st.write("Electricity bill   : PHP", A25con)
        st.write("Energy consumption :", Y25, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write(A25N, ": PHP", A25con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total25)
    st.write("Energy consumption:", Kh25, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-24th app
if ask24 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))
    A24F = (A24B / 30) * (A24D+(A24E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))
    A24 = (A24F * (A24W * A24M))

    # TOTAL: watt/hour kada araw.
    wh24 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24)

    # TOTAL: Kilo-watt/hour kada month.
    Kh24 = ((wh24 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total24 = cost * Kh24

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost
    A24con = ((A24 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000
    Y24 = (A24*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23, Y24]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")
    if max_app == Y24:
        st.write("***")
        st.write("Name of appliance  :", A24N)
        st.write("Electricity bill   : PHP", A24con)
        st.write("Energy consumption :", Y24, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write(A24N, ": PHP", A24con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total24)
    st.write("Energy consumption:", Kh24, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-23th app
if ask23 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))
    A23F = (A23B / 30) * (A23D+(A23E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))
    A23 = (A23F * (A23W * A23M))

    # TOTAL: watt/hour kada araw.
    wh23 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23)

    # TOTAL: Kilo-watt/hour kada month.
    Kh23 = ((wh23 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total23 = cost * Kh23

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost
    A23con = ((A23 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000
    Y23 = (A23*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22, Y23]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")
    if max_app == Y23:
        st.write("***")
        st.write("Name of appliance  :", A23N)
        st.write("Electricity bill   : PHP", A23con)
        st.write("Energy consumption :", Y23, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write(A23N, ": PHP", A23con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total23)
    st.write("Energy consumption:", Kh23, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-22th app
if ask22 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))
    A22F = (A22B / 30) * (A22D+(A22E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))
    A22 = (A22F * (A22W * A22M))

    # TOTAL: watt/hour kada araw.
    wh22 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21 + A22)

    # TOTAL: Kilo-watt/hour kada month.
    Kh22 = ((wh22 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total22 = cost * Kh22

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost
    A22con = ((A22 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000
    Y22 = (A22*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21, Y22]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")
    if max_app == Y22:
        st.write("***")
        st.write("Name of appliance  :", A22N)
        st.write("Electricity bill   : PHP", A22con)
        st.write("Energy consumption :", Y22, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write(A22N, ": PHP", A22con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total22)
    st.write("Energy consumption:", Kh22, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-21th app
if ask21 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))
    A21F = (A21B / 30) * (A21D+(A21E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))
    A21 = (A21F * (A21W * A21M))

    # TOTAL: watt/hour kada araw.
    wh21 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20 + A21)

    # TOTAL: Kilo-watt/hour kada month.
    Kh21 = ((wh21 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total21 = cost * Kh21

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost
    A21con = ((A21 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000
    Y21 = (A21*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20, Y21]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")
    if max_app == Y21:
        st.write("***")
        st.write("Name of appliance  :", A21N)
        st.write("Electricity bill   : PHP", A21con)
        st.write("Energy consumption :", Y21, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write(A21N, ": PHP", A21con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total21)
    st.write("Energy consumption:", Kh21, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-20th app
if ask20 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.

    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))
    A20F = (A20B / 30) * (A20D+(A20E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))
    A20 = (A20F * (A20W * A20M))

    # TOTAL: watt/hour kada araw.
    wh20 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19 + A20)

    # TOTAL: Kilo-watt/hour kada month.
    Kh20 = ((wh20 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total20 = cost * Kh20

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost
    A20con = ((A20 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000
    Y20 = (A20*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19, Y20]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")
    if max_app == Y20:
        st.write("***")
        st.write("Name of appliance  :", A20N)
        st.write("Electricity bill   : PHP", A20con)
        st.write("Energy consumption :", Y20, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write(A20N, ": PHP", A20con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total20)
    st.write("Energy consumption:", Kh20, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-19th app
if ask19 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.

    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))
    A19F = (A19B / 30) * (A19D+(A19E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))
    A19 = (A19F * (A19W * A19M))

    # TOTAL: watt/hour kada araw.
    wh19 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18 + A19)

    # TOTAL: Kilo-watt/hour kada month.
    Kh19 = ((wh19 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total19 = cost * Kh19

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost
    A19con = ((A19 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000
    Y19 = (A19*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18, Y19]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")
    if max_app == Y19:
        st.write("***")
        st.write("Name of appliance  :", A19N)
        st.write("Electricity bill   : PHP", A19con)
        st.write("Energy consumption :", Y19, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write(A19N, ": PHP", A19con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total19)
    st.write("Energy consumption:", Kh19, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-18th app
if ask18 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))
    A18F = (A18B / 30) * (A18D+(A18E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))
    A18 = (A18F * (A18W * A18M))

    # TOTAL: watt/hour kada araw.
    wh18 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17 + A18)

    # TOTAL: Kilo-watt/hour kada month.
    Kh18 = ((wh18 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total18 = cost * Kh18

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost
    A18con = ((A18 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000
    Y18 = (A18*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17, Y18]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")
    if max_app == Y18:
        st.write("***")
        st.write("Name of appliance  :", A18N)
        st.write("Electricity bill   : PHP", A18con)
        st.write("Energy consumption :", Y18, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write(A18N, ": PHP", A18con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total18)
    st.write("Energy consumption:", Kh18, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-17th app
if ask17 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))
    A17F = (A17B / 30) * (A17D+(A17E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))
    A17 = (A17F * (A17W * A17M))

    # TOTAL: watt/hour kada araw.
    wh17 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16 + A17)

    # TOTAL: Kilo-watt/hour kada month.
    Kh17 = ((wh17 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total17 = cost * Kh17

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost
    A17con = ((A17 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000
    Y17 = (A17*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16, Y17]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")
    if max_app == Y17:
        st.write("***")
        st.write("Name of appliance  :", A17N)
        st.write("Electricity bill   : PHP", A17con)
        st.write("Energy consumption :", Y17, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write(A17N, ": PHP", A17con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total17)
    st.write("Energy consumption:", Kh17, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-16yth app
if ask16 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))
    A16F = (A16B / 30) * (A16D+(A16E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))
    A16 = (A16F * (A16W * A16M))

    # TOTAL: watt/hour kada araw.
    wh16 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 +
            A16)

    # TOTAL: Kilo-watt/hour kada month.
    Kh16 = ((wh16 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total16 = cost * Kh16

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost
    A16con = ((A16 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000
    Y16 = (A16*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15,
            Y16,]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    if max_app == Y16:
        st.write("***")
        st.write("Name of appliance  :", A16N)
        st.write("Electricity bill   : PHP", A16con)
        st.write("Energy consumption :", Y16, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write(A16N, ": PHP", A16con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total16)
    st.write("Energy consumption:", Kh16, "kWh")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-15th app
if ask15 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))
    A15F = (A15B / 30) * (A15D+(A15E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))
    A15 = (A15F * (A15W * A15M))

    # TOTAL: watt/hour kada araw.
    wh15 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 +
            A9 + A10 + A11 + A12 + A13 + A14 + A15)

    # TOTAL: Kilo-watt/hour kada month.
    Kh15 = ((wh15 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total15 = cost * Kh15

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost
    A15con = ((A15 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000
    Y15 = (A15*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14, Y15]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")
    if max_app == Y15:
        st.write("***")
        st.write("Name of appliance  :", A15N)
        st.write("Electricity bill   : PHP", A15con)
        st.write("Energy consumption :", Y15, "kWh")
    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write(A15N, ": PHP", A15con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total15)
    st.write("Energy consumption:", Kh15, "kWh")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-14th app
if ask14 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))
    A14F = (A14B / 30) * (A14D+(A14E/60))

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
    A13 = (A13F * (A13W * A13M))
    A14 = (A14F * (A14W * A14M))

    # TOTAL: watt/hour kada araw.
    wh14 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 +
            A8 + A9 + A10 + A11 + A12 + A13 + A14)

    # TOTAL: Kilo-watt/hour kada month.
    Kh14 = ((wh14 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total14 = cost * Kh14

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost
    A14con = ((A14 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000
    Y14 = (A14*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13, Y14]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")
    if max_app == Y14:
        st.write("***")
        st.write("Name of appliance  :", A14N)
        st.write("Electricity bill   : PHP", A14con)
        st.write("Energy consumption :", Y14, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write(A14N, ": PHP", A14con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total14)
    st.write("Energy consumption:", Kh14, "kWh")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-13th app
if ask13 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))
    A13F = (A13B / 30) * (A13D+(A13E/60))

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
    A13 = (A13F * (A13W * A13M))

    # TOTAL: watt/hour kada araw.
    wh13 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13)

    # TOTAL: Kilo-watt/hour kada month.
    Kh13 = ((wh13 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total13 = cost * Kh13

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
    A12con = ((A12 * 30) / 1000) * cost
    A13con = ((A13 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000
    Y13 = (A13*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12, Y13]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")
    if max_app == Y13:
        st.write("***")
        st.write("Name of appliance  :", A13N)
        st.write("Electricity bill   : PHP", A13con)
        st.write("Energy consumption :", Y13, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write(A13N, ": PHP", A13con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total13)
    st.write("Energy consumption:", Kh13, "kWh")
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-12th app
if ask12 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))
    A12F = (A12B / 30) * (A12D+(A12E/60))

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
    wh13 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12)

    # TOTAL: Kilo-watt/hour kada month.
    Kh12 = ((wh13 * 30) / 1000)

    # TOTAL: para ma compute ang (cost) kada month.
    total12 = cost * Kh12

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
    A12con = ((A12 * 30) / 1000) * cost

    # INDIVIDUAL: Kilo-watt/hour
    Y1 = (A1*30)/1000
    Y2 = (A2*30)/1000
    Y3 = (A3*30)/1000
    Y4 = (A4*30)/1000
    Y5 = (A5*30)/1000
    Y6 = (A6*30)/1000
    Y7 = (A7*30)/1000
    Y8 = (A8*30)/1000
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000
    Y12 = (A12*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11, Y12]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")
    if max_app == Y12:
        st.write("***")
        st.write("Name of appliance  :", A12N)
        st.write("Electricity bill   : PHP", A12con)
        st.write("Energy consumption :", Y12, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total12)
    st.write("Energy consumption:", Kh12, "kWh")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-11th app
if ask11 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))
    A11F = (A11B / 30) * (A11D+(A11E/60))

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
    wh11 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11)

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
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000
    Y11 = (A11*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")
    if max_app == Y11:
        st.write("***")
        st.write("Name of appliance  :", A11N)
        st.write("Electricity bill   : PHP", A11con)
        st.write("Energy consumption :", Y11, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total11)
    st.write("Energy consumption:", Kh11, "kWh")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-10th app
if ask10 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))
    A10F = (A10B / 30) * (A10D+(A10E/60))

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
    wh10 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10)

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
    Y9 = (A9*30)/1000
    Y10 = (A10*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")
    if max_app == Y10:
        st.write("***")
        st.write("Name of appliance  :", A10N)
        st.write("Electricity bill   : PHP", A10con)
        st.write("Energy consumption :", Y10, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
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
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total10)
    st.write("Energy consumption:", Kh10, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-9th app
if ask9 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))
    A9F = (A9B / 30) * (A9D+(A9E/60))

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
    wh9 = (A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9)

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
    Y9 = (A9*30)/1000

    # OUTPUT1
    st.markdown("## **THE RESULTS:**")
    # Identify the high consumption appliance
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")
    if max_app == Y9:
        st.write("***")
        st.write("Name of appliance  :", A9N)
        st.write("Electricity bill   : PHP", A9con)
        st.write("Energy consumption :", Y9, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write(A3N, ": PHP", A3con)
    st.write(A4N, ": PHP", A4con)
    st.write(A5N, ": PHP", A5con)
    st.write(A6N, ": PHP", A6con)
    st.write(A7N, ": PHP", A7con)
    st.write(A8N, ": PHP", A8con)
    st.write(A9N, ": PHP", A9con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total9)
    st.write("Energy consumption:", Kh9, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-8th app
if ask8 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))
    A8F = (A8B / 30) * (A8D+(A8E/60))

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
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")
    if max_app == Y8:
        st.write("***")
        st.write("Name of appliance  :", A8N)
        st.write("Electricity bill   : PHP", A8con)
        st.write("Energy consumption :", Y8, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write(A3N, ": PHP", A3con)
    st.write(A4N, ": PHP", A4con)
    st.write(A5N, ": PHP", A5con)
    st.write(A6N, ": PHP", A6con)
    st.write(A7N, ": PHP", A7con)
    st.write(A8N, ": PHP", A8con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total8)
    st.write("Energy consumption:", Kh8, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-7th app
if ask7 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))
    A7F = (A7B / 30) * (A7D+(A7E/60))

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
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6, Y7]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")
    if max_app == Y7:
        st.write("***")
        st.write("Name of appliance  :", A7N)
        st.write("Electricity bill   : PHP", A7con)
        st.write("Energy consumption :", Y7, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write(A3N, ": PHP", A3con)
    st.write(A4N, ": PHP", A4con)
    st.write(A5N, ": PHP", A5con)
    st.write(A6N, ": PHP", A6con)
    st.write(A7N, ": PHP", A7con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total7)
    st.write("Energy consumption:", Kh7, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-6th app
if ask6 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))
    A6F = (A6B / 30) * (A6D+(A6E/60))

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
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5, Y6]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")
    if max_app == Y6:
        st.write("***")
        st.write("Name of appliance  :", A6N)
        st.write("Electricity bill   : PHP", A6con)
        st.write("Energy consumption :", Y6, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write(A3N, ": PHP", A3con)
    st.write(A4N, ": PHP", A4con)
    st.write(A5N, ": PHP", A5con)
    st.write(A6N, ": PHP", A6con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total6)
    st.write("Energy consumption:", Kh6, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-5th app
if ask5 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))
    A5F = (A5B / 30) * (A5D+(A5E/60))

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
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4, Y5]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")
    if max_app == Y5:
        st.write("***")
        st.write("Name of appliance  :", A5N)
        st.write("Electricity bill   : PHP", A5con)
        st.write("Energy consumption :", Y5, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write(A3N, ": PHP", A3con)
    st.write(A4N, ": PHP", A4con)
    st.write(A5N, ": PHP", A5con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total5)
    st.write("Energy consumption:", Kh5, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-4th app
if ask4 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))
    A4F = (A4B / 30) * (A4D+(A4E/60))

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
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3, Y4]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")
    if max_app == Y4:
        st.write("***")
        st.write("Name of appliance  :", A4N)
        st.write("Electricity bill   : PHP", A4con)
        st.write("Energy consumption :", Y4, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write(A3N, ": PHP", A3con)
    st.write(A4N, ": PHP", A4con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total4)
    st.write("Energy consumption:", Kh4, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-3rd app
if ask3 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))
    A3F = (A3B / 30) * (A3D+(A3E/60))

    # INDIVIDUALLY: para ma compute ang average use (watt/hour) kada araw over the month.
    A1 = (A1F * (A1W * A1M))
    A2 = (A2F * (A2W * A2M))
    A3 = (A3F * (A3W * A3M))

    # TOTAL: watt/hour kada araw.
    wh3 = (A1 + A2 + A3)

    # TOTAL: Kilo-watt/hour kada month.
    Kh3 = ((wh3 * 30) / 1000)

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
    st.write("***")
    st.markdown("**HIGHEST ENERGY CONSUMPTION**")
    apps = [Y1, Y2, Y3]
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
    if max_app == Y3:
        st.write("***")
        st.write("Name of appliance  :", A3N)
        st.write("Electricity bill   : PHP", A3con)
        st.write("Energy consumption :", Y3, "kWh")

    # OUTPUT2
    st.write("***")
    st.markdown("**INDIVIDUAL ELECTRICITY BILL**")
    st.write(A1N, ": PHP", A1con)
    st.write(A2N, ": PHP", A2con)
    st.write(A3N, ": PHP", A3con)
    st.write("***")
    st.markdown("**TOTAL ELECTRICITY BILL AND ENERGY CONSUMPTION**")
    st.write("Electricity bill: PHP", total3)
    st.write("Energy consumption:", Kh3, "kWh")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Calculate 1-2nd app
if ask2 == 2:
    # INDIVIDUALLY: para ma compute ang average use (hour) kada araw over the month.
    A1F = (A1B / 30) * (A1D+(A1E/60))
    A2F = (A2B / 30) * (A2D+(A2E/60))

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
    A1F = (A1B / 30) * (A1D+(A1E/60))

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
