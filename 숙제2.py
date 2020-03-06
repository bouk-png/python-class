def contract:
    print("계약 기간을 입력해 주세요.")
    contract_period = int(sys.stdin.readline())
    print("계약 기간은 %s달입니다." %contract_period)
    for x in range(1, contrarct_period + 1):
        print("계약기간이 %s 달 지났습니다." %x)
    if x == contract_period:
        print("재계약하시겠습니까?")
        y = int(sys.stdin.readline())
        if y == 1:
            print("재계약 기간을 입력해 주세요.")
        elif y == 0:
            print("재계약을 포기하셨습니다.")
    

def player_lent:
    print("임대 기간을 입력해 주세요")
    lent_period = int(sys.stdin.readline())
    print("임대 기간은 %s달입니다." %lent_period)
    for  n in range(1, lent_period + 1):
        print("임대 기간이 %s달 지났습니다." %n)
    if x == lent_period:
        print("임대가 만료되어 선수가 팀으로 복귀하였습니다.")
    print("선수를 임대 보내시겠습니까?")
    i = int(sys.stdin.readline())
    if i == 1:
        print("임대 기간을 입력해주세요.")
        lent_period2 = int(sys.stdin.readline())
    elif i == 0:
        print("선수가 팀으로 복귀하였습니다.")

'''
선수계약
이름
선수 프로필
클래스

문제
계약기간 - 임대기간 
임대기간 입력 - 임대기간은 임대기간 따로 진행 계약 기간이랑 상관 없음

이 둘이 같이 진행되어야함
남은 계약기간 - 1
남은 임대기간 - 1

player_contract()
player_lent()


for 문 반복문에서 -> 함수화
'''

    

