import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0d538f0d92ffc811f567e1aa87b9621b'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recommend(movie):
    # Find the index of the movie
    movie_index = movies[movies['title'] == movie].index[0]

    # Get the similarity scores for the selected movie
    distances = similarity[movie_index]

    # Get a sorted list of (index, similarity score) for the most similar movies
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Fetch the titles of the recommended movies
    recommended_movies = []
    recommended_movies_poster =[]

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender')

# Dropdown for movie selection
selected_movie_name = st.selectbox("Select a movie", movies['title'].values)


if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Define columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], use_container_width=True)
            # Set the movie name below the poster with a lighter font color
            st.markdown(
                f"<div style='text-align: center; color: grey; font-size: 16px;'>{names[idx]}</div>",
                unsafe_allow_html=True,
            )



st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: darkgrey;
    }
    label {
        font-size: 25px !important; 
        color: grey;
    }
    /* Style for the dropdown box */
    .stSelectbox > div {
        background-color: grey; 
        color: white; 
        border-radius: 8px; 
        font-size: 16px;
    }
    h1 {
       color: white;
        text-align: center;
    }
    
    
    <style>
    .stButton > button {
        background-color: black; 
        color: red; /* White text */
        font-size: 16px; /* Font size */
        border-radius: 8px;
    </style>
    """,
    unsafe_allow_html=True,
)