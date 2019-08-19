from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from plab.forms import SignUpForm

"""
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('first')
    else:
        form = SignUpForm()
    return render(request, 'login.html', {'form': form})
"""

class FirstView(View):
    def get(self, request):
        return render(request, "index.html")

