import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movies data
df = pd.read_csv("movies.csv")

st.title("Task 4: Movie Recommender")
st.write("Select a movie you like, and get recommendations!")

# Movie selection
movie_list = df['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    # Content-based recommendation
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df['genres'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    
    idx = df[df['title'] == selected_movie].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # top 5 similar
    movie_indices = [i[0] for i in sim_scores]
    
    st.write("### You may also like:")
    for i in movie_indices:
        st.write(f"- {df['title'][i]}")
