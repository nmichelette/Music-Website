from django.urls import path
from . import views

app_name = 'recommender'

urlpatterns = [
    path('best/', views.searchform_get, name='best'),
    path('bestp/', views.searchform_post, name='bestp'),
    path('search/', views.searchpage, name='searchpage'),
    path('home/', views.home, name ='home'),

]
