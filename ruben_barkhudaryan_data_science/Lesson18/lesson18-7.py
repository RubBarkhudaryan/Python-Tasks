print("Pandas: How to read write files")
print("Working with xml files")

import pandas as pd

filepath = "dataset/xml/books.xml"

df = pd.read_xml(filepath, xpath="//book[year=2005]")
print(df)
