#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:09:24 2022

@author: riddhi
"""

import matplotlib.pyplot as plt
import pandas as pd

Data =  pd.read_csv(r'/Users/riddhi/Documents/GitHub/final-project-rmd/data_cleaning/data_gdp_ghg.csv')

Norway_gdp_ghg = Data.loc[Data['Country'] == ('Norway')]
Denmark_gdp_ghg = Data.loc[Data['Country'] == ('Denmark')]
India_gdp_ghg = Data.loc[Data['Country'] == ('India')]
China_gdp_ghg = Data.loc[Data['Country'] == ('China')]

Gdp_Ghg = Data.loc[Data['Country'].isin(['Norway','Denmark', 'India', 'China'])]

Norway_gdp_ghg.columns

x =Norway_gdp_ghg['GDP per capita']
y= Norway_gdp_ghg['CO2 Emmissions per capita']

x1 = Denmark_gdp_ghg['GDP per capita']
y1 = Denmark_gdp_ghg['CO2 Emmissions per capita']

x2 =India_gdp_ghg['GDP per capita']
y2 = India_gdp_ghg['CO2 Emmissions per capita']

x3 =China_gdp_ghg['GDP per capita']
y3= China_gdp_ghg['CO2 Emmissions per capita']


fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Norway')
axs[0, 1].plot(x1, y1, 'tab:orange')
axs[0, 1].set_title('Denmark')
axs[1, 0].plot(x2, y2, 'tab:green')
axs[1, 0].set_title('India')
axs[1, 1].plot(x3, y3, 'tab:red')
axs[1, 1].set_title('China')

for ax in axs.flat:
    ax.set(xlabel='GDP per capita', ylabel='CO2 emissions')


# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()



fig.savefig('plot.png')

