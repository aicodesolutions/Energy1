
# This script is used to generate hourly consumption data for 30 days by adding random values to the existing data.
# The script reads the initial data from a CSV file, creates a template data for one day, and then adds random values to the template data to create additional data for the next 30 days.   
# The final data is written to a new CSV file.It removes the template data from the final data.
# The script assumes that the input CSV file contains hourly consumption data for one day (24 records) and that the data is in the following format:
# it only proces two columns Datetime and Consumption. Any other corlumns will be duplicated in the final data.

#  Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# ...existing code...

# Function to create consumption data for 24 hours
def create_template_data(tempdate, season='Winter'):
    df = pd.DataFrame()  # Create an empty DataFrame
    df['Datetime'] = pd.date_range(start=tempdate, periods=24, freq='H')  # Generate a range of 24 hourly timestamps
    if season == 'Winter':
        # Define consumption values for each hour
        df['Consumption'] = [1, 1, 1, 1, 1.2, 1.4, 1.4, 1.5, 1.2,1.2, 1.2, 1.2, 1.2, 1.3, 1.3, 1.5, 1.5, 1.4, 1.4, 1.4, 1.2, 1.2, 1, 1]
    if season == 'Summer':
        # Define consumption values for each hour
        df['Consumption'] = [1.2, 1.2, 1.2, 1.2, 1.4, 1.6, 1.6, 1.7, 1.4,1.4, 1.4, 1.4, 1.4, 1.5, 1.5, 1.7, 1.7, 1.6, 1.6, 1.6, 1.4, 1.4, 1.2, 1.2]
    return df

# Function to create additional data by adding random values to the consumption data
def create_additional_data(df1, tempdate):
    df = pd.DataFrame()  # Create an empty DataFrame
    df['Datetime'] = pd.date_range(start=tempdate, periods=24, freq='H')  # Generate a range of 24 hourly timestamps
    # Add random values between -1.1 and 1.1 to the existing consumption data
    df['Consumption'] = df1['Consumption'] + (0.01 * (random.randrange(1,10)-5))
    return df

# Read the input CSV file containing hourly consumption data
df = pd.read_csv('template.csv')
# Get the first 24 records (1 day) from the DataFrame
df = df.head(24)

# Function to generate data for a given month
def generate_monthly_data(start_date, days_in_month, season):
    df1 = create_template_data(start_date, season)
    df=df1
    for i in range(1, days_in_month):
        tempdate = start_date.split('/')[0] + '/' + str(i + 1) + '/' + start_date.split('/')[2]
        df1 = create_additional_data(df1, tempdate)
        df = pd.concat([df, df1])
    
    return df

# Generate data for each month
df = pd.DataFrame()
df = pd.concat([df, generate_monthly_data('1/1/2024', 31, 'Winter')])
df = pd.concat([df, generate_monthly_data('2/1/2024', 28, 'Winter')])
df = pd.concat([df, generate_monthly_data('3/1/2024', 31, 'Winter')])
df = pd.concat([df, generate_monthly_data('4/1/2024', 30, 'Summer')])
df = pd.concat([df, generate_monthly_data('5/1/2024', 31, 'Summer')])
df = pd.concat([df, generate_monthly_data('6/1/2024', 30, 'Summer')])
df = pd.concat([df, generate_monthly_data('7/1/2024', 31, 'Summer')])
df = pd.concat([df, generate_monthly_data('8/1/2024', 31, 'Summer')])
df = pd.concat([df, generate_monthly_data('9/1/2024', 30, 'Summer')])
df = pd.concat([df, generate_monthly_data('10/1/2024', 31, 'Winter')])
df = pd.concat([df, generate_monthly_data('11/1/2024', 30, 'Winter')])
df = pd.concat([df, generate_monthly_data('12/1/2024', 31, 'Winter')])

# Remove the template data from the final data
df = df[24:]
# Sort the data by the 'Datetime' column
df = df.sort_values(by='Datetime')
# Reset the index of the DataFrame
df = df.reset_index(drop=True)

plt.figure(figsize=(10, 6))
df['Consumption'].plot(title='Energy Consumption Over Time')
plt.show()

# Write the final data to a new CSV file
df.to_csv('Hourlydata1.csv', index=False)
print('Data written to file')
#-----