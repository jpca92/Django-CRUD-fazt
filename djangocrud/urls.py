
from django.contrib import admin
from django.urls import path
from tasks.views import *
from tasks import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('tasks/', tasks, name='tasks' )
]
