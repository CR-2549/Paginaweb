from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'catalogo/',
        views.catalogo,
        name='catalogo'
    ),

    path(
        'crear/',
        views.crear_game,
        name='crear_post'
    ),

]