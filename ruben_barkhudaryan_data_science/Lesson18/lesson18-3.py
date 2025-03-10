print("Pandas: How to read write files")
print("Working with xml files")

import pandas as pd
from io import StringIO

xml = """<?xml version="1.0" encoding="UTF-8" ?>
<bookstore>
    <book category="cooking">
        <title lang="en"> Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>

    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J.K. Rowling</author>
        <year>2005</year>
        <price>25.75</price>
    </book>
    
    <book category="web">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>40.50</price>
    </book>
</bookstore>
"""

filepath = "dataset/xml/books.xml"

with open(filepath, "w") as f:
    f.write(xml)

with open(filepath, "r") as f:
    df = pd.read_xml(StringIO(f.read()))

print(df)
