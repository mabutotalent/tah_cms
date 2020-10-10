from django.urls import path

from .views import (
    DashboardCreateView, DashboardDeleteView,
    DashboardUpdateView, DashboardPostListView,
    DashboardPostUpdateView, DashboardPostDeleteView,
    DashboardPostCreateView, DashboardIndexTemplateView,
    CommentListView, CommentDeleteView, CommentUpdateView)


urlpatterns = [
    path('', DashboardCreateView.as_view(), name='dashboard'),
    path('<pk>/delete', DashboardDeleteView.as_view(), name='category_delete'),
    path('update/<pk>', DashboardUpdateView.as_view(), name='category_update'),
    path('post_list/', DashboardPostListView.as_view(), name='posts_list'),
    path('post_update/<pk>/', DashboardPostUpdateView.as_view(), name='post_update'),
    path('<pk>/post_delete/', DashboardPostDeleteView.as_view(), name='post_delete'),
    path('post_create/', DashboardPostCreateView.as_view(), name='create_post'),
    path('home/', DashboardIndexTemplateView.as_view(), name='home'), 
    path('comment/', CommentListView.as_view(), name='comment_list'),
    path('<pk>/comment_delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment_update/<pk>/', CommentUpdateView.as_view(), name='comment_update'),
]