import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('finance_liquor_sales.csv')
cn = df.groupby('category_name')
print(cn.first())


bottles_sold = df.groupby(by=['zip_code', ]).agg({'bottles_sold': 'sum'})
plt.scatter(bottles_sold.index, bottles_sold, c=np.random.rand(len(bottles_sold.index), 3))
plt.title('Bottles sold')
plt.xlabel('Zip code')
plt.ylabel('Bottles sold')
plt.show()


total_sales = sum(df['sale_dollars'])
sales = df.groupby(by=['store_name']).agg({'sale_dollars': 'sum'})
sorted_sales = sales.apply(lambda x: x.sort_values(ascending=True))
per_sorted_sales = sorted_sales.apply(lambda x: (x / total_sales) * 100).round(2).tail(15)
p = plt.barh(per_sorted_sales.index, per_sorted_sales.values.flatten(), height=0.7)
plt.title('%Sales by store')
plt.xlabel('%Sales', fontsize=12)
plt.ylabel('Store name', fontsize=1)
plt.bar_label(p, fmt='%.2f')
plt.xlim(right=15)
plt.xlim([0, 20])
plt.show()
