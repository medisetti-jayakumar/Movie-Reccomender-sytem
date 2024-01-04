# 1. MOVIE RECCOMENDER SYSTEM

### This app automatically suggests the 5 movie names related to the entered movie whatever you enter.

    - when we selected the movie name from the suggestions or entered the movie name in entry box what we need to search.
    - just click on the reccomend button .
    - then, automatically suggests the 5 movie names rellated to that movie name.

### About the Movie Reccomender System
A movie recommender system is a type of software application that provides personalized movie suggestions to users based on their preferences, behavior, or past interactions. These systems use various algorithms and techniques to analyze user data and recommend movies that the user is likely to enjoy. There are two primary types of movie recommender systems:

#### >> Content-Based Recommender Systems:

    - These systems recommend movies based on the characteristics of the movies and the user's preferences.
    - Features such as genre, actors, directors, and keywords are used to create a profile of each movie.
    - User preferences are also modeled based on their interactions with previously watched movies.
    - Recommendations are made by comparing the user profile with the features of available movies.

#### >> Collaborative Filtering Recommender Systems:

    - These systems recommend movies based on the preferences and behaviors of similar users.
    - Users are grouped together based on their movie-watching history, and recommendations are made by considering the preferences of users in the same group.
    - Collaborative filtering can be user-based (finding similar users) or item-based (finding similar movies).

#### >> Hybrid Recommender Systems:

    - Hybrid systems combine both content-based and collaborative filtering approaches to provide more accurate and diverse recommendations.
    - By leveraging the strengths of both methods, hybrid systems aim to overcome the limitations of individual approaches.

#### >> Matrix Factorization:

    - Matrix factorization techniques, such as Singular Value Decomposition (SVD) or Alternating Least Squares (ALS), are often used in collaborative filtering.
    - These techniques decompose the user-item interaction matrix to identify latent factors that represent user and item preferences.
    Natural Language Processing (NLP):

 In some advanced recommender systems,
 #### >> natural language processing techniques 
    - NLP tecxhniques are employed to analyze textual data, such as movie reviews or descriptions.
    This information can be used to enhance the understanding of user preferences and improve recommendations.
    - Popular examples of movie recommender systems include those used by streaming platforms like Netflix, Amazon Prime Video, and Hulu. These systems play a crucial role in enhancing user experience by helping users discover new and relevant content based on their tastes and preferences

###### The entire code will be here:
    [Entire code](https://github.com/medisetti-jayakumar/student-mark-predictor)

## 2. languages and Tools used

- STREAMLIT 
- PYTHON
- NLTK (COUNT VECTORIZER, COSINE SIMILSRITY)


## 3. installed packages


### install the streamlit library
    pip install m- streamlit

## Streamlit 
[click here for streamlit journey](https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/)

#### > Streamlit for Python:

Streamlit is a Python library. It simplifies turning data scripts into interactive web apps.

    #### > Easy Development:

    To Write top-down, declarative code for Minimal effort for web app creation.

    #### > Interactive Widgets:

    It Includes widgets (e.g., sliders, buttons) to Enables real-time data interaction.

    #### > Data Science Integration:

    It Integrates with Pandas, Matplotlib, Plotly to Ideal for showcasing data insights.

    #### > Simple Sharing and Deployment:

    Easy sharing and deployment.It allows others to interact without coding
### install the nltk
    pip install nltk

## About NLTK
[click here for nltk journey](https://www.nltk.org/)

    #### > Text Processing Toolbox:

    NLTK is a Python library for natural language processing (NLP).
    It offers tools for tasks like tokenization, stemming, and parsing.

    #### > Rich Linguistic Resources:

    NLTK provides linguistic resources and pre-trained models.
    This wealth of data supports research and experimentation in NLP.

    #### > Algorithms for NLP:

    NLTK implements algorithms for tasks like part-of-speech tagging and sentiment analysis.
    It serves as a comprehensive toolkit for building NLP models.

    #### > Education and Research Hub:

    NLTK is widely used in education and research.
    It aids teaching computational linguistics and supports advanced NLP exploration.

    #### > Community-Driven and Extensible:

    NLTK has an active community and is extensible for Continuous development and contributions keep it relevant in the evolving field of NLP.

But, here we simply implemented the project by the cosine-similarity
### install some python libraries
Numpy, Pandas, ast....



#### Activate the environment to the streamlit application


 ## 4. Download the Data

[Download Dataset](https://github.com/medisetti-jayakumar/Movie-Reccomender-sytem/blob/main/Dataset.zip)


## 5. Model building

    In this notebook , build the machine learning model for the reccomender system.

[jupyter-notebook-will be here](https://github.com/medisetti-jayakumar/Movie-Reccomender-sytem/blob/main/movie_reccomender_notebook.ipynb)

## 6. Creating the stream-lit application
    The entire stremlit application code will with the reccomender system model be here

[stream-lit application code](https://github.com/medisetti-jayakumar/Movie-Reccomender-sytem/blob/main/movie.py)

## 7. syntax to run the streamlit application
    streamlit run movie.py
Here , movie.py is the application file
 ## 8. Result
#### The input page looks like as follows:
![Alt text](<image_section/Screenshot 2023-12-21 144017.png>)

#### >> when we click on the entry box, automatically suggests the movie names
![Alt text](<image_section/Screenshot 2023-12-21 144045.png>)
#### >> select or enter the movie name what you need then click on reccomend button
![Alt text](<image_section/Screenshot 2023-12-21 144056.png>)
#### >> The result page looks like as follows:
![Alt text](<image_section/Screenshot 2023-12-21 144107.png>)
##### >> Again i wann search for pirates of the carribean  movie name
![Alt text](<image_section/Screenshot 2023-12-21 144222.png>)
#### >> The result page looks like as follows:
![Alt text](<image_section/Screenshot 2023-12-21 144243.png>)


