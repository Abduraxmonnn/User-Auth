# Django
from django.db import models


class CustomUser(models.Model):
    """
        This model represents user accounts within your application. It builds upon Django's
        built-in AbstractUser class, providing a foundation for authentication, permissions,
        and user-related functionality. You can extend this model to include custom fields
        and methods specific to your application's requirements.

        Attributes:
            id (int): Unique identifier for the user.

        Note:
            It's important to tailor the fields and methods of this model to match your
            application's needs while adhering to security best practices.
    """

    phone_number = models.IntegerField(unique=True)

    otp = models.CharField(max_length=4, blank=True, null=True)
    invite_code = models.CharField(max_length=6, blank=True, null=True)
    another_invite_code = models.CharField(max_length=6, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        ordering = ['id', ]
