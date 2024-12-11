import pandas as pd

data = [1, 2, 3, 4, 5, 6, 7]

series = pd.Series(data=data)

res_list = series.to_list()

print(series)

print(res_list)
