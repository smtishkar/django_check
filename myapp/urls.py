from django.urls import path
import myapp.views as views


urlpatterns = [
    path('',views.index, name='index'),

    
]