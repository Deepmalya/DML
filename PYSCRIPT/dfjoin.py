#Script dfjoin.py
#This script joins two dataframes based on key values and prnts the result,
# also displays the result of concatanation of two dataframes 

import numpy as np
import pandas as pd

left_frame = pd.DataFrame({'key': range(5),
                            'left_value': ['a', 'b', 'c','d','e']})
right_frame = pd.DataFrame({'key': range(2,7),
                            'right_value': ['f', 'g', 'h','i','j']})

print( left_frame)
print('\n')
print( right_frame)
print('\n')
joined_frame = pd.merge(left_frame, right_frame, on='key', how='inner')
print(joined_frame)
combined_frame = pd.concat([left_frame, right_frame])
print(combined_frame)
