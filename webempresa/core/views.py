from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    active_page = 'home'
    return render(request,'core/home.html',{'active_page':active_page})

def about(request):
    active_page = 'about_us'
    return render(request,'core/about_us.html',{'active_page':active_page})

def store(request):
    active_page = 'store'
    return render(request,'core/store.html',{'active_page':active_page})

