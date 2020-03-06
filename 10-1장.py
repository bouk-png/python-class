import time

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
#sleep
for x in range(1, 61):
    print(x)
    time.sleep(1)

#오늘 시간
print("지금부터 xx년 xx월 로또를 시작합니다.")

'''
첫번 째 번호를 뽑겠습니다.
3
2
1
첫 번째 번호는 x! (뽑은시간 - 현재 시간 나오게 )
(각각 쉬는 시간 조금)
두번 째 번호를 뽑겠습니다.
'''