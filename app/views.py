from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return render(request,'app/hello.html',{})

def index(request):
    return render(request,'app/index.html',{})