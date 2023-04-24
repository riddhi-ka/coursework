# Data Skills 2: Homework 2
## Data Visualization

### Due Monday October 24th before midnight

Note that there are three parts to this assignment.  Your final repo should include two Jupyter notebooks, shapefiles that you downloaded (part 3), data from the Urban institute (part 2) and saved png files of any static plots (part 2). 

__Part 1 (10%):__ Answer the final project quiz on Canvas.  Full credit for submitting any reasonable answers.

__Part 2 (45%):__ Urban Institute Education Data Portal

_The Data:_

The Urban Institute hosts an open data portal on education in the United States.  Researchers at Urban clean and assemble a wide variety of data, and then make the organized data available for download.  In this case, you will retrieve college data from the Education Data Portal:

https://educationdata.urban.org/data-explorer/explorer

You must use their interface, which builds a SQL query behind-the-sceens as you select options, then returns custom-built csv documents to you for download.  Certain data is only available for certain years; in this case we will be working with the date ranges 2001-2016, because that range enables a large number of options.

Depending on the options you select, you may receive more than one data file that needs to be merged together.  You will also receive a data dictionary.

_You must commit the downloaded csv files with your code into your repository._ There are too many ways to customize your query, and I am not giving any guidelines on what options you select beyond the date range listed above, so the graders will not be able to reproduce your data.

_The Task:_

You work in the education policy field, and you are proposing your organization use the Urban Institute data to study higher education.  Their nicely organized data offers a lot of opportunities to gain insights into the field.

The result of this project will be:
  1. One Jupyter notebook with all your code, plots, and writeup.
     - We use Jupyter notebooks here because of the interactive widgits
	 - Before committing your final notebook, click the "Kernal" menu and select "Restart & Run All", then save it and commit.  This will help make sure your code works in sequence, and will make it easier for the TAs to grade.
     - Note one key hazard of working in Jupyter notebooks: Jupyter cells do not count as a method of organization or substitute for functions!
  2. All data loading and merging code (but not downloading, which must use the Urban web interface)
  3. The creation of plots:
     - _One_ static plot from MatPlotLib/Pandas/Seaborn.  This plots should be a "headline" result that you would, for example, embed in a writeup to your colleagues about why they should consider using this data.  Note that you will not be creating such a writeup - we're just framing the goal of our data visualizations. You should show effort in your code toward making it a nice plot.
     - _One_ interactive plot from Bokeh that includes multiple data options.  This plot should allow you and your colleagues to explore an assortment of interesting questions you could answer with this data.

You will then include an approximately 5-10 line writeup in a Jupyter cell (change the type from Code to Markdown) about how this part went and what you observed using data visualization.  In your writeup, focus particularly on generalization - were you able to use functions with your code in a way that lets you make changes easier later, or that makes your code more legible for someone else to read?  How was the balance between using MatPlotLib and Seaborn?  Was there something you discovered by visualizing the data that you didn't expect, or couldn't see any other way?  How did you inform your plot selection - did you have a specific research question?

__Part 3 (45%): Spatial Data__

You will be creating an interactive choropleth.  To begin, you will choose:

  * Any one **continent**
  * Any two **countries within that continent**
  * Any two variables for each country that you will use to scale colors on the choropleth.  You should use a data API (e.g. pandas_datareader) to download the variables.
   
You will create a single plot using GeoPandas and MatPlotLib (not Bokeh) which includes two interactive elements:

  * One element to select the country
  * One element to select the variable to display on the map
  
**Your code must be generalized using functions, so that you could easily add more countries within that continent to the geographic options, and more variables to the data options.**
