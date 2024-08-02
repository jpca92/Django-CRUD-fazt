from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title=models.CharField(max_length=100)
    description= models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important= models.BooleanField(default=False)

    # Django ya tiene la entidad User creada por el formulario de las vistas
    # Solo debemos importar el modulo user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.title + ' - '  + self.user.username
