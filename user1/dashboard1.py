import streamlit as st
import pandas as pd
#df = pd.read_csv("ConsumptionHourly.csv")  
#df = pd.read_csv("final_filled_data.csv") 
df = pd.read_csv("newdata.csv") 


df = df.set_index("Datetime")
df.index = pd.to_datetime(df.index)
#

#
if 1:
    st.write('Energy Dashboard')
    chart_data = df[:24]
    st.line_chart(chart_data)

