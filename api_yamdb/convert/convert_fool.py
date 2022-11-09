import sqlite3

import pandas as pd

conn = sqlite3.connect('api_yamdb/db.sqlite3')
c = conn.cursor()

genre = pd.read_csv('api_yamdb/static/data/genre.csv')
genre.to_sql('reviews_genre', conn, if_exists='append', index=False)

genre = pd.read_csv('api_yamdb/static/data/category.csv')
genre.to_sql('reviews_category', conn, if_exists='append', index=False)

genre = pd.read_csv('api_yamdb/static/data/comments.csv')
genre.to_sql('reviews_comment', conn, if_exists='append', index=False)

genre = pd.read_csv('api_yamdb/static/data/genre_title.csv')
genre.to_sql('reviews_title_genre', conn, if_exists='append', index=False)

genre = pd.read_csv('api_yamdb/static/data/review.csv')
genre.to_sql('reviews_review', conn, if_exists='append', index=False)

genre = pd.read_csv('api_yamdb/static/data/titles.csv')
genre.to_sql('reviews_title', conn, if_exists='append', index=False)

genre = pd.read_csv('api_yamdb/static/data/users.csv')
genre.to_sql('users_user', conn, if_exists='append', index=False)
