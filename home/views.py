from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html',)

def contact(request):
    return render(request, 'contact.html',)

def portfolio(request):
    return render(request, 'portfolio.html',)

def price(request):
    return render(request, 'price.html',)

def services(request):
    return render(request, 'services.html',)

def blog(request):
    return render(request, 'blog-home.html')

def elements(request):
    return render(request, 'elements.html')

def blogsingle(request):
    return render(request, 'blog-single.html')