from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegistrationForm()

    return render(request, "absensi/main.html", {'form': form})

