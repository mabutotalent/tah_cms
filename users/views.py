from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.models import auth
from django.contrib import messages
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import CustomUser


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users')


class RegisterUserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('index')

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'posts/index.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')
    return render(request, 'users/logout.html')


# class UserProfileUpdateView(UpdateView):
#     form_class = CustomUserCreationForm
#     template_name = 'users/user_profile.html'
#     success_url = reverse_lazy('users')

#     # def get_success_url(self):
#     #     return reverse('users')
