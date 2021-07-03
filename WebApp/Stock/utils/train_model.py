

import pandas as pd
from django.conf import settings
from pandas.core.base import DataError


class TrainModel:
    valid_data = pd.DataFrame()
    df = pd.DataFrame()
    final_dataset = pd.DataFrame()
    new_dataset = pd.DataFrame()
    saved_model_path = None
    data_to_train = None


    def __init__(self, data,train_name) -> None:
        self.data_to_train = data
        self.saved_model_path = settings.MEDIA_ROOT+'/{}.h5'.format(train_name)

        self.get_data()
        super().__init__()

    def get_data(self): 
        self.df=pd.read_csv(self.data_to_train)

        if self.df.empty:
            raise FileExistsError('File does not exist')

        print('data read success')
    
    def clean(self):
        try:
            self.df["Date"]=pd.to_datetime(self.df.Date,format="%Y-%m-%d")
            pass
        except:
            self.df["DateTime"]=pd.to_datetime(self.df.Date,format="%Y-%m-%d")

        self.df["DateTime"]=pd.to_datetime(self.df.Date,format="%Y-%m-%d")
        self.df.index=self.df['Date']

        data=self.df.sort_index(ascending=True,axis=0)

        # taking wanted features only
        new_dataset=pd.DataFrame(index=range(0,len(self.df)),columns=['Date','Close'])

        for i in range(0,len(data)):
            new_dataset["Date"][i]=data['Date'][i]
            new_dataset["Close"][i]=data["Close"][i]
            

        new_dataset.index=new_dataset.Date
        new_dataset.drop("Date",axis=1,inplace=True)
        # set global variables
        self.new_dataset = new_dataset
        self.final_dataset=new_dataset.values



    def train(self):
        import numpy as np
        from keras.layers import LSTM, Dense, Dropout
        from keras.models import Sequential
        from sklearn.preprocessing import MinMaxScaler

        # final_dataset=new_dataset.values
        # training splits
        train_data=self.final_dataset[0:987,:]
        valid_data=self.final_dataset[987:,:]

        # scaling data
        scaler=MinMaxScaler(feature_range=(0,1))
        scaled_data=scaler.fit_transform(self.final_dataset)

        x_train_data,y_train_data=[],[]

        for i in range(60,len(train_data)):
            x_train_data.append(scaled_data[i-60:i,0])
            y_train_data.append(scaled_data[i,0])
            
        x_train_data,y_train_data=np.array(x_train_data),np.array(y_train_data)

        x_train_data=np.reshape(x_train_data,(x_train_data.shape[0],x_train_data.shape[1],1))

        # LSTM MODEL
        lstm_model=Sequential()
        lstm_model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train_data.shape[1],1)))
        lstm_model.add(LSTM(units=50))
        lstm_model.add(Dense(1))

        # using mean_squared error on the training
        lstm_model.compile(loss='mean_squared_error',optimizer='adam')
        lstm_model.fit(x_train_data,y_train_data,epochs=1,batch_size=1,verbose=2)

        inputs_data=self.new_dataset[len(self.new_dataset)-len(valid_data)-60:].values
        inputs_data=inputs_data.reshape(-1,1)
        inputs_data=scaler.transform(inputs_data)


        X_test=[]
        for i in range(60,inputs_data.shape[0]):
            X_test.append(inputs_data[i-60:i,0])
        X_test=np.array(X_test)

        X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

        # predicting closing price
        predicted_closing_price= lstm_model.predict(X_test)
        predicted_closing_price=scaler.inverse_transform(predicted_closing_price)

        # saving trained model
        lstm_model.save(self.saved_model_path)

        train_data=self.new_dataset[:987]
        valid_data=self.new_dataset[987:]
        valid_data['Predictions']=predicted_closing_price
        return valid_data
    def get_valid_data(self):
        return self.valid_data

