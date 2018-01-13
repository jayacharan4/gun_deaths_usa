
# coding: utf-8

# In[14]:


import csv
file=open("guns.csv")
csvreader=csv.reader(file)
data=list(csvreader)
headers=data[0]
data=data[1:]
data[:2]
#headers


# In[10]:


years=[]
year_counts=dict()
for each in data:
    years.append(each[1])
for each in years:
    year=each
    if year in year_counts:
        year_counts[year]=year_counts[year]+1
    else:
        year_counts[year]=1
year_counts        
        


# In[13]:


import datetime 
dates=[datetime.datetime(year=int(each[1]),month=int(each[2]),day=1)for each in data]
#dates[:5]


# In[27]:


date_counts={}
for each_date in dates:
    if each_date not in date_counts:
        date_counts[each_date]=0
    else:
        date_counts[each_date]+=1
""""for idx,val in date_counts.items():
    print(val)
    date_counts
"""


# In[29]:


sex_counts=dict()
race_counts=dict()
for each in data:
    sex=each[5]
    if sex in sex_counts:
        sex_counts[sex]+=1
    else:
        sex_counts[sex]=1
for each in data:
    race=each[7]
    if race in race_counts:
        race_counts[race]+=1
    else:
        race_counts[race]=1
sex_counts
race_counts
#Organizing data in dictionaries,with respect to the dates,years,sex and race
#


# In[33]:


file1=open("census.csv")
csvread=csv.reader(file1)
census=list(csvread)
census[:2]


# In[35]:


mapping={
    
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}
race_per_hundredk=dict()
for each_key in race_counts:
    each_value=race_counts[each_key]
    result=(each_value/mapping[each_key])*100000
    race_per_hundredk[each_key]=result
race_per_hundredk


# In[42]:


intents=list()
races=[]
for each_data in data:
    intent=each_data[3]
    intents.append(intent)
    race=each_data[7]
    races.append(race)
homicide_race_counts={}
for i,race in enumerate(races):
    if intents[i]=="Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race]+=1
        else:
            homicide_race_counts[race]=1
race_per_hundredk={}
for key,val in homicide_race_counts.items():
    race_per_hundredk[key]=(val/mapping[key])*100000
    
race_per_hundredk

