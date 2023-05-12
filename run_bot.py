# **Importing Libraries To Use The ChatBot**
import streamlit as st
from streamlit_chat import message
import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
import json
import random

# Loading The Above Trained Model
# Loading our Intents file
# Loading the unique words stored using Pickle earlier
# Loading The number and name of Classes that was classified and stored at
##   the top most cell using pickle

model = load_model('AssistaBot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


# Defining Function for Tokenizing the patterns
# Basically splitting The Words into Arrays 

## And performing Lemmantization
## Basically stemming each words and creating short form for the words
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# Defining function for Bag Of Words that basically creates an array that contains
# 0 or 1 for each of the word that exist in the sentences
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # Assigning 1 if the current word is in Vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))


# Defining Function For Predicting Class 
# And Filtering Out the prediction below a particular threshold(0.25)
def predict_class(sentence, model):
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # Sorting by Strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Defining Function To retrieve The Response
def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

# Defining Function For retriving the Final Response After Predicting The Class of Intent
def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


def main():
    st.title("Chatbot")

    while True:
        input_key = "input_" + str(random.randint(1, 1000))  # Generate a unique key for the input widget
        confirmation_key = "confirmation_" + str(random.randint(1, 1000))  # Generate a unique key for the confirmation widget

        i = st.text_input(">", key=input_key)

        if i.lower() == 'exit':
            j = st.text_input("Are you sure? (Yes/No)", key=confirmation_key)
            if j.lower() == 'yes':
                break
            elif j.lower() == 'no':
                message(random.choice(["Good to see you back", "Welcome back", "Good to have you back"]))
                continue

        a = chatbot_response(i)  # Replace with your chatbot response logic
        # Assign a unique key to the streamlit_chat widget
        chat_key = "chat_" + str(random.randint(1, 1000))
        message(a, key=chat_key)
        message(a)


        
                          
if __name__ == "__main__":
    main()
  
