#Pandas
# ## 1. Setup
# ### Import
# Before moving on to learn pandas first we need to install it and import it. If you install [Anaconda distributions](https://www.anaconda.com/) on your local machine or using [Google Colab](https://research.google.com/colaboratory) then pandas will already be available there, otherwise, you follow this installation process from [pandas official's website](https://pandas.pydata.org/docs/getting_started/install.html).
# Importing libraries
import numpy as np
import pandas as pd
# we can set numbers for how many rows and columns will be displayed
pd.set_option('display.min_rows', 10) #default will be 10 
pd.set_option('display.max_columns', 20)
# ## 2. Loading Different Data Formats Into a Pandas Data Frame
# ### Reading CSV file
# read csv file
df = pd.read_csv('online_store_customer_data.csv')
df.head(3)
# Loading csv file with skip first 2 rows without header
df_csv = pd.read_csv('online_store_customer_data.csv', skiprows=2, header=None)
df_csv.head(3)
# ### Read CSV file from URL
# Read csv file from url
#from io import StringIO
#import requests
url="https://github.com/norochalise/pandas-tutorial-article-2022/tree/main/dataset/online_store_customer_data.csv"
#s=requests.get(url).content
#c=pd.read_csv(io.StringIO(s.decode('utf-8')))
#df_url = pd.read_csv(url)
#s=requests.get(url).text
#df_url = pd.read_csv(StringIO(s))
df_url = pd.read_csv(url, sep = "\t")
df_url.head(3)
# ### Write CSV file
# saving df_url dataframe to csv file
df_url.to_csv('csv_from_url.csv')
df_url.to_csv('demo_text.txt')
# ### Read text file
# read plain text file
df_txt = pd.read_csv("demo_text.txt")
# ### Read Excel file
# read excel file
df_excel = pd.read_excel('excel_file.xlsx', sheet_name='Sheet1')
df_excel
# ### Write Excel file
# save dataframe to the excel file
df_url.to_csv('demo.xlsx')
# ## 3. Data preprocessing
# Data preprocessing is the process of making raw data to clean data. This is the most crucial part of data the science. In this section, we will explore data first then we remove unwanted columns, remove duplicates, handle missing data, etc. After this step, we get clean data from raw data.
# ### 3.1 Data Exploring
# #### Retrieving rows from data frame.
# display first 3 rows
df.head(3)
# display last 6 rows
df.tail(6)
# #### Retrieving sample rows from data frame.
# Display random 7 sample rows
df.sample(7)
# #### Retrieving information about dataframe
df.info()
# display datatypes
df.dtypes
df.dtypes.value_counts()
# #### Display number of rows and columns.
df.shape
df.columns
# display Age columns first 3 rows data
df['Age'].head(3)
# display first 4 rows of Age, Transaction_date and Gender columns
df[['Age', 'Transaction_date', 'Gender']].head(4)
# #### Retrieving a Range of Rows
# for display 2nd to 6th rows
df[2:7]
# for display starting to 10th
df[:11]
# for display last two rows
df[-2:]
#  ### 3.2 Data Cleaning
# After the explore our datasets may need to clean them for better analysis. Data coming in from multiple sources so It's possible to have an error in some values. This is where data cleaning becomes extremely important. In this section, we will delete unwanted columns, rename columns, correct appropriate data types, etc.
# #### Delete Columns name
# Drop unwanted columns
df.drop(['Transaction_ID'], axis=1, inplace=True)
# #### Change Columns name
# create new df_col dataframe from df.copy() method.
df_col = df.copy()
# rename columns name
df_col.rename(columns={"Transaction_date": "Date", "Gender": "Sex"}, inplace=True)
df_col.head(3)
# #### Adding a new column to a DataFrame
# Add a new ajusted column which value will be amount_spent * 100
df_col['new_col'] = df_col['Amount_spent'] * 100
df_col.head(3)
# #### String value change or replace
df_col.head(3)
# changing Female to Woman and Male to Man in Sex column.
#first argument in loc function is condition and second one is columns name. 
df_col.loc[df_col.Sex == "Female", 'Sex'] = 'Woman' 
df_col.loc[df_col.Sex == "Male", 'Sex'] = 'Man'
df_col.head(3)
# Now Sex columns values are changed Female to Woman and Male to Man.
# #### Datatypes change
df_col.info()
# In our `Date` columns, it's object type so now we will convert this to date types, and also we will convert `Referal` columns float64 to float32.
# change object type to datefime64 format
df_col['Date'] = df_col['Date'].astype('datetime64[ns]')
# change float64 to float32 of Referal columns
df_col['Referal'] = df_col['Referal'].astype('float32')
df_col.info()
# ### 3.3 Remove duplicate
# Display duplicated entries
df.duplicated().sum()
# duplicate rows dispaly, keep arguments will--- 'first', 'last' and False
duplicate_value = df.duplicated(keep='first')
df.loc[duplicate_value, :]
# dropping ALL duplicate values
df.drop_duplicates(keep = 'first', inplace = True)
# ### 3.4 Handling missing values
# Handling missing values in the common task in the data pre-processing part. For many reasons most of the time we will encounter missing values. Without dealing with this we can't do the proper model building. For this section first, we will find out missing values then we decided how to handle them. We can handle this by removing affected columns or rows or replacing appropriate values there.
# #### Display missing values information
df.isna().sum().sort_values(ascending=False)
# #### Delete Nan rows
# If we have less Nan value then we can delete entire rows by `dropna()` function. For this function, we will add columns name in subset parameter.
# df copy to df_copy
df_new = df.copy()
#Delete Nan rows of Job Columns
df_new.dropna(subset = ["Employees_status"], inplace=True)
# #### Delete entire columns
# If we have a large number of nan values in particular columns then dropping those columns might be a good decision rather than imputing.
df_new.drop(columns=['Amount_spent'], inplace=True)
df_new.isna().sum().sort_values(ascending=False)
# #### Impute missing values
# Sometimes if we delete entire columns that will be not the appropriate approach. Delete columns can affect our model building because we will lose our main features. For imputing we have many approaches so here are some of the most popular techniques.
# **Method 1** - Impute fixed value like 0, 'Unknown' or 'Missing' etc. We inpute Unknown in Gender columns
df['Gender'].fillna('Unknown', inplace=True)
# **Method 2** - Impute Mean, Median and Mode
# Impute Mean in Amount_spent columns
mean_amount_spent = df['Amount_spent'].mean()
df['Amount_spent'].fillna(mean_amount_spent, inplace=True)
#Impute Median in Age column
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)
# Impute Mode in Employees_status column
mode_emp = df['Employees_status'].mode().iloc[0]
df['Employees_status'].fillna(mode_emp, inplace=True)
# **Method 3** - Imputing forward fill or backfill by `ffill` and `bfill`. In `ffill` missing value impute from the value of the above row and for `bfill` it's taken from the below rows value.
df['Referal'].fillna(method='ffill', inplace=True)
df.isna().sum().sum()
# Now we deal with all missing values with different methods. So now we haven't any null values.
# ## 4. Memory management
# When we work on large datasets, There we get one big issue is a memory problem. We need too large resources for dealing with this. But there are some methods in pandas to deal with this. Here are some methods or strategies to deal with this problem with help of pandas.
# ### Change datatypes
df_memory = df.copy()
memory_usage = df_memory.memory_usage(deep=True)
memory_usage_in_mbs = round(np.sum(memory_usage / 1024 ** 2), 3)
print(f" Total memory taking df_memory dataframe is : {memory_usage_in_mbs:.2f} MB ")
# #### Change object to category datatypes
# Our data frame is small in size. Which is 1.15 MB. Now We will convert our object datatype to category.
# Object datatype to category convert
df_memory[df_memory.select_dtypes(['object']).columns] = df_memory.select_dtypes(['object']).apply(lambda x: x.astype('category'))
# convert object to category
df_memory.info(memory_usage="deep")
# Now its reduce 1.15 megabytes to 216.6 kb. It's almost reduced 5.5 times.
# #### Change int64 or float64 to int 32, 16, or 8
# By default, pandas store numeric values to int64 or float64. Which takes more memory. If we have to store small numbers then we can change to 64 to 32, 16, and so on. For example, our Referal columns have only 0 and 1 values so for that we don't need to store at float64. so now we change it to float16.
# Change Referal column datatypes
df_memory['Referal'] = df_memory['Referal'].astype('float32')
# convert object to category
df_memory.info(memory_usage="deep")
# After changing only one column's data types we reduce 216 kb to 179 kb.
# **Note: Before changing datatypes please make sure it's consequences.**
# ## 5. Data Analysis
# ### 5.1. Calculating Basic statistical measurement
df.describe().T
# We know already above code will display only numeric columns basic statistical information. for object or category columns we can use `describe(include=object)` .
df.describe(include=object).T
# We can calculate the mean, median, mode, maximum values, minimum values of individual columns we simply use these functions.
# Calculate Mean
mean = df['Age'].mean()
# Calculate Median
median = df['Age'].median()
#Calculate Mode
mode = df['Age'].mode().iloc[0]
# Calculate standard deviation
std = df['Age'].std()
# Calculate Minimum values
minimum = df['Age'].min()
# Calculate Maximum values
maximum = df.Age.max()
print(f" Mean of Age : {mean}")
print(f" Median of Age : {median}")
print(f" Mode of Age : {mode}")
print(f" Standard deviation of Age : {std:.2f}")
print(f" Maximum of Age : {maximum}")
print(f" Minimum of Age : {minimum}")
# In pandas we can display the correlation of different numeric columns. For this we can use `.corr()` function.
# calculate correlation
df.corr(numeric_only = True)
# ### 5.2 Basic built in function for data analysis
# #### Number of uniqe values in category column
# for display how many unique values are there in State_names column
df['State_names'].nunique()
# #### Shows all unique values
# for display uniqe values of State_names column
df['State_names'].unique()
# #### Counts of unique values
df['Gender'].value_counts()
# If we want to show with the percentage of occurrence rather number than we use `normalize=True` argument in `value_counts()` function
# Calculate percentage of each category
df['Gender'].value_counts(normalize=True)
df['State_names'].value_counts().sort_values(ascending = False).head(20)
# Sort Values by State_names
df.sort_values(by=['State_names']).head(3)
# For sorting our dataframe by Amount_spent with ascending order:
# Sort Values Amount_spent with ascending order
df.sort_values(by=['Amount_spent']).head(3)
# For sorting our dataframe by Amount_spent with descending order:
# Sort Values Amount_spent with descending order
df.sort_values(by=['Amount_spent'], ascending=False).head(3)
# Alternatively, We can use `nlargest()` and `nsmallest()` functions for displaying largest and smallest values with desired numbers. for example, If we want to display 4 largest Amount_spent rows then we use this:
# nlargest
df.nlargest(4, 'Amount_spent').head(10) # first argument is how many rows you want to disply and second one is columns name
# For 3 smallest Amount_spent rows
# nsmallest
df.nsmallest(3, 'Age').head(10)
# #### Conditional queries on Data
# filtering - Only show Paypal users
condition = df['Payment_method'] == 'PayPal'
df[condition].head(4)
# We can apply multiple conditional queries like before. For example, if we want to display all Married female people who lived in New York then we use the following:
# first create 3 condition
female_person = df['Gender'] == 'Female'
married_person = df['Marital_status'] == 'Married'
loc_newyork = df['State_names'] == 'New York'
# we passing condition on our dataframe
df[female_person & married_person & loc_newyork].head(4)
# ### 5.3 Summarizing or grouping data
# #### Groupby
# **Grouping by one column:** For example, if we want to find `maximum` values of `Age` and `Amount_spent` by `Gender` then we can use this:
df[['Age', 'Amount_spent']].groupby(df['Gender']).max()
# To find `mean`, `count`, and `max` values of `Age` and `Amount_spent` by `Gender` then we can use `agg()` function with `groupby()` .
# Group by one columns
state_gender_res = df[['Age','Gender','Amount_spent']].groupby(['Gender']).agg(['count', 'mean', 'max'])
state_gender_res
# **Grouping by multiple columns:** To find total count, maximum and minimum values of Amount_spent by State_names, Gender, and Payment_method then we can pass these columns names under `groupby()` function and add `.agg()` with `count`, `mean`, `max` argument.
#Group By multiple columns
state_gender_res = df[['State_names','Gender','Payment_method','Amount_spent']].groupby([ 'State_names','Gender', 'Payment_method']).agg(['count', 'min', 'max'])
state_gender_res.head(12)
# #### Cross Tabulation (Crosstab)
# For creating a simple crosstab between Maritatal_status and Payment_method columns we just use `crosstab()` with both column names.
pd.crosstab(df.Marital_status, df.Payment_method)
# We can include subtotals by `margins` parameter:
pd.crosstab(df.Marital_status, df.Payment_method, margins=True, margins_name="Total")
# If We want a display with percentage than `normalize=True` parameter help
pd.crosstab(df.Marital_status, df.Payment_method, normalize=True, margins=True, margins_name="Total")
# In this crosstab features, we can pass multiple columns names for grouping and analyzing data. For instance, If we want to see how the `Payment_method` and `Employees_status` are distributed by `Marital_status` then we will pass these columns' names in `crosstab()` function and it will show below.
pd.crosstab(df.Marital_status, [df.Payment_method, df.Employees_status])
# ## 6. Data Visualization
# Visualization is the key to data analysis. The most popular python package for visualization are matplotlib and seaborn but sometimes pandas will be handy for you. Pandas also provide some visualization plots easily. For the basic analysis part, it will be easy to use. For this section, we are exploring some different types of plots using pandas. Here are the plots.
# ### 6.1 Line plot
# For creating a line plot in pandas we use `.plot()` with two columns name for the argument. For example, we create a line plot from one dummy dataset.
dict_line = {
    'year': [2016, 2017, 2018, 2019, 2020, 2021],
    'price': [200, 250, 260, 220, 280, 300]
}
df_line = pd.DataFrame(dict_line)
# use plot() method on the dataframe
df_line.plot('year', 'price');
# The above line chart shows prices over a different time. It shows like price trend.
# ### 6.2 Bar plot
# A bar plot is also known as a bar chart shows quantitative or qualitative values for different category items. In a bar plot data are represented in the form of bars. Bars length or height are used to represent the quantitative value for each item. Bar plot can be plotted horizontally or vertically. For creating these plots look below.
# **For horizontal bar:**
df['Employees_status'].value_counts().plot(kind='bar');
# **For vertical bar:**
df['Employees_status'].value_counts().plot(kind='barh');
# ### 6.3 Pie plot
# A pie plot is also known as a pie chart. A pie plot is a circular graph that represents the total value with its components. The area of a circle represents the total value and the different sectors of the circle represent the different parts. In this plot, the data are expressed as percentages. Each component is expressed as a percentage of the total value.
# In pandas for creating pie plot. We use `kind=pie` in `plot()` function in dataframes columns or series.
df['Segment'].value_counts().plot(
    kind='pie');
# ### 6.4 Box Plot
# A box plot is also known as a box and whisker plot. This plot is used to show the distribution of a variable based on its quartiles. Box plot displays the five-number summary of a set of data. The five-number summary is the minimum, first quartile, median, third quartile, and maximum. It will also be popular to identify outliers.
# We can plot this by one column or multiple columns. For multiple columns, we need to pass columns name in `y` variable as a list.
df.plot(y=['Amount_spent'], kind='box');
# In a boxplot, we can plot the distribution of categorical variables against a numerical variable and compare them. Let's plot it with the Employees_status and Amount_spent columns with pandas `boxplot()` method:
import matplotlib.pyplot as plt
#np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
#fig, ax = plt.subplots(figsize=(6,6))
#df.boxplot(by ='Employees_status', column =['Amount_spent'],ax=ax, grid = False);

# ### 6.5 Histogram
# A histogram shows the frequency and distribution of quantitative measurement across grouped values for data items. It is commonly used in statistics to show how many of a certain type of variable occurs within a specific range or bucket. Below we will plot a histogram for looking Age distribution.
df.plot(
    y='Age',
    kind='hist',
    bins=10
);
# ### 6.6 KDE plot
# A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analogous to a histogram. KDE represents the data using a continuous probability density curve in one or more dimensions.
df.plot(
    y='Age',
    xlim=(0, 100),
    kind='kde'
);
# ### 6.7 Scatterplot
# A scatterplot is used to observe and show relationships between two quantitative variables for different category items. Each member of the dataset gets plotted as a point whose x-y coordinates relate to its values for the two variables. Below we will plot a scatterplot to display relationships between Age and Amount_spent columns. 
df.plot(
    x='Age',
    y='Amount_spent',
    kind='scatter'
)