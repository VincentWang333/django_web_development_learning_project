from django.shortcuts import render 

from django.http import HttpResponse

def index(requres):
    return HttpResponse("hi, welcome to the pratice index")
