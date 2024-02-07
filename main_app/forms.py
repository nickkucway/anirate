from django.forms import ModelForm
from .models import Watchlist, Review

class WatchlistForm(ModelForm):
    class Meta:
        model = Watchlist
        exclude =['user']

        