import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load models and data
popular_df = pickle.load(open('models/popular.pkl', 'rb'))
pt = pickle.load(open('models/pt.pkl', 'rb'))
books = pickle.load(open('models/books.pkl', 'rb'))
similarity_scores = pickle.load(open('models/similarity_scores.pkl', 'rb'))

# Streamlit App
def main():
    st.set_page_config(
        page_title="Book Recommender System",
        page_icon="📚",
        layout="wide",
    )

    st.title("My Book Recommender")

    # Home Page
    st.header("Top 50 Books")
    display_books(popular_df)

    # Recommendation Page
    st.header("Recommend Books")
    user_input = st.text_input("Enter a book title:")
    if st.button("Submit"):
        recommend_books(user_input)

def display_books(data):
    num_cols = 4
    num_books = len(data)
    col_width = st.get_option("deprecation.showfileUploaderEncoding")
    columns = st.columns(num_cols)

    for i in range(num_books):
        with columns[i % num_cols]:
            # Adjust the width parameter to control image size
            st.image(data['Image-URL-M'].iloc[i], caption=data['Book-Title'].iloc[i], width=200, use_column_width=col_width)
            st.write("**Title:**", data['Book-Title'].iloc[i])
            st.write("**Author:**", data['Book-Author'].iloc[i])

            # Check if 'num_ratings' exists before accessing it
            if 'num_ratings' in data.columns:
                st.write("**Votes:**", data['num_ratings'].iloc[i])

            # Check if 'avg_rating' exists before accessing it
            if 'avg_rating' in data.columns:
                st.write("**Rating:**", round(data['avg_rating'].iloc[i], 2))



def recommend_books(user_input):
    index = np.where(pt.index == user_input)[0]
    if len(index) == 0:
        st.error("Book not found. Please enter a valid book title.")
        return

    index = index[0]
    similar_items = sorted(enumerate(similarity_scores[index]), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    display_books(pd.DataFrame(data, columns=['Book-Title', 'Book-Author', 'Image-URL-M']))

if __name__ == "__main__":
    main()
