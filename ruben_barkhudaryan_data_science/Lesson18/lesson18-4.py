print("Pandas: How to read write files")
print("Working with xml files")

import pandas as pd
from io import BytesIO

filepath = "dataset/xml/books.xml"

with open(filepath, "rb") as f:
    bio = BytesIO(f.read())

df = pd.read_xml(bio)
print(df)
