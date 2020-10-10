from django.views.generic import ( CreateView,
                                ListView,
                                DeleteView,
                                UpdateView, TemplateView )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from categories.models import Category
from posts.models import Post, Comment
from users.models import CustomUser


class DashboardIndexTemplateView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'dashboard/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(DashboardIndexTemplateView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all()
        context['users'] = CustomUser.objects.all()
        return context


class DashboardCreateView(LoginRequiredMixin, CreateView):
    model = Category 
    template_name = 'dashboard/category.html'
    fields = ['title']

    def get_success_url(self):
        return reverse('dashboard')

    def get_context_data(self, **kwargs):
        context = super(DashboardCreateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class DashboardUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['title']
    template_name = 'dashboard/category_update.html'

    def get_success_url(self):
        return reverse('dashboard')


class DashboardDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('dashboard')


class DashboardPostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'dashboard/post_create.html'
    fields = ['author', 'title', 'category', 'status', 'image', 'content']

    def get_success_url(self):
        return reverse('posts_list')


class DashboardPostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'dashboard/post_list.html'


class DashboardPostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['author', 'title', 'category', 'status', 'image']
    template_name = 'dashboard/post_update.html'

    def get_success_url(self):
        return reverse('posts_list')


class DashboardPostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list')


class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'dashboard/comment_list.html'
    context_object_name = 'comments'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body', 'active']
    template_name = 'dashboard/comment_update.html'

    def get_success_url(self):
        return reverse('comment_list')








