ook Recommendation System using Flask (read.md)
This repository contains a simple book recommendation system implemented using Flask and collaborative filtering.

Features:

Recommend books based on user input
Trained on a dataset of books
Popular books list on the homepage
Personalized recommendations based on book title
Installation:

Make sure you have Python installed.
Clone the repository:
git clone [https://github.com/your-username/your-repository.git](https://github.com/neeraj46665/Book-Recommendation-System.git)
Install required packages:
cd your-repository
pip install -r requirements.txt
Usage:

Run the Flask application:
python app.py
Open your browser and navigate to http://127.0.0.1:5000/ to access the home page.

Browse popular books on the homepage.

For personalized recommendations, go to http://127.0.0.1:5000/recommend and enter a book title.

Click "Submit" to see recommended books based on collaborative filtering.

Dependencies:

Flask
Pickle
NumPy
Files:

app.py: Main Flask application file.
models/popular.pkl: Pickled data about popular books.
models/pt.pkl: Pickled preprocessed data.
models/books.pkl: Pickled information about books.
models/similarity_scores.pkl: Pickled similarity scores for books.
