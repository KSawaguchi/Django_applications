from django.shortcuts import render
# Create your views here.

def index(request):
    context = {
        'name': 'Ken',
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def info(request):
    return render(request, 'myapp/info.html')