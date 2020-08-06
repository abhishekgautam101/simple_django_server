from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
 
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'authen/dashboard.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'authen/signup.html', {'form': form})

def landing_view(request):
    return render(request, 'authen/landing.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'authen/dashboard.html')
    else:
        form = AuthenticationForm()
    return render(request, 'authen/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/landing')