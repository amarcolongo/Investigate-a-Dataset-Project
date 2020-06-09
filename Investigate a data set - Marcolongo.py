#!/usr/bin/env python
# coding: utf-8

# # Project: Investigating movie data
# 
# ## Table of Contents

# ## Introduction
# In this project I will be analyzing various data for several movies. I will examine the relationship between both budget and revenue as well as ratings and revenue. 

# ## Data Wrangling

# In[221]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[222]:


movie_data = pd.read_csv(r"C:\Users\yankeeh8er\Desktop\python_work\tmdb-movies.csv")


# ## Let's check and see what we are working with

# In[223]:


movie_data.head()


# From the previous query we see that we have 21 different columns in our data. Next we will look at exactly what each column represents. 

# In[224]:


movie_data.info()


# ### Next I will cross-reference the columns to find any potential correlations between them

# In[225]:


movie_data.corr()


# **Results**: Ignoring obvious matches, like budget and budget_adj, we see that the strongest correlations are between revenue and vote count, and budget and revenue. 

# ## Exploratory Data Analysis
# 
# 
# ### What factors are predictive of financial success for a particular movie?
# *To answer this question I will examine the relationship between budget and revenue, and revenue and vote count*

# In[226]:


df = movie_data


# In[227]:


print(df)


# Next I will define several variables to make it easier to create graphs

# In[228]:


movie_budget = movie_data['budget']
movie_revenue = movie_data['revenue']
movie_vote_count = movie_data['vote_count']


# In[229]:


print(movie_budget.head(), movie_revenue.head(), movie_vote_count.head())


# In[230]:


data_set1 = movie_data.loc[: ,['revenue','budget']]


# In[231]:


data_set1.plot()
plt.title('Revenue vs Budget')
plt.xlabel('Budget in 10 Thousands of $')
plt.ylabel('Revenue in Billions of $');


# ### Analysis:
#     We see from the graph that the peaks in budget are almost always asscociated with a peak in revenue. To check this more closely I will calculate the correlation between both revenue and budget. 

# In[232]:


df['revenue'].corr(df['budget'])


# ### Results:
#     From looking at the correlation function we see that their is a positive correlation of 0.73 between budget and revenue. This is a strong positive correlation and we can infer from this that the variables are closely related to one another. 

# # Next Steps

#  I will next compare the revenue and the vote count to determine if their is a link between critical acclaim and profit.
#  Before I can compare revenue and vote_count I will need to adjust the revenue so that it can be shown on the same scale as the vote count. I will definie a new variable scaled_revenue which will be revenue divided by 100000. I will then add this column to our movie_data. 

# In[233]:


scaler = lambda x: x/100000
scaled_revenue = df['revenue'].apply(scaler)
new_movie_data = df['scaled_revenue'] = scaled_revenue


# In[234]:


data_set2 = df.loc[: ,['scaled_revenue','vote_count']]


# In[235]:


data_set2.plot()
plt.title('Scaled Revenue vs Vote Count')
plt.xlabel('vote_count in 10 Thousands')
plt.ylabel('Revenue in Billions of $')
plt.ylim([-1,10000]);


# ### Analysis:
#     From this graph it is clear to see that there is a very strong connection between revenue and critical acclaim. In the next section I will look at the coorelation between these quantities. 

# In[236]:


df['scaled_revenue'].corr(df['vote_count'])


# ### Results:
#      By examining the coorelation between our variables we see that there is a very strong connection between revenue and vote count. This result makes it clear to see why Hollywood studios spend so much money on Oscar campaigns each year. Getting critics to vote for a movie is better predictor of financial success then even spending lots of money on a films budget. 

# # Next Steps

#   I will next look at the relationship between a films runtime and it's revenue. Thier are 2 school's of thought on this subject. The first is that audiences are less likely to go to the theaters to see a long movie due to people being busy and such. The second is that people are more likely to go see a longer movie in theathers due to them feeling like they are getting more for their money watching a longer film. I will analyze revenue versus run time to see if there is any connection between the two. 

# In[237]:


data_set3 = df.loc[: ,['scaled_revenue','runtime']]


# In[238]:


data_set3.plot()
plt.title('Scaled Revenue vs Runtime')
plt.xlabel('Runtime in Minutes')
plt.ylabel('Revenue in Billions of $')
plt.ylim([-1,2500]);


# ### Analysis:
#     From this graph it is clear that there is little to no relationship between a movies runtime and it's revenue. I will next check the coorelation between the 2 just to be sure but I expect a very weak coorelation. 

# In[239]:


df['scaled_revenue'].corr(df['runtime'])


# ### Results:
#     As expected we see a very weak coorelation. It is clear that increasing a movies runtime has no effect on how much money the movie will make. One interesting conclusion from this is that longer runtimes did not cause the movies to be less profitable either. The main conclusion that can be drawn from this is that audiences will see the movies that they want to see regardless of how long or short the movies are. 

# # Conclusion:
#    In this paper I set out to compare one dependent variable, the revenue, to three different independent variables, the budget, the critical reception, and finally the runtime. What I found was that the best predictor of financal success for a movie is the critical reception that the film got. For studios critical reception in the one thing that they lest control, the big studios throw Oscar parties and give gifts to the voters, but it is hard to know what effect if any that actually has on how they vote. The second strongest coorelation was between budget and revenue. This is an area that is firmly in the studio's control. We are definitely seeing more and more big budget movies each year, and I believe that is in large part due to this coorelation. 

# In[ ]:




