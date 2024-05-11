from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from schedule.models import Schedule


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()

    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    else:
        user_form = UserCreationForm()
    return render(request, "register.html", {"user_form": user_form})


@login_required(login_url="/login/")
def profile_view(request):
    schedules = (
        Schedule.objects.filter(user=request.user)
        .filter(conclude=False)
        .order_by("-id")
    )

    if request.method == "POST":
        schedule = Schedule.objects.filter(id=request.POST.get("id"))
        schedule.delete()

    return render(request, "profile.html", {"schedules": schedules})
