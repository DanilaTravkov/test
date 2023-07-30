import pandas as pd
import json


with open('./trial_task.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(data, 'products', ['order_id', 'warehouse_name', 'highway_cost'])
grouped_df = df.groupby(['order_id', 'warehouse_name', 'highway_cost'])['quantity'].sum().reset_index()
grouped_df['tarrif_cost'] = grouped_df['highway_cost'] / grouped_df['quantity']
print(grouped_df)


