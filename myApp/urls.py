from . import views 
from django.urls import path


urlpatterns =[
    path('', views.todo_list,name="todo_list"),
    path('create', views.create_todo,name="create_todo"),
    path('complete_todo/<int:id>/',views.complete_todo, name='complete_todo'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),

]