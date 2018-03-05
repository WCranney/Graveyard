
# coding: utf-8

# # Standard

# In[145]:

import pandas as pd


# In[146]:

import string


# In[147]:

import re


# In[148]:

TRAIN_FILE = "train.csv"


# In[149]:

# read data
train = pd.read_csv(TRAIN_FILE)


# In[150]:

text = train["comment_text"]
trunc = text.iloc[:100]


# In[151]:

# convert comment text to lowercase
text = text.apply(lambda x: x.lower())


# In[152]:

# create translation table, all punctuation mapped to None
#table = str.maketrans('', '', string.punctuation)


# In[153]:

# strip comment text of punctuation
#text = text.apply(lambda x: x.translate(table))


# In[154]:

# replace all whitespace with a single space
#text = text.apply(lambda x: re.sub( '\s+', ' ', x).strip())


# In[ ]:

tokens = []


# In[ ]:

def extract_to_dictionary(comment, dictionary):
    for word in comment.split():
        if word not in dictionary:
            dictionary.append(word)

text.apply(extract_to_dictionary, dictionary=tokens)


# In[ ]:

print(tokens)

