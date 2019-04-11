from django.urls import path
from . import views # from . means from the current directory

urlpatterns = [
    path('', views.home, name='blog-home'), # blog-home makes it easier to do a reverse lookup
    path('about/', views.about, name='blog-about'),
]
