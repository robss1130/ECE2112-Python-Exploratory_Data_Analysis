#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### This version of notebook serves as a laboratory for experimenting with codes as well as just gathering data, by that I mean just getting some values that I will be using for setting up the graph for the final finish of the code.###

# In[14]:


# Load the spreadsheet
file_path = r"C:\Users\PC\Documents\Python Codes\Modules\Incentives\Top Spotify Music Incentives\spotify-2023.csv" #Originally was C:\Users\Simon\Documents\Codes\Project\Top Spotify Music Incentives\spotify-2023.csv 
data = pd.read_csv(file_path, encoding='cp1252')


# In[40]:


#Use .shape to get number of row and column respectively and assign their values to a variable
row_count, column_count = data.shape


# In[30]:


#get mean, median, and standard deviation
mean_values = numeric_data.mean()
median_values = numeric_data.median()
std_values = numeric_data.std()

print("Mean of Numeric Columns:\n", mean_values)
print("\nMedian of Numeric Columns:\n", median_values)
print("\nStandard Deviation of Numeric Columns:\n", std_values)


# In[ ]:




