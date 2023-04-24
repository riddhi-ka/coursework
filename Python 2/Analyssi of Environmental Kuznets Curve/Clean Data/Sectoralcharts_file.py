#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:58:17 2022

@author: riddhi
"""

import os
import pandas as pd
import numpy as np
import pandas_datareader.data as web
from pandas_datareader import wb
base_path = r'/Users/riddhi/Documents/GitHub/final-project-rmd/Clean Data'
data_gdp_ghg_path = os.path.join(base_path,'data_gdp_ghg.csv' )
gdp_ghg_df = pd.read_csv(data_gdp_ghg_path)

base_path2 = r'/Users/riddhi/Documents/GitHub/final-project-rmd/Raw Data'
ghg_path = os.path.join(base_path2,'ghg-emissions-by-sector.csv' )

#Merging categorization income level for countries
gdp_ghg_df.columns
gdp_ghg_df = gdp_ghg_df.loc[gdp_ghg_df['Year'] == 2019]
gdp_ghg_df = gdp_ghg_df.drop(columns=['Unnamed: 0','GDP per capita', 'Year', 'CO2 Emissions per capita'])
countries_df = wb.get_countries()
countries_df.head()
countries_df1 = countries_df.drop(columns=['iso2c','region', 'lendingType' , 'adminregion', 'capitalCity', 'latitude', 'longitude', 'name'])
countries_df1 = countries_df1.loc[countries_df1['incomeLevel'] != 'Aggregates']
countries_df1.rename(columns = {'iso3c':'Code'}, inplace = True)
Income_catg_df = gdp_ghg_df.merge(countries_df1, how='left', on='Code')
Income_catg_df.dropna(inplace=True)

#Merging Sector data to the Income ctaegorization file
sectoral_ghg_df = pd.read_csv(ghg_path)
ghg_2019 = sectoral_ghg_df.loc[sectoral_ghg_df['Year'] == 2019]
ghg_2019.dropna(subset=['Code'], inplace=True)
ghg_2019.loc[ghg_2019['Code'] != "OWID_WRL"]
Sectral_ghg_data = Income_catg_df.merge(ghg_2019, how='left', on='Code')
Sectral_ghg_data = Sectral_ghg_data.drop(columns=['Entity'])

def calculation_func(Incomelevel):
    col_list = ['Agriculture','Land-use change and forestry', 'Waste', 'Industry','Manufacturing and construction', 'Transport', 'Electricity and heat','Buildings', 'Fugitive emissions', 'Other fuel combustion','Aviation and shipping']   
    data = Sectral_ghg_data.loc[Sectral_ghg_data['incomeLevel'] == Incomelevel]
    Sum_ghg = data[col_list].sum()
    Total=Sum_ghg.to_frame().reset_index()
    Total.rename(columns = {0:'GHG emissions', 'index': 'Sectors'}, inplace=True)
    per_ghg = Total['GHG emissions'].sum()
    
    if Incomelevel == 'High income':
        Total['ghg_pct_HI'] = (Total['GHG emissions'] / per_ghg).round(2)
        Total_high_inc = Total
        return Total_high_inc
        
    elif Incomelevel == 'Upper middle income':
        Total['ghg_pct_UMI'] = (Total['GHG emissions'] / per_ghg).round(2)

        Total_upper_middle_inc = Total
        return Total_upper_middle_inc
    
    elif Incomelevel == 'Lower middle income':
        Total['ghg_pct_LMI'] = (Total['GHG emissions'] / per_ghg).round(2)
    
        Total_lower_middle_inc = Total
        return Total_lower_middle_inc
    
    elif Incomelevel == 'Low income':
        Total['ghg_pct_LI'] = (Total['GHG emissions'] / per_ghg).round(2)
        Total_low_inc = Total
        return Total_low_inc



Total_high_inc = calculation_func('High income')
Total_upper_middle_inc = calculation_func('Upper middle income')
Total_lower_middle_inc = calculation_func('Lower middle income')
Total_low_inc = calculation_func('Low income')


Total_perc_GHG1 = Total_high_inc.merge(Total_low_inc, how='left', on='Sectors')
Total_perc_GHG2 = Total_upper_middle_inc.merge(Total_lower_middle_inc, how='left', on='Sectors')
Total_GHG_perc = Total_perc_GHG1.merge(Total_perc_GHG2, how= 'left', on = 'Sectors')
Total_GHG_perc.columns
Total_GHG_perc = Total_GHG_perc.drop(columns=['GHG emissions_x_x','GHG emissions_y_x', 'GHG emissions_x_y' , 'GHG emissions_y_y'])

Total_GHG_perc.to_csv(r'/Users/riddhi/Documents/GitHub/final-project-rmd/Clean Data/Total_GHG_perc.csv')


GDP_path = r'/Users/riddhi/Documents/GitHub/final-project-rmd/Raw Data'

#Loading Manufacturing data
data_gdp_manu_path = os.path.join(GDP_path,'Manufacturing.csv')
Manu_data = pd.read_csv(data_gdp_manu_path, skiprows=(4))

#Loading Agriculture data
data_gdp_agri_path = os.path.join(GDP_path,'Agriculture.csv')
Agri_data = pd.read_csv(data_gdp_agri_path, skiprows=(4))

#Loading Industry data
data_gdp_indu_path = os.path.join(GDP_path,'Industry.csv')
Indu_data = pd.read_csv(data_gdp_indu_path, skiprows=(4))

#Cleaning Data Files


Manu_data.columns
drop_col = ['Country Name','Indicator Name', 'Indicator Code',
       '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
       '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2020', '2021','Unnamed: 66']

Manu_data = Manu_data.drop(columns= drop_col)
Manu_data.rename(columns = {'Country Code':'Code'}, inplace = True)

Agri_data = Agri_data.drop(columns= drop_col)
Agri_data.rename(columns = {'Country Code':'Code'}, inplace = True)

Indu_data = Indu_data.drop(columns= drop_col)
Indu_data.rename(columns = {'Country Code':'Code'}, inplace = True)

#merging Data sets to create one base file 
Total_GDP1 = gdp_ghg_df.merge(Manu_data, on='Code')
Total_GDP2 = gdp_ghg_df.merge(Agri_data, on='Code')
Total_GDP3 = gdp_ghg_df.merge(Indu_data, on='Code')

Total_GDP23 = Total_GDP2.merge(Total_GDP3, on='Code')

Total_GDP = Total_GDP1.merge(Total_GDP23, on='Code')
Total_GDP.columns

Drop_columns = ['Country_x','Country_y']
Total_GDP.drop(columns= Drop_columns, inplace= True)
Total_GDP.rename(columns = {'2019':'Manufacturing', '2019_x': 'Agriculture', '2019_y': 'Industry'}, inplace = True)
Total_GDP.dropna

Total_gdp_categorization = Total_GDP.merge(Income_catg_df, how = 'left' , on = 'Code')
Total_gdp_categorization.drop(columns=['Country_y'], inplace= True)
Total_gdp_categorization.rename(columns = {'Country_x':'Country Name'}, inplace = True)


#Calculation fro GDP percentage
column_list = ['Manufacturing', 'Agriculture','Industry']

def calculations_func(Income_level):
    column_list = ['Manufacturing', 'Agriculture','Industry']
    Total_data =  Total_gdp_categorization.loc[Sectral_ghg_data['incomeLevel'] == Income_level]
    Total_data.drop(columns = ['incomeLevel'], inplace =True)
    Sum_gdp = Total_data[column_list].sum()
    Total_gdp=Sum_gdp.to_frame().reset_index()
    Total_gdp.rename(columns = {0:'GDP', 'index': 'Sectors'}, inplace=True)
    per_gdp = Total_gdp['GDP'].sum()
   
    if Income_level == 'High income':
        Total_gdp['gdp_pct_HI'] = (Total_gdp['GDP'] / per_gdp).round(2)
        Total_gdphigh_inc = Total_gdp
        return Total_gdphigh_inc
        
    elif Income_level == 'Upper middle income':
        Total_gdp['gdp_pct_UMI'] = (Total_gdp['GDP'] / per_gdp).round(2)

        Total_gdpupper_inc = Total_gdp
        return Total_gdpupper_inc
    
    elif Income_level == 'Lower middle income':
        Total_gdp['gdp_pct_LMI'] = (Total_gdp['GDP'] / per_gdp).round(2)
    
        Total_gdplower_inc = Total_gdp
        return Total_gdplower_inc
    
    elif Income_level == 'Low income':
        Total_gdp['gdp_pct_LI'] = (Total_gdp['GDP'] / per_gdp).round(2)
        Total_gdplow_inc = Total_gdp
        return Total_gdplow_inc


Total_gdphigh_inc = calculations_func('High income')
Total_gdpupper_inc = calculations_func('Upper middle income')
Total_gdplower_inc = calculations_func('Lower middle income')
Total_gdplow_inc = calculations_func('Low income')


Total_perc_GDP1 = Total_gdphigh_inc.merge(Total_gdplow_inc, how='left', on='Sectors')
Total_perc_GDP2 = Total_gdpupper_inc.merge(Total_gdplower_inc, how='left', on='Sectors')
Total_GDP_perc = Total_perc_GDP1.merge(Total_perc_GDP2, how= 'left', on = 'Sectors')
Total_GDP_perc.columns
Total_GDP_perc = Total_GDP_perc.drop(columns=['GDP_x_x', 'GDP_y_x','GDP_x_y', 'GDP_y_y'])

Total_GDP_perc.to_csv(r'/Users/riddhi/Documents/GitHub/final-project-rmd/Clean Data/Total_GDP_perc.csv')
