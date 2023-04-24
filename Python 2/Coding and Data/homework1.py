# Data Skills 2
# Autumn 2022
#
# Homework 1
#
# Due Monday October 10th before midnight on Gradescope.  Please read the academic integrity
# section of the syllabus for guidelines on how to collaborate and cite sources, and the grading
# rubric posted on Canvas (under syllabus).
#
# Be sure to clean up your code, removing unnecessary elements like intermediate output that were
# only used in debugging.  Write this as if it were something you were doing for your work as a
# research assistant.  You will be graded on how well you generalize and organize your code.
#
# #################################################


# 1. The two datasets included in the assignment repo are downloaded directly from the BEA.  The file
# labeled "total" has the total employment per state for the years 2000 and 2017.  The file labeled
# "by industry" has employment per industry in each of 10 industries per state for the same years.
# Load and merge the data into a panel dataframe, with the columns: "state", "year", and one for each
# of the 10 industries.  Every state-year combination should uniquely identify a row.  No more and no
# less than 12 columns should remain.  Do any necessary cleaning for the data to be easily usable.

#Loadingand Reading Data
import os
base_path = r'/Users/riddhi/Documents/GitHub/homework-1-riddhi-ka-1'
industry = os.path.join(base_path,'SAEMP25N by industry.csv' )
total = os.path.join(base_path,'SAEMP25N total.csv' )
import pandas as pd
industry_df = pd.read_csv(industry, skiprows=(4))

industry_df.head()

total_df = pd.read_csv(total, skiprows=(4))

total_df.head()

#mCleaning the Industry Dataframe
industry_df.columns
total_df.columns
industry_df = industry_df[industry_df['Description'] != 'By industry']

industry_df.columns = industry_df.columns.str.replace(' ', '')
industry_df['Description'] = industry_df['Description'].str.strip()

industry_df['2000'].unique()
import numpy as np
industry_df= industry_df.replace(['(T)', '(D)'], np.NaN)
industry_df= industry_df.iloc[:-5]
industry_df['2000'] = industry_df['2000'].apply(pd.to_numeric, errors='coerce')
industry_df['2017'] = industry_df['2017'].apply(pd.to_numeric, errors='coerce')
industry_df.columns
industry_df.drop(["GeoFips", "LineCode"], axis = 1, inplace=True)
industry_df.columns
#Cleaning the total employment Data Frame
total_df= total_df.replace(['(T)', '(D)'], np.NaN)
total_df= total_df.iloc[:-3]
total_df['2000'] = total_df['2000'].apply(pd.to_numeric, errors='coerce')
total_df['2017'] = total_df['2017'].apply(pd.to_numeric, errors='coerce')
total_df.columns
total_df.drop(["GeoFips"], axis = 1, inplace=True)
total_df.columns

#reshape the two data sets seprately and merge and do some cleaning (calculation_)
#drop the total employment 

#Reshaping the Industry Datframe
industry_df_reshaped = industry_df.melt(id_vars=['GeoName', 'Description'], var_name='Year', value_name='Employment')

industry_Final = industry_df_reshaped.pivot(index =['GeoName', 'Year'], values ='Employment',
                         columns =['Description'])


#Reshaping the Total employment Datframe

total_df_reshaped= total_df.melt(id_vars=['GeoName'], var_name='Year', value_name='Total Employment')

#Merging the industry and total employment dataframe
merged_df = industry_Final.merge(total_df_reshaped, on =['GeoName','Year'], how ='outer')
merged_df.columns


# The values should be given as the share of the total employment in that place and time, e.g. if
# total employment in a place and time was 100, and the employment in one industry was 10, then the
# value shown for that state-year industry should be 0.1.


merged_df.iloc[:,2:]=merged_df.iloc[:,2:].div(merged_df['Total Employment'],axis=0)
merged_df.drop(["Total Employment"], axis = 1, inplace=True)
merged_df.rename(columns = {'GeoName':'State'}, inplace = True)
merged_df.columns

Final_df = merged_df

# Output this dataframe to a csv document named "data.csv" and sync it to your homework repo with
# your code.

Final_df.to_csv('data.csv')

# 2. Using the dataset you created, answer the following questions:
#
# a. Find the states with the top five share of manufacturing employment in the year 2000, then show
# how their share of employment in manufacturing changed between 2000 and 2017.  Use a basic plot to
# display the information.
#


Manufacturing_df= Final_df[['State', 'Year', 'Manufacturing']]
Manufacturing_states = Manufacturing_df.sort_values(by=['State', 'Year']).nlargest(5, 'Manufacturing')
state_list = Manufacturing_states["State"].values.tolist()
Top_Manufacturing_states = Manufacturing_df[Manufacturing_df.State.isin(state_list)]

Top_Manufacturing_states.columns
Top_Manufacturing_states

import matplotlib.pyplot as plt

import seaborn as sns

Plot = sns.barplot(data=Top_Manufacturing_states, x="State", y="Manufacturing", hue="Year").set(title='Employment of Manufacturing states for 2000 & 2017', 
                                                xlabel = 'State Name', ylabel= '% of Manufacturing Emp to Total Emp')
plt.savefig('q2_plot_png.png')
plt.show()

# b. Show which five states have the highest concentration of employment in any single industry in each
# of 2000 and 2017, and what those industries are.

Top_states = Final_df.melt(id_vars=['State', 'Year'], var_name='Description', value_name='Employment')

top_2000 = Top_states.loc[Top_states['Year'] == '2000'].nlargest( 5, 'Employment')
top_2017 = Top_states.loc[Top_states['Year'] == '2017'].nlargest( 5, 'Employment')

list_2000 = top_2000['Description'].tolist()
list_2017 = top_2017['Description'].tolist()

print(list_2000)
print(list_2017)
