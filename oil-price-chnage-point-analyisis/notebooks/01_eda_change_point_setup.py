import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Load data
df = pd.read_csv('D:\\KAIM5\\week 10\\oil-price-chnage-point-analyisis\\data\\BrentOilPrices.csv')

# Convert date
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df = df.sort_values('Date').reset_index(drop=True)

# Plot raw price
plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['Price'], label='Brent Oil Price')
plt.title('Brent Oil Price Over Time')
plt.xlabel('Date')
plt.ylabel('USD per Barrel')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate log returns
df['log_return'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
df = df.dropna()

# Plot log returns
plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['log_return'], label='Log Returns', color='orange')
plt.title('Log Returns of Brent Oil Price')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Stationarity test
adf_result = adfuller(df['log_return'])
print("ADF Statistic:", adf_result[0])
print("p-value:", adf_result[1])
if adf_result[1] < 0.05:
    print("Series is stationary")
else:
    print("Series is NOT stationary")
