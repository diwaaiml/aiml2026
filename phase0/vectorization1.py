import numpy as np
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([10, 20, 30, 40, 50])
# # c = []
# # for i in range(len(a)):
# #     c.append(a[i] + b[i])
# # print(c)
# # c = a + b
# # print(c)
# # a1=[22,60,100,10]
# print(a * 2)
# print(a ** 2)
# print(np.sqrt(a))

# x = np.array([1, 5, 10, 15])
# mask = x > 5
# [False, False, True, True]
# print(np.where(x>6,x,"Not"))
# [10, 15]

# a = np.array([1, 2, 3])
# b = np.array([[10], [20], [30]])

# print(a + b)

import pandas as pd

df = pd.DataFrame({"price": [100, 200, 300]})

df["price_with_tax"] = df["price"] * 1.2

print(df)

for i in range(len(df)):
    df.loc[i, "price_with_tax"] = df.loc[i, "price"] * 1.2

print(df)
print(df.index)