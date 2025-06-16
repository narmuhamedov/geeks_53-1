from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# После того когда вы окончательно создали таблицу как указан пример блога ниже
# Проводим миграции python manage.py makemigrations затем python manage.py migrate
# После этого заходите в файл admin.py и регистрируете его 

class Blog(models.Model):
  title = models.CharField(max_length=100, verbose_name='Напишите название блога')
  image = models.ImageField(upload_to='blog/', verbose_name='Загрузите картинку')
  description = models.TextField(verbose_name='Дайте описание блога')
  TYPE_BLOG = (
    ('IT', 'IT'),
    ('Business', 'Business'),
    ('SMM', 'SMM')
  )
  type_blog = models.CharField(max_length=100, choices=TYPE_BLOG)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'новость'
    verbose_name_plural = 'новости'



class Reviews(models.Model):
  choice_news = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE, related_name='post', verbose_name='post')
  text = models.TextField(verbose_name='введите комментарий')
  author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  mark =  models.PositiveIntegerField(null=True, validators=[
    MinValueValidator(1, message="Оценка должна быть не меньше 1."),
            MaxValueValidator(5, message="Оценка должна быть не больше 5.")
  ])
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.choice_news}--{self.text}'
  