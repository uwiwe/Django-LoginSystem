from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class MyCustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Cambiado de username a email
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
