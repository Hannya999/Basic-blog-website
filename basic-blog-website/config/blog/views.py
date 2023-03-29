from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class BlogChairmanView(CreateView):
    model = Post
    template_name = 'chairman.html'
    fields = ['body']

class BlogVicePresidentView(CreateView):
    model = Post
    template_name = 'vice_president.html'
    fields = ['body']

class BlogCommunicationView(CreateView):
    model = Post
    template_name = 'communication.html'
    fields = ['body']


