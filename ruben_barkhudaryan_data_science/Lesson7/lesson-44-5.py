print("Dataframe as specialized dictionary")
import numpy as np
import pandas as pd

area_dict={'California': 423967, 'Texas': 695662,
 'New York': 141297, 'Florida': 170312, 'Illinois': 149995}
area=pd.Series(area_dict)
population_dict = {'California': 38332521,
 'Texas': 26448193,
 'New York': 19651127,
 'Florida': 19552860,
 'Illinois': 12882135}
population = pd.Series(population_dict)
print(pd.DataFrame(population,columns=['population']))

data=[{'a':i,'b':2*i}
      for i in range(3)]
print(pd.DataFrame(data))

print(pd.DataFrame([{'a':1,'b':2},{'b':3,'c':4}]))
      
