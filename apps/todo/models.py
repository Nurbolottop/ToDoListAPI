from django.db import models
from apps.users.models import User

# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="user_todo",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="todo_image/",
        verbose_name="Фотография",
        blank = True, null = True
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Завершено"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Список дел"
        verbose_name_plural = "Список дел"
        unique_together = ('user', 'title')