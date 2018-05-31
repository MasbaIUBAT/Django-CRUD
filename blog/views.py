from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
	template_name = 'list.html'
	model = Post

class PostCreateView(CreateView):
	template_name = 'create.html'
	form_class = PostForm

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostCreateView, self).form_valid(form)


class PostDetailView(DetailView):
	template_name = 'detail.html'
	model = Post

class PostUpdateView(UpdateView):
	template_name = 'update.html'
	form_class = PostForm
	model = Post


class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('list')


