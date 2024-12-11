print("Data Selection in DataFrame")
print("dataframe as dictionary")
import numpy as np
import pandas as pd
area = pd.Series({'California': 423967, 'Texas': 695662,
 'New York': 141297, 'Florida': 170312,
 'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
 'New York': 19651127, 'Florida': 19552860,
 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
##print(data)
##print(data['area'])
##print(data['pop'])
##print(data.area)
##print(data.pop)
##print(data.area is data['area'])
##print(data.pop is data['pop'])
data['density']=data['pop']/data['area']
print(data)
