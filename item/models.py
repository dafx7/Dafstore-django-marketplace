from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225) 

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
