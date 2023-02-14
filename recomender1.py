import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class recomender_system :
    
    
    movies_data  = pd.read_csv('C:\c++\My codes\python\project\movie rent system\data\movies.csv')
    
    
    def feature_selection(self) :
        
        selected_features = ['genres','keywords','tagline', 'cast', 'director','production_companies']
        for feature in selected_features :
                self.movies_data[feature] = self.movies_data[feature].fillna('')       ################# Change Fillna to empty #############
        
        combined_features = self.movies_data['genres'] + ' ' + self.movies_data['keywords'] + ' ' + self.movies_data['tagline'] +' '+ self.movies_data['cast'] + ' ' + self.movies_data['director'] + '' + self.movies_data['production_companies']
        
        return combined_features
    
    def feature_vectoraization (self) :
        
        vectorizer  = TfidfVectorizer()
        feature_vectors = vectorizer.fit_transform(self.feature_selection())
        
        return feature_vectors
    
    def cosinesimilarity(self) :
        
        similarity = cosine_similarity(self.feature_vectoraization(),self.feature_vectoraization())
        return similarity
    
    def getmovies(self,sorted_similar_movies) :
        
        # print('Movies suggested for you :')
        self.sorted_similar_movies = sorted_similar_movies
        i = 1 
        movies1 = []

        for movie in self.sorted_similar_movies :
            index = movie[0]
            title_form_index = self.movies_data[self.movies_data.index == index]['title'].values[0]
            
            if (i < 31 ) :
                # print( i , "." , title_form_index)
                movies1.append(title_form_index)
                
                i+=1
                
        return movies1        
                
    def recomend (self,movie_name) :
        self.movie_name = movie_name
        
        # movie_name = input("Search movies : ")
        
        similarity = self.cosinesimilarity()

        list_of_all_titles = self.movies_data['title'].tolist()
        # print(self.movie_name)

        close_match = difflib.get_close_matches(self.movie_name,list_of_all_titles)
        #print("got Here!")
        match = close_match[0]
        # print(close_match)
        index_of_the_movie = self.movies_data[self.movies_data.title == match]['index'].values[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score,key = lambda x : x[1] , reverse=True)
        
        movielist = self.getmovies(sorted_similar_movies) 
        # print(movielist)
        return movielist

        
# mrs = recomender_system()

# r = mrs.recomend('Avatar') 

# print(r)