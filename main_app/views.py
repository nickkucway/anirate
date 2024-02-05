from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import requests

def home(request):
    return render(request, 'home.html')

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

def results(request, anime_search):
    anime_search = anime_search
    api_url = f'https://api.jikan.moe/v4/anime?q={anime_search}&sfw'
    response = requests.get(api_url)
    data = response.json()
    anime_titles = [anime for anime in data.get('data', [])]
    return render(request, 'results.html', {'titles': anime_titles})