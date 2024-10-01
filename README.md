# Movie Recommendation System

This project is a **content-based movie recommendation system** that suggests similar movies based on movie features such as **genre, cast, director, and description**. The app is built using Streamlit and **TF-IDF Vectorizer for feature extraction**, and **cosine similarity for calculating similarity score**s between movies.

## Dataset
The data is sourced from [Indian Regional Movies Dataset](https://www.kaggle.com/datasets/snathjr/indian-regional-movie)
 and contains Bollywood and regional Indian movies and has a shape of (2850, 10), with the following columns:

`movie_id`: IMDb movie ID
`description`: Movie description (1098 null values)
`language`: Movie language (stored as list in string format)
`released`: Release date (651 null values)
`rating`: Movie rating
`writer`: Writer of the movie (stored as list in string format)
`director`: Director(s) of the movie (stored as list in string format)
`cast`: Cast members (stored as list in string format)
`genre`: Movie genre (stored as list in string format)
`name`: Movie title


## Data Preprocessing
*  Dropped rows with null values, reducing the shape to `(1586, 10)`.
*  Dropped unnecessary columns: `released`, `rating`, and `writer`.
*  Converted stringified lists (for `language`, `director`, `cast`, and `genre`) into actual lists.
*  Selected only the first director and first 4 cast members.
*  Created a new `corpus` column by joining the `director`, `cast`, `genre`, `language`, and `description` for each movie.
*  Converted the `corpus` to **lowercase** and applied **lemmatization** to normalize words.

## Feature Extraction & Similarity
*  Used **TF-IDF Vectorizer** to transform the `corpus` into a matrix of shape `(1586, 10210`) where 1586 is the **number of movies**, and 10210 is the **number of unique words**.
   * **TF-IDF (Term Frequency-Inverse Document Frequency)** is used to **convert text into vectors**. It gives **higher importance to rare words**, making it more effective than raw frequency counts.
   *  **Why Use TF-IDF Instead of CountVectorizer?**<br>
        TF-IDF was chosen over CountVectorizer because it **assigns lower weight to common words** and **higher weight to more unique** and relevant words. This results in more accurate recommendations, as important words like unique genres, directors, or cast members are given more emphasis. CountVectorizer would treat all words equally, which could reduce recommendation quality by over-representing frequent but less meaningful words.
*  Calculated **pairwise cosine similarity** between the movies, generating a **similarity score** matrix of shape `(1586, 1586)`.
   *  Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle between them.<br>
   
In the context of this recommendation system, **each movie is represented as a vector based on its features** (e.g., `genre`, `cast`, `director`, and `description`), and **cosine similarity** is used to calculate **how similar each movie is to every other movie**.


## Model
The system recommends the top 5 movies that are most similar to the selected one using **cosine similarity scores**. These scores are based on how close the movie vectors are, which are created using the **TF-IDF** process.


## Future Improvements
*  Integrate a **collaborative recommendation system** that uses user data and ratings to give personalized experience to each user.
*  Explore **hybrid models** by combining content-based and collaborative filtering approaches for improved recommendations.

## Application
The app was built using Streamlit. Users can select a movie, and the app will recommend 5 similar movies.

### App Code (app.py)
The `app.py` script loads two pickle files:

*  `movie_list.pkl`: Preprocessed data containing movie information.
*  `similarity.pkl`: Similarity score matrix.
The app shows the top 5 recommended movies using a simple Streamlit interface.

##  Instructions to Run the App
*  Install the required dependencies by running:
   ```bash 
   pip install -r requirements.txt
   
*  Run the app:
  ```bash
   streamlit run app.py
