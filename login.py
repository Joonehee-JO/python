#작성자 : 조준희
#학과 : 소프트웨어
#학번 : 2017038076
#조 : 파이썬클라쓰(4조)
#프로그램 내용 : 홈페이지 로그인 부분
#최종 완성일자 : 6월 14일
from django.shortcuts import render, redirect
from websites import templates
from .models import User
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
