from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    review_content = models.TextField(default="")
    show = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('details', kwargs={'id': self.show})

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.IntegerField()
    title = models.TextField(default='')
    image = models.TextField(default='')



def __str__(self):
    return self.Watchlist
    