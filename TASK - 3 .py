#!/usr/bin/env python
# coding: utf-8

# # TASK - 3 

# # THE SPARKS FOUNDATION

# NAME : RISHIKESHAN VEERAVELU
# 

# BATCH : GRIPJAN2021

# #  Topic : Exploratory Data Analysis - Retail..

# ● Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’..
# ● As a business manager, try to find out the weak areas where you can
# work to make more profit. 
# ● What all business problems you can derive by exploring the data?

# # IMPORTING LIBRARIES :

# In[21]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# 
# # IMPORTING DATASET : 

# In[22]:


data = pd.read_csv('C:/Users/datasets/SampleSuperstore.csv')
print(data)


# In[23]:


data.head()


# # EXPLORITARY DATA ANAYSIS (EDA) :

# In[24]:


data.shape


# In[25]:


data.info()


# # Checking the NULL data :

# In[26]:


data.isnull().sum()


# After analysing the data there are no null values in the data. so we can do EDA easily...|

# In[27]:


data.describe()


# In[28]:


data.duplicated().sum()


# Removing the duplicated values from our dataset

# In[29]:


x = data.drop_duplicates()


# In[30]:


print(x)


# In[31]:


x.nunique() #no.of distinct observaton in each coloumns


# In[32]:


data.corr()


# In[33]:


data.columns #old coloumn 


# # Visualization of Data :

# In[34]:


sns.countplot(x=data['Ship Mode'])   


# In[35]:


sns.countplot(x=data['Sub-Category' ])


# In[16]:


#Representing using pie-charts :


# In[36]:


plt.figure(figsize=(16,12))
data['Sub-Category'].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()


# After seeing the piechart "Binders" having the highest value count(15.2%)

# In[37]:


shipping = data.groupby('Ship Mode').sum().sort_values('Sales',ascending=False)
print(shipping)


# After the analysis shipping mode standard class generated the highest revenue profit of Rs.164088.78

# 
# # Buissness facts in this data :

# quality sold and discount also high in standard class.
# 
# Discount and sales price also less in same day coloumns.

# In[38]:


topstate = data.groupby('State').sum().sort_values('Profit',ascending=False)
print(topstate)


# In[20]:


topstate.head


# In[39]:


sns.countplot(x=data['Sub-Category'])

width = 2.90
plt.show()


# In[40]:


sns.countplot(x=data['Region'])  #Graph for the region plot


# In[41]:


region = data.groupby('Region').sum().sort_values('Sales',ascending=False)
print(region)


# According to our analysis in region the west region has high profit. The south region has highest discount.

# In[42]:


sns.countplot(x=data['Segment'])


# In[43]:



segment= data.groupby('Segment').sum().sort_values('Segment',ascending=False)
print(segment)


# "In this output the profit for segment coloumn is consumer of rs.60928.67".
# "The consumer has the larger discount of rs.821"
# 

# In[44]:


sns.countplot(x=data['Category'])


# In[45]:


category= data.groupby('Category').sum().sort_values('Sales',ascending=False)
print(category)


# As per the output the Technology has the highest profit. The office suppies has the highest discount

# # Comparison by sales and profit in sub-category

# In[46]:


data.groupby('Sub-Category')['Sales','Profit'].agg(['sum']).plot.bar()
plt.show()


# # sub category in region wise :

# In[47]:


sns.countplot(x='Sub-Category',hue='Region',data=data)


# In[48]:


plt.figure(figsize = (2,5))
sns.lineplot('Discount','Profit',data = data,color='violet')
plt.show()


# In[49]:


num = data[['Sales','Quantity','Discount','Profit']]


# In[50]:


num


# In[51]:


num = data[['Sales','Quantity','Discount','Profit']]
num.hist(bins=50,figsize=(10,8),color='red')
plt.show()


# In[52]:


sns.pairplot(data,hue='Sub-Category')
figsize=(12,10)


# In[53]:


final = data.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
final[:].plot.bar(color=['Red','black'])
plt.xlabel('sub-category')
plt.ylabel('profit or loss')
plt.show()


# # Conclusion :
Highest sales in phones,chairs,storage,tables,binders have above 20000. Highest profit in fields of copiers,paper and Accessories.

Highest sale and Highest profit comes from Newyork and California..

# # Thankyou.

# In[ ]:




