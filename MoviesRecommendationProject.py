#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


movies_data= pd.read_csv("movies.csv")


# In[3]:


movies_data.head()


# In[4]:


movies_data.shape


# In[5]:


selected_features=['genres','keywords','tagline','cast','director']


# In[6]:


print(selected_features)


# In[9]:


for feature in selected_features:
    movies_data[feature]=movies_data[feature].fillna('')


# In[12]:


combined_feature = movies_data['genres']+ ''+movies_data['tagline']+ ''+movies_data['cast']+ ''+movies_data['director']


# In[14]:


print(combined_feature)


# In[16]:


vectorizer = TfidfVectorizer()


# In[18]:


feature_vectors = vectorizer.fit_transform(combined_feature)


# In[19]:


print(feature_vectors)


# In[20]:


similarity = cosine_similarity(feature_vectors)


# In[21]:


movie_name = input("Enter your favourite movie name: ")


# In[22]:


list_of_all_titles = movies_data['title'].tolist()


# In[23]:


print(list_of_all_titles)


# In[24]:


find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)


# In[25]:


print(find_close_match)


# In[26]:


close_match= find_close_match[0]
print(close_match)


# In[29]:


index_of_the_movie= movies_data[movies_data.title == close_match]['index'].values[0]


# In[30]:


similarity_score= list(enumerate(similarity[index_of_the_movie]))


# In[31]:


print(similarity_score)


# In[32]:


len(similarity_score)


# In[33]:


sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1], reverse=True)


# In[34]:


print(sorted_similar_movies)


# In[42]:


print('movies recommended for you: \n')
    
i = 1
    
for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index= movies_data[movies_data.index==index]['title'].values[0]
        if (i<11):
            print(i, '',title_from_index)
            i+=1


# In[51]:


#Taking the value from the user 
movie_name = input("Enter your favourite movie name: ")
#Creating a list with all the movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist()
#Finding the close match given by the user 
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match= find_close_match[0]
#Finding the index of the movie with title 
index_of_the_movie= movies_data[movies_data.title == close_match]['index'].values[0]
#getting s lidt of similar movies
similarity_score= list(enumerate(similarity[index_of_the_movie]))
#Sorting the movies based on their similarity score
sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1], reverse=True)
#Printing the name of similar movies based on the index
print('movies recommended for you: \n')
    
i = 1
    
for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index= movies_data[movies_data.index==index]['title'].values[0]
        if (i<5):
            print(i, '',title_from_index)
            i+=1

