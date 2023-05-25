# ***Creating Custom All-Rounder ChatBot***
1. **Problem Statement**
    - Create an all rounder chatbot that can engage in conversation and answer the same questions related to multiple domains like Science, Technology, History, Geography, News, Sports and many others.
<br>***(if possible try adding features like providing personalized recommendations, updates of ongoing events around the world)***
<br>
<br>

1. **Objective**
  - The chatbot should have the ability to process Natural Language provided by the Humans and should be able to provide relevant & accurate answers or responses according to the queries given to it.
<br>***(If possible try making the chatbot possible to learn continuously and improve itself overtime)*** 

1. **Approaches**
  - Using nltk library for performing tokenization, stemming, classification.
  - Using pickle library for dumping or storing the words & classes.
  - Creating Training data after performing neccessary steps below:

     - Like processing the data
     - Initializing Bag of words
     - creating the base word
  - Using $Sequential$ to arrange the keras layers in an sequential order.
  - Using $3 Dense Layers$ with manually calculated number of neurons.
  - Using $SGD(Stocastic Gradient Descent)$ as optimizer while compiling the model.
  - *Created Function*
      - Tokenize the patterns.
      - Creating Bag Of Words that basically creates an array that contains which $0$ or $1$ for each of the word that exist in the sentences.
      - To predict Class and Filter Out the predictions below a particular threshold$(0.25)$.
      - To retrieve the Responses.
      - To fetch the Final response after predicting the class intent.
      - Finally writing an While loop to take input and reponse with respect to the input given by the user.

1. **Observation**
  - We multiplied between $2-4$ to the previously defined First Neurons$(128)$ as our the number of intents increased, so gradually the number of neurons increases too.
  - Then again multiplying $2\times64 =128$ layers in the second layer.
  - And then Defining the $3rd Layer$ which is the output layer contains the number of neurons that will be equal to the number of intents to predict output intent with the activation set as $softmax.$
  - While Compiling the model we used $SGD(Stochastic Gradient Decent)$ with $Nesterov Accelerated Gradient$ as using it will probably may give us good results with respect to the model.

1. **Learning Outcomes**
- Learned about how does $Sequential$ model actually works based on stack of layers where each layers has exactly one $Input Tensor$ and one $Output Tensor.$
- Learned about how the defined $Neurons$ of each layers matters with respect to the complexity of the dataset being used.
- Learned about how optimzers can boost the probability of getting better results, like in this case using $SGD$ along with $Nesterov Accelerated Gradient$ which is an momentum-based $SGD optimizer$.


**Topic Supported By the ChatBot:** *Science, Technology, Philosophy, History, Geography, Scientist, Currencies, Finance, Disease, Musicians, Entrepreneurs, General Knowledge, and many others.*
