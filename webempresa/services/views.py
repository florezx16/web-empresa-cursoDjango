from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    services = Service.objects.all()
    active_page = 'services'
    return render(request,'services/services.html',{'active_page':active_page,'services':services})