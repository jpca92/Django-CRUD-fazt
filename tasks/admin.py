from django.contrib import admin
from .models import Task

# creamos una clase para poder visualizar la fecha de creacion
# la fecha de creacion la dejamos auto por eso no se ve inicialmente
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )


# Importamos el modelo de Task
# ponemos la siguiente linea para que aparezca en el panel de admin
admin.site.register(Task, TaskAdmin)

