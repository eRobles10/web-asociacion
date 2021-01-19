from django.shortcuts import render, get_object_or_404
from .models import Blog, Post, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PageForm
# Create your views here.


class PostsListView(ListView):
    template_name = "blog/blog.html"
    model = Post
    categories= Category.objects.all()
    paginate_by = 4
    last_3_posts = Post.objects.all()[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        context['last_3_posts'] = self.last_3_posts
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"


class PostCreateView(CreateView):
    model = Post
    form_class= PageForm
    success_url = reverse_lazy('blog')
    
class PostUpdateView(UpdateView):
    model = Post
    fields= ['title','intro','content', 'image', 'categories']
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('update',args=[self.object.id])+"?success"


class CategoryListView(ListView):
    model = Post
    template_name = "blog/blog.html"
    categories= Category.objects.all()
    paginate_by = 4
    def get_queryset(self, *args, **kwargs):
     return Post.objects.filter(categories=self.kwargs['pk'])

    last_3_posts = Post.objects.all()[:3]

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        context['last_3_posts'] = self.last_3_posts
        return context



