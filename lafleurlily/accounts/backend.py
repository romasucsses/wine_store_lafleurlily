from django.contrib.auth import get_user_model

from accounts.models import User
from django.contrib.auth.backends import ModelBackend


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, is_active=False):
        # User = get_user_model()

        try:
            user = User.objects.get(email=username)
            if user.is_active:
                return user
            # if user.check_password(password):
            #     return user
        except User.DoesNotExist:
            return None
