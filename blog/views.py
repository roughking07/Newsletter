from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.
def index(request):
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=832e9a649ae34f37a0d77947c4c1d771"
    response = requests.get(url) 
    jsonResponse = response.json()
    articles = jsonResponse['articles'] 
    return render(request,'index.html',{'articles':articles})

def specific(request):
    return HttpResponse("SJFvbvav")

def article(request,article_id):
    return render(request,'index.html',{'article_id':article_id})

def about(request):
    return render(request,'about.html')