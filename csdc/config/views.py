from django.shortcuts import render

from user.models import User, UserProfile

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html', { 'admins': User.objects.filter(is_superuser=True), 'users': UserProfile.objects.filter(role='Mentor') })