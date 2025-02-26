
# This script is used to generate hourly consumption data for 30 days by adding random values to the existing data.
# The script reads the initial data from a CSV file, creates a template data for one day, and then adds random values to the template data to create additional data for the next 30 days.   
# The final data is written to a new CSV file.It removes the template data from the final data.
# The script assumes that the input CSV file contains hourly consumption data for one day (24 records) and that the data is in the following format:
# it only proces two columns Datetime and Consumption. Any other corlumns will be duplicated in the final data.

#  Import necessary libraries
import pandas as pd
import numpy as np

# Function to create consumption data for 24 hours
# The sum of consumption from 0-6 hours is 10, 6-12 hours is 20, 12-18 hours is 30, and 18-24 hours is 40
def create_template_data(tempdate, season='Winter'):
    df = pd.DataFrame()  # Create an empty DataFrame
    df['Datetime'] = pd.date_range(start=tempdate, periods=24, freq='H')  # Generate a range of 24 hourly timestamps
    if season == 'Winter':
        # Define consumption values for each hour
        df['Consumption'] = [10, 12, 12, 14, 16, 18, 18, 20, 10, 12, 12, 14, 10, 12, 12, 14, 16, 18, 18, 20, 10, 12, 12, 14]
    return df

# Function to create additional data by adding random values to the consumption data
def create_additional_data(df1, tempdate):
    df = pd.DataFrame()  # Create an empty DataFrame
    df['Datetime'] = pd.date_range(start=tempdate, periods=24, freq='H')  # Generate a range of 24 hourly timestamps
    # Add random values between -1.1 and 1.1 to the existing consumption data
    df['Consumption'] = df1['Consumption'] + np.random.uniform(-1.1, 1.1, len(df1))
    return df

# Read the input CSV file containing hourly consumption data
df = pd.read_csv('ConsumptionHourly.csv')
# Get the first 24 records (1 day) from the DataFrame
df = df.head(24)

# Create template data for January 1, 2024
df1 = create_template_data('1/1/2024', season='Winter')
# Concatenate the initial data with the template data
df = pd.concat([df, df1])

# Create a loop to add data for the next 30 days
# change the number based on the number of days you want to add
for i in range(1, 30):
    tempdate = '1/' + str(i + 1) + '/2024'  # Generate the date for the next day
    df1 = create_additional_data(df1, tempdate)  # Create additional data for the next day
    df = pd.concat([df, df1])  # Concatenate the new data with the existing data

#remove the template data from the final data
df = df[24:]   
# Sort the data by the 'Datetime' column
df = df.sort_values(by='Datetime')
# Reset the index of the DataFrame
df = df.reset_index(drop=True)

# Write the final data to a new CSV file
df.to_csv('ConsumptionHourly1.csv', index=False)
print('Data written to file')  # Print a message indicating that the data has been written to the file
