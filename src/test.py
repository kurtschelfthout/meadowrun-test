import numpy as np
import bottleneck as bn

def my_cool_function():
    a = np.array([1, 2, np.nan, 4, 5])
    print(f"I was here {bn.nanmean(a)}")
    return a