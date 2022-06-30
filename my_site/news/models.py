from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Описание', blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)
    photo = models.ImageField('Фото', upload_to='photo/%y/%m/%d/', blank=True)
