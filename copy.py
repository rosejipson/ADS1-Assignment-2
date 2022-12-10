# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:35:50 2022

@author: RJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file(fname):
    data = pd.read_excel(fname)
    dtranspose= data.set_index('Country Name').transpose()
    return data, dtranspose
    

coun_list= ['American Samoa','China','Brazil','Italy','Zimbabwe','India']


def filter_bar_data(data):
    data=data[['Country Name','Indicator Name','1990','2000','1994','2013','2019','2020']]
    data = data [(data["Country Name"]=="American Samoa") | 
                 (data["Country Name"]=="China") | 
                 (data["Country Name"]=="Brazil") |
                 (data["Country Name"]=="Italy") | 
                 (data["Country Name"]=="Zimbabwe") |
                 (data["Country Name"]=="India")]
    return data

def filter_line_plot(data):
    data=data[['Country Name','Indicator Name','1990','2000','1994','2013','2019']]
    data =data [(data["Country Name"]=="Mexico") | 
                (data["Country Name"]=="Brazil") | 
                (data["Country Name"]=="Canada") |
                (data["Country Name"]=="Spain") |
                (data["Country Name"]=="Finland") | 
                (data["Country Name"]=="Iceland")]
    return data
    
    
def barplot(data, label1, label2):
    plt.figure(figsize=(25,19))
    ax= plt.subplot(1,1,1)
    x = np.arange(6)
    width= 0.2

    bar1= ax.bar(x, data["1990"],width,label= 1990)
    bar2= ax.bar(x+width, data["1994"], width, label=1994)
    bar3= ax.bar(x+width*2, data["2000"], width, label=2000)
    
    ax.set_xlabel("Country Names", fontsize= 40)
    ax.set_ylabel(label1, fontsize= 40)
    ax.set_title(label2, fontsize=40)
    ax.set_xticks(x, coun_list, fontsize=30, rotation=90)
    ax.legend(fontsize=30)
             
    ax.bar_label(bar1, padding=2, rotation=90, fontsize= 18)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize= 18)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize= 18)
    plt.show()    
     
           
def line_plot(data,label1,label2):
    plt.figure(figsize=(25,10))
    for i in range(len(coun_list)):
        plt.plot(CO2_data1.index,CO2_data1[coun_list[i]], label=coun_list[i])
        plt.title(label2, size=18)
        plt.xlabel("Years", size=12)
        plt.ylabel(label1, size=12)
        plt.xticks(rotation=90)
        plt.legend(fontsize=6)
        plt.savefig("lineplot.png")
        plt.show()
        
      

forest_data, forest_data1 = read_file("Forest Area.xls")
forest_data = filter_bar_data(forest_data)
Urban_data, Urban_data1 = read_file("Urban Population.xls") 
Urban_data = filter_bar_data(Urban_data)


CO2_data, CO2_data1=read_file("CO2 emission.xls")   
CO2_data= filter_line_plot(CO2_data)
Population_data, Population_data1 = read_file("Total Population.xls")             
Population_data= filter_line_plot(Population_data)          


"""
coun_list= ['American Samoa','China','Brazil','Italy','Zimbabwe','India']   
    
plt.figure(figsize=(30,15))
ax= plt.subplot(1,1,1)
x = np.arange(6)
width= 0.2

bar1= ax.bar(x, Urban_data["1990"],width, label= 1990)
bar2= ax.bar(x+width, Urban_data["1994"],width,label=1994)
bar3= ax.bar(x+width*2, Urban_data["2000"],width,label=2000)

ax.set_xlabel("Country Names", fontsize= 40)
ax.set_ylabel(label1, fontsize= 40)
ax.set_title(label2, fontsize= 40)
ax.set_xticks(x, coun_list, rotation=90, fontsize= 30)
ax.legend(fontsize=30)
         
ax.bar_label(bar1, padding=2, rotation=90, fontsize= 15)
ax.bar_label(bar2, padding=2, rotation=90, fontsize= 15)
ax.bar_label(bar3, padding=2, rotation=90, fontsize= 15)
plt.show()                       
"""         


 
coun_list= ['Mexico','Brazil','Canada','Spain','Finland','Iceland'] 
 
"""     
plt.figure(figsize=(25,10))       
         
plt.figure()
for i in range(len(coun_list)):
    plt.plot(Population_data1.index, Population_data1[coun_list[i]], label=coun_list[i])
plt.title("Total Population", size=12)
plt.xlabel("Years", size=12)
plt.ylabel("Total Population", size=12)
plt.xticks(rotation=90)
plt.legend(fontsize=6)
plt.savefig("lineplot.png")
plt.show()
"""

barplot(forest_data, "Forest Area (% of land area)","Total Forest Area")
barplot(Urban_data, '(annual %) of UPG','Urban population growth') 

line_plot(CO2_data,"CO2 Emission in KT","CO2 Emission (KT)")
line_plot(Population_data,"Total Population","Total Population")               