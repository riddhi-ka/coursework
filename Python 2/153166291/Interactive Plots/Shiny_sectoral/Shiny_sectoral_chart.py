import seaborn as sns
import matplotlib.pyplot as plt
from shiny import App, render, ui
import pandas as pd
import seaborn

#path = r'/Users/riddhi/Documents/GitHub/final-project-rmd/Sectoral_Charts'
#GDP_data = os.path.join(base_path,'Total_GDP_perc.csv')
#GHG_data = os.path.join(base_path,'Total_GHG_perc.csv')
Total_GDP_perc = pd.read_csv(r'/Users/riddhi/Documents/GitHub/final-project-rmd/Clean Data/Total_GDP_perc.csv')
Total_GHG_perc = pd.read_csv(r'/Users/riddhi/Documents/GitHub/final-project-rmd/Clean Data/Total_GHG_perc.csv')

Indicator = ['GHG Emission', 'GDP']
Income_catg = ['High Income', 'Low Income', 'Upper middle income', 'Lower middle income']
Total_GDP_perc.columns

logo_url = 'https://www.appam.org/assets/1/15/uchicago_harris_color_rgb_(2)_(1).png?63619'
logo_url1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/The_World_Bank_logo.svg/1280px-The_World_Bank_logo.svg.png'


Indicator = ['GHG Emission', 'GDP']
Income_catg = ['High Income', 'Low Income', 'Upper middle income', 'Lower middle income']
data = Total_GDP_perc['gdp_pct_HI']
keys = ['Manufacturing', 'Agriculture', 'Industry']
palette_color = seaborn.color_palette('bright')
app_ui = ui.page_fluid(

    ui.row(
        ui.column(4, ui.img(src=logo_url, height=100, width=288)),
        ui.column(4, ui.h1('Sectoral Chart'), ui.hr()),
        ui.column(4, ui.img(src=logo_url1, height=100, width=288)),
        ui.column(4, ui.input_select(id='Income_catg', 
                                     label='Choose an income category level',
                                     choices=list(Income_catg))),
        ui.column(4, ui.input_select(id='Indicator', 
                                     label='Choose an indicator variable',
                                     choices=list(Indicator))),
    ),
    ui.row(
        ui.column(6, ui.output_plot('hist')),
    )
)
def server(input, output, session):
    @output
    @render.plot
    def hist():
        
     if (input.Income_catg() == 'High Income') & (input.Indicator() == 'GHG Emission') :
        ax = sns.barplot(data=Total_GHG_perc, x="ghg_pct_HI", y="Sectors")
        ax.set_xlabel("GHG emission percentage")
        ax.set_ylabel("Sectors")
        return ax
    
     if (input.Income_catg() == 'Low Income') & (input.Indicator() == 'GHG Emission') :
        ax = sns.barplot(data=Total_GHG_perc, x="ghg_pct_LI", y="Sectors")
        ax.set_xlabel("GHG emission percentage")
        ax.set_ylabel("Sectors")
        return ax
    
     if (input.Income_catg() == 'Upper middle income') & (input.Indicator() == 'GHG Emission') :
        ax = sns.barplot(data=Total_GHG_perc, x="ghg_pct_UMI", y="Sectors")
        ax.set_xlabel("GHG emission percentage")
        ax.set_ylabel("Sectors")
        return ax
    
     if (input.Income_catg() == 'Lower middle income') & (input.Indicator() == 'GHG Emission') :
        ax = sns.barplot(data=Total_GHG_perc, x="ghg_pct_LMI", y="Sectors")
        ax.set_xlabel("GHG emission percentage")
        ax.set_ylabel("Sectors")
        return ax
    
     if (input.Income_catg() == 'High Income') & (input.Indicator() == 'GDP') :
        ax = sns.barplot(data=Total_GDP_perc, x="gdp_pct_HI", y="Sectors")
        ax.set_xlabel("GDP percentage")
        ax.set_ylabel("Sectors")
        return ax

     if (input.Income_catg() == 'Low Income') & (input.Indicator() == 'GDP') :
        ax = sns.barplot(data=Total_GDP_perc, x="gdp_pct_LI", y="Sectors")
        ax.set_xlabel("GDP percentage")
        ax.set_ylabel("Sectors")
        return ax
    
     if (input.Income_catg() == 'Upper middle income') & (input.Indicator() == 'GDP') :
        ax = sns.barplot(data=Total_GDP_perc, x="gdp_pct_UMI", y="Sectors")
        ax.set_xlabel("GDP percentage")
        ax.set_ylabel("Sectors")
        return ax
    
     if (input.Income_catg() == 'Lower middle income') & (input.Indicator() == 'GDP') :
        ax = sns.barplot(data=Total_GDP_perc, x="gdp_pct_LMI", y="Sectors")
        ax.set_xlabel("GDP percentage")
        ax.set_ylabel("Sectors")
        return ax
    
app = App(app_ui, server)