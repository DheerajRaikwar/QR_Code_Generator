from django.urls import path
from Generator import views

urlpatterns = [ 
    path('',views.index,name='index'),
    
]
