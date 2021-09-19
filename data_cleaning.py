import pandas as pd

filename = '/Users/rajasreekalli/Downloads/sales_predictions.csv'

# 1.How many rows and columns?
df = pd.read_csv(filename)
print(df)
#ans:     Item_Identifier  Item_Weight Item_Fat_Content  Item_Visibility  ... Outlet_Size  Outlet_Location_Type        Outlet_Type  Item_Outlet_Sales
#0              FDA15        9.300          Low Fat         0.016047  ...      Medium                Tier 1  Supermarket Type1          3735.1380
#1              DRC01        5.920          Regular         0.019278  ...      Medium                Tier 3  Supermarket Type2           443.4228
#2              FDN15       17.500          Low Fat         0.016760  ...      Medium                Tier 1  Supermarket Type1          2097.2700
#3              FDX07       19.200          Regular         0.000000  ...         NaN                Tier 3      Grocery Store           732.3800
#4              NCD19        8.930          Low Fat         0.000000  ...        High                Tier 3  Supermarket Type1           994.7052
#...              ...          ...              ...              ...  ...         ...                   ...                ...                ...
#8518           FDF22        6.865          Low Fat         0.056783  ...        High                Tier 3  Supermarket Type1          2778.3834
#8519           FDS36        8.380          Regular         0.046982  ...         NaN                Tier 2  Supermarket Type1           549.2850
#8520           NCJ29       10.600          Low Fat         0.035186  ...       Small                Tier 2  Supermarket Type1          1193.1136
#8521           FDN46        7.210          Regular         0.145221  ...      Medium                Tier 3  Supermarket Type2          1845.5976
#8522           DRG01       14.800          Low Fat         0.044878  ...       Small                Tier 1  Supermarket Type1           765.6700
#[8523 rows x 12 columns]
#2. What are the datatypes of each variable
types = df.dtypes
print(types)
#ans:Item_Identifier               object
#Item_Weight                  float64
#Item_Fat_Content              object
#Item_Visibility              float64
#Item_Type                     object
#Item_MRP                     float64
#Outlet_Identifier             object
#Outlet_Establishment_Year      int64
#Outlet_Size                   object
#Outlet_Location_Type          object
#Outlet_Type                   object
#Item_Outlet_Sales            float64
#dtype: object
#3. Are there duplicates? If so, drop any duplicates.
print(df.drop_duplicates())
#ans:
#     Item_Identifier  Item_Weight Item_Fat_Content  Item_Visibility  ... Outlet_Size  Outlet_Location_Type        Outlet_Type  Item_Outlet_Sales
#0              FDA15        9.300          Low Fat         0.016047  ...      Medium                Tier 1  Supermarket Type1          3735.1380
#1              DRC01        5.920          Regular         0.019278  ...      Medium                Tier 3  Supermarket Type2           443.4228
#2              FDN15       17.500          Low Fat         0.016760  ...      Medium                Tier 1  Supermarket Type1          2097.2700
#3              FDX07       19.200          Regular         0.000000  ...         NaN                Tier 3      Grocery Store           732.3800
#4              NCD19        8.930          Low Fat         0.000000  ...        High                Tier 3  Supermarket Type1           994.7052
#...              ...          ...              ...              ...  ...         ...                   ...                ...                ...
#8518           FDF22        6.865          Low Fat         0.056783  ...        High                Tier 3  Supermarket Type1          2778.3834
#8519           FDS36        8.380          Regular         0.046982  ...         NaN                Tier 2  Supermarket Type1           549.2850
#8520           NCJ29       10.600          Low Fat         0.035186  ...       Small                Tier 2  Supermarket Type1          1193.1136
#8521           FDN46        7.210          Regular         0.145221  ...      Medium                Tier 3  Supermarket Type2          1845.5976
#8522           DRG01       14.800          Low Fat         0.044878  ...       Small                Tier 1  Supermarket Type1           765.6700

#[8523 rows x 12 columns]

#4. Identify missing values.
item_missing = df.isna()
print(item_missing.sum())
#ans:Item_Identifier                 0
#Item_Weight                  1463
#Item_Fat_Content                0
#Item_Visibility                 0
#Item_Type                       0
#Item_MRP                        0
#Outlet_Identifier               0
#Outlet_Establishment_Year       0
#Outlet_Size                  2410
#Outlet_Location_Type            0
#Outlet_Type                     0
#Item_Outlet_Sales               0
#dtype: int64
#5.Decide on how to address the missing values and do it! (This requires your judgement, so explain your choice).
address_missing=df.loc[0:8522,:].fillna(method='ffill')
print(address_missing)
#ans:
#     Item_Identifier  Item_Weight Item_Fat_Content  Item_Visibility  ... Outlet_Size  Outlet_Location_Type        Outlet_Type  Item_Outlet_Sales
#0              FDA15        9.300          Low Fat         0.016047  ...      Medium                Tier 1  Supermarket Type1          3735.1380
#1              DRC01        5.920          Regular         0.019278  ...      Medium                Tier 3  Supermarket Type2           443.4228
#2              FDN15       17.500          Low Fat         0.016760  ...      Medium                Tier 1  Supermarket Type1          2097.2700
#3              FDX07       19.200          Regular         0.000000  ...      Medium                Tier 3      Grocery Store           732.3800
#4              NCD19        8.930          Low Fat         0.000000  ...        High                Tier 3  Supermarket Type1           994.7052
#...              ...          ...              ...              ...  ...         ...                   ...                ...                ...
#8518           FDF22        6.865          Low Fat         0.056783  ...        High                Tier 3  Supermarket Type1          2778.3834
#8519           FDS36        8.380          Regular         0.046982  ...        High                Tier 2  Supermarket Type1           549.2850
#8520           NCJ29       10.600          Low Fat         0.035186  ...       Small                Tier 2  Supermarket Type1          1193.1136
#8521           FDN46        7.210          Regular         0.145221  ...      Medium                Tier 3  Supermarket Type2          1845.5976
#8522           DRG01       14.800          Low Fat         0.044878  ...       Small                Tier 1  Supermarket Type1           765.6700

#[8523 rows x 12 columns]
#6.Confirm that there are no missing values after addressing them.
final_missing = address_missing.isna()
print(final_missing.sum())
#ans:Item_Identifier              0
#Item_Weight                  0
#Item_Fat_Content             0
#Item_Visibility              0
#Item_Type                    0
#Item_MRP                     0
#Outlet_Identifier            0
#Outlet_Establishment_Year    0
#Outlet_Size                  0
#Outlet_Location_Type         0
#Outlet_Type                  0
#Item_Outlet_Sales            0
dtype: int64
#7.Find and fix any inconsistent categories of data (example: fix cat, Cat, and cats so that they are consistent) 
df['Item_Fat_Content'] = (df['Item_Fat_Content'].replace(['LF','low fat'],'Low Fat'))
df['Item_Fat_Content'] = (df['Item_Fat_Content'].replace(['reg'],'Regular'))
print(df['Item_Fat_Content'].value_counts())
print(df['Outlet_Type'].value_counts())
#ans:Low Fat    5517
#Regular    3006
#Name: Item_Fat_Content, dtype: int64
##Supermarket Type1    5577
#Grocery Store        1083
#Supermarket Type3     935
#Supermarket Type2     928
#Name: Outlet_Type, dtype: int64
#8. For any numerical columns, obtain the summary statistics of each (min, max, mean)
print("The mean of all numerical columns only:\n",df.mean(numeric_only = True))
print("The min of all numerical columns only:\n",df.min(numeric_only = True))
print("The max of all numerical columns only:\n",df.max(numeric_only = True))
#ans:The mean of all numerical columns only:
# Item_Weight                    12.857645
#Item_Visibility                 0.066132
#Item_MRP                      140.992782
#Outlet_Establishment_Year    1997.831867
#Item_Outlet_Sales            2181.288914
#dtype: float64
#The min of all numerical columns only:
# Item_Weight                     4.555
#Item_Visibility                 0.000
#Item_MRP                       31.290
#Outlet_Establishment_Year    1985.000
#Item_Outlet_Sales              33.290
#dtype: float64
#The max of all numerical columns only:
# Item_Weight                     21.350000
#Item_Visibility                  0.328391
#Item_MRP                       266.888400
#Outlet_Establishment_Year     2009.000000
#Item_Outlet_Sales            13086.964800
#dtype: float64