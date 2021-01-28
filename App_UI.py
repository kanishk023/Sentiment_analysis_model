# IMPORTING THE LIBRARIES
import numpy as np
import pandas as pd
import pickle
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output 

import plotly.express as px


from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer




# INTRODUCE GLOBAL VARIABLE
app = dash.Dash()
project_name = None
    


# FUNCTIONS
def load_model ():
    
    global df
    df = pd.read_csv('balanced_reviews.csv')
    
    global pickle_model
    file = open ('pickle_model.pkl', 'rb')    
    pickle_model = pickle.load(file)

    
    global vocab
    file = open("feature.pkl", 'rb') 
    vocab = pickle.load(file)
    
    
    global etsy_sample
    etsy_sample = pd.read_csv('newreview.csv')



def open_browser():
    # Open the default web browser
    webbrowser.open_new('http://127.0.0.1:8050/')


def check_review(reviewText):
    
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace", vocabulary = vocab)
    reviewText = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))


    return pickle_model.predict(reviewText)


def create_app_ui():
    main_layout = html.Div(
        children  = [
        html.H1(children='Sentiments Analysis with Insights', id='Main_title', style={'text-align': 'center' }),
 
    
           #piechart 
        dcc.Dropdown(id='chart',
                 options=[
                     {'label':'Chart','value':'overall'}],
                 value='overall',
                 multi=False,
                 clearable=False,
                 style={'width':"50%"}
                 ),
    
        dcc.Graph(id='piechart'),
        
    
            #TEXTBOX TO ENTER USER DATA    
        html.H1(children = 'Check Your Sample Review Here', id = 'Main_title3'),
        html.Div(dcc.Textarea(
                                id='textarea_review',
                                placeholder='Enter the review here...',
                                style={'width': '100%', 'height': 100}
                                )
                ),

        html.H2(id = 'result', children = None , style = {'color':'red'}),
        
        
                    # DROPDOWN TO CHECK REVIEW
        html.H1(children = 'Select A Sample Review From Dropdown', id = 'Main_title3'),
        html.Div(dcc.Dropdown(
                                id = 'dropdown1', 
                                options =  [{'label': i,'value': i} for i in etsy_sample['reviews_df']],
                                placeholder = 'Enter Sample Review Text Here...',
                                style={'background':'rgb(225, 225, 225)'}, optionHeight=80
                                )
                ),
        html.Button(children='Find Review', id='button_click', n_clicks=0),
        html.Br(),
        html.H2(children=None, id='result_2', style = {'color':'red'}),
        html.Br()  
        
        ]        
        )

    return main_layout




@app.callback(
    Output("piechart", "figure"), 
    [Input("chart", "value")
     ])
def generate_chart(chart):
    dff=df
    
    fig = px.pie(
        data_frame=dff,
        names=chart)
    return fig




@app.callback(
                Output('result','children'),
                [Input('textarea_review', 'value')]
                )
def update_app_ui(textarea_value):
    
    
    result_list = check_review(textarea_value)
    
    if (result_list[0] == [0]):
        result = 'Negative'
    elif (result_list[0] == [1]):
        result = 'Positive'
    else:
        result = ' '
        
        
    return result

        

@app.callback(
                Output('result_2', 'children'),
                [Input('dropdown1', 'value')]
                )
def update_dropdown(dropdown_value):
    
    result_list = check_review(dropdown_value)
    
    if (result_list[0] == [0]):
        result = 'Negative'
    elif (result_list[0] == [1]):
        result = 'Positive'
    else:
        result = ' '
        
    return result
    



# Main Function to control the Flow of your Project
def main():
    load_model()    
    open_browser()
    

    global project_name
    project_name = "Sentiments Analysis with Insights" 
      
    global app
    app.layout = create_app_ui()
    app.title = project_name
    # go to https://www.favicon.cc/ and download the ico file and store in assets directory 
    app.run_server() 
  
    app = None
    project_name = None




if __name__ == '__main__':
    main()
