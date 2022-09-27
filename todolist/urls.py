from django.urls import path
from todolist.views import change_task, delete_task, show_todolist
from todolist.views import register, login_user, logout_user, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete-task/<int:pk>', delete_task, name='delete-task'),
    path('change-task/<int:pk>', change_task, name='change-task'),
]