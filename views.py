#작성자 : 조준희
#조 : 4조(파이썬클라쓰)
#프로그램 내용 : 홈페이지 회원가입과 로그인, 로그아웃, 아이디 찾기, 비밀번호 찾기
#최종 완성일자 : 6월 14일
from django.shortcuts import render, redirect
from websites import templates
from .models import User
# Create your views here.
def login(request) :
    if request.method == "POST" :
        users = User.objects.all()
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        for item in users :
            if item.User_id == ID :
                user = User.objects.get(User_id=ID)
                if user.pw == password :
                    login = int(1)
                    logout = int(1)
                    item.status = login
                    item.save()
                    return render(request, 'main.html', {'login':login, 'logout':logout})
                else :
                    error = int(1)
                    return render(request, 'login.html', {'error1':error})
        error = int(1)
        return render(request, 'login.html', {'error1':error})
    return render(request, 'login.html')

def login1(request) :
    if request.method == "POST" :
        users = User.objects.all()
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        for item in users :
            if item.User_id == ID :
                user = User.objects.get(User_id=ID)
                if user.pw == password :
                    login = int(1)
                    logout = int(1)
                    item.status = login
                    item.save()
                    return render(request, 'main.html', {'login':login, 'logout':logout})
                else :
                    error = int(1)
                    return render(request, 'signup.html', {'error1':error})
        error = int(1)
        return render(request, 'signup.html', {'error1':error})
    return render(request, 'signup.html')


def signup(request) :
    if request.method == "POST" :
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        password_again = request.POST.get('password_again')
        name = request.POST.get('name')
        identification_number = int(request.POST.get('identification_number'))
        users = User.objects.all()
        for item in users :
            if item.User_id == ID :
                error = int(2)
                return render(request, 'signup.html', {'error':error})
            elif item.identification_number == identification_number :
                error = 5
                return render(request, 'signup.html', {'error':error})
        if password_again != password :
            error = int(1)
            return render(request, 'signup.html', {'error':error})
        elif len(request.POST.get('name')) == 0 :
            error = 3
            return render(request,'signup.html', {'error':error})
        elif len(request.POST.get('identification_number')) != 6 :
            error = 4
            return render(request, 'signup.html',{'error':error})

        user = User(name=name, pw=password, User_id=ID, identification_number = identification_number)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')


def logout(request) :
    user = User.objects.all()
    for item in user :
        if item.status == 1 :
            item.status = 0
            item.save()
            login = 0
            return render(request, 'main.html', {'login':login})


def find_id(request) :
    if request.method == "POST" :
        if len(request.POST.get('identification_number')) != 6 :
            error = int(2)
            return render(request, 'find_id.html', {'error':error})
        identification_number = int(request.POST.get('identification_number'))
        users = User.objects.all()
        for user in users : 
            if user.identification_number == identification_number :
                user1 = User.objects.get(identification_number = identification_number)
                ID = user1.User_id
                return render(request, 'correct.html', {'id':ID})
        error = int(1)
        return render(request, 'find_id.html', {'error':error})
    return render(request, 'find_id.html')


def find_pw(request) :
    if request.method == "POST" :
        ID = request.POST.get('ID')
        identification_number = int(request.POST.get('identification_number'))
        users = User.objects.all()
        for item in users :
            if item.User_id == ID :
                if item.identification_number == identification_number :
                    user = User.objects.get(User_id=ID)
                    pw = user.pw
                    return render(request, 'correct2.html', {'pw':pw})
        error = 1
        return render(request, 'find_pw.html', {'error':error})
    return render(request, 'find_pw.html')
