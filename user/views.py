from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib.auth import authenticate #사용자가 있는지 검사하는 함수
from django.contrib import auth

# Create your views here.

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return render(request, 'signup.html', {'error': '아이디와 패스워드를 입력해주세요.'})
        else:
            UserModel.objects.create_user(username=username, password=password, address=address, phone=phone)
            return redirect('/login') # 회원가입이 완료되었으므로 로그인 페이지로 이동


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user_ck = authenticate(request, username=username, password=password) # 사용자 이메일로 불러오기
        if user_ck is not None:  # 이메일로 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, user_ck)
            return redirect('/home')
        else:
            return render(request,'login.html',{'error':'이메일 혹은 패스워드를 확인 해 주세요'})  # 로그인 실패
    
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            return render(request, 'login.html')
        
def home_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            return render(request, 'home.html',)
        else:  # 로그인이 되어 있지 않다면
            return redirect('/login')


def logout(request):   #로그아웃 함수
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect('/login')
