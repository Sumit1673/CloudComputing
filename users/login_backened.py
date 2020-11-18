from .models import  StaffDataModel
from datetime import datetime
from django.utils import timezone

class LoginAuthBackened():

    def authenticate(self, request, username=None, password=None):
        try:
            print(username, password)
            user = StaffDataModel.objects.get(username=username)
            if user.password == password:
                user.is_authenticated = True
                user.is_active = True # added
                user.last_login = timezone.now()
                return user
            else:
                return False

        except Exception as e:
          print(e)
        return None

    def get_user(self, user_id):
        try:
            return StaffDataModel.objects.get(pk=user_id)
        except:
            return None
