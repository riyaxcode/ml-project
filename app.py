import streamlit as st
import pandas as pd
import pickle
import requests

# --- CSS STYLING ---
st.markdown("""
    <style>
    /* 1. MOVIE CARD STYLES (Hover Effect) */
    .movie-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .movie-img {
        border-radius: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
        cursor: pointer;
    }
    .movie-img:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    .movie-title {
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 5px;
        height: 40px;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }

    /* 2. BUTTON STYLES (Red Color) */
    div.stButton > button {
        background-color: #FF0000; /* Red background */
        color: white;              /* White text */
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    /* Darker red when hovering over the button */
    div.stButton > button:hover {
        background-color: #CC0000; 
        color: white;
        border: none;
    }
    div.stButton > button:active {
        background-color: #990000;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=429d8ef2a929d522ee1b9cb1043e6961&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    st.snow()
    index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies:
        movie_id = movie_list.iloc[i[0]].movie_id
        recommended_movies.append(movie_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# --- Load Data ---
try:
    movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movie_list = pd.DataFrame(movie_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Pickle files not found.")
    st.stop()

st.title("Movie Recommendation System")

option = st.selectbox(
    "Choose your favorite movie to recommend!",
    movie_list['title'].values
)

# This button is now styled by the CSS above
if st.button("Recommend"):
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(option)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.markdown(f"""
                <div class="movie-container">
                    <div class="movie-title">{name}</div>
                    <img src="{poster}" class="movie-img">
                </div>
            """, unsafe_allow_html=True)

st.divider()
st.write("Rate this recommendation:")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
try:
    selected = st.feedback("thumbs")
    if selected is not None:
        st.markdown(f"You selected: {sentiment_mapping[selected]}")
except AttributeError:
    pass