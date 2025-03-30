import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
col1, col2 = st.columns(2, gap="small",border=True)
df = pd.read_csv("EnergyHrs1.csv")  
if 1:
    col1.write('Estimated consumption')   
    #col1.line_chart(df)
    col1.line_chart(data=df, x='Hour of the Day', y='Estimated Consumption', x_label=None, y_label=None) 

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Solar', 'Fossil','Wind', 'BioFuel'
sizes = [45, 15, 30, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
col2.write('Energy Mix')
col2.pyplot(fig1)
col2.write(" Your appliances ")
col3,col4=col2.columns(2, gap="small",border=True)
col3.image("images/bulb.jpg",  width=400, )
col3.write("4 bulbs")
col4.image("images/tv.png",  width=400, )
col4.write("1 T V")