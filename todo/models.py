from django.db import models
from blog.models import Blog

class TodoModel(models.Model):
    task = models.CharField(max_length=100)
    read_blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('Выполнено', 'Выполнено'),
        ('Невыполнено', 'Невыполнено')
    )
    status = models.CharField(max_length=100,
                                 choices=STATUS,
                                 default='Невыполено'
                                 )
    
    def __str__(self):
        return self.task