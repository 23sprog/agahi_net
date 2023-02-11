from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

# User Manager
class UserManager(BaseUserManager):

    def create_user(self, email, username, password):

        if not email:
            raise ValidationError("You must enter your email")

        if not username:
            raise ValidationError("You must enter your username")

        if not password:
            raise ValidationError("You must enter your password")

        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user