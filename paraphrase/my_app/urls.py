from django.urls import path

from . import views


urlpatterns = [
    path('paraphrase/home', views.index, name='home'),
    path('paraphrase/', views.PhraseCreateView.as_view(), name='form'),
    
]