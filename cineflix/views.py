import imp
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from cineflix.models import Movie
from .forms import MovieForm
from django.db.models import Q




# Create your views here.

def movie_criate(request): 
  
    if request.method == 'POST': 
        form = MovieForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return render(request, 'cineflix/movie_success.html')

    else: 
        form = MovieForm() 
        return render(request, 'cineflix/movie_create.html', {'form' : form}) 

class MovieList(ListView):
    model = Movie
    template_name = 'cineflix/movie_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        movies = Movie.objects.all()
        
        if self.request.GET.get('search_box'):
            search_box = self.request.GET['search_box']
            movies = Movie.objects.filter(Q(name__icontains = search_box) | Q(genre__icontains = search_box))

        context.update({
            'object_list': movies,
            })

        return context

class MovieDetail(DetailView):
    model = Movie
    template_name = 'cineflix/movie_detail.html'


    def get_success_url(self):
        return reverse('cineflix:movie_list')

class MovieUpdate(UpdateView):
    model = Movie
    template_name = 'cineflix/movie_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('cineflix:movie_list')

class MovieDelete(DeleteView):
    model = Movie
    template_name = 'cineflix/movie_confirm_delete.html'
    success_url = reverse_lazy('cineflix:movie_list')