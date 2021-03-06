from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

User = get_user_model()

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, password1)
        except:
            user = None

        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['invalid_user'] = 1
    return render(request, "accounts/form.html", {"form": form}) 

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['invalid_user'] = 1
    return render(request, "accounts/form.html", {"form": form})    
    
def logout_view(request):
    logout(request)
    return redirect("login")
