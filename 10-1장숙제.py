import time
import random
import sys
from datetime import datetime


def lots_of_numbers(max):
    for x in range(0, max):
        print(x)

#프로그램이 몇초가 걸렸는지 알아보는 방법
'''
t1 = time.time()
lots_of_numbers(100)
t2 = time.time()

print("%s초가 걸렸습니다." %(t2 - t1))
'''
'''
print(time.asctime())

t = (2007, 5, 27, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))
'''
'''
#로컬타임 저장
print(time.localtime())
t = time.localtime()

#튜플로 t에 넣어논 값들을 접근할 수 있음
year = t[0]
month = t[1]
min = t[4]

print(year, month, min)
'''
'''
#sleep
for x in range(1, 61):
    print(x)
    time.sleep(1)
'''
    
#오늘 시간
def lotto():
    print("지금부터 %s년 %s월 %s일 로또를 시작합니다." %(datetime.today().year, datetime.today().month, datetime.today().day))
    print("첫 번째 번호를 뽑겠습니다.")
    time.sleep(1)
    for x in range(1, 4):
        print(x)
        time.sleep(1)
    first_num = random.randint(1, 45)
    print("첫 번째 번호는 %s!" %first_num)
    print("현재 시각은 %s입니다." %time.asctime())
    time.sleep(3)
    
    print("두 번째 번호를 뽑겠습니다.")
    time.sleep(1)
    for x in range(1, 4):
        print(x)
        time.sleep(1)
    second_num = random.randint(1, 45)
    print("두 번째 번호는 %s!" %second_num)
    print("현재 시각은 %s입니다." %time.asctime())
    time.sleep(3)

    print("세 번째 번호를 뽑겠습니다.")
    time.sleep(1)
    for x in range(1, 4):
        print(x)
        time.sleep(1)
    third_num = random.randint(1, 45)
    print("세 번째 번호는 %s!" %third_num)
    print("현재 시각은 %s입니다." %time.asctime())
    time.sleep(3)

    print("네 번째 번호를 뽑겠습니다.")
    time.sleep(1)
    for x in range(1, 4):
        print(x)
        time.sleep(1)
    fourth_num = random.randint(1, 45)
    print("네 번째 번호는 %s!" %fourth_num)
    print("현재 시각은 %s입니다." %time.asctime())
    time.sleep(3)

    print("다섯 번째 번호를 뽑겠습니다.")
    time.sleep(1)
    for x in range(1, 4):
        print(x)
        time.sleep(1)
    fifth_num = random.randint(1, 45)
    print("다섯 번째 번호는 %s!" %fifth_num)
    print("현재 시각은 %s입니다." %time.asctime())
    time.sleep(3)

    print("여섯 번째 번호를 뽑겠습니다.")
    time.sleep(1)
    for x in range(1, 4):
        print(x)
        time.sleep(1)
    sixth_num = random.randint(1, 45)
    print("여섯 번째 번호는 %s!" %sixth_num)
    print("현재 시각은 %s입니다." %time.asctime())
    time.sleep(3)

    print("혹시 모든 번호를 맞히셨다면 은행을 찾아주시기 바랍니다!")
    return -1

while 1:
    print("로또에 참여하시겠습니까?")
    print("1: yes ㅣ 0: No")
    x = int(sys.stdin.readline())
    if x == 1: 
        lotto()
    elif x == 0:
        print("로또에 참여하지 않으셨습니다.")
        break

'''
첫번 째 번호를 뽑겠습니다.
3
2
1
첫 번째 번호는 x! (뽑은시간 - 현재 시간 나오게 )
(각각 쉬는 시간 조금)
두번 째 번호를 뽑겠습니다.
'''

