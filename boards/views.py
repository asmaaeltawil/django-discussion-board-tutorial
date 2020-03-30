from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Board
# Create your views here.

def home(request):

    boards = Board.objects.all()

    return render(request,'home.html',{'boards':boards})


def board_topics(request,board_id):
    # try:
    #     board = Board.objects.get(pk=board_id)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board,pk=board_id)
    return render(request,'topics.html',{'board':board})





def about(request):

    return HttpResponse(request,"yes")