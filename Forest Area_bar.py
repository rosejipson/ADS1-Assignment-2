# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:19:43 2022

@author: RJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# def read_file(fname):
#     data= pd.read_excel(fname)
#     dtranspose= data.set_index('Country Name').transpose()
#     return data, dtranspose


# #def bar_plot():
    

# data = pd.read_excel("E:/MSc Data Science Assignments/Assignment 2/Forest Area.xls")
# # print(data)

# data=data[['Country Name','Indicator Name','1990','2000','1994','2013','2019','2020']]
# data1= data.set_index('Country Name').transpose()
# print (data1)
# data = data [(data["Country Name"]=="American Samoa") | (data["Country Name"]=="China") | (data["Country Name"]=="Brazil") | (data["Country Name"]=="Italy") | (data["Country Name"]=="Zimbabwe") | (data["Country Name"]=="India")]


# #data2= pd.DataFrame()
# coun_list= ['American Samoa','China','Brazil','Italy','Zimbabwe','India']

# # for i in coun_list:
# #     data2[i]= data1[i]
    
# # data2 = data2.transpose()   
# # print(data2)


# plt.figure(figsize=(25,18))
# ax= plt.subplot(1,1,1)
# x = np.arange(6)
# width= 0.2

# bar1= ax.bar(x, data["1990"],width, label= 1990)
# bar2= ax.bar(x+width, data["1994"],width,label=1994)
# bar3= ax.bar(x+width*2, data["2000"],width,label=2000)

# ax.set_xlabel("Countries")
# ax.set_ylabel('% of land area')
# ax.set_title('Forest Area')
# ax.set_xticks(x, coun_list, rotation=90)
# ax.legend(fontsize=30)
         
# ax.bar_label(bar1, padding=2, rotation=90)
# ax.bar_label(bar2, padding=2, rotation=90)
# ax.bar_label(bar3, padding=2, rotation=90)
# plt.show()         
           


# data=pd.read_excel("E:/MSc Data Science Assignments/Assignment 2/Urban Population.xls")
         
# data=data[['Country Name','Indicator Name','1990','2000','1994','2013','2019','2020']]
# data1= data.set_index('Country Name').transpose()
# print (data1)
# data = data [(data["Country Name"]=="American Samoa") | (data["Country Name"]=="China") | (data["Country Name"]=="Brazil") | (data["Country Name"]=="Italy") | (data["Country Name"]=="Zimbabwe") | (data["Country Name"]=="India")]


# #data2= pd.DataFrame()
# coun_list= ['American Samoa','China','Brazil','Italy','Zimbabwe','India']       
         
# plt.figure(figsize=(25,18))
# ax= plt.subplot(1,1,1)
# x = np.arange(6)
# width= 0.2

# bar1= ax.bar(x, data["1990"],width, label= 1990)
# bar2= ax.bar(x+width, data["1994"],width,label=1994)
# bar3= ax.bar(x+width*2, data["2000"],width,label=2000)

# ax.set_xlabel("Countries")
# ax.set_ylabel('% of land area')
# ax.set_title('Forest Area')
# ax.set_xticks(x, coun_list, rotation=90)
# ax.legend(fontsize=30)
         
# ax.bar_label(bar1, padding=2, rotation=90)
# ax.bar_label(bar2, padding=2, rotation=90)
# ax.bar_label(bar3, padding=2, rotation=90)
# plt.show()                       
         


data=pd.read_excel("E:/MSc Data Science Assignments/Assignment 2/CO2 emission.xls")    

data=data[['Country Name','Indicator Name','1990','2000','1994','2013','2019']]
data1= data.set_index('Country Name').transpose()
data1 = data1.drop(index="Indicator Name")
print (data1)
data = data [(data["Country Name"]=="Mexico") | (data["Country Name"]=="Brazil") | (data["Country Name"]=="Canada") | (data["Country Name"]=="Spain") | (data["Country Name"]=="Finland") | (data["Country Name"]=="Iceland")]

#data2= pd.DataFrame()
coun_list= ['Mexico','Brazil','Canada','Spain','Finland','Iceland']  
   
plt.figure(figsize=(25,18))

plt.figure()
for i in range(len(coun_list)):
    plt.plot(data1.index, data1[coun_list[i]], label=coun_list[i])
plt.title("Head", size=18)
plt.xlabel("Year", size=12)
plt.ylabel("ylabel", size=12)
plt.xticks(rotation=90)
plt.legend(fontsize=5)
plt.savefig("lineplot.png")
plt.show()
         
         
# data=pd.read_excel("E:/MSc Data Science Assignments/Assignment 2/Total Population.xls")             
         
# data=data[['Country Name','Indicator Name','1990','2000','1994','2013','2019','2020']]
# data1= data.set_index('Country Name').transpose()
# data1 = data1.drop(index="Indicator Name")
# print (data1)
# data = data [(data["Country Name"]=="Mexico") | (data["Country Name"]=="Brazil") | (data["Country Name"]=="Canada") | (data["Country Name"]=="Spain") | (data["Country Name"]=="Finland") | (data["Country Name"]=="Iceland")]

# data2= pd.DataFrame()
# coun_list= ['Mexico','Brazil','Canada','Spain','Finland','Iceland']  
     
# plt.figure(figsize=(25,18))       
         
# plt.figure()
# for i in range(len(coun_list)):
#     plt.plot(data1.index, data1[coun_list[i]], label=coun_list[i])
# plt.title("Head", size=18)
# plt.xlabel("Year", size=12)
# plt.ylabel("ylabel", size=12)
# plt.xticks(rotation=90)
# plt.legend(fontsize=6)
# plt.savefig("lineplot.png")
# plt.show()
                  
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         