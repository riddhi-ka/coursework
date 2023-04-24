# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:45:19 2022

@author: khadk
"""

import pandas as pd

from bokeh.io import output_notebook
import plotly.express as px
output_notebook()

import plotly.io as io
io.renderers.default='browser'

#Reading the data
data_gdp_ghg = pd.read_csv('data_gdp_ghg.csv')
continent = pd.read_csv('continents-according-to-our-world-in-data.csv').drop(columns=['Code', 'Year']).rename(columns={"Entity": "Country"})
population = pd.read_csv('population.csv', skiprows=4).drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
population = population.melt(id_vars=["Country Name"], var_name="Year", value_name="Population").rename(columns={"Country Name": "Country"}).dropna()
population['Year'] = pd.to_numeric(population['Year'])

#Merging the data
data_gdp_ghg_cont = data_gdp_ghg.merge(continent, how='left', on=["Country"]).drop(columns=['Code', 'Unnamed: 0']).dropna()
data_gdp_ghg_pop = data_gdp_ghg_cont.merge(population, how='left', on=["Country", "Year"]).dropna()
data_gdp_ghg_pop.to_csv('data_gdp_ghg_pop.csv')

#Plotting the GDP per capita vs CO2 emmissions per capita graph 
size_1 = data_gdp_ghg_pop["Population"].to_list()
fig = px.scatter(data_gdp_ghg_pop, x="GDP per capita", y="CO2 Emissions per capita", 
                 size=size_1, color="Continent", animation_frame="Year", hover_name="Country", size_max=60)
fig.show()

#Plotting the continent wise CO2 emmissions per capita 
fig1 = px.bar(data_gdp_ghg_pop, 
             x ="Continent", 
             y ="CO2 Emissions per capita",
             color ='Continent',
             animation_frame ='Year',
             hover_name ='Country')
fig1.show()