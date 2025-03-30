import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

#st.header("Your Estimated Consumption Today")
#st.write(f"You are logged in as {st.session_state.role}.")

import pandas as pd
df = pd.read_csv("EnergyHrs2.csv")  
df = df.set_index("Datetime")
df.index = pd.to_datetime(df.index)
#
if 1:
    st.write('Current Energy Consumption')
    chart_data = df
    st.line_chart(chart_data)

labels = 'Solar', 'Fossil','Wind', 'BioFuel'
sizes = [45, 15, 30, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
col1, col2 = st.columns(2, gap="small",border=True)
col1.write('Current Energy Mix')
col1.pyplot(fig1)
col2.write(" Appliances Connected ")
col3,col4,col5=col2.columns(3, gap="small")
col3.image("images/bulb.jpg",  width=400, )
col3.write("432 bulbs")
col4.image("images/tv.png",  width=400, )
col4.write("45 T Vs")
col5.image("images/wm.jpg",  width=400, )
col5.write("12 Washing Machines")