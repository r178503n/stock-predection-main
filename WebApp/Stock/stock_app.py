import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from django.conf import settings
from django_plotly_dash import DjangoDash

# app = dash.Dash()
app = DjangoDash('SimpleExample') 
# server = app.server


# scaling data



# df= pd.read_csv(settings.MEDIA_ROOT+"/stock_data.csv")

'''
Front end dashboard app with flask

'''
def predictions()->dict:
    import numpy as np
    import pandas as pd
    from keras.models import load_model
    from sklearn.preprocessing import MinMaxScaler
    scaler=MinMaxScaler(feature_range=(0,1))

    df_nse = pd.read_csv(settings.MEDIA_ROOT+"/NSE-TATAGLOBAL.csv")

    df_nse["Date"]=pd.to_datetime(df_nse.Date,format="%Y-%m-%d")
    df_nse.index=df_nse['Date']


    data=df_nse.sort_index(ascending=True,axis=0)
    new_data=pd.DataFrame(index=range(0,len(df_nse)),columns=['Date','Close'])

    for i in range(0,len(data)):
        new_data["Date"][i]=data['Date'][i]
        new_data["Close"][i]=data["Close"][i]

    new_data.index=new_data.Date
    new_data.drop("Date",axis=1,inplace=True)

    dataset=new_data.values

    train=dataset[0:987,:]
    valid=dataset[987:,:]

    scaler=MinMaxScaler(feature_range=(0,1))
    scaled_data=scaler.fit_transform(dataset)

    x_train,y_train=[],[]

    for i in range(60,len(train)):
        x_train.append(scaled_data[i-60:i,0])
        y_train.append(scaled_data[i,0])

    # filling training arrays
    x_train,y_train=np.array(x_train),np.array(y_train)

    x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

    # saving trained model
    model=load_model(settings.MEDIA_ROOT+"/saved_lstm_model.h5")

    inputs=new_data[len(new_data)-len(valid)-60:].values
    inputs=inputs.reshape(-1,1)
    inputs=scaler.transform(inputs)

    X_test=[]
    for i in range(60,inputs.shape[0]):
        X_test.append(inputs[i-60:i,0])
    X_test=np.array(X_test)

    X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
    closing_price=model.predict(X_test)
    closing_price=scaler.inverse_transform(closing_price)

    train=new_data[:987]
    valid=new_data[987:]
    valid['Predictions']=closing_price
    return {'train':train,'valid':valid}



def get_dashboard(stock_name,context):
    context = predictions()
    train = context['train']
    valid = context['valid']
    

    app.layout = html.Div([
   
    html.H1("Stock Price Analysis Dashboard", style={"textAlign": "center"}),
   
    dcc.Tabs(id="tabs", children=[
       
        dcc.Tab(label= stock_name+ 'Stock Data',children=[
			html.Div([
				html.H2("Actual closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="Actual Data",
					figure={
						"data":[
							go.Scatter(
								x=train.index,
								y=valid["Close"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				),
				html.H2("LSTM Predicted closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="Predicted Data",
					figure={
						"data":[
							go.Scatter(
								x=valid.index,
								y=valid["Predictions"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				)				
			])        		


        ]),
     


    ])
])


# @app.callback(Output('highlow', 'figure'),
#               [Input('my-dropdown', 'value')])
# def update_graph(selected_dropdown):
#     dropdown = {"TSLA": "Tesla","AAPL": "Apple","FB": "Facebook","MSFT": "Microsoft",}
#     trace1 = []
#     trace2 = []
#     for stock in selected_dropdown:
#         trace1.append(
#           go.Scatter(x=df[df["Stock"] == stock]["Date"],
#                      y=df[df["Stock"] == stock]["High"],
#                      mode='lines', opacity=0.7, 
#                      name=f'High {dropdown[stock]}',textposition='bottom center'))
#         trace2.append(
#           go.Scatter(x=df[df["Stock"] == stock]["Date"],
#                      y=df[df["Stock"] == stock]["Low"],
#                      mode='lines', opacity=0.6,
#                      name=f'Low {dropdown[stock]}',textposition='bottom center'))
#     traces = [trace1, trace2]
#     data = [val for sublist in traces for val in sublist]
#     figure = {'data': data,
#               'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', 
#                                             '#FF7400', '#FFF400', '#FF0056'],
#             height=600,
#             title=f"High and Low Prices for {', '.join(str(dropdown[i]) for i in selected_dropdown)} Over Time",
#             xaxis={"title":"Date",
#                    'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 
#                                                        'step': 'month', 
#                                                        'stepmode': 'backward'},
#                                                       {'count': 6, 'label': '6M', 
#                                                        'step': 'month', 
#                                                        'stepmode': 'backward'},
#                                                       {'step': 'all'}])},
#                    'rangeslider': {'visible': True}, 'type': 'date'},
#              yaxis={"title":"Price (USD)"})}
#     return figure


# @app.callback(Output('volume', 'figure'),
#               [Input('my-dropdown2', 'value')])
# def update_graph(selected_dropdown_value):
#     dropdown = {"TSLA": "Tesla","AAPL": "Apple","FB": "Facebook","MSFT": "Microsoft",}
#     trace1 = []
#     for stock in selected_dropdown_value:
#         trace1.append(
#           go.Scatter(x=df[df["Stock"] == stock]["Date"],
#                      y=df[df["Stock"] == stock]["Volume"],
#                      mode='lines', opacity=0.7,
#                      name=f'Volume {dropdown[stock]}', textposition='bottom center'))
#     traces = [trace1]
#     data = [val for sublist in traces for val in sublist]
#     figure = {'data': data, 
#               'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', 
#                                             '#FF7400', '#FFF400', '#FF0056'],
#             height=600,
#             title=f"Market Volume for {', '.join(str(dropdown[i]) for i in selected_dropdown_value)} Over Time",
#             xaxis={"title":"Date",
#                    'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 
#                                                        'step': 'month', 
#                                                        'stepmode': 'backward'},
#                                                       {'count': 6, 'label': '6M',
#                                                        'step': 'month', 
#                                                        'stepmode': 'backward'},
#                                                       {'step': 'all'}])},
#                    'rangeslider': {'visible': True}, 'type': 'date'},
#              yaxis={"title":"Transactions Volume"})}
#     return figure


# if __name__=='__main__':
# 	app.run_server(debug=True)
