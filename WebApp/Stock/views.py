from django.conf import settings
from django.shortcuts import render

from Stock.utils.predict_model import PredictModel
from Stock.utils.train_model import TrainModel

from .dashboad import *

# Create your views here.


def index(request):
    # training = TrainModel(data=settings.MEDIA_ROOT+'/NSE-TATAGLOBAL.csv', train_name='trained_model')
    #training.clean()
    #training.train()
    predict = PredictModel(data=settings.MEDIA_ROOT+'/NSE-TATAGLOBAL.csv', trained_name='trained_model')
    predict.clean()
    predict.predict()

    return render(request, template_name='index.html', context={})

