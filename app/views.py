from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post

# This view is for main page
def mainpage(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}
    return render(request,template_name='app/index.html',context=ctx)


class PostListView(ListView):
    model = Post
    template_name = 'app/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post-detail.html'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'app/post-detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)