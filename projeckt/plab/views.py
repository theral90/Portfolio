from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from plab.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'register.html', {'form': form})


"""class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('index')"""


class HomePageView(View):
    def get(self, request):
        return render(request, "index.html")


class LoginPageView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterPageView(View):
    def get(self, request):
        return render(request, "register.html")


class FormPageView(View):
    def get(self, request):
        return render(request, "form.html")


class ProfileList(ListView):
    model = Profile

class ProfileView(DetailView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile
    fields = ['user','bio','location']
    success_url = reverse_lazy('profile_new')

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['user','bio','location']
    success_url = reverse_lazy('profile_list')

class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('proflie_list')
