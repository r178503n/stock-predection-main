

from .base_settings import *

try:
    # pyright: reportMissingImports=false
    import dj_database_url

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

    # define postgrel database connections

    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)
    DATABASES['default']['CONN_MAX_AGE'] = 500
    print('<------------ USING PRODUCTION SETTINGS ------------>')
    
except Exception:
    print('refused production environment')
    pass
    # logging.error('<------------ THIS ENVIRONMENT IS NOT AVAILABLE ------------>')

CUSTOM_DOMAIN_NAME = 'https://docking-stock-prediction.herokuapp.com' 


ALLOWED_HOSTS = ['*', CUSTOM_DOMAIN_NAME]


DEBUG = True

