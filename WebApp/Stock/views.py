from django.conf import settings
from django.shortcuts import render

from Stock.utils.predict_model import PredictModel
from Stock.utils.train_model import TrainModel

# from .dashboad import *
from .stock_app import *

# Create your views here.

stock_context = dict({'stock_list': [
          {'key':'NGM', 'name':'NSE-TATAGLOBAL'},
          {'key':'MSFT','name':'Microsoft'},
            {'key':'NMS','name':'Facebook'}
]})

def index(request):
    #context = dict({'fdsf':'fds'})
    #list = ['NSE-TATAGLOBAL','two','three']
    #context.setdefault('stock_list',stocks)

    stock_context.setdefault('status', None)

    return render(request,'index.html', stock_context)

def predictionView(request,name):
    import yfinance as yf
    data = yf.download(tickers=name, period='6d', interval='1m')
    

    print(data)
    print(name)
    # settings.MEDIA_ROOT+'/NSE-TATAGLOBAL.csv'

    predict = PredictModel(data=data, trained_name=name+'_trained_model')
    predict.clean()
    predict.predict()
    
    get_dashboard(stock_name = name, context= predict.get_results())


    context = dict()
    context.setdefault('name',name)
    
    return render(request,'predicted.html', context)

def trainView(request, name):

    try:
        import yfinance as yf
        data = yf.download(tickers=name, period='5d', interval='5m')
        #settings.MEDIA_ROOT+'/NSE-TATAGLOBAL.csv

        training = TrainModel(data=data, train_name=name+'_trained_model')
        training.clean()
        training.train()

        # context = dict()
        print(name)
        
        stock_context.setdefault('status',{'code':1,'message':'successfully trained for '+name})

    except:
        stock_context.setdefault('status',{'code':0,'message':'training failed for'+name})

    # get_dashboard(stock_name = name)
    
    # return render(request,'index.html', context)
    return render(request,'index.html', stock_context)

