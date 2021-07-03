from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from Intelligence.models import Prediction, Video
from Intelligence.predictions import VggProcess
from Intelligence.serializers.prediction_serializer import \
    PredictionDetailsSerializer
from Intelligence.serializers.video_serializer import VideoSerializer


# Upload video view.
class UploadVideoView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser,)

    # variables
    def post(self, request):
        data = request.data
        file_serializer = VideoSerializer(data=data)

        if file_serializer.is_valid():
            file_serializer.save()
            Prediction.objects.all().delete()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        print(file_serializer.errors)
        return Response({'message':'failed uploading video'}, status =status.HTTP_417_EXPECTATION_FAILED)


class PredictView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny] 

    # variables
 
    def get(self, request):

        vprocess = VggProcess()
        p = Prediction.objects.all()
        try:
            vprocess.iterate_prediction(p)
            return Response({'message':'successfully finished prediction'}, status =status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message':'failed predicting'}, status =status.HTTP_417_EXPECTATION_FAILED)
        
# Get predicted list view.
class PredictedListView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny]

 
    def get(self, request):

        p = Prediction.objects.exclude(n__isnull=True).exclude(pred__exact='')
  
        if p.exists():
            ser = PredictionDetailsSerializer(p , many=True)
            return Response(ser.data, status =status.HTTP_200_OK)
        return Response({'message':'list empty'}, status =status.HTTP_417_EXPECTATION_FAILED)
       



class SplitImagesFromVideo(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [AllowAny] 
  
    def get(self, request):
        video = Video.objects.last()

        vprocess = VggProcess()

        try:
            Prediction.objects.all().delete()
            vprocess.split_images_from_video(video.file.url)
            return Response({'message':'finished spliting video'}, status =status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'message':'failed spliting video'}, status =status.HTTP_417_EXPECTATION_FAILED)

      
        
