from django.shortcuts import render

def index(request):
    return render(request,"briks/index.html")

def blog(request):
    return render(request,"briks/blog.html")

def blog_2004(request):
    return render(request,"briks/blog_2004.html")

def about(request):
    return render(request,"briks/about.html")

def contact(request):
    return render(request,"briks/contact.html")

def portfolio_one(request):
    return render(request,"briks/portfolio_one.html")

def portfolio_two(request):
    return render(request,"briks/portfolio_two.html")

# Create your views here.
