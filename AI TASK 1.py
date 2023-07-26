#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk
nltk.download('omw-1.4')
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def preprocess_text(text):
    # Tokenize the text into individual words
    tokens = word_tokenize(text.lower())

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize the words to their base form
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

def compute_similarity(job_description, resume):
    # Preprocess the job description and resume texts
    job_tokens = preprocess_text(job_description)
    resume_tokens = preprocess_text(resume)

    # Create word frequency distributions
    job_freqdist = nltk.FreqDist(job_tokens)
    resume_freqdist = nltk.FreqDist(resume_tokens)

    # Calculate the similarity score
    similarity_score = nltk.jaccard_distance(set(job_freqdist), set(resume_freqdist))

    return similarity_score

def check_candidate(job_description):
    candidate_data = input("Enter the candidate's data: ")

    similarity_threshold = 0.6  # Adjust this threshold as needed

    similarity_score = compute_similarity(job_description, candidate_data)

    if similarity_score <= similarity_threshold:
        print("This candidate is a potential match!")
    else:
        print("This candidate may not be the best fit.")

# Example usage
job_description = "We are looking for a software engineer with experience in Python and machine learning."

check_candidate(job_description)


# In[ ]:




