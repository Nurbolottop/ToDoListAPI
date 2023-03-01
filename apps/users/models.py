from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Ваша почта",
        unique=True
        )
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Ваш тел.номер"
    )
    created_at=models.DateTimeField(
        auto_now_add=True
    )
    age = models.CharField(
        max_length=255,
        verbose_name="Ваш возраст"
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"
        