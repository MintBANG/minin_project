import os
from django.contrib.sites import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from board.forms import BoardForm, ImageForm
from board.models import Board, BoardImage
from config import settings
from users.models import Users
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def main(request):
    return render(request, 'index.html')

def like(request, bid):
    result = Board.objects.get(id=bid)
    user = Users.objects.get(user_id=request.session['user_id'])
    if result.like.filter(id=user.id).exists():
        result.like.remove(user)
        message = "del like"
    else :
        result.like.add(user)
        message = "add like"
    return JsonResponse({'message':message, 'like_cnt':result.like.count()})

def register(request):
    if request.method == "GET":
        boardForm = BoardForm()
        return render(request, 'register.html', {'boardForm': boardForm})

    elif request.method == "POST":
        boardForm = BoardForm(request.POST, request.FILES)
        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.writer = Users.objects.get(user_id=request.session['user_id'])
            board.save()
            return redirect('/list_seasons')

def update(request, bid):
    post = Board.objects.get(id=bid)
    if request.method == "GET":
        # boardForm = BoardForm(instance=post)
        return render(request, 'update.html', {'post':post})
    elif request.method == "POST":
        boardForm = BoardForm(request.POST, request.FILES)
        if boardForm.is_valid():
            post.title = boardForm.cleaned_data['title']
            post.image = boardForm.cleaned_data['image']
            post.contents = boardForm.cleaned_data['contents']
            post.save()
            return redirect('/post/' + str(bid))


def delete(request, bid):
    post = Board.objects.get(id=bid)
    post.delete()

    return redirect('/list_seasons')

def post(request, bid):
    result = Board.objects.get(id=bid)
    context = {
        "result" : result
    }
    return render(request, 'post1.html', context)

def read(request, bid):
    result = Board.objects.prefetch_related('boardimage_set').get(id=bid)

    context = {
        "result": result
    }

    return render(request, 'post1.html', context)

def list_seasons(request):
    posts = Board.objects.all().order_by('-id')
    return render(request, 'list.html', {'posts': posts})

def read_list(request):
    posts = Board.objects.all().order_by('-id')
    json = {'posts':[]}
    for post in posts:
        json['posts'].append({"title":post.title,
                              "contents":post.contents})
    return JsonResponse(json)

def doctor(request):
    return render(request, 'doctor.html')


#---------------------------------------------------------------------------------------------------------
# 이미지
def upload(request):
    if request.method == "GET":
        imageForm = ImageForm()
        return render(request, 'upload.html', {'imageForm': imageForm})

    elif request.method == "POST":
        imageForm = ImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
            board = imageForm.save(commit=False)
            board.save()
            return redirect('/list_image')

def list_image(request):
    posts = BoardImage.objects.all().order_by('-id')
    return render(request, 'list_image.html', {'posts': posts})

def view(request, bid):
    result = BoardImage.objects.get(id=bid)
    context = {
        "result" : result
    }
    return render(request, 'view.html', context)


def download_image(request, bid):
    # 이미지 파일 경로 설정
    image_path = os.path.join(settings.MEDIA_ROOT, 'images', str(id=bid) + '.jpg')

    # 파일이 존재하는 경우
    if os.path.exists(image_path):
        # 다운로드할 파일 오픈
        with open(image_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(image_path)
            return response

    # 파일이 존재하지 않는 경우
    return HttpResponse('File not found')

def search(request):
    image_list = BoardImage.objects.all()

    search_key = request.GET.get('search_key')
    if search_key:
        image_list = image_list.filter(image_title__icontains=search_key)
    return render(request, 'list_image.html', {'image_list': image_list})

def get_queryset(self):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')
    notice_list = Board.objects.order_by('-id')

    if search_keyword:
        if len(search_keyword) > 1:
            if search_type == 'all':
                search_notice_list = notice_list.filter(
                    Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                        writer__user_id__icontains=search_keyword))
            elif search_type == 'image_title':
                search_notice_list = notice_list.filter(image_title__icontains=search_keyword)

            return search_notice_list
        else:
            messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
    return notice_list

#--------------------------------------------------------------------------------------------------------
# 시즌별 용
def list(request):
    result = Board.objects.all().order_by('-id')

    context = {
        "result": result
    }
    return render(request, 'list2.html', context)


def post_1(request):
    return render(request, 'seasons/post_1.html')

