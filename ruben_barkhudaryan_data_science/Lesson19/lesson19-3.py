print("Working with Datatypes")

print("Compressing the files")

import pandas as pd

# from sqlalchemy import create_engine

df = pd.read_csv("dataset/csv/data.csv", index_col=0, skiprows=(1, 20, 2))

# df = pd.read_csv("dataset/csv/data.csv", usecols=["COUNTRY", "AREA"])

# df = pd.read_csv("dataset/csv/data.csv", index_col=0, usecols=[0, 1, 3])

# engine = create_engine("sqlite:///dataset/sql/data.db", echo=False)

# df = pd.read_sql(
#     "dataset/sql/data.db", con=engine, index_col="ID", columns=["COUNTRY", "AREA"]
# )

print(df)



