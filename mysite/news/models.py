from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)  #  blank - необязательно для заполнения
    created_at = models.DateTimeField(auto_now_add=True) # auto_now, auto_now_add, and default are mutually exclusive
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')  # проверка, чтобы файл был именно изображением
    is_published = models.BooleanField(default=True)

