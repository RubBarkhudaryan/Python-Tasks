print("Pandas: How to read write files")
print("Working with xml files")

import pandas as pd

df = pd.read_xml("https://www.w3schools.com/xml/books.xml")

print(df)
