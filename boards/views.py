from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Board
from django.contrib.auth.models import User
from .models import Topic,Post
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


def new_topic(request,board_id):
    board = get_object_or_404(Board,pk=board_id)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            created_by=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('board_topics',board_id=board.pk)
    return render(request,'new_topic.html',{'board':board})









def about(request):

    return HttpResponse(request,"yes")