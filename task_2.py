import pandas as pd
from main import data

df = pd.json_normalize(data, 'products', ['order_id', 'warehouse_name', 'highway_cost'])

df['income'] = df['price'] * df['quantity']
df['expenses'] = df['highway_cost'] * df['quantity']

grouped_df = df.groupby('product').agg({
    'quantity': 'sum',
    'income': 'sum',
    'expenses': 'sum',
}).reset_index()

grouped_df['profit'] = grouped_df['income'] - grouped_df['expenses']

print(grouped_df)



# grouped_df = df.groupby(['product'])[['quantity']].sum().reset_index()
# print(grouped_df)

