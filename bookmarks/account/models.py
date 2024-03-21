from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    Расширенная модель пользователя.
    """

    user = models.OneToOneField(settings.AUTH_USER,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='users/%Y%m%d')

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
