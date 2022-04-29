from tkinter import TkVersion
import pandas as pd
import altair as alt


# https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/netflix_titles.csv

"""
Load the dataset into a Pandas data frame and determine what data type is used to store the release_year feature.
"""
netflix_titles = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/netflix_titles.csv')

#netflix_titles.head()
#netflix_titles.info()
# see data type for release_year
"""
print(type(netflix_titles['release_year'][0]))
#int64

# Filter your dataset so it contains only TV Shows. How many of those TV Shows were rated TV-Y7?
"""
# filter to only tv shows with rating of TV-Y7
tv_shows = netflix_titles[netflix_titles['type'] == 'TV Show']
tv_y7 = tv_shows[tv_shows['rating'] == 'TV-Y7']
print(tv_y7.shape[0])

# filter to shows between 2000 and 2009
tv_y7_2000_2009 = tv_y7[(tv_y7['release_year'] >= 2000) & (tv_y7['release_year'] <= 2009)]

# count the number of rows
print(tv_y7_2000_2009.shape[0])

url = 'https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/cereal.csv'
cereal = pd.read_csv(url)
"""
After importing the dataset into a pandas data frame, determine the median amount of protein in cereal brands manufactured by Kelloggs. (mfr code "K")
"""
print(cereal.head())
# determine the median amount of protein in dataframe with mfr code "K"
print(cereal[cereal['mfr'] == 'K']['protein'].median())
#print(cereal.info())

"""
In order to comply with new government regulations, all cereals must now come with a "Healthiness" rating. This rating is calculated based on this formula: healthiness = (protein + fiber) / sugar

Create a new healthiness column populated with values based on the above formula.

Then, determine the median healthiness value for only General Mills cereals (mfr = "G"), rounded to two decimal places.
"""
cereal['healthiness'] = (cereal['protein'] + cereal['fiber']) / cereal['sugars']
print(cereal[cereal['mfr'] == 'G']['healthiness'].median())



url = 'https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/titanic.csv'
titanic = pd.read_csv(url)

"""
After loading the dataset into a pandas DataFrame, create a new column called NameGroup that contains the first letter of the passenger's surname in lower case.

Note that in the dataset, passenger's names are provided in the Name column and are listed as: Surname, Given names

For example, if a passenger's Name is Braund, Mr. Owen Harris, the NameGroup column should contain the value b.

Then count how many passengers have a NameGroup value of k.
"""
# get first letter of surname
titanic['NameGroup'] = titanic['Name'].str.split(',').str[0].str.lower().str[0]
# count  number of passengers with NameGroup value of k
print(titanic[titanic['NameGroup'] == 'k'].shape[0])

