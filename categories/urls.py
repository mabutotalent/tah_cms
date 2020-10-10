from django.urls import path 

from .views import IndexListView, SearchPostListView, CategoryDetailView, PostCategoryDetailView


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('search/', SearchPostListView.as_view(), name='search_results'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='post_category'),
    path('post_category/<int:pk>/', PostCategoryDetailView.as_view(), name='category_post_detail'),
]