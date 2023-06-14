from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment


def mainpage(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, template_name='app/index.html', context=ctx)


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'app/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'app/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self,*args, **kwargs):
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context = {"total_likes":total_likes}
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def like_view(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('posts'))


class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'app/post-comment.html'
    context_object_name = 'comments'
    ordering = ['-date_sent']
