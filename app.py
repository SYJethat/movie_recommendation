import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response= requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list =sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommend_poster_movie = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch the movie poster
        recommend_poster_movie.append(fetch_poster(movie_id))  
    return recommended_movies, recommend_poster_movie


st.title("Movie Recomendation System")

movie = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie)

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
    "How would you like to be Movies ",
    movies['title'].values)
if st.button('Recommend'):
    name,poster = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5,gap='large')
    with col1:
        #st.header(name[0])
        # st.image(poster[0])
        st.image(poster[0], caption=name[0])
    with col2:
        # st.header(name[1])
        # st.image(poster[1])
        st.image(poster[1], caption=name[1])

    with col3:
        # st.header(name[2])
        # st.image(poster[2])
        st.image(poster[2], caption=name[2])
    with col4:
        # st.header(name[3])
        # st.image(poster[3])
        st.image(poster[3], caption=name[3])
    with col5:
        # st.header(name[4])
        # st.image(poster[4])
        st.image(poster[4], caption=name[4])
        
    
st.caption('Made by :sparkling_heart: with  :red[_Suraj Yadav_ ]...:sunglasses:')

