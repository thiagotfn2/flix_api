from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avalição não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avalição não pode ser superior a 0 estrelas.'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)

