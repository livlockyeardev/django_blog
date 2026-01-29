from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog_post(request):
    return HttpResponse("This is a blog post.")