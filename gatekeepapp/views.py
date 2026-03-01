from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == "guard":
                return redirect("guard_dashboard")
            elif user.role == "resident":
                return redirect("resident_dashboard")
            else:
                return redirect("admin:index")

        else:
            return render(request, "gatekeepapp/login.html", {"error": "Invalid credentials"})

    return render(request, "gatekeepapp/login.html")



@login_required
def guard_dashboard(request):
    return render(request, "core/guard.html")

@login_required
def resident_dashboard(request):
    return render(request, "core/resident.html")