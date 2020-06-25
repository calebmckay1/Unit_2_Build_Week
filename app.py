import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pickle

########### Initiate
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='CHD'



########### layout

app.layout = html.Div(children=[
    html.H1('Risk Of Heart Disease'),
    html.Div([
            html.H6('Age'),
                dcc.Slider(
                    id='slider-1',
                    min=18,
                    max=73,
                    step=1,
                    marks={i:str(i) for i in range(18, 74, 5)},
                    value=35
                ),
                html.Br(),

            html.H6('BMI'),
                dcc.Slider(
                    id='slider-2',
                    min=10,
                    max=70,
                    step=1,
                    marks={i:str(i) for i in range(10, 71, 5)},
                    value=30
                ),
                html.Br(),
                
            html.H6('Total Cholestrol'),
                dcc.Slider(
                    id='slider-3',
                    min=100,
                    max=700,
                    step=10,
                    marks={i:str(i) for i in range(100, 701, 50)},
                    value=250
                ),
                 html.Br(),

            html.H6('Diastolic Blood Pressure'),
                dcc.Slider(
                    id='slider-4',
                    min=40,
                    max=160,
                    step=2,
                    marks={i:str(i) for i in range(40, 161, 20)},
                    value=100
                ),
                html.Br(),

            html.H6('Systolic Blood Pressure'),
                dcc.Slider(
                    id='slider-5',
                    min=60,
                    max=300,
                    step=10,
                    marks={i:str(i) for i in range(60, 301, 20)},
                    value=140
                ),
                html.Br(),

            html.H6('Heart Rate'),
                dcc.Slider(
                    id='slider-6',
                    min=30,
                    max=180,
                    step=5,
                    marks={i:str(i) for i in range(30, 181,15)},
                    value=75
                ),
                html.Br(),

            html.H6('Glucose Level'),
                dcc.Slider(
                    id='slider-7',
                    min=40,
                    max=400,
                    step=10,
                    marks={i:str(i) for i in range(40, 401, 40)},
                    value=100
                ),
                 html.Br(),


             html.H6('Cigarettes Per Day'),
                dcc.Slider(
                    id='slider-8',
                    min=0,
                    max=70,
                    step=1,
                    marks={i:str(i) for i in range(0, 71,5)},
                    value=8
                ),
                
                
                
            
                
                html.Br(),
                html.H6('# of Neighbors:'),
                dcc.Dropdown(
                    id='k-drop',
                    options=[{'label': i, 'value': i} for i in [5,10,15,20,25]],
                    value=5
                ),
         
        html.H6(id='message', children='output is here'),
    ]),
])



@app.callback(Output('message', 'children'),
              [Input('k-drop', 'value'),
               Input('slider-1', 'value'),
               Input('slider-2', 'value'),
               Input('slider-3', 'value'),
               Input('slider-4', 'value'),
               Input('slider-5', 'value'),
               Input('slider-6', 'value'),
               Input('slider-7', 'value'),
               Input('slider-8', 'value')])
def display_results(k, value0, value1,value2, value3, value4, value5, value6, value7):
    # read in the correct model
    file = open(f'resources2/model_k{k}.pkl', 'rb')
    model=pickle.load(file)
    file.close()
    # define the new observation from the slide values
    new_observation=[[value0, value1, value2, value3, value4, value5, value6, value7]]
    prediction=model.predict(new_observation)
    outcomes=['Not At Risk', 'At Risk']
    risk =prediction[0]
    return f'You are {outcomes[risk]} heart disease.'


############ Execute
if __name__ == '__main__':
    app.run_server()
