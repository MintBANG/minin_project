import bcrypt
from django.shortcuts import render, redirect

from users.models import Users


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        user_id = request.POST.get('user_id', None)
        user_pw = request.POST.get('user_pw', None)

        new_password = user_pw.encode('utf-8')
        new_salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(new_password, new_salt)

        user = Users()
        user.user_id = user_id
        user.user_pw = hashed_password.decode('utf-8')

        user.save()

        return redirect('/users/login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        user_id = request.POST.get('user_id', None)
        user_pw = request.POST.get('user_pw', None)

        try:
            user = Users.objects.get(user_id=user_id)

            if bcrypt.checkpw(user_pw.encode('utf-8'), user.user_pw.encode('utf-8')):
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                print('로그인 성공')
                return redirect('/')
            else:
                print('로그인 실패')

        except Users.DoesNotExist:
            print('회원 가입한 적 없음')

        return redirect('/users/login')


def logout(request):
    request.session['is_login'] = False
    return redirect('/')