from django.shortcuts import render

# Create your views here.

from .models import Course

def home(request):
    courses = Course.objects.all()[:2]  # Get the first 2 courses
    return render(request, 'home.html', {'courses': courses})
