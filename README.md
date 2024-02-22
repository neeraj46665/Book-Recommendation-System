# Book Recommendation System using Flask

This is a simple book recommendation system implemented using Flask. The system uses collaborative filtering to recommend books based on user input. The recommendation model has been trained on a dataset of books.

## Installation

Make sure you have Python installed. Clone the repository and install the required packages using the following commands:

\`\`\`bash
git clone [https://github.com/your-username/your-repository.git](https://github.com/neeraj46665/Book-Recommendation-System.git)
cd your-repository
pip install -r requirements.txt
\`\`\`

## Usage

Run the Flask application:

\`\`\`bash
python app.py
\`\`\`

Open your browser and navigate to http://127.0.0.1:5000/ to access the home page.

Browse through the popular books displayed on the home page.

If you want personalized recommendations, go to http://127.0.0.1:5000/recommend and enter a book title in the input field.

Click the "Submit" button, and the system will provide you with a list of recommended books based on collaborative filtering.

## Dependencies

- Flask
- Pickle
- NumPy

## Files

- `app.py`: The main Flask application file.
- `models/popular.pkl`: Pickled file containing data about popular books.
- `models/pt.pkl`: Pickled file containing preprocessed data.
- `models/books.pkl`: Pickled file containing information about books.
- `models/similarity_scores.pkl`: Pickled file containing similarity scores for books.

