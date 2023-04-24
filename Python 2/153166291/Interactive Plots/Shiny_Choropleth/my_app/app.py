from shiny import App, render, ui, reactive
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
from pandas_datareader import wb

logo_url = 'https://www.appam.org/assets/1/15/uchicago_harris_color_rgb_(2)_(1).png?63619'
logo_url1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/The_World_Bank_logo.svg/1280px-The_World_Bank_logo.svg.png'

app_ui = ui.page_fluid(

    ui.row(ui.column(4, ui.img(src=logo_url, height=100, width=288)),
        ui.column(4, ui.h2('Data Visualization of CO2 Emissions per-capita vs GDP per-capita'), align="center"),
    ),
    ui.row(
        ui.column(12, ui.h4('')),
    ),
    ui.row(
        ui.column(12, ui.input_slider("n", "Choose a year", 1990, 2019, 1, ticks=False, sep='', width='800px'), align="center"),
    ),
    ui.row(
        ui.column(12, ui.output_plot("create_data1"), align="right"),
    ),
    ui.row(
        ui.column(12, ui.h4('')),
    ),
    ui.row(
        ui.column(12, ui.output_plot("create_data2"), align="right"),
    ),

)


def server(input, output, session):

    def get_data():
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')).rename(columns={'iso_a3':'Code'})
        data_gdp_ghg = pd.read_csv('data_gdp_ghg.csv')
        countries = wb.get_countries()
        income_level = countries[~countries['incomeLevel'].isin(['Aggregates', 'Not classified'])][['iso3c', 'incomeLevel']].rename(columns={"iso3c": "Code"})
        data_regression = data_gdp_ghg.merge(income_level, how='outer', on=["Code"]).dropna()
        data_chrpleth = data_regression.merge(world, how='left', on=["Code"]).dropna()
        data_plot = data_chrpleth[data_chrpleth['Year'] == input.n()][['Country','CO2 Emissions per capita', 'GDP per capita', 'geometry' ]]
        data_plot.to_csv('data_plot.csv')
        data_plot = data_plot[data_plot.Country != 'Solomon Islands']
        data_plot = data_plot[data_plot.Country != 'Qatar']
        data_plot = data_plot[data_plot.Country != 'Luxembourg']
        return GeoDataFrame(data_plot)


    @output
    @render.plot
    def create_data1():
        data_plot = get_data()
        fig, ax = plt.subplots(figsize=(15, 15))
        fig.patch.set_facecolor('whitesmoke')
        divider = make_axes_locatable(ax)
        cax = divider.append_axes('right', size='3%', pad=0.1)
        ax = data_plot.plot(ax=ax, column='CO2 Emissions per capita', legend=True, cax=cax, cmap='plasma', figsize=(15, 15))
        ax.axis('off')
        ax.set_title('CO2 emissions (Metric tons per capita)')
        return ax

    @output
    @render.plot
    def create_data2():
        data_plot2 = get_data()
        fig, ax = plt.subplots(figsize=(15, 15))
        fig.patch.set_facecolor('whitesmoke')
        divider = make_axes_locatable(ax)
        cax = divider.append_axes('right', size='3%', pad=0.1)
        ax = data_plot2.plot(ax=ax, column='GDP per capita', legend=True, cax=cax, cmap='plasma', figsize=(15, 15))
        ax.axis('off')
        ax.set_title('GDP per capita (Current USD)')
        return ax


app = App(app_ui, server)
