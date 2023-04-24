# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:51:49 2022

@author: khadk
"""

from shiny import App, render, ui, reactive
import pandas as pd
import seaborn as sns

import statsmodels.api as sm
from bokeh.io import output_notebook
output_notebook()

data = sm.datasets
logo_url = 'https://www.appam.org/assets/1/15/uchicago_harris_color_rgb_(2)_(1).png?63619'
logo_url1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/The_World_Bank_logo.svg/1280px-The_World_Bank_logo.svg.png'


app_ui = ui.page_fluid(
   
    ui.row(ui.column(4, ui.img(src=logo_url, height=100, width=288)),
           ui.column(4, ui.h1('Kuznets curve!'), ui.hr(), align='center')),
    ui.row(ui.column(4, ui.em(ui.h3("Final Project")),
                        offset=1,
                        align='center'),
           ui.column(4, ui.h3('PPHA 30538 Autumn 2022'),
                        offset=2,
                        align='center')),
    ui.row(ui.column(4, ui.input_slider(id='yr',
                                        label='Choose a Year',
                                        min = 1990, max=2019, value=20, sep=''),
                        offset=4,
                        align='center')),
    ui.row(ui.column(12, ui.output_plot('ts')), align='center')
)



def server(input, output, session):
    @reactive.Calc
    def get_data():
        data_gdp_ghg_pop = pd.read_csv('C:\Deva\Chicago\Quarters\Fall 2022\DAP II\Project\data_gdp_ghg_pop.csv')

        return data_gdp_ghg_pop[data_gdp_ghg_pop['Year'] == input.yr()]

    @output
    @render.plot
    def ts():
        df = get_data()
        sns.set()
        ax = sns.scatterplot(data=df, x="GDP per capita", y="CO2 Emmissions per capita", hue="Continent")
        
              
        return ax


app = App(app_ui, server)
