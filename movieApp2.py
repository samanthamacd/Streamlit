import streamlit as st
import pandas as pd
import plotly.express as px

df_movies = pd.read_csv('MovieData.csv')

custom_palette = ['#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464']


st.title('Movie Data Insights')

st.header('Movie Revenue Over Time')
selected_genre = st.selectbox('Select a Genre', df_movies['Primary_Genre'].unique())
filtered_data_by_genre = df_movies[df_movies['Primary_Genre'] == selected_genre]
fig1 = px.line(filtered_data_by_genre, x='Year', y='Revenue', title='Revenue Over Time by Genre')
fig1.update_layout(template='plotly_dark', colorway=custom_palette)
st.plotly_chart(fig1)
st.markdown('This line plot shows how movie revenues have varied over time within the selected genre.')

st.header('Distribution of Movie Ratings')
selected_year = st.slider('Select a Year', int(df_movies['Year'].min()), int(df_movies['Year'].max()), 2020)
filtered_data_by_year = df_movies[df_movies['Year'] == selected_year]
fig2 = px.histogram(filtered_data_by_year, x='Rating', title='Movie Ratings Distribution')
fig2.update_traces(marker_color='#FF6F61')
st.plotly_chart(fig2)
st.markdown('This histogram displays the distribution of ratings for movies released in the selected year.')

st.header('Gender Diversity in Top Films')
top_film_each_year = df_movies.loc[df_movies.groupby('Year')['Rating'].idxmax()]
fig3 = px.bar(top_film_each_year, x='Year', y=['Female_Ratio', 'Male_Ratio'], title='Gender Diversity in Top Films Each Year')
fig3.update_layout(template='plotly_white', colorway=custom_palette)
st.plotly_chart(fig3)
st.markdown('This bar chart illustrates the gender diversity in cast and crew of the top-rated film of each year.')

st.header('Director Insights')
selected_director = st.selectbox('Select a Director', df_movies['Director'].unique())
director_movies = df_movies[df_movies['Director'] == selected_director]
fig_director = px.bar(director_movies, x='Year', y='Rating', color='Primary_Genre', title=f'Movies by {selected_director}')
st.plotly_chart(fig_director)
st.markdown('This bar chart shows the movies directed by the selected director, along with their ratings.')