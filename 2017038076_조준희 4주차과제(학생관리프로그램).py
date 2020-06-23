st=[{'학과':'null','학번':0,'이름':'null','국어':0,'수학':0,'총점':0,'평균':0,'학점':'NULL'},{'학과':'null','학번':0,'이름':'null','국어':0,'수학':0,'총점':0,'평균':0,'학점':'NULL'},{'학과':'null','학번':0,'이름':'null','국어':0,'수학':0,'총점':0,'평균':0,'학점':'NULL'},{'학과':'null','학번':0,'이름':'null','국어':0,'수학':0,'총점':0,'평균':0,'학점':'NULL'},{'학과':'null','학번':0,'이름':'null','국어':0,'수학':0,'총점':0,'평균':0,'학점':'NULL'}]
num=0
while (1) :
    num=int(input("항목을 고르세요\n 1.데이터추가\t 2.데이터검색\t 3.데이터삭제\t 4.데이터 정렬\t 0.프로그램종료\n"))

    if num == 1 :
        n=int(input("몇명의 학생을 추가하십니까?:"))
        for i in range (0,n) :
            if (n>5):
                print("이 프로그램에는 6명이상의 학생을 입력할 수 없습니다.")
                break
            st[i]['학과'] = input("학생의 학과를 추가해주세요:")
            st[i]['학번'] = input("학생의 학번을 추가해주세요:")
            st[i]['이름'] = input("학생의 이름을 추가해주세요:")
            st[i]['국어'] = input("학생의 국어점수를 추가해주세요:")
            st[i]['수학'] = input("학생의 수학점수를 추가해주세요:")
            if (n-1>i) :
                print("==========%d번학생입력이 끝났습니다. %d번학생으로 넘어갑니다.=============\n"%(i+1,i+2))
            st[i]['총점'] = int(st[i].get('국어'))+int(st[i].get('수학'))
            st[i]['평균'] = float(st[i].get('총점'))/2
            if st[i]['평균'] >= 90:
                st[i]['학점'] = 'A'
            elif st[i]['평균'] >= 80:
                st[i]['학점'] = 'B'
            elif st[i]['평균'] >= 70:
                st[i]['학점'] = 'C'
            else:
                st[i]['학점'] = 'F'

    elif num == 2:
        str = input("찾고자하는 학생의 이름 또는 학번을 입력하세요 : ")
        for i in range(0,n) :
            if str == st[i]['이름'] :
                print(st[i])
            elif str == st[i]['학번'] :
                print(st[i])

    elif num == 3 :
        x = input("지우고싶은 학생의 학번 또는 이름을 입력하세요 :")
        for i in range(0,n) :
            if x == st[i].get('학번') :
                del st[i]
                print("%d학번의 학생의 정보가 삭제되었습니다." %int(x))
                break
            elif x==st[i].get('이름') :
                del st[i]
                print("%s의 학생의 정보가 삭제되었습니다."%x)

    elif num == 4 :
        for i in range(0,n) :
            list=sorted(st[i].get('학과'))
            print(list)

    elif num == 0 :
        break

    else :
        print("잘못 입력하신 것 같습니다. 다시 한번 입력해주십쇼.\n")
