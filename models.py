#작성자 : 조준희
#학과 : 소프트웨어
#학번 : 2017038076
#조 : 파이썬클라쓰(4조)
#프로그램 내용 : 유저 모델 제작
###############################
from django.db import models

class User(models.Model):  
    name = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    User_id = models.CharField(max_length=200)
    status = models.IntegerField(default = 0)
    identification_number = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name
