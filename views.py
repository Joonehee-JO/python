#작성자 : 조준희
#학과 : 소프트웨어
#학번 : 2017038076
#조 : 파이썬클라쓰(4조)
#프로그램 내용 : 홈페이지 회원가입과 로그인, 로그아웃, 아이디 찾기, 비밀번호 찾기
#최종 완성일자 : 6월 14일
##############################
from django.shortcuts import render, redirect
from websites import templates
from .models import User
# Create your views here.
def login(request) : #로그인을 구현하기 위한 함수 / 포스트형식으로 값이 들어오면 해당 값을 이용하여 해당되는 User객체가 있는지 확인하고 생성되어있다면 해당 객체의 상태필드를 이용하여 로그인 구현
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

def login1(request) : #현재 웹페이지의 login창과 signup창에서 로그인을 수행할 수 있도록 구현했기에 signup창에서의 로그인과 login창에서의 로그인함수를 만들었다.
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


def signup(request) : #회원가입을 위한 기능 / 이 기능을 통하여 직접만든 User모델에 들을 추가하여 객체를 생성한다.
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


def logout(request) : #로그아웃을 위한 기능 / User모델 각 객체의 필드 중 상태필드를 활용하여 해당 고객이 로그인상태인지 확인하고 로그아웃을 처리한다.
    user = User.objects.all()
    for item in user :
        if item.status == 1 :
            item.status = 0
            item.save()
            login = 0
            return render(request, 'main.html', {'login':login})


def find_id(request) : #User객체들 중 유일한 값을 활용하여 해당되는 객체를 찾고 해당객체의 id필드를 html창으로 보내줌으로써 아이디찾는 기능을 구현
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


def find_pw(request) : #User객체들 중 유일한 값을 활용하여 해당되는 객체를 찾고 해당객체의 pw필드를 html창으로 보내줌으로써 찾는 기능을 구현
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
