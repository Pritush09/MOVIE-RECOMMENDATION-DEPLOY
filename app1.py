import streamlit as st
import pickle
import requests


def fetching_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    # the above is to hit the api and get the required poster for a given movie_id
    data = response.json()
    print(data)
    # data['poster_path'] it is not complete path we ahve do this
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movies_index = movies_list_[movies_list_.title == movie].index[0]
    distance = similarity[movies_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:8]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies_list_.loc[i[0]].id

        recommended_movies.append(movies_list_.loc[i[0]].title)

        # fetching the movies poster
        recommended_movies_posters.append(fetching_poster(movie_id))
    return recommended_movies , recommended_movies_posters

similarity = pickle.load(open('similarity.pkl','rb'))
movies_list_ = pickle.load(open('movies.pkl','rb'))

movies_list_t = movies_list_['title'].values
# if this does not take place then convert the dataframe to dictionary then pickle it

##################### the begining of the website ###########################
st.title('Movies Recommmender System')  # this gives the title to our website

selected_movies = st.selectbox(
    "What will you like to see today",   # this shows the movies in the box
    movies_list_t
)

if st.button("Recommend"):                           # this create a button with name recommend
     names , posters = recommend(selected_movies)

     col1, col2, col3, col4, col5, col6, col7 = st.columns(7)  # this represents the movie and there posters in columnwise orders

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

     with col6:
        st.text(names[5])
        st.image(posters[5])

     with col7:
        st.text(names[6])
        st.image(posters[6])


