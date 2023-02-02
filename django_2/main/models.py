from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Краткое описание')
    text = models.TextField('Текст статьи')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Task(models.Model):
    title = models.CharField('Название ', max_length=100)
    text = models.TextField('Текст задачи')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
