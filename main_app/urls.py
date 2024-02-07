from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    #path for returning anime results search
    path('results/', views.results, name="results"),
    path('details/<int:id>', views.details, name="details"),
    path('index', views.index, name="index")
]

