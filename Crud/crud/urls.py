from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<int:deleteid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
    
   
]