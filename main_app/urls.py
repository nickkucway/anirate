from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    #path for returning anime results search
    path('results/', views.results, name="results"),
    path('details/<int:id>', views.details, name="details"),
    path('index', views.index, name="index"),
    #path to add show to watchlist
    path('details/<int:id>/add_to_watchlist', views.add_to_watchlist, name="add_to_watchlist"),
    #Paths for reviews
    path('reviews/create/', views.ReviewCreate.as_view(), name = 'reviews_create'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name = 'reviews_update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name = 'reviews_delete'),
]

