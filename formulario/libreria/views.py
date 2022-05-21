from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
	return HttpResponse('<h1 style="color: red;">Hola Mundo</h1>')

def index(request):
	return render(request,'page/index.html')