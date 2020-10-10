from django.urls import path 

from .views import UserCreateView, UsersListView, login, logout, RegisterUserCreateView


urlpatterns = [
    path('list/', UsersListView.as_view(), name='users'),
    path('register/', UserCreateView.as_view(), name='users_create'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register_user/', RegisterUserCreateView.as_view(), name='register_user'),
    # path('users_update/<pk>/', UserProfileUpdateView.as_view(), name='userr_update'),
]