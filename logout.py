#작성자 : 조준희
#학과 : 소프트웨어
#학번 : 2017038076
#조 : 파이썬클라쓰(4조)
#프로그램 내용 : 홈페이지 로그아웃 기능
#최종 완성일자 : 6월 14일
###########################
def logout(request) : #로그아웃을 위한 기능 / User모델 각 객체의 필드 중 상태필드를 활용하여 해당 고객이 로그인상태인지 확인하고 로그아웃을 처리한다.
    user = User.objects.all()
    for item in user :
        if item.status == 1 :
            item.status = 0
            item.save()
            login = 0
            return render(request, 'main.html', {'login':login})
