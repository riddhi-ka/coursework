# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:59:05 2022

@author: khadk
"""

import wbdata
from pandas_datareader import wb

data_gdp_ghg=wbdata.get_dataframe(indicators={'EN.ATM.CO2E.PC': 'CO2 Emissions per capita','NY.GDP.PCAP.CD': 'GDP per capita' }).reset_index()
countries = wb.get_countries()
countries = countries[~countries['incomeLevel'].isin(['Aggregates', 'Not classified'])][['name','iso3c']].rename(columns={"iso3c": "Code"})
countries = countries.rename(columns={"name": "country"})
data_gdp_ghg = data_gdp_ghg.merge(countries, on='country', how='outer').dropna().rename(columns={"date": "Year"})
data_gdp_ghg['Year'] = data_gdp_ghg['Year'].astype('int')
data_gdp_ghg['CO2 Emissions per capita'] = data_gdp_ghg['CO2 Emissions per capita'].astype('int')
data_gdp_ghg['GDP per capita'] = data_gdp_ghg['GDP per capita'].astype('int')
data_gdp_ghg = data_gdp_ghg[data_gdp_ghg.Year <= 2019]
data_gdp_ghg = data_gdp_ghg.rename(columns={"country": "Country"})
data_gdp_ghg = data_gdp_ghg.drop(data_gdp_ghg[data_gdp_ghg.Country == "Afghanistan"].index)
data_gdp_ghg.to_csv('data_gdp_ghg.csv')