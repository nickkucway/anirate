from django.forms import ModelForm
from .models import Watchlist

class WatchlistForm(ModelForm):
    class Meta:
        model = Watchlist
        exclude =['user']
