from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.

def home(request):

    boards = Board.objects.all()

    return render(request,'home.html',{'boards':boards})