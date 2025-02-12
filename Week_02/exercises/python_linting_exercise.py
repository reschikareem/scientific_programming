# Import libraries
import pandas as pd
import numpy as np

# Initialize data of lists
data =                pd.DataFrame({'Name': ['tom', 'nick', 'krish', 'jack']          ,
                     'Age': [20, 21, 19, 18]})

# Create DataFrame
df = pd.DataFrame(                  data)       
print(       type(df)               )

# Print the output
print(df.head())