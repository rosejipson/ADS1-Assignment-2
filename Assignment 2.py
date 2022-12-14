# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:35:50 2022

@author: RJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(fname):
    """This function is used to read the file and return the transpose the
    file and data."""

    data = pd.read_excel(fname)
    dtranspose = data.set_index('Country Name').transpose()
    return data, dtranspose


# These two lists are created for storing the selected countries for two plots.
coun_list1 = ['Peru', 'China', 'Brazil', 'Italy', 'Zimbabwe', 'Japan']
coun_list2 = ['Iraq', 'Belgium', 'Mexico', 'China', 'Nepal', 'Indonesia']


def filter_bar_data(data):
    """This Function is created to filter the datas with the years
    and country names for bar plots"""

    data = data[['Country Name', 'Indicator Name',
                 '1990', '2000', '1994', '2013', '2019', '2020']]
    data = data[(data["Country Name"] == "Peru") |
                (data["Country Name"] == "China") |
                (data["Country Name"] == "Brazil") |
                (data["Country Name"] == "Italy") |
                (data["Country Name"] == "Zimbabwe") |
                (data["Country Name"] == "Japan")]
    return data


def filter_line_plot(data):
    """This Function is created to filter the datas with the years and country
    names for line plots """

    data = data[['Country Name', 'Indicator Name',
                 '1990', '1994', '2000', '2013', '2019']]
    data = data[(data["Country Name"] == "Iraq") |
                (data["Country Name"] == "Belgium") |
                (data["Country Name"] == "Mexico") |
                (data["Country Name"] == "China") |
                (data["Country Name"] == "Nepal") |
                (data["Country Name"] == "Indonesia")]
    return data


"""
This barplot function is used to plot mutiple bar graph with Country Name
and % of Urban Population and land area on x and y axis respectively
comparing with three different years. """


def barplot(data, label):
    plt.figure(figsize=(26, 16))
    ax = plt.subplot(1, 1, 1)
    x = np.arange(6)
    width = 0.2

    bar1 = ax.bar(x, data["1990"], width, label=1990)
    bar2 = ax.bar(x+width, data["1994"], width, label=1994)
    bar3 = ax.bar(x+width*2, data["2000"], width, label=2000)

    ax.set_xlabel("Country Names", fontsize=40)
    ax.set_title(label, fontsize=40)
    ax.set_xticks(x, coun_list1, fontsize=30, rotation=90)
    ax.legend(fontsize=30)

    ax.bar_label(bar1, padding=2, rotation=90, fontsize=12)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize=12)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize=12)
    plt.savefig(label+"barplot.png", bbox_inches="tight")
    plt.show()


"""This line_plot function is used to plot line graph with Country Name
CO2 Emission and Total Population on x and y axis respectively
comparing with three different years."""


def line_plot(data, label):
    plt.figure(figsize=(20, 18))
    dd = data.set_index('Country Name')
    tran = dd.transpose()
    tran = tran.drop(index=['Indicator Name'])
    for i in range(len(coun_list2)):
        plt.plot(tran.index, tran[coun_list2[i]], label=coun_list2[i])

    plt.title(label, size=25)
    plt.xlabel("Years", size=25)
    plt.xticks(rotation=90)
    plt.legend(fontsize=18)
    plt.savefig(label+"lineplot.png", bbox_inches="tight")
    plt.show()


""" Here we read the files which used for multiple bar graph into proper
variables and filter them using the function filter_bar_data"""

forest_data, forest_data1 = read_file("Forest Area.xls")
forest_data = filter_bar_data(forest_data)
Urban_data, Urban_data1 = read_file("Urban population.xls")
Urban_data = filter_bar_data(Urban_data)


CO2_data, CO2_data1 = read_file("CO2 emission.xls")
CO2_data = filter_line_plot(CO2_data)
Population_data, Population_data1 = read_file("Total Population.xls")
Population_data = filter_line_plot(Population_data)


barplot(forest_data, "Forest Area")
barplot(Urban_data, 'Urban Population')

line_plot(CO2_data, "CO2 Emission (KT)")
line_plot(Population_data, "Total Population")
