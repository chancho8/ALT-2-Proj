import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('2020-Make-and-model-data-(xls).xlsx')

pd.set_option("display.max_columns", 60)
##print(pd.get_option("display.max_columns"))
##print(df.columns.tolist())

birthYear = df['Year Of Birth'].to_numpy()
failPctg = df['FAIL %'].to_numpy()
passPctg = df['PASS %'].to_numpy()

fig, ax = plt.subplots()
ax.scatter(birthYear,failPctg)

plt.show()


sum = 0
for i in range(birthYear.size):
    if failPctg[i] >= 80:
        sum += 2020 - birthYear[i]
mean = sum/(birthYear.size)
print(mean)

