#!/usr/bin/env python
# coding: utf-8

# In[116]:


import pandas as pd


# In[118]:


#Load the spreadhsheet
new_path = r"C:\Users\PC\Documents\Python Codes\Modules\Incentives\Top Spotify Music Incentives\spotify-2023-(uncleaned).csv"

dataset = pd.read_csv(new_path, encoding='cp1252')


# In[120]:


dataset


# In[122]:


#Check for any missing values
dataset.isnull().any() #This will display True for any columns that contains an empty entry


# #### Columns 'in_shazam_charts' and 'key' appears to contain missing values

# In[125]:


#Check for specific rows on which the columns becomes null or does not contain any value
dataset[dataset['in_shazam_charts'].isna()==1]


# In[127]:


#Just fill up the missing entries with 0 so at least no alteration to the data was done
dataset['in_shazam_charts'] = dataset['in_shazam_charts'].fillna(0)


# In[129]:


#While fill up the songs with no key with just N/A
dataset['key'] = dataset['key'].fillna('N/A')


# In[131]:


#Check if the missing values were properly replaced
check = dataset.iloc[727] 
print(check)


# In[133]:


# Check for duplicate songs with the same song name and artist name
duplicate_songs = dataset[dataset.duplicated(subset=['track_name', 'artist(s)_name'], keep=False)]

duplicate_songs_list = duplicate_songs.drop_duplicates()

duplicate_songs_list


# In[135]:


duplicate_songs_list = duplicate_songs_list.drop_duplicates()


# In[137]:


# Remove duplicates specifically targetted on 'track_name' and 'artist(s)_name' columns and keep only the first occurrence
cleaned_dataset = dataset.drop_duplicates(subset=['track_name', 'artist(s)_name'], keep='first')

cleaned_dataset


# In[147]:


#For further verification if all duplicates have been removed
cleaned_dataset.duplicated(subset=['track_name', 'artist(s)_name']).any()


# In[149]:


# Save the cleaned dataframe onto a new csv file
cleaned_dataset.to_csv(r"C:\Users\PC\Documents\Python Codes\Modules\Incentives\Top Spotify Music Incentives\Spotify_2023_(Cleaned).csv", index=False, encoding='cp1252')

