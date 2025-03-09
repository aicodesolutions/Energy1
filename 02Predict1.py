import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_features(df):
    """
    Create time series features based on time series index.
    """
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df

# Load the dataset
df = pd.read_csv('hourlydata1.csv')
df.head()

# Convert Datetime to datetime type and set as index
df['Datetime'] = pd.to_datetime(df['Datetime'])

df = df.set_index('Datetime')
df = df.sort_index()
#copy the data, subtract 1 year from the datetime column, and conctenate the two dataframes
df_copy = df.copy()
df_copy1 = df.copy()
df_copy.index = df_copy.index - pd.DateOffset(years=1)
df = pd.concat([df_copy, df])
df.head()
#copy the data, add 1 year to the datetime column, and conctenate the two dataframes    
df_copy = df_copy1.copy()
df_copy.index = df_copy.index + pd.DateOffset(years=1)
df = pd.concat([df_copy, df])
df = df.sort_index()
#remove data that is more than current date
df = df.loc[df.index < '2025-03-10']
#remove duplicates
df = df[~df.index.duplicated(keep='first')] 
# Plot the time series data
plt.figure(figsize=(10, 6))
df['Consumption'].plot(title='Energy Consumption Over Time')
plt.show()

# Apply the feature creation function
df = create_features(df)


# Split the data into training and test sets
train = df.loc[df.index < '2025-01-01']
test = df.loc[df.index >= '2025-01-01']

import xgboost as xgb
from sklearn.metrics import root_mean_squared_error
#https://medium.com/@gayathri.s.de/predicting-energy-consumption-using-time-series-forecasting-da965751ab95
# Define features and target
features = ['hour', 'dayofweek', 'month', 'year']
X_train = train[features]
y_train = train['Consumption']
X_test = test[features]
y_test = test['Consumption']
# Initialize and train the model
model = xgb.XGBRegressor(n_estimators=1000, early_stopping_rounds=50, learning_rate=0.01)
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=100)
#
fi = pd.DataFrame(data=model.feature_importances_,
             index=model.feature_names_in_,
             columns=['importance'])
fi.sort_values('importance').plot(kind='barh', title='Feature Importance')
plt.show()
#
# Predict on the test set
y_pred = model.predict(X_test)
# Calculate RMSE
rmse = root_mean_squared_error(y_test, y_pred)
print(f'RMSE: {rmse}')
#from statsmodels.tsa.arima.model import ARIMA
# Assuming 'data.csv' is your dataset file

# Plot predictions vs actual
plt.figure(figsize=(10, 6))
plt.plot(test.index, y_test, label='Actual')
plt.plot(test.index, y_pred, label='Predicted', color='red')
plt.legend()
plt.title('Energy Consumption: Actual vs Predicted')
plt.show()

# Predict on the current dat
X_day=X_test.tail(24)
y_day = model.predict(X_day)
y_daypred=y_train.tail(24)
plt.figure(figsize=(10, 6))
plt.plot(X_day.index, y_daypred, label='Actual')
plt.plot(X_day.index, y_day, label='Predicted', color='red')
plt.legend()
plt.title('Energy Consumption: Actual vs Predicted')
plt.show()

X_day['Prediction'] = y_day.tolist()
# Save the model
import joblib
joblib.dump(model, 'model.pkl')
# Save the feature list
joblib.dump(features, 'features.pkl')
# Save the last day's predictions
X_day.to_csv('predictions.csv')


#https://github.com/Gayathri-Selvaganapathi/energy_consumption_prediction

#https://www.kaggle.com/code/robikscube/time-series-forecasting-with-machine-learning-yt
