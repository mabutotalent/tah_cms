from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Category
from posts.models import Post


class IndexListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super(IndexListView, self).get_queryset()
        queryset =  Post.objects.filter(status='publish').order_by('-created')
        return queryset


class SearchPostListView(ListView):
    model = Post
    template_name = 'posts/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super(SearchPostListView, self).get_queryset()
        queryset = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=queryset) | Q(author__username__icontains=queryset)
        )


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_post.html'
    context_object_name = 'category'


class PostCategoryDetailView(DetailView):
    model = Post
    template_name = 'categories/category_post_detail.html'
    context_object_name = 'category_post'




    

    
    

