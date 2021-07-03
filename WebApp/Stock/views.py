from django.conf import settings
from django.shortcuts import render

from Stock.utils.predict_model import PredictModel
from Stock.utils.train_model import TrainModel

# from .dashboad import *
from .stock_app import *

# Create your views here.


def index(request):
    context = dict({'fdsf':'fds'})
    list = ['NSE-TATAGLOBAL','two','three']
    context.setdefault('list',list)
    return render(request,'index.html', context)

def predictionView(request,name):
    print(name)
    predict = PredictModel(data=settings.MEDIA_ROOT+'/NSE-TATAGLOBAL.csv', trained_name='trained_model')
    #valid = predict.get_results()['valid']
    #train = predict.get_results()['train']
    predict.clean()
    predict.predict()
    # print( predict.get_results())

    context = dict()
    
    context.setdefault('name',name)
    get_dashboard(stock_name = name, context={})
    
    return render(request,'predicted.html', context)

def trainView(request,name):

    #training = TrainModel(data=settings.MEDIA_ROOT+'/NSE-TATAGLOBAL.csv', train_name='trained_model')
    #training.clean()
    #training.train()

    context = dict()
    
    context.setdefault('name',name)
    get_dashboard(stock_name = name)
    
    return render(request,'predicted.html', context)

