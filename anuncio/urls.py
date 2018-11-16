from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as django_views
from . import views


app_name = 'anuncio'

urlpatterns = [

    #path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', django_views.LoginView.as_view(template_name="anuncio/login.html"), name='login'),
    path('logout/', django_views.LogoutView.as_view(next_page="/anuncio/"), name='logout'),
    path('sobre/', views.sobre  ,name='sobre'),
    path('categoria/add/',  views.CategoriaView.as_view(), name='add_categoria'),
    path('', views.index, name='index'),
]
