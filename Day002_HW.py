#!/usr/bin/env python
# coding: utf-8

# # Python 下載CSV檔案與解析
# 
# 
# * 了解 csv 檔案格式與內容
# * 能夠利用套件存取 csv 格式的檔案
# 
# 

# ## 作業目標
# 
# * 比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異
# 
# * 根據範例檔案的結果：
#     1. 取出班次一的每一個時間
#     2. 將班次一的每一個時間用一種資料型態保存
#     3. 將班次一到五與其所有時間用一種資料型態個別保存
# 

# ### 比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異

# In[4]:


'''
File I/O的輸出結果為一個個的字串
而CSV Reader則將每一列輸出為一個List
'''


# ### 根據範例檔案的結果：
# 
# 1. 取出班次一的每一個時間
# 2. 將班次一的每一個時間用一種資料型態保存
# 3. 將班次一到五與其所有時間用一種資料型態個別保存

# In[5]:


import csv

# 開啟 CSV 檔案
with open('./data/example.csv', newline='',encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row)


# In[39]:



import pandas as pd
pd.set_option('display.max_rows', None)
df=pd.read_csv("./data/example.csv",encoding="utf-8-sig")
print(df)


# In[47]:


# 1. 取出班次一的每一個時間
One=data[['班次1']]
print (One)


# In[58]:


# 2. 將班次一的每一個時間用一種資料型態保存
import numpy as np
One['班次1'].values.tolist()


# In[62]:


# 3. 將班次一到五與其所有時間用一種資料型態個別保存

OnetoFive=data[['班次1','班次2','班次3','班次4','班次5']]
np.array(OnetoFive)
#OnetoFive[0:4].as_matrix()


# In[ ]:




