from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('delete/<int:id>',views.delete,name='delete'),

]
