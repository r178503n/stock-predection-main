import os

from django.conf import settings


def create_directory(name):
    try:
        os.makedirs(name)
    except OSError as e:
        pass
        #if e.errno != e.errno.EEXIST:
        #    raise
def file_upload_path(instance, filename):
    file_array = filename.split('.')
    extension = file_array[1]
    file_name = '{0}.{1}'.format(
       instance.upload_file_url(), extension)
    #  
    print(instance.upload_file_url())

    fullname = os.path.join(settings.MEDIA_ROOT, file_name)
    if os.path.exists(fullname):
        os.remove(fullname)
    return file_name
