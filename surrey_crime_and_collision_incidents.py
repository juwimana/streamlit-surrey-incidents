import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

#import the data from Github URL
ccc19 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202019', sep='\t')
ccc18 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202018',sep ='\t')
ccc17 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202017',sep ='\t')
ccc16 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202016',sep='\t')
ccc15 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202015',sep='\t')
ccc14 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202014',sep='\t')
ccc13 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202013',sep='\t')
ccc12 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202012',sep='\t')
ccc11 = pd.read_csv('https://raw.githubusercontent.com/juwimana/Surrey-Crime-and-Collision-Incidents/main/Crime%20and%20Collision%20Incidents%202011',sep='\t')
csv_files = [ccc12, ccc13, ccc14, ccc15, ccc16, ccc17, ccc18, ccc19]
data = ccc11.append(csv_files)
raw_data = ccc11.append(csv_files)

df_year = pd.DataFrame()
df_year = pd.crosstab(data["INCIDENT_TYPE"],data["YEAR"],margins=True,margins_name="Total")

df_month = pd.DataFrame()
df_month = pd.crosstab(data["INCIDENT_TYPE"],data["MONTH"],margins=True,margins_name="Total",\
                       normalize="all")

st.title("Surrey Crime and Collision Incident 2014-19 Analysis")

#Which incident type occured most in the past eight years (2011-19) in Surrey
year = st.selectbox("Year:",(2011, 2012, 2013, 2014, 2015, 2016, 2017,\
					 2018, 2019))
st.write(f"{year} Incident Frequency")

fig1, ax1 = plt.subplots(figsize=(20,10))
ax1 = sns.countplot(x=data[data["YEAR"]==year]["INCIDENT_TYPE"])
ax1.set_xlabel("Incident Type")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

incident = st.selectbox("Incident:",list(data["INCIDENT_TYPE"].unique()))
st.write(f"{year} {incident} Incident Frequency")
data2 = data[data["YEAR"]==year]

fig, ax = plt.subplots(figsize=(20,10))
ax = sns.countplot(x=data2[data2["INCIDENT_TYPE"]==incident]["MONTH"])
ax.set_ylabel("Frequency")
ax.set(xticklabels=["January", "February", "March", "April", "May", "June",\
	  "July", "August","September", "October", "November", "December"])
st.pyplot(fig)






