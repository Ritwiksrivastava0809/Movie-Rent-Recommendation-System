# Movie-Rent-Recommendation-System

This is a desktop application built using Tkinter that recommends movies to users based on their rental history. The recommendations are generated using a machine learning algorithm based on cosine similarity. User data is stored in a MySQL database, and the database connection is done using Python's mysql-connector package.

## Project Overview

The project consists of the following steps:

  Data collection: Movie data is collected from an external API or database. For this project, we used the MovieLens dataset, which contains movie ratings and tags from users. We used a subset of this data that contains 10,000 movies and 100,000 ratings.

  Data preprocessing: The movie data is preprocessed by cleaning and transforming it into a format suitable for use with the machine learning algorithm. The data is then split into training and testing sets.

  Model training: A machine learning model is trained on the training set using cosine similarity. The model takes in a user's rental history and outputs a list of recommended movies. The model is trained using scikit-learn's cosine_similarity function.

  Model prediction: The trained model is used to generate movie recommendations for the user based on their rental history.

  Database management: User data is stored in a MySQL database using Python's mysql-connector package. The database stores user information such as name, address, and rental history.

  GUI design: The desktop application is built using Tkinter and designed to allow users to enter their rental history, view recommended movies, and manage their account information
  
  
## Project Structure
  
  The project is structured into the following folders:

  data: contains the movie data in CSV format
  models: contains the trained model and the vectorizer used for data preprocessing
  database: contains the SQL scripts used to create the database tables
  src: contains the code for the desktop application
  
## Requirements

To run the project, you need to have Python 3.7 or later installed. The following Python packages are also required:

  pandas
  numpy
  scikit-learn
  mysql-connector-python
  tkinter

You can install the required packages by running the following command:
    
    pip install -r requirements.txt
    
## Usage

### Model Training and Prediction

To train the machine learning model and generate movie recommendations, run the model_training.py script in the src folder. This script loads the movie data from the data folder, trains the machine learning model, and generates movie recommendations for a specified user's rental history.

### Desktop Application

To run the desktop application, navigate to the src folder and run the following command:
    
    python main.py

This will launch the desktop application. Users can enter their rental history, view recommended movies, and manage their account information using the GUI.

## Contributing

If you would like to contribute to this project, please create a pull request. We welcome contributions of all kinds, including bug fixes, new features, and improvements to documentation.

 
