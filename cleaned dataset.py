import pandas as pd

df = pd.read_csv("rawdata/amazon_sales.csv")

print(df.head())
print(df.shape)
print(df.info())

import pandas as pd

df = pd.read_csv("rawdata/amazon_sales.csv")

print(df.head())
print(df.shape)
print(df.info())

print(df.duplicated().sum())
print(df['product_category'].value_counts())
print(df['payment_method'].value_counts())
print(df['rating'].describe())

df['order_date'] = pd.to_datetime(df['order_date'], format="%d-%m-%Y")

df['order_year'] = df['order_date'].dt.year
df['order_month'] = df['order_date'].dt.month

df['revenue_per_unit'] = df['total_revenue'] / df['quantity_sold']

df['high_discount'] = df['discount_percent'].apply(
    lambda x: 'Yes' if x >= 30 else 'No'
)

df.to_csv("data/cleaned_data.csv", index=False)

print("Cleaned dataset saved")
print(df.shape)
