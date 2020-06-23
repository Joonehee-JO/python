#작성자 : 조준희
#학과 : 소프트웨어
#학번 : 2017038076
#조 : 파이썬클라쓰(4조)
#프로그램 내용 : 홈페이지 회원가입과 로그인, 로그아웃, 아이디 찾기, 비밀번호 찾기
#최종 완성일자 : 6월 14일
########################
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
