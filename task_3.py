import pandas as pd
from main import data

df = pd.json_normalize(data, 'products', ['order_id', 'warehouse_name', 'highway_cost'])

df['income'] = df['price'] * df['quantity']
df['expenses'] = df['highway_cost'] * df['quantity']

order_profit_df = df.groupby('order_id')[['income', 'expenses']].sum().reset_index()
order_profit_df['order_profit'] = order_profit_df['income'] + order_profit_df['expenses']
print(order_profit_df[['order_id', 'order_profit']])

average_profit = order_profit_df['order_profit'].mean()
print(f"\nСредняя прибыль c заказов: {average_profit:.3f}")