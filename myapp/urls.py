from django.urls import path
import myapp.views as views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index'),
    path('one_recepie/<int:recepie_id>',views.one_recepie, name='one_recepie'),
    path('signup',views.registration, name='registration'),
    path('login/', views.sign_in, name='login')

    
]