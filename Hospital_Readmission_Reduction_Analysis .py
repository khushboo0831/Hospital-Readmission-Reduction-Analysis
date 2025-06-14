#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


data=pd.read_csv("Hospital_Readmissions_Reduction_Program (2).csv")
data.head()


# In[11]:


data.describe()


# In[12]:


data.info()


# In[13]:


data.isnull().sum()


# In[14]:


np.shape(data)


# # hospital column

# In[15]:


#total different count of hospital
data["Hospital Name"].value_counts().shape


# In[16]:


data["Number of Readmissions"].value_counts()  # many of the data is missing


# In[17]:


data["Number of Readmissions"]=data["Number of Readmissions"].replace("Not Available",0)


# In[18]:


data["Number of Readmissions"]=data["Number of Readmissions"].replace("Too Few to Report",0)


# In[19]:


data["Number of Readmissions"]=data["Number of Readmissions"].astype(int)


# In[20]:


data.groupby("Hospital Name")["Number of Readmissions"].mean().sort_values(ascending=False) #mean of readmission in particular hospital


# In[21]:


plt.figure(figsize=(16,10))
plots=data.groupby("Hospital Name")["Number of Readmissions"].mean().sort_values(ascending=False)[:10].plot(kind="bar")
for bar in plots.patches:  
    plots.annotate(format(bar.get_height(), '.2f'), 
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')


# In[22]:


data["Number of Discharges"].value_counts()


# In[15]:


data["Number of Discharges"]=data["Number of Discharges"].replace("Not Available",0)


# In[23]:


data.groupby("Hospital Name")["Number of Readmissions"].mean().sort_values(ascending=False)


# In[24]:


plt.figure(figsize=(16,10))
plots=data.groupby("Hospital Name")["Number of Readmissions"].mean().sort_values(ascending=False)[:10].plot(kind="bar")
for bar in plots.patches:  
    plots.annotate(format(bar.get_height(), '.2f'), 
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')


# In[25]:


data["State"].value_counts()


# In[26]:


data["Measure Name"]=data["Measure Name"].str.split("READM-30-").str[1]   #showing disease


# In[27]:


data["Measure Name"].value_counts()


# In[28]:


data.groupby("Measure Name")["Number of Readmissions"].mean()


# In[29]:


l=data.groupby("Measure Name")["Number of Readmissions"].mean().reset_index()
l


# In[30]:


plt.figure(figsize=(16,10))
plots=sns.barplot(x=l["Measure Name"],y=l["Number of Readmissions"])
for bar in plots.patches:  
    plots.annotate(format(bar.get_height(), '.2f'), 
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')


# In[31]:


#pie chart for above graph and data
plt.figure(figsize=(16,10))
data.groupby("Measure Name")["Number of Readmissions"].mean().plot(kind="pie",autopct="%1.1f%%")
plt.legend(title="Number Of Readmission",loc="upper right")


# In[32]:


data["Number of Discharges"].dtypes


# In[35]:


data["Number of Discharges"] = data["Number of Discharges"].replace("Not Available", 0)
data["Number of Discharges"] = data["Number of Discharges"].astype(int)


# In[ ]:





# In[36]:


data["Number of Discharges"]=data["Number of Discharges"].astype(int)


# In[37]:


dis=data.groupby("Measure Name")["Number of Discharges"].mean().reset_index()
dis


# In[38]:


plt.figure(figsize=(16,10))
plots=sns.barplot(x=dis["Measure Name"],y=dis["Number of Discharges"])


for bar in plots.patches:  
    plots.annotate(format(bar.get_height(), '.2f'), 
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')


# In[39]:


#pie chart for above graph and data
plt.figure(figsize=(16,10))
data.groupby("Measure Name")["Number of Discharges"].mean().plot(kind="pie",autopct="%1.1f%%")
plt.legend(title="Number of Dischargesn",loc="upper right")


# In[40]:


data["Predicted Readmission Rate"].value_counts()


# In[41]:


data["Predicted Readmission Rate"]=data["Predicted Readmission Rate"].replace("Not Available",0)


# In[42]:


data["Expected Readmission Rate"].value_counts()


# In[43]:


data["Expected Readmission Rate"]=data["Expected Readmission Rate"].replace("Not Available",0)


# In[44]:


data["Number of Readmissions"]=data["Number of Readmissions"].astype(float)


# In[45]:


data["Predicted Readmission Rate"]=data["Predicted Readmission Rate"].astype(float)


# In[46]:


plt.figure(figsize=(16,10))
sns.kdeplot(data["Predicted Readmission Rate"],label="Predicted Readmission Rate")
sns.kdeplot(data["Number of Readmissions"],color="red",label="Actual Readmission rate")   #almost same
plt.legend()


# In[47]:


data["Expected Readmission Rate"]=data["Expected Readmission Rate"].astype(float)


# In[48]:


plt.figure(figsize=(16,10))
sns.scatterplot(x=data["Expected Readmission Rate"], y=data["Predicted Readmission Rate"], color='purple')


# In[49]:


plt.figure(figsize=(16,10))
sns.scatterplot(x=data["Number of Readmissions"],y=data["Predicted Readmission Rate"])
plt.plot([data['Number of Readmissions'].min(), data['Number of Readmissions'].max()],
         [data['Number of Readmissions'].min(), data['Number of Readmissions'].max()],
         color='red')
#scatter show relation bw re and pre
#if perfect prediction will be there than point will align with the line 
#these shows error


# In[50]:


plt.figure(figsize=(16,10))
sns.scatterplot(x=data["Expected Readmission Rate"],y=data["Predicted Readmission Rate"],color="red")
plt.plot([data['Number of Readmissions'].min(), data['Number of Readmissions'].max()],
         [data['Number of Readmissions'].min(), data['Number of Readmissions'].max()],
         color='blue')


# In[52]:


numeric_data = data.select_dtypes(include=['number'])


# In[64]:


plt.figure(figsize=(16, 10))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
plt.show()


# In[65]:


data.columns


# In[66]:


sns.boxplot(data["Number of Discharges"])


# In[56]:


sns.boxplot(data["Predicted Readmission Rate"])


# In[ ]:





# In[57]:


data["Expected Readmission Rate"]=data["Expected Readmission Rate"].astype(float)


# In[58]:


sns.boxplot(x=data["Expected Readmission Rate"])


# In[59]:


sns.boxplot(data["Number of Readmissions"])


# In[60]:


read=data.groupby(["Measure Name","State"])["Number of Readmissions"].sum().sort_values(ascending=False).iloc[:20].reset_index()
read   #for each state highest number of measure with  readmission rate


# In[61]:


disch=data.groupby(["Measure Name","State"])["Number of Discharges"].sum().sort_values(ascending=False).iloc[:20].reset_index()
disch  #for each state highest number of measure name with discharge


# In[62]:


#state wise readmission avg
stat_read=data.groupby("State")["Number of Readmissions"].mean().sort_values(ascending=False).reset_index()
stat_read


# In[63]:


plt.figure(figsize=(16,10))
plots=sns.barplot(x=stat_read["State"],y=stat_read["Number of Readmissions"])
for bar in plots.patches:  
    plots.annotate(format(bar.get_height(), '.1f'), 
                   (bar.get_x() + bar.get_width() / 2, 
                    bar.get_height()), ha='center', va='bottom',
                   size=15, xytext=(0, 8),
                   textcoords='offset points',rotation=90)


# In[67]:


from sklearn.metrics import mean_absolute_error

print("Mean Absolute error for expected and predicted Readmission Rate:",mean_absolute_error(data["Number of Readmissions"],data["Predicted Readmission Rate"]))


# In[68]:


import scipy.stats as stats


# In[69]:


#statistic for predicted readmission
print("For Predicted Readmission")
print(data["Predicted Readmission Rate"].mean())
print(data["Predicted Readmission Rate"].std())

#for number od readmission
print("For Number of readmission")
print(data["Number of Readmissions"].mean())
print(data["Number of Readmissions"].std())


# In[70]:


#t- test for actual and predicted
#H0=there is no difference between actual and predicted readmission
#H1=there is a difference between actual and predicted value

#t-test using scipy library
t_value,p_value=stats.ttest_rel(data["Number of Readmissions"],data["Predicted Readmission Rate"])
print("T_Value :",t_value)
print("p_value :",p_value)

if(p_value < .05):
    print("Reject the Null Hypothesis ")
else:
    print("Accept the Null Hypothesis")


# In[74]:


# since the p value is less than 0.05 than we will reject the null hypothesis so we can see
#that there is a difference between actual and predicted value


# In[ ]:





# In[ ]:





# In[ ]:




