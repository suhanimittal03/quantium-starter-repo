import pandas as pd 

sales_data_0 = pd.read_csv('data/daily_sales_data_0.csv')
sales_data_1 = pd.read_csv('data/daily_sales_data_1.csv')
sales_data_2 = pd.read_csv('data/daily_sales_data_2.csv')
# print(sales_data_0.head())

sales_data = pd.concat([sales_data_0, sales_data_1, sales_data_2])
# print(sales_data)

mask = sales_data['product'] == 'pink morsel'

sales_data_copy = sales_data[mask]
sales_data_copy.reset_index(inplace=True, drop=True)
sales_data_copy['price'] = sales_data_copy['price'].replace({'\$': ''}, regex=True).astype(float).astype(int)
sales_data_copy['date'] = pd.to_datetime(sales_data_copy['date'])
print(sales_data_copy.dtypes)

sales_data_copy['sales'] = sales_data_copy['price']*sales_data_copy['quantity']
sales_data_copy = sales_data_copy.drop(['price', 'quantity', 'product'], axis=1)
print(sales_data_copy.head())

sales_data_copy.to_csv('pink_morsels_sales_data.csv', index=False)