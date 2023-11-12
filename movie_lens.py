#!/mnt/c/Users/deepe/Documents/jupyter-books/vscode/venv/bin/python
# coding: utf-8

# Importing necessary libraries
import pandas as pd
import numpy as np

# Reading datasets from CSV files
movie = pd.read_csv("movie.csv")
user = pd.read_csv("user.csv")
ratings = pd.read_csv("ratings.csv")

# Data Overview

# Display the first 5 rows of the user dataset
user.head()

# Check the dimensions (number of rows and columns) of the user dataset
user.shape

# Get data types and missing values information for the user dataset
user.info()

# Display the statistical summary of the user dataset
user.describe()

# Display the first 5 rows of the movie dataset
movie.head()

# Check the dimensions of the movie dataset
movie.shape

# Get data types and missing values information for the movie dataset
movie.info()

# Display the statistical summary of the movie dataset
movie.describe()

# Display the first 5 rows of the ratings dataset
ratings.head()

# Check the dimensions of the ratings dataset
ratings.shape

# Get data types and missing values information for the ratings dataset
ratings.info()

# Display the statistical summary of the ratings dataset
ratings.describe()

# How many movies belong to a particular genre?

# List of genres
genres = ['Action', 'Adventure', 'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama',
           'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

# Count the number of movies in each genre
movie[genres].sum().sort_values(ascending=False)

# Find movies with more than one genre
movie["Number of Genres"] = movie.loc[:, genres].sum(axis=1)
movies_with_multiple_genres = movie[movie['Number of Genres'] > 1]
movies_with_multiple_genres.shape

# Which movies have been most preferred by users?

# Merge the movie and ratings datasets
# Merge the movie and ratings datasets
df_merge = movie.merge(ratings, on='movie id', how='inner')

# Convert the 'rating' column to numeric, coercing non-numeric values to NaN
df_merge['rating'] = pd.to_numeric(df_merge['rating'], errors='coerce')

non_numeric_ratings = df_merge[~df_merge['rating'].apply(lambda x: str(x).isnumeric())]
print("## non_numeric_ratings ##")
print(non_numeric_ratings)

non_numeric_ratings = df_merge[~df_merge['rating'].apply(lambda x: str(x).isnumeric())]
print("## non_numeric_ratings ##")
print(non_numeric_ratings)

# Check for non-numeric values in the 'movie title' column
non_numeric_titles = df_merge[~df_merge['movie title'].str.isnumeric()]
print("## non_numeric_titles ##")
print(non_numeric_titles)

df_merge['rating'] = pd.to_numeric(df_merge['rating'], errors='coerce')


# Filter out rows with non-numeric ratings
df_merge = df_merge[df_merge['rating'].apply(lambda x: str(x).isnumeric())]

# Convert the 'rating' column to numeric
df_merge['rating'] = pd.to_numeric(df_merge['rating'])

# Calculate the average rating by movie title
avg_rating = df_merge.groupby(['movie title'])['rating'].mean().reset_index()

# # # Get the average ratings for each movie
# avg_rating = df_merge.groupby(['movie title']).mean()[['rating']].reset_index()

# Rename the 'rating' column to 'Avg_rating'
avg_rating.rename(columns={'rating': 'Avg_rating'}, inplace=True)

# Display the top-rated movies based on average rating
top_rated_movies = avg_rating.sort_values(ascending=False, by='Avg_rating')

# Display movies with the highest average rating (5.0)
top_rated_movies[top_rated_movies['Avg_rating'] == 5.0]

# Find movies with the most ratings
movie_count = df_merge.groupby(['movie title'])['rating'].count().reset_index()
movie_count.rename(columns={'rating': 'Rating_counts'}, inplace=True)
movie_count.sort_values(ascending=False, by='Rating_counts').head()

# Merge the movie_count and movie datasets
movie_100 = movie_count[movie_count['Rating_counts'] > 100]
df_top = avg_rating.merge(movie_100, on='movie title', how='inner')

# Display top-rated movies with more than 100 ratings
top_rated_movies_100 = df_top.sort_values(ascending=False, by='Avg_rating').head(25)
top_rated_movies_100

# Extract insights about the relationship between user demographics and movie ratings

# Merge all three datasets (movie, user, and ratings)
df_merge_all = df_merge.merge(user, on='user id', how='inner')

# Explore user demographics
user['gender'].value_counts(normalize=True)
df_merge_all.groupby('gender').rating.mean()

df_merge_all.groupby('occupation').rating.mean().sort_values(ascending=False)
df_merge_all.groupby(['occupation', 'gender']).rating.mean()
