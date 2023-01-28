from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField('Наименование', max_length=100)
    description = models.TextField('Краткое описание')
    text = models.TextField('Текст статьи')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
