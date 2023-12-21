import streamlit as st
import pandas as pd
import requests
import pickle

movies_list = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))




def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=f3c1ee617fc510092edff37a39c9e4f5'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def reccomend(movie):
    index = movies[movies["title"]==movie].index[0]
    distance = similarity[index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])

    reccomend_movies=[]
    reccomend_movie_posters=[]
    for i in movie_list[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        reccomend_movies.append(movies.iloc[i[0]].title)
        reccomend_movie_posters.append(fetch_poster(movie_id))
    return reccomend_movies,reccomend_movie_posters



st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Type a movie Name what you want: ",
                   movies['title'].values)


if st.button('Reccomend'):
    names,posters = reccomend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

