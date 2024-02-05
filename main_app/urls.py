from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    #path for returning anime results search
    path('results/<str:anime_search>', views.results, name="results")
]

