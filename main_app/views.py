from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Watchlist, Review
from .forms import WatchlistForm
import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


def home(request):
     api_url = f'https://api.jikan.moe/v4/recommendations/anime'
     response = requests.get(api_url)
     data = response.json()['data']
     anime1 = data[0]['entry'][1]
     anime2 = data[1]['entry'][1]
     anime3 = data[2]['entry'][1]
     anime4 = data[3]['entry'][1]
     anime5 = data[4]['entry'][1]
     anime6 = data[5]['entry'][1]
     return render(request, 'home.html',{'anime1': anime1, 'anime2': anime2, 'anime3': anime3, 'anime4': anime4, 'anime5': anime5, 'anime6': anime6})

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
    anime_details = response.json()['data']
    form = WatchlistForm()
    
    reviews = Review.objects.filter(show =int(id))
    
    return render(request, 'anime/details.html', {'anime': anime_details, 'form': form, 'reviews': reviews})

# @login_required
# def index(request):
#     animes = []
#     titles = Watchlist.objects.filter(user=request.user)
#     for title in titles:
#         api_url = f'https://api.jikan.moe/v4/anime/{title.show}/full'
#         result = requests.get(api_url)
#         result = result.json()['data']
#         animes.append(result)
#     return render(request, 'anime/index.html', {'animes': animes})

@login_required
def index(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, 'anime/index.html', {'watchlist': watchlist})

@login_required
def add_to_watchlist (request, id):
   form = WatchlistForm(request.POST)
   if form.is_valid():
      new_show = form.save(commit=False)
      new_show.show = id
      new_show.user = request.user
      new_show.save()
      return redirect('index')
   print(form.errors)
   return HttpResponse('Form not valid')

class ReviewCreate(CreateView):
  model = Review
  fields = ['rating', 'review_content', 'show']
   
  def get_initial(self):
        initial = super().get_initial()
        # Get the `show` query parameter to pre-fill the form
        initial['show'] = self.request.GET.get('show', '')
        return initial

  def form_valid(self, form):
      # self.request.user is the logged in user 
      form.instance.user = self.request.user
      return super().form_valid(form)

class ReviewUpdate(UpdateView):
   model = Review
   fields = ['rating','review_content']

class ReviewDelete(DeleteView):
   model = Review
  
   def get_success_url(self):
    review = self.object
    show_id = review.show
    return reverse_lazy('details', kwargs={'id': show_id})
