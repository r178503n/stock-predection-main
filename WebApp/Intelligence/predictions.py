
import urllib.request

import cv2
import numpy as np
from django.conf import settings
from django.core.files.base import ContentFile

from Intelligence.models import Prediction
from Intelligence.serializers.prediction_serializer import \
    PredictionCreateSerializer


class VggProcess():

    def iterate_prediction(self,predictionList, ):
        from tensorflow.keras.preprocessing import image

        for p in predictionList:
            details = dict()
            # get image from cloudinary
            full_path = '{}.jpg'.format(p.file.url)
            urllib.request.urlretrieve(full_path, "pred.jpg")

            # load image
            img = image.load_img('pred.jpg',color_mode='rgb', target_size=(224, 224))
            arr = self.convert_tonumpy(img)

            # run model prediction
            values = self.predict_images(arr)
            details = dict(details, **values)

            # update prediction values in the database
            instance = Prediction.objects.get(id = p.id)
            
            update_serializer = PredictionCreateSerializer(instance, data=details, many=False)


            if update_serializer.is_valid():
                update_serializer.save()
                print('_______________')
                print('saved prediction')
            print('_______________')
            print(update_serializer.errors)
  
        return None


    def convert_tonumpy(self, image_input):
        from tensorflow.keras.preprocessing import image

        # Converts a PIL Image to 3D Numy Array
        x = image.img_to_array(image_input)
        x.shapes
        # Adding the fouth dimension, for number of images
        x = np.expand_dims(x, axis=0)
        return x
    
    def predict_images(self, nparr):
        from keras.applications.vgg16 import VGG16
        from tensorflow.keras.applications.vgg16 import (decode_predictions,
                                                         preprocess_input)
        vgg16_weights = settings.MEDIA_ROOT+ "\\model\\vgg16_weights_tf_dim_ordering_tf_kernels.h5"

        # model = VGG16(weights='imagenet')
        model = None

        try: 
            model = VGG16(weights = vgg16_weights)

        except Exception as e:
            print('cannot locate file')

        
        if not model:
            model = VGG16(weights='imagenet')
        
        print(model)

        x = preprocess_input(nparr)
        features = model.predict(x)
        p = decode_predictions(features)
        dict = {
        'n':str(p[0][0][0]),
        'name':str(p[0][0][1]),
        'pred':str(p[0][0][2])}
        print(dict)

        return dict

    def split_images_from_video(self, srcVideoUrl):
        print('_______________________')
        vidcap = cv2.VideoCapture(srcVideoUrl)
        print(vidcap)

        print('reading images from video')
        currentframe = 0
        while(True):
       
            # reading from frame
            ret,frame = vidcap.read()
        
            if ret:    
              
                ret, buf = cv2.imencode('.jpg', frame) # cropped_image: cv2 / np array
                # convert bytes to image object
                content = ContentFile(buf.tobytes())
                # save file to database
                p =  Prediction()
                p.file.save('{}.jpg'.format(currentframe), content)
          
                currentframe += 1
                print(str(currentframe) + '.jpg')
                
            else:
                print('nothing to read now.')
                break
        
        vidcap.release()
        cv2.destroyAllWindows()
        print('finished reading images from video')
        print('_______________________')
