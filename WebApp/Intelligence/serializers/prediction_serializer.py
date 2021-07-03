
import pandas as pd
from Intelligence.models import Prediction
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class PredictionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['id','name','n','pred','file_url']



class PredictionDetailsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Prediction
        fields = ['id','name','n','pred','file_url']

    def get_name(self, instance):
        return str(instance.name).replace('_',' ') 
  
