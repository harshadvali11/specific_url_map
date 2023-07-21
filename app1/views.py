from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>Pelli Kaani Prasaduuuuuu</h1>')

def second(request):
    return HttpResponse('<h1>Parasad U will not get Malleshwari </h1>')