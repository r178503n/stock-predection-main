
from django.contrib.auth.models import User

# django.setup()


admin_email='root@gmail.com'

try:
      
    admin = User.objects.filter(email = admin_email)
    
    def createUser():
        u = User(username=admin_email, email=admin_email)
        u.set_password('root')
        u.is_superuser = True
        u.is_staff = True
        u.save()

    if admin.exists():
        print('superuser already exist... ', admin.first())

    else:
        print('creating super user...')
        createUser()
        
except:
    pass
