from django.db import models
from django.urls import reverse

# Create your models here.

genre_movie = (
    ("Ação", "Ação"), 
    ("Aventura", "Aventura"), 
    ("Cinema de arte", "Cinema de arte"), 
    ("Chanchada", "Chanchada"), 
    ("Comédia", "Comédia"), 
    ("Comédia de ação", "Comédia de ação"), 
    ("Comédia de terror", "Comédia de terror"), 
    ("Comédia dramática", "Comédia dramática"), 
    ("Comédia romântica", "Comédia romântica"), 
    ("Dança", "Dança"), 
    ("Documentário", "Documentário"), 
    ("Docuficção", "Docuficção"), 
    ("Drama", "Drama"), 
    ("Espionagem", "Espionagem"), 
    ("Faroeste", "Faroeste"), 
    ("Fantasia", "Fantasia"), 
    ("Fantasia científica", "Fantasia científica"), 
    ("Ficção científica", "Ficção científica"), 
    ("Filmes com truques", "Filmes com truques"), 
    ("Filmes de guerra", "Filmes de guerra"), 
    ("Mistério", "Mistério"), 
    ("Musical", "Musical"), 
    ("Filme policial", "Filme policial"), 
    ("Romance", "Romance"), 
    ("Terror", "Terror"), 
    ("Thriller", "Thriller"), 
)

class Movie(models.Model):
    name = models.CharField('Nome', max_length=70)
    genre = models.CharField('Gênero', max_length = 35, choices = genre_movie, default = 'Ação')
    duration = models.TimeField('Duração')
    description = models.TextField('Descrição', max_length=250)
    poster = models.ImageField('foto', upload_to='images/')
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cineflix:movie_detail', kwargs={'pk': self.pk})