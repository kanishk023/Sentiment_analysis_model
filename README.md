# Sentiment_analysis_model
Created a Sentiment analysis model using Machine Learning and NLP techniques to gain Real Time Analysis on customer reviews with Data Cleaning and 
Processing on a large 32M+ Dataset.

## About the data:
The Dataset contains 32M+ records in raw JSON format.
The raw data was cleaned and processed and converted to csv with desired columns.


## Creating The NLP model

### Data Preprocessing
1. The Dataset was processed and review ratings were categorised into "Positive Reviews" and "Negative Reviews".
2. NUll Values were removed.

### Data Split

The data was split in the following way:
1. 75% of the data for training.
2. 25% of the data for testing.

### Training the Model

1. A set of vectors containing the count of word occurrences was created.
2. NLP techniques (StopWords, PorteStemmer) were used to create a set of vectors of more important words.
3. TF-IDF Vectorizer was used for word for word embedding


## Creating the User Interface

The data was cleaned using using python and its different libraries and a Loacally Hosted Web based UI Page was created using DASH


Dash and its various components used are

```sh
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc
```


A UI tab was created with 2 options:
* A textbox Area to analyze the sentimens of a 'user input' customer review.
* A dropdown with some sample reviews to choose from, That are scrapped from a product page from 'etsy.com' using **BeautifulSoup**, and **Selenium**.

![image](https://user-images.githubusercontent.com/73426895/106101585-1a40a480-6164-11eb-87f3-46509a5992c0.png)



## Result

The best model(the one with the best roc_auc_score) was saved in a Pickle file.<br>

**91% accuracy** was achieved on the test set.<br>


## Final Notes

What's in the files?

1. **App_UI.py** has the code to locally host the solution.
2. **Scrapper.py** has the code of user reviews that was scrapped form a product page using **BeautifulSoup**, and **Selenium**.
3. **pickle_model.pkl** has the sentiment analysis model.<br>
It can be restored and used as follows:

```
file = open ('pickle_model.pkl', 'rb')    
    pickle_model = pickle.load(file)
```

Thank You!


