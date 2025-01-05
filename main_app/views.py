from django.shortcuts import render
from .models import Attend

# Create your views here.

def attend_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            attend_object = Attend(attender=request.user)
            attend_object.save()

    return render(request, "main_app/attend.html", {})
