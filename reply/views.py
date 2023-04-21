from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from board.models import Board
from reply.forms import CommentForm
from reply.models import Comment


def like(request, cid):
    comment = Comment.objects.get(Q(id=cid))
    user = request.user
    if comment.like.filter(id=user.id).exists():
        comment.like.remove(user)
        message = "del like"
    else :
        comment.like.add(user)
        message = "add like"
    return JsonResponse({'message':message,
                         'like_cnt':comment.like.count()})

def delete(request, cid):
    comment = Comment.objects.get(Q(id=cid))
    comment.delete()
    return redirect('/comment/list')


def read(request, cid):
    comment = Comment.objects.get(Q(id=cid))
    return render(request, 'comment/read.html', {'comment': comment})


def list(request):
    comments = Comment.objects.all().order_by('-id')
    return render(request, 'comment/list.html', {'comments': comments})


def register(request, bid):
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.board = Board.objects.get(Q(id=bid))
            comment.save()
            return redirect('/post/' + str(bid))
