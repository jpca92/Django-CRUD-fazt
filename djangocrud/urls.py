
from django.contrib import admin
from django.urls import path
from tasks.views import *
from tasks import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),

    path('tasks/', tasks, name='tasks' ),
    path('tasks_completed/', tasks_completed, name='tasks_completed' ),
    path('tasks/create/', create_task, name= 'create_task'),
    path('tasks/<int:task_id>/', task_detail, name= 'task_detail'),
    path('tasks/<int:task_id>/complete', complete_task, name= 'complete_task'),
    path('tasks/<int:task_id>/delete', delete_task, name= 'delete_task'),

    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
]

