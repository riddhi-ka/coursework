Research question

Our research aims to investigate the Environmental Kuznets Curve (EKC). The EKC suggests that environmental degradation gets worse in the early stages of growth of a country, but eventually reaches a peak and starts declining as income exceeds a certain level.
Using the relationship between CO2 emissions per capita (as an indication of environmental degradation) and GDP per capita, we aim to analyze:
1.Is this inverted U-shaped relationship observed in a cross-sectional analysis   of GDP per capita vs CO2 emissions countries?
2. Which sectors most contribute to the movement observed along this curve?
3. Is a difference in sentiment also observed in the statements made by countries at the 2022 United Nations Climate Change Conference across selected countries of low, middle, and high-income levels?
 
Plots and Results

We first started by generating a choropleth displaying the weightage of the distribution of GDP per capita and CO2 emissions per capita to get an overview of the difference in the distribution between the two variables in any given year from 1990 to 2019. Observing the difference in the color shades between the two plots could give us an indication as to where along the Kuznets curve the countries could potentially lie. It also gives us an overall picture of the intensity of polluters. We used matplotlib and shiny to create this interactive plot.
 
We then plotted the actual Kuznets curve through a cross-sectional display of GDP per capita on the x axis and CO2 emissions per capita on the y axis of all countries (to understand where they fall on the curve) with a slider to choose the year (to understand how their position on the curve evolves which each passing year). We added a color code to show different continents. We used seaborn and shiny to create this plot. Additionally, we created an animated version of this plot in plotly showing the movement across the years and we scaled the points on the graph according to the population of the country. 
Results: We could observe the difference between European countries vs other continents distinctively since European countries have managed to achieve a higher GDP per capita with relatively lower emissions. That being said, because of the number of countries plotted, it was tough to observe a distinctive inverted-U shaped curve which is why a regression helped us plot that relationship. 
 
We then picked 2 middle-income countries, India and China and two high-income countries, Norway and Denmark, and plotted their individual Kuznets curves to understand the relationship of the two variables for a single country. We used matplotlib to create this static graph. 
Result: Here, we could see the difference between India and China vs Norway and Denmark with India and China having a rising Kuznets curve whereas Norway and Denmark having an inverse U-shaped curve. 
 
We also proceeded to use sectoral GDP data and sectoral emissions to see which sectors are contributing to the GDP and emissions in the 4 income categories of countries (low, lower-middle, upper-middle, high-income). We used seaborn and shiny to create these interactive bar graphs.
Result: We observed that high income countries have decreasing levels of emissions in the agricultural sector and have a negative value for land use change and forestry which implies that the forest coverage has reduced significantly. A  major sector across all countries contributing to emissions was Electricity and Heat. 
 
We then conducted a linear and polynomial regression (with degree 2) of the two variables and displayed the coefficients as well as plotted the results.
Result: The linear regression showed an upward sloping statistically significant relationship between the two variables. The polynomial regression did show a inverted U-shaped curve which validated the Kuznets curve hypothesis.
 
We then downloaded statements made at the 2022 United Nations Climate Change Conference by 3 countries each belonging to the 4 income categories (total 12) and conducted a sentiment analysis on them and graphically plotted the results. 
Results: Out of the countries we analysed, Peru had a particularly negative sentiment whereas Switzerland was observed to have a very positive sentiment. 
 
We faced the following difficulties in our analyses:
 
1.    While plotting the Kuznets curve, choropleth and conducting the regression analysis, we realised that there were a few outliers that were skewing the results which we had to manually remove. 
2.    While conducting the regression analysis, we found that interpreting the results of the polynomial regression was tricky since we did not have coefficients to interpret and had to rely on metrics such as the RMSE. 
3.    We also observed that we could not achieve the level of interactivity within the graphs that we wanted to achieve through shiny since it doesn’t seamlessly support animation (which we ended up using plotly for).
4.  There were a few key countries that did not make statements at the COP27 conference. Additionally, we could not attribute the result of the sentiment analysis to their actions and future plans to combat climate change. 

While this research aims to offer a preliminary analysis of the Environmental Kuznets curve using a worldwide country dataset, we feel that the validity of the hypothesis and the shape of the curve could be more robustly tested by adding control variables to our regression analysis. Additionally, while the world bank had CO2 emission data beginning 1990, if a credible dataset with estimated CO2 emissions emissions before that could be created, this analysis will end up strengthening significantly.

 
 


