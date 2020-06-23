#작성자 : 조준희
#학과 : 소프트웨어
#학번 : 2017038076
#조 : 파이썬클라쓰(4조)
#프로그램 내용 : 유저 앱 관련 기능을 사용하기 위한 경로 지정
##############################
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('find_id/', views.find_id, name = "find_id"),
    path('find_pw/', views.find_pw, name="find_pw"),
    path('login1/', views.login1, name="login1"),
]
