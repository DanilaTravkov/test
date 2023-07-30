import pandas as pd
from main import data

# task 4
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None) # раскомментируйте это, чтобы увидеть всю таблицу

df = pd.json_normalize(data, 'products', ['order_id', 'warehouse_name', 'highway_cost'])

df['income'] = df['price'] * df['quantity']
df['expenses'] = df['highway_cost'] * df['quantity']

warehouse_product_df = df.groupby(['order_id', 'warehouse_name', 'product']).agg({
    'quantity': 'sum',
    'income': 'sum',
    'expenses': 'sum',
}).reset_index()

warehouse_product_df['profit'] = warehouse_product_df['income'] + warehouse_product_df['expenses']
warehouse_profit_df = warehouse_product_df.groupby('warehouse_name')['profit'].sum().reset_index()
merged_df = pd.merge(warehouse_product_df, warehouse_profit_df, on='warehouse_name', suffixes=('', '_warehouse'))

merged_df['percent_profit_product_of_warehouse'] = (merged_df['profit'] / merged_df['profit_warehouse']) * 100

result_df = merged_df[['warehouse_name', 'product', 'quantity', 'profit', 'percent_profit_product_of_warehouse']]
print(result_df)

# task 5
df_sorted = merged_df.sort_values(by='percent_profit_product_of_warehouse', ascending=False)

df_sorted['accumulated_percent_profit_product_of_warehouse'] = df_sorted['percent_profit_product_of_warehouse'].cumsum()

print(df_sorted)


# task 6
def categorize(percentage):
    if percentage <= 70:
        return 'A'
    elif percentage > 90:
        return 'C'
    else:
        return 'B'


df_sorted['category'] = df_sorted['accumulated_percent_profit_product_of_warehouse'].apply(categorize)
print(df_sorted)

pd.reset_option('display.max_columns')
pd.reset_option('display.max_rows')  # не нужно, если не стоит set_option
