

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
        try:
            self.get_data()
        except:
            self.df = data
        super().__init__()

    def get_data(self): 
        self.df=pd.read_csv(self.data_to_train)

        if self.df.empty:
            raise FileExistsError('File does not exist')

        print('data read success')
    
    def clean(self):
        print('__________________')
        print('cleaning')
        # try:
        #     self.df["Datetimetime"]=pd.to_Datetimetime(self.df.Datetimetime,format="%Y-%m-%d")
        #     pass
        # except:
        #     self.df["Datetimetime"]=pd.to_Datetimetime(self.df.Datetimetime,format="%Y-%m-%d")
        print(self.df)

        self.df["Datetime"]=pd.to_datetime(self.df.index,format="%Y-%m-%d")
        #self.df.index=self.df['Datetime']

        data=self.df.sort_index(ascending=True,axis=0)

        # taking wanted features only
        new_dataset=pd.DataFrame(index=range(0,len(self.df)),columns=['Datetime','Close'])

        for i in range(0,len(data)):
            new_dataset["Datetime"][i]=data['Datetime'][i]
            new_dataset["Close"][i]=data["Close"][i]
            

        new_dataset.index=new_dataset.Datetime
        new_dataset.drop("Datetime",axis=1,inplace=True)
        # set global variables
        self.new_dataset = new_dataset
        self.final_dataset=new_dataset.values
        print('finished cleaning')

        print('__________________')



    def train(self):
        print('__________________')
        print('training')
        import numpy as np
        from keras.layers import LSTM, Dense, Dropout
        from keras.models import Sequential
        from sklearn.preprocessing import MinMaxScaler
        train_percentage = int(len(self.df)*(30/100))

        # final_dataset=new_dataset.values
        # training splits
        train_data=self.final_dataset[0:train_percentage,:]
        valid_data=self.final_dataset[train_percentage:,:]

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

        train_data=self.new_dataset[:train_percentage]
        valid_data=self.new_dataset[train_percentage:]
        valid_data['Predictions']=predicted_closing_price

        print('finished training')

        print('__________________')
        return valid_data
    def get_valid_data(self):
        return self.valid_data

