print("Pandas: How to read write files")
print("Working with xml files")

import pandas as pd

filepath = "dataset/xml/books.xml"

df = pd.read_xml(filepath, elems_only=True)
print(df)

print()

df = pd.read_xml(filepath, attrs_only=True)
print(df)
