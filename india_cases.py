import urllib
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


df = pd.read_csv('WHO-COVID-19-global-data.csv')
df_india = df[df.Country == 'India']

#plot()
world_date = df_india.loc[(df_india["Date_reported"] >= '2021-02-01') & (df_india["Date_reported"] <= '2021-02-31')]
x=world_date["Date_reported"]
y=world_date["New_deaths"]
z=world_date["New_cases"]
x = np.arange(len(x))
fig, ax = plt.subplots()
graph1=plt.plot(x,y,color='red', linestyle='dotted', linewidth = 1,marker='o', markerfacecolor='red', markersize=2,label="deaths")
graph2=plt.plot(x,z,color='blue', linestyle='dotted', linewidth = 1,marker='*', markerfacecolor='blue', markersize=7,label="cases")
plt.xlabel("Feb 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.ylabel("New Death's And Cases's In Feb 2021", fontname="Gabriola", fontsize=18)
plt.title("India's Covid Situation In February  2021",fontname='Franklin Gothic Medium', fontsize=18,y=1.10)
ax.set_xticks(x)
fig.tight_layout()
plt.legend()
plt.grid(color = 'g', linestyle = '--', linewidth = 0.5)
plt.show()


#subplot(2,1,1)
#subplot(2,1,2)
world_date = df_india.loc[(df_india["Date_reported"] >= '2021-02-01') & (df_india["Date_reported"] <= '2021-02-31')]
x=world_date["Date_reported"]
y=world_date["New_deaths"]
z=world_date["New_cases"]
x = np.arange(len(x))
fig, ax = plt.subplots()
plt.subplot(2, 1, 1)
graph2=plt.plot(x,z,color='blue', linestyle='dotted',linewidth = 1,marker='*', markerfacecolor='blue', ms=7,label="cases")
plt.ylabel("Cases's", fontname="Gabriola", fontsize=18)
plt.grid(color='g',linestyle = '--', linewidth = 0.6)
plt.legend()
plt.subplot(2, 1, 2)
graph1=plt.plot(x,y,color='red', linestyle='dotted',linewidth = 1,marker='o', markerfacecolor='red', ms=5,label="deaths")
plt.xlabel("feb 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.ylabel("Death's", fontname="Gabriola", fontsize=18)
fig.tight_layout()
plt.legend()
plt.grid(color = 'b', linestyle = '--', linewidth = 0.5)
plt.suptitle("India's Covid Situation In February 2021",fontname='Franklin Gothic Medium', fontsize=18,y=1.10)
plt.show()



#subplot(1,2,1)
#subplot(1,2,2)
world_date = df_india.loc[(df_india["Date_reported"] >= '2021-02-01') & (df_india["Date_reported"] <= '2021-02-31')]
x=world_date["Date_reported"]
y=world_date["New_deaths"]
z=world_date["New_cases"]
x = np.arange(len(x))
fig, ax = plt.subplots()
plt.subplot(1, 2, 1)
graph2=plt.plot(x,z,color='blue', linestyle='dotted',linewidth = 1,marker='*', markerfacecolor='blue', ms=7,label="cases")
plt.ylabel("Cases's", fontname="Gabriola", fontsize=18)
plt.xlabel("feb 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.grid(color='g',linestyle = '--', linewidth = 0.6)
plt.legend()
plt.subplot(1, 2, 2)
graph1=plt.plot(x,y,color='red', linestyle='dotted',linewidth = 1,marker='o', markerfacecolor='red', ms=5,label="deaths")
plt.xlabel("feb 2021 (day's)", fontname="Gabriola", fontsize=18)
plt.ylabel("Death's", fontname="Gabriola", fontsize=18)
fig.tight_layout()
plt.legend()
plt.grid(color = 'b', linestyle = '--', linewidth = 0.5)
plt.suptitle("India's Covid Situation In February 2021",fontname='Franklin Gothic Medium', fontsize=18,y=1.10)
plt.show()
