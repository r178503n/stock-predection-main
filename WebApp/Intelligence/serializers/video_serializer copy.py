
import pandas as pd
from Intelligence.models import Prediction, Video
from rest_framework import serializers
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['file']
