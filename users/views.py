from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms, models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


#register
class RegisterView(generic.View):
    def get(self, request):
        form = forms.CustomRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request):
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'users/register.html', {'form': form})




# def register_view(request):
#     if request.method == "POST":
#         form = forms.CustomRegisterForm(request.POST)
#         #form = UserCreationForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('/login/')
#     else:
#         form = forms.CustomRegisterForm
#         #form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})

#authorization

class LoginView(generic.View):
    def get(self, request):
        form = forms.AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    
    def post(self, request):
        form = forms.LoginWithCaptchaForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:user_list')
        return render(request, 'users/login.html', {'form':form})




# def auth_login_view(request):
#     if request.method == 'POST':
#         form = forms.LoginWithCaptchaForm(data=request.POST)
#         #form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('users:user_list')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})

# #выход из сессии
class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


# def auth_logout_view(request):
#     logout(request)
#     return ('users:login')

#Список зарегистрированных пользователей

class UserListView(LoginRequiredMixin, generic.ListView):
    model = models.CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'

# @login_required
# def user_list_view(request):
#     users = models.CustomUser.objects.all()
#     #users = User.objects.all()
#     return render(request, 'users/user_list.html', {'user_list': users})