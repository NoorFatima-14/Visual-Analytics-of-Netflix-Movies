

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


print("Loading dataset...")
df = pd.read_csv(r"C:\Users\LENOVO T450\Downloads\netflix_titles.csv")


df_movies = df[df['type'] == 'Movie'].copy()

print("Total Movies:", len(df_movies))


#  Dataset Summary

print("\nDataset Info:")
print(df_movies.info())

print("\nMissing Values:")
print(df_movies.isnull().sum())



#  Handle Missing Values

df_movies['director'] = df_movies['director'].fillna("Unknown")
df_movies['country'] = df_movies['country'].fillna("Unknown")


df_movies['duration'] = df_movies['duration'].str.replace(" min", "", regex=False)
df_movies['duration'] = pd.to_numeric(df_movies['duration'], errors='coerce')
df_movies['duration'] = df_movies['duration'].fillna(df_movies['duration'].median()).astype(int)

df_movies['release_year'] = pd.to_numeric(df_movies['release_year'], errors='coerce')
df_movies['release_year'] = df_movies['release_year'].fillna(df_movies['release_year'].median()).astype(int)


#  Top 10 Countries Producing Netflix Movies

top_countries = df_movies['country'].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.barh(top_countries.index, top_countries.values)
plt.title("Top 10 Countries Producing Netflix Movies")
plt.xlabel("Number of Movies")
plt.ylabel("Country")
plt.tight_layout()
plt.show()



#  Movies Release Trend Over The Years

trend = df_movies['release_year'].value_counts().sort_index()

plt.figure(figsize=(12,5))
plt.plot(trend.index, trend.values, marker='o')
plt.title("Movie Release Trend Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Movies Released")
plt.tight_layout()
plt.show()



#  Rating Distribution

rating_counts = df_movies['rating'].value_counts()

plt.figure(figsize=(10,6))
plt.barh(rating_counts.index, rating_counts.values)
plt.title("Distribution of Movie Ratings")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()


#  Most Common Genres

genres = df_movies['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(12)

plt.figure(figsize=(10,6))
plt.barh(top_genres.index, top_genres.values)
plt.title("Most Common Genres on Netflix")
plt.xlabel("Number of Movies")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()


# Top Directors

top_directors = df_movies['director'].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.barh(top_directors.index, top_directors.values)
plt.title("Top 10 Most Featured Directors on Netflix")
plt.xlabel("Number of Movies")
plt.ylabel("Director")
plt.tight_layout()
plt.show()


#  Key Insights Summary

print("\n----------------------------")
print("      Key Insights")
print("----------------------------")

print(f"Total Netflix Movies: {len(df_movies)}")
print(f"Country with most movies: {top_countries.index[0]} ({top_countries.iloc[0]})")
print(f"Most common rating: {rating_counts.idxmax()}")
print(f"Most common genre: {top_genres.index[0]}")
print(f"Most featured director: {top_directors.index[0]}")


print("\n Completed Successfully!")
print("*********************************")
