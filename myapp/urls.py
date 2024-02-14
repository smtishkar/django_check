from django.urls import path
import myapp.views as views


urlpatterns = [
    path('',views.index, name='index'),
    path('one_recepie/<int:recepie_id>',views.one_recepie, name='one_recepie')

    
]