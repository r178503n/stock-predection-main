import pandas as pd
from django.conf import settings
from pandas.core.base import DataError


class PredictModel:
    valid_data = pd.DataFrame()
    df = pd.DataFrame()
    final_dataset = pd.DataFrame()
    new_dataset = pd.DataFrame()
    saved_model_path = None
    data_to_predict= None
    # results
    train = None
    valid = None

    new_data = None
    dataset = None


    def __init__(self, data,trained_name) -> None:
        print('this is init')
        self.data_to_predict = data
        self.saved_model_path = settings.MEDIA_ROOT+'/{}.h5'.format(trained_name)

        self.get_data()
        super().__init__()

    def get_data(self):
        try:
            self.df=pd.read_csv(self.data_to_predict)
        except:
            print('________________________')
            print('reading remote')
            self.df = self.data_to_predict
        


        if self.df.empty:
            raise FileExistsError('File does not exist')

        print('data read success')
    def clean(self):
        # try:
        #     self.df.rename(columns = {'Datetimetime','Datetime'})
        # except:
        #     pass
        print(self.df)
        
        self.df["Datetime"]=pd.to_datetime(self.df.index,format="%Y-%m-%d")
        #self.df.index=self.df['Datetime']


        data=self.df.sort_index(ascending=True,axis=0)
        new_data=pd.DataFrame(index=range(0,len(self.df)),columns=['Datetime','Close'])

        for i in range(0,len(data)):
            new_data["Datetime"][i]=data['Datetime'][i]
            new_data["Close"][i]=data["Close"][i]

        new_data.index=new_data.Datetime
        new_data.drop("Datetime",axis=1,inplace=True)
        self.new_data = new_data

        self.dataset=new_data.values
    
    def predict(self):
        import numpy as np
        from keras.models import load_model
        from sklearn.preprocessing import MinMaxScaler
        train_percentage = int(len(self.df)*(20/100))

        scaler= MinMaxScaler(feature_range=(0,1))
        scaled_data=scaler.fit_transform(self.dataset)
        x_train,y_train=[],[]

        train=self.dataset[0:train_percentage,:]
        valid=self.dataset[train_percentage:,:]

        for i in range(60,len(train)):
            x_train.append(scaled_data[i-60:i,0])
            y_train.append(scaled_data[i,0])

        # filling training arrays
        x_train,y_train=np.array(x_train),np.array(y_train)

        x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
        
        model=load_model(self.saved_model_path)
        inputs=self.new_data[len(self.new_data)-len(valid)-60:].values
        inputs=inputs.reshape(-1,1)
        inputs=scaler.transform(inputs)

        X_test=[]
        for i in range(60,inputs.shape[0]):
            X_test.append(inputs[i-60:i,0])
        X_test=np.array(X_test)

        X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
        closing_price=model.predict(X_test)
        closing_price=scaler.inverse_transform(closing_price)

        train=self.new_data[:train_percentage]
        valid=self.new_data[train_percentage:]
        valid['Predictions']=closing_price
   

        self.valid = valid
        self.train = train
      
    def get_results(self):

        return {'train':self.train, 'valid':self.valid}



# process = PredictModel(data ='././NSE-TATAGLOBAL.csv', trained_name='saved_lstm_model4')

# process.clean()
# process.predict()
