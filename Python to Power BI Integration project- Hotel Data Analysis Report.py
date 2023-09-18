#!/usr/bin/env python
# coding: utf-8

# # Hotel Data Analaysis Report
# You boss wants a report to understand the relationship between average daily rate for hotels and the lead time before booking.
# 
# 1.You need to compile a collection of excel sheets into a single dataset and filter out cancellations
# 
# 2.Create a simple linear regression between these two variables

# In[112]:


# bring in our libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress,pearsonr


# In[2]:


#bring in our dataset 2018 sheet
df2018=pd.read_excel("C:/Users/saikr/OneDrive/Desktop/Power BI Enterprise DNA/Copy of SQL Project 1. Hotel_Revenue_Historical_Full.xlsx",
                sheet_name="2018")

#bring in our dataset 2019 sheet 
df2019=pd.read_excel("C:/Users/saikr/OneDrive/Desktop/Power BI Enterprise DNA/Copy of SQL Project 1. Hotel_Revenue_Historical_Full.xlsx",
                sheet_name="2019")

#bring in our dataset 2020 sheet
df2020=pd.read_excel("C:/Users/saikr/OneDrive/Desktop/Power BI Enterprise DNA/Copy of SQL Project 1. Hotel_Revenue_Historical_Full.xlsx",
                sheet_name="2020")


# In[3]:


full_dataset=pd.concat([df2018,df2019,df2020],ignore_index=True)  #using concat to append 3 datasets. 
#axis=0 by default(check by pressing shift+tab inside bracket. we append so length is increased so axis=0


# In[4]:


full_dataset.tail(5)


# In[5]:


full_dataset.info()


# In[6]:


full_dataset.columns


# In[7]:


# filter out cancellations rows but before that lets ee distribution of cancellations
sns.histplot(full_dataset['is_canceled'])


# In[8]:


full_dataset['is_canceled'].value_counts(normalize=True)  #count the number of cancellations and non-cancellations for checking distribution. Normalise=true gives cancellation percentage rather than number) 


# In[9]:


full_dataset['is_canceled']==1  #double equal to would mean equal to so each row is checked against 
#whether is_canceled is equal to 1. single '=' would mean assignment .so we need to use double '='


# In[10]:


full_dataset['is_canceled']!=1  # checking only the non-canceled bookings


# In[11]:


filtered_data=full_dataset[full_dataset['is_canceled']!=1]  #put the filter above for rows with tickets not cancelled inside the full_dataset to get all rwos for the tickets not canceled


# In[12]:


filtered_data.info()


# In[14]:


#univariate and bivariate analysis

sns.distplot(filtered_data['lead_time' ])


# In[15]:


sns.distplot(filtered_data['adr' ])


# In[20]:


plt.figure(figsize=(6,6))
sns.boxplot(data=filtered_data,y='lead_time',x='hotel')  #showfliers=FALSE removes outliers
plt.title(f"The mean is {filtered_data['lead_time'].mean():.2f}");


# In[22]:


plt.figure(figsize=(6,6))
sns.violinplot(data=filtered_data,y='lead_time',x='hotel')  #showfliers=FALSE removes outliers\

City_mean=filtered_data[filtered_data['hotel']=='City Hotel']['lead_time'].mean()
Resort_mean=filtered_data[filtered_data['hotel']=='Resort Hotel']['lead_time'].mean()
plt.title(f"The mean is {filtered_data['lead_time'].mean():.2f} , Resort_mean is {Resort_mean:.2f} and City_mean is {City_mean:.2f}");


# In[23]:


plt.figure(figsize=(6,6))
sns.boxenplot(data=filtered_data,y='lead_time',x='hotel')  #showfliers=FALSE removes outliers\

City_mean=filtered_data[filtered_data['hotel']=='City Hotel']['lead_time'].mean()
Resort_mean=filtered_data[filtered_data['hotel']=='Resort Hotel']['lead_time'].mean()
plt.title(f"The mean is {filtered_data['lead_time'].mean():.2f} , Resort_mean is {Resort_mean:.2f} and City_mean is {City_mean:.2f}");


# In[ ]:


plt.figure(figsize=(6,6))
sns.violinplot(data=filtered_data,y='lead_time',x='hotel')  #showfliers=FALSE removes outliers\

City_mean=filtered_data[filtered_data['hotel']=='City Hotel']['lead_time'].mean()
Resort_mean=filtered_data[filtered_data['hotel']=='Resort Hotel']['lead_time'].mean()
plt.title(f"The mean is {filtered_data['lead_time'].mean():.2f} , Resort_mean is {Resort_mean:.2f} and City_mean is {City_mean:.2f}");


# In[ ]:


plt.figure(figsize=(6,6))
sns.violinplot(data=filtered_data,y='lead_time',x='hotel')  #showfliers=FALSE removes outliers\

City_mean=filtered_data[filtered_data['hotel']=='City Hotel']['lead_time'].mean()
Resort_mean=filtered_data[filtered_data['hotel']=='Resort Hotel']['lead_time'].mean()
plt.title(f"The mean is {filtered_data['lead_time'].mean():.2f} , Resort_mean is {Resort_mean:.2f} and City_mean is {City_mean:.2f}");


# In[ ]:


sns.histplot(filtered_data[filtered_data['hotel']=='City_Hotel'])['lead_time']


# In[24]:


filtered_data[filtered_data['hotel']=='Resort Hotel']['lead_time']


# In[25]:


[filtered_data['hotel']=='Resort Hotel']


# In[26]:


filtered_data[filtered_data['hotel']=='Resort Hotel']


# In[29]:


#dist plot of rows with hotel==city_hotel

sns.distplot(filtered_data[filtered_data['hotel']=='City Hotel']['lead_time'])


# In[32]:


# dist plot for lead time booking (how many days in advance customers booked) for Resort Hotel

sns.distplot(filtered_data[filtered_data['hotel']=='Resort Hotel']['lead_time'])


# In[33]:


# laying the lead time for city hotel rows and resort hotel rows on top of each other
sns.distplot(filtered_data[filtered_data['hotel']=='City Hotel']['lead_time'])
sns.distplot(filtered_data[filtered_data['hotel']=='Resort Hotel']['lead_time'])


# In[45]:


# dist plot for city hotel rows for avg dialy rate (adr)

sns.distplot(filtered_data[filtered_data['hotel']=='City Hotel']['adr'])


# In[46]:


sns.distplot(filtered_data[filtered_data['hotel']=='Resort Hotel']['adr'])


# In[70]:


# combining adr for city hotel and resort hotel. showing the legends and adding the mean.

sns.distplot(filtered_data[filtered_data['hotel']=='City Hotel']['adr'],label='City Hotel')
sns.distplot(filtered_data[filtered_data['hotel']=='Resort Hotel']['adr'],label='Resort_Hotel')
city_hotel_adr_mean=filtered_data[filtered_data['hotel']=='City Hotel']['adr'].mean()
resort_hotel_adr_mean=filtered_data[filtered_data['hotel']=='Resort Hotel']['adr'].mean()
plt.axvline(resort_hotel_adr_mean,color='orange',linestyle='--',label='adr for resort hotels')
plt.axvline(city_hotel_adr_mean,color='blue',linestyle='--',label='adr for city hotels')

plt.legend()
plt.title(f"The adr combined is {filtered_data['adr'].mean():.2f} , Resort hotel adr is {resort_hotel_adr_mean:.2f} and city hotel adr is {city_hotel_adr_mean:.2f}")


plt.savefig('ADR_distribution.png')


# In[71]:


city_mean=filtered_data[filtered_data['hotel']=='City Hotel']['adr'].mean()


# In[72]:


city_mean


# In[76]:


# bivariate analysis and linear regression

#regplot is a  regression plot. here we dont see a strong relationship between adr and lead_Time
sns.regplot(data=filtered_data,y='adr',x='lead_time',line_kws={'color':'red'})


# In[82]:


#joint plot-->this gives us the distribution and plot

sns.jointplot(data=filtered_data,y='adr',x='lead_time',kind='kde',hue='hotel')


# In[81]:


sns.jointplot(data=filtered_data,y='adr',x='lead_time',kind='reg',joint_kws={'line_kws':{'color':'red'}})


# In[84]:


sns.jointplot(data=filtered_data,y='adr',x='lead_time',kind='hex')


# In[85]:


#linear Regression
# the output shows it is a bad model. R value is not significant. if 1 day of lead time increases, model shows cost is expected to go up 
#by 0.0183 than lead time with 1 day less. so not much adr change with additonal lead time increase 
linregress(filtered_data['lead_time'],filtered_data['adr'])


# In[101]:


#accessing slope output,intercept and r-squared and saving it to variables


slope=linregress(filtered_data['lead_time'],filtered_data['adr'])[0]
intercept=linregress(filtered_data['lead_time'],filtered_data['adr'])[1]
rsquared=linregress(filtered_data['lead_time'],filtered_data['adr'])[2]


# In[102]:


slope


# In[103]:


# passing the values into a dataframe 
regression_table=pd.DataFrame({'Name':['slope','intercept','rsquared'],'Values':[slope,intercept,rsquared]})
regression_table


# In[114]:


#describing the relationship

correlation=pearsonr(filtered_data['adr'],filtered_data['lead_time'])[0]
slope=linregress(filtered_data['lead_time'],filtered_data['adr'])[0]
intercept=linregress(filtered_data['lead_time'],filtered_data['adr'])[0]
regression_table=pd.DataFrame({'Name':['correlation','slope','intercept'],'Coefficients':[correlation,slope,intercept]})


# In[92]:





# In[ ]:




