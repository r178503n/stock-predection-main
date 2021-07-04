from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Stock.utils.predict_model import PredictModel
from Stock.utils.train_model import TrainModel

# from .dashboad import *
from .stock_app import *

# Create your views here.

stock_context = dict({'stock_list': [
          {'key':'NGM', 'name':'NSE-TATAGLOBAL'},
          {'key':'MSFT','name':'Microsoft'},
            {'key':'NMS','name':'Facebook'}
],'status':None})

def index(request,):
    #context = dict({'fdsf':'fds'})
    #list = ['NSE-TATAGLOBAL','two','three']
    #context.setdefault('stock_list',stocks)

    #stock_context.setdefault('status', None)


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

# class TView(APIView):
#     authentication_classes = (JSONWebTokenAuthentication,)
#     permission_classes = [AllowAny] 

#     # variables
 
#     def get(self, request,name):

#         return Response({'message':'failed predicting'}, status =status.HTTP_417_EXPECTATION_FAILED)
 

def trainView(request, name):
    # stock_context = dict()

    try:
        import yfinance as yf

        # downloading data
        data = yf.download(tickers=name, period='5d', interval='5m')

        # training model
        training = TrainModel(data=data, train_name=name+'_trained_model')
        training.clean()
        training.train()
        stock_context['status']= {'code':1,'message':'Successfully trained for '+name}
        

    except Exception as e:
        stock_context['status']= {'code':0,'message':'Training failed for'+name}
    


    # get_dashboard(stock_name = name)
    # request.session['vote'] ={'code':0,'message':'Training failed for'+name}
  
    return render(request,'index.html', stock_context)
    #HttpResponseRedirect('/')
    #from django.urls import reverse
    #return HttpResponseRedirect(reverse('index'), stock_context)

