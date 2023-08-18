# Django
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.manager import BaseManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager, BaseManager):
    def create_user(self, phone_number, password):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError(_('Users must have an phone_number'))

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, phone_number, password):
        """
        Creates and saves an admin with the given username and password.
        """
        user = self.create_user(phone_number, password)
        user.is_registered = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        user = self.create_user(phone_number, password=password)
        user.is_admin = True
        user.is_registered = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
