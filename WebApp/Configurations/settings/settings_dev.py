
from .base_settings import *

# DEBUG = int(os.environ.get('DEBUG', default=1))
DEBUG = True
CUSTOM_DOMAIN_NAME = 'Configurations'
ALLOWED_HOSTS = ['*', '127.0.0.1']

# Host Backend urls

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'elitecode',
    'API_KEY': '488823284154167',
    'API_SECRET': 'SGVVIikZyAXkFO5jZXHYyvdOryI',
    }


import cloudinary
import cloudinary.api
import cloudinary.uploader

cloudinary.config( 
  cloud_name ='elitecode',
  api_key = '488823284154167',
  api_secret = 'SGVVIikZyAXkFO5jZXHYyvdOryI',

)
