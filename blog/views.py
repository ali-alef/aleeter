from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView, DeleteView
)

from .models import Post


def aboutPage(request):
    return render(request, 'blog/aboutPage.html')


class postView(ListView):
    template_name = 'blog/homePage.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 4


class postDetailView(DetailView):
    model = Post


class postDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog-home')

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class postCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class postUpdateView(UserPassesTestMixin, UpdateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('blog-home')

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
