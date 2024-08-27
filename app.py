import streamlit as st
import pickle
import requests
import streamlit.components.v1 as components

# Custom CSS for a professional appearance with enhanced font visibility
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stHeader {
        font-family: 'Trebuchet MS', sans-serif;
        color: #222;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stSelectbox {
        font-size: 16px;
        padding: 5px;
        border-radius: 5px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
        color: #333;
    }
    .stText {
        color: #333;
        font-size: 14px;
        font-weight: 500;
    }
    .stImage > img {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }
    .stImage > img:hover {
        transform: scale(1.05);
    }
    .carousel-container {
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Fetch poster function
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Load movie data and similarity model
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# App header
st.header("🎬 Movie Recommender System")

# Image carousel component
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

# List of movie posters
imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]

# Display image carousel
st.markdown('<div class="carousel-container">', unsafe_allow_html=True)
imageCarouselComponent(imageUrls=imageUrls, height=200)
st.markdown('</div>', unsafe_allow_html=True)

# Movie selection dropdown
selectvalue = st.selectbox("Select a movie from the dropdown", movies_list)

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

# Show recommendations on button click
if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
