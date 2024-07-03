from django.db import models
from django.contrib.auth.models import User
class Books(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.PositiveBigIntegerField(default=100)
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Authors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Books)
    created_at = models.DateTimeField(auto_now_add=True)
