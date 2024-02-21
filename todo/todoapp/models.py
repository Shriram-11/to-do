from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
