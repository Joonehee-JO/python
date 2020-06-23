#작성자 : 조준희
#학과 : 소프트웨어
#학번 : 2017038076
#조 : 파이썬클라쓰(4조)
#프로그램 내용 : 아이디 찾기, 비밀번호 찾기
#최종 완성일자 : 6월 14일
#####################
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
