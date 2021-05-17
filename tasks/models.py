from django.db import models
from .constants import STATUS_CATEGORY, STATUS_TASKS


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    date_modified = models.DateTimeField(auto_now_add=True, verbose_name='День modified')
    status = models.CharField(choices=STATUS_CATEGORY, max_length=10, verbose_name='Статус')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категроии'

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Задание')
    description = models.TextField(max_length=255, verbose_name='Описание')
    date_created = models.DateTimeField(auto_now=True, verbose_name='День создания')
    date_modified = models.DateTimeField(auto_now_add=True, verbose_name='День modified')
    status = models.CharField(choices=STATUS_TASKS, max_length=9, verbose_name='Статус')
    deadline = models.DateTimeField(auto_created=True, verbose_name='Дедлайн')
    done = models.BooleanField(default=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title