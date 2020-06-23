import threading
class calc :
    value_1 = 0
    value_2 = 0
    value_3 = 0

    def sum_1(self):
        for i in range (1,1001):
          self.value_1 += i
        print("1+2+3+.....+1000=",self.value_1)

    def sum_2(self):
        for i in range (1,100001):
            self.value_2 += i
        print("1+2+3+.....+100000=",self.value_2)

    def sum_3(self):
        for i in range(1,10000001):
            self.value_3 += i
        print("1+2+3+.....+10000000=",self.value_3)

result_1 = calc()
result_2 = calc()
result_3 = calc()

th1 = threading.Thread(target = result_1.sum_1())
th2 = threading.Thread(target = result_2.sum_2())
th3 = threading.Thread(target = result_3.sum_3())
