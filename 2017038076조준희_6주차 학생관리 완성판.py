#파일이름 : 학생관리 프로그램(개인과제)
#작성자 : 조준희
#학번 : 2017038076
#학과 : 소프트웨어학과
###################
class student:
    st=[]
    people = 0
    def interface(self,n) :
        self.people += n
        for i in range(0, n):
            self.st[i]['학과'] = input("학생의 학과를 추가해주세요:")
            self.st[i]['학번'] = input("학생의 학번을 추가해주세요:")
            self.st[i]['이름'] = input("학생의 이름을 추가해주세요:")
            self.st[i]['국어'] = int(input("학생의 국어점수를 추가해주세요:"))
            self.st[i]['수학'] = int(input("학생의 수학점수를 추가해주세요:"))
            if (n - 1 > i):
                print("==========%d번학생입력이 끝났습니다. %d번학생으로 넘어갑니다.=============\n" % (i + 1, i + 2))
            self.st[i]['총점'] = self.st[i].get('국어') + self.st[i].get('수학')
            self.st[i]['평균'] = self.st[i].get('총점') / 2
            if self.st[i]['평균'] >= 90:
                self.st[i]['학점'] = 'A'
            elif self.st[i]['평균'] >= 80:
                self.st[i]['학점'] = 'B'
            elif self.st[i]['평균'] >= 70:
                self.st[i]['학점'] = 'C'
            elif self.st[i]['평균'] >= 60:
                self.st[i]['학점'] = 'D'
            else:
                self.st[i]['학점'] = 'F'

    def interface_2(self,n,count_1):
        self.people += n
        for i in range(0,n,1):
            self.st[i+count_1]['학과'] = input("학생의 학과를 추가해주세요:")
            self.st[i+count_1]['학번'] = input("학생의 학번을 추가해주세요:")
            self.st[i+count_1]['이름'] = input("학생의 이름을 추가해주세요:")
            self.st[i+count_1]['국어'] = int(input("학생의 국어점수를 추가해주세요:"))
            self.st[i+count_1]['수학'] = int(input("학생의 수학점수를 추가해주세요:"))
            if (n - 1 > i):
                print("==========%d번학생입력이 끝났습니다. %d번학생으로 넘어갑니다.=============\n" % (i + 1, i + 2))
            self.st[i+count_1]['총점'] = self.st[i+count_1].get('국어') + self.st[i+count_1].get('수학')
            self.st[i+count_1]['평균'] = self.st[i+count_1].get('총점') / 2
            if self.st[i+count_1]['평균'] >= 90:
                self.st[i+count_1]['학점'] = 'A'
            elif self.st[i+count_1]['평균'] >= 80:
                self.st[i+count_1]['학점'] = 'B'
            elif self.st[i+count_1]['평균'] >= 70:
                self.st[i+count_1]['학점'] = 'C'
            elif self.st[i+count_1]['평균'] >= 60:
                self.st[i+count_1]['학점'] = 'D'
            else:
                self.st[i+count_1]['학점'] = 'F'

    def search(self,count_1) :
        str = input("찾고자하는 학생의 이름 또는 학번을 입력하세요 : ")
        for i in range(0, count_1):
            if str == self.st[i]['이름']:
                print(self.st[i])

            elif str == self.st[i]['학번']:
                print(self.st[i])

    def delete(self,count_1):
        str = input("삭제할 학생의 학번 또는 이름을 입력해주세요 :")
        for i in range(0, count_1):
            if str == self.st[i].get('학번'):
                del self.st[i]
                print("%s학번의 학생의 정보가 삭제되었습니다." %str)
                break

            elif str == self.st[i].get('이름'):
                del self.st[i]
                print("%s의 학생의 정보가 삭제되었습니다." %str)
                break

    def sort_x(self,count_1):
        list=[]
        from operator import itemgetter
        x = int(input("어떤 순으로 정렬하시겠습니까\n1. 학과 \t2. 이름\n"))
        if x == 1:
            list = sorted(self.st, key=itemgetter('학과'))
        elif x == 2:
            list = sorted(self.st, key=itemgetter('이름'))
        for i in range(0,count_1):
            print(list[i])
count = 0
count_1 = 0
while(1):
    num = int(input("항목을 고르세요\n 1.데이터추가\t 2.데이터검색\t 3.데이터삭제\t 4.데이터 정렬\t 0.프로그램종료\n"))
    if num == 1 :
        n = int(input("몇명의 학생을 추가하십니까 :"))
        student_interface = student()
        for i in range(0,n):
            student_interface.st.append({'학과':'','학번':'','이름':'', '국어':0,'수학':0,'총점':0,'평균':0,'학점':''})
        if count == 0 :
            student_interface.interface(n)
        elif count >= 1:
            student_interface.interface_2(n,count_1)
        count_1 += n
        count += 1

    elif num == 2:
        student_interface.search(count_1)

    elif num == 3 :
        student_interface.delete(count_1)
        count_1 -= 1

    elif num == 4 :
        student_interface.sort_x(count_1)

    elif num == 0 :
        break

    else :
        print("잘못 입력하신 것 같습니다. 다시 한번 입력해주십쇼.\n")
