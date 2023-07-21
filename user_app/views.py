from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm       # username, email, pass1, pass2
# Create your views here.
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def user_signup(request):
    if request.method == "POST":
        data = request.POST
        form = NewUserForm(data)
        if form.is_valid():
            user = form.save()               # user entry in auth_user table
            print(user)
            messages.success(request, f"User '{user.username}' registered Successfully. You can login here")
            return redirect("user_login")
        else:
            messages.error(request, "Unsuccessful Signup. Invalid information.")

    elif request.method == "GET":
        form = NewUserForm()
        return render(request=request, template_name="user_register.html", context={"signup_form":form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = user_name, password = password)   # database ke sath verify krega
            if user:
                login(request, user)
                messages.success(request,"Logged in succesfully..!")

                return redirect("home_page")
            else:
               messages.error(request,"Invalid username or password.")
    elif request.method == "GET":
        return render(request, "login.html", {"login_form": AuthenticationForm()})


def user_logout(request):
    logout(request)
    return redirect("user_login")
