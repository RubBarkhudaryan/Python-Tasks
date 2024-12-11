print("Numpy structured arrays\n")

import numpy as np


print(np.dtype({"names": ("name", "age", "weight"), "formats": ("U10", "i4", "f8")}))


print(
    np.dtype(
        {
            "names": ("name", "age", "weight"),
            "formats": ((np.str_, 10), int, np.float32),
        }
    )
)

print(np.dtype("S10,i4,f8"))
