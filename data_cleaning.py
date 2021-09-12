import pandas as pd
filename = '/Users/rajasreekalli/Downloads/sales_predictions.csv'

# 1.How many rows and columns?
df = pd.read_csv(filename)
print(df)
#2. What are the datatypes of each variable
types = df.dtypes
print(types)
#3. Are there duplicates? If so, drop any duplicates.
print(df.drop_duplicates())

#4. Identify missing values.
item_missing = df.isna()
print(item_missing.sum())
#5.Decide on how to address the missing values and do it! (This requires your judgement, so explain your choice).
address_missing=df.loc[0:8522,:].fillna(method='ffill')
print(address_missing)
#6.Confirm that there are no missing values after addressing them.
final_missing = address_missing.isna()
print(final_missing.sum())
#7.Find and fix any inconsistent categories of data (example: fix cat, Cat, and cats so that they are consistent) 
df['Item_Fat_Content'] = (df['Item_Fat_Content'].replace(['LF','low fat'],'Low Fat'))
df['Item_Fat_Content'] = (df['Item_Fat_Content'].replace(['reg'],'Regular'))
print(df['Item_Fat_Content'].value_counts())
print(df['Outlet_Type'].value_counts())
#8. For any numerical columns, obtain the summary statistics of each (min, max, mean)
print("The mean of all numerical columns only:\n",df.mean(numeric_only = True))
print("The min of all numerical columns only:\n",df.min(numeric_only = True))
print("The max of all numerical columns only:\n",df.max(numeric_only = True))
