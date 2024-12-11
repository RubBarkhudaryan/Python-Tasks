print("Pandas: How to read write files")
print("Working with xml files")

import numpy as np
import pandas as pd

geom_df = pd.DataFrame(
    {
        "shape": ["square", "circle", "triangle"],
        "degrees": [360, 360, 180],
        "sides": [4, np.nan, 3],
    }
)

print(geom_df.to_xml())
