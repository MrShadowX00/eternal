from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('ru/',views.index_ru, name='index_ru'),
    path('en/',views.index_en, name='index_en'),
]