from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Watchlist
import requests

def home(request):
     api_url = f'https://api.jikan.moe/v4/recommendations/anime'
     response = requests.get(api_url)
     data = response.json()['data']
     anime1 = data[0]['entry'][1]
     anime2 = data[1]['entry'][1]
     anime3 = data[2]['entry'][1]
     return render(request, 'home.html',{'anime1': anime1, 'anime2': anime2, 'anime3': anime3})

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def results(request):
    anime_search=request.GET.get('anime_search', '')
    api_url = f'https://api.jikan.moe/v4/anime?q={anime_search}&sfw'
    response = requests.get(api_url)
    data = response.json()
    anime_titles = [anime for anime in data.get('data', [])]
    return render(request, 'anime/results.html', {'titles': anime_titles})

def details(request, id):
    api_url = f'https://api.jikan.moe/v4/anime/{id}/full'
    response = requests.get(api_url)
    # data = response.json()
    anime_details = response.json()['data']
    # print(data)
    return render(request, 'anime/details.html', {'anime': anime_details})

def index(request):
    animes = []
    titles = Watchlist.objects.filter(user=request.user)
    for title in titles:
        api_url = f'https://api.jikan.moe/v4/anime/{title.show}/full'
        result = requests.get(api_url)
        result = result.json()['data']
        animes.append(result)
    return render(request, 'anime/index.html', {'animes': animes})

