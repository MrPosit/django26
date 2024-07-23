from django.db import models
from django.contrib.auth.models import AbstractUser
from django_ckeditor_5.fields import CKEditor5Field

class Author(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='authors/', default='authors/default.png')
    birthdate = models.DateField('Дата рождения')
    profession = models.CharField('Профессия', max_length=255)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', related_name='posts')
    content = CKEditor5Field('Содержание', config_name='extends')
    bbcode_content = models.TextField('BBCode содержание', blank=True, null=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateField('Обновлено', auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.created_at}) by {self.author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
