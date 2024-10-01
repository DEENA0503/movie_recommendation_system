import pickle
import streamlit as st

# heading
st.header('Movie Recommender')

# loading pkl files
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))



def recommend(movie_name):
    # getting the index of the movie drom the dataframe
    movie_index = movies[movies['name'] == movie_name].index[0]
    
    # fetching similarity score from the similarity matrix using the index
    # coverting it into enumerate object to fetch the index of movie along with the similarity score
    # sorting the similarity scores in descending order 
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
       # fetching the names of recommended movies
        recommended_movie_names.append(movies.iloc[i[0],1]) 

    return recommended_movie_names


# fetching movie names for selectbox
movie_list = movies['name'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list )


if st.button('Show Recommendation'):

    recommended_movie_names = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    img_path = "image.png"
    # showing all 5 recommended movies
    with col1:
        st.text(recommended_movie_names[0])
        st.image(img_path)
    with col2:
        st.text(recommended_movie_names[1])
        st.image(img_path)
    with col3:
        st.text(recommended_movie_names[2])
        st.image(img_path)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(img_path)
    with col5:
        st.text(recommended_movie_names[4])
        st.image(img_path)