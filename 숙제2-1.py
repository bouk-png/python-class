import sys

class Player():
    def __init__(self, name, age, position):
        self.player_name = name
        self.player_age = age
        self.player_position = position
    
    def set_contract_period(self, contract_period):
        self.player_contract_period = contract_period
    
    def set_lent_period(self, lent_period):
        self.player_lent_period = lent_period

    def set_team(self, team):
        self.player_team = team

def player_contract():
    #계약 할 것인가 물어보기 1은 yes 0은 no
    print("계약하시겠습니까?")
    print("yes: 1 | no: 0")
    y = int(sys.stdin.readline())
    if y == 1:
        print("계약 기간을 입력해 주세요.")
        contract_p = int(sys.stdin.readline())
        print("계약 기간은 %s달입니다." %contract_p)
        return contract_p
    elif y == 0:
        print("계약을 포기하셨습니다.")
        return -1


def player_lent():
    #임대 할 것인가 물어보기 1은 yes 0은 no
    print("임대하시겠습니까?")
    print("yes: 1 | no: 0")
    x = int(sys.stdin.readline())
    if x == 1:
        print("임대 기간을 입력해 주세요")
        lent_p = int(sys.stdin.readline())
        print("임대 기간은 %s달입니다." %lent_p)
        return lent_p
    elif x == 0:
        print("선수가 팀으로 복귀하였습니다.")
        return -1

def time_pass(contract_period, lent_period):
    '''
    아래 있는 while문 종료 조건
    1. 계약기간 끝 임대기간 끝
    2. 계약기간 끝 임대기간 남음
    '''
    while 1:
        #남은 기간임으로 -1 해준 기간을 출력
        contract_period = contract_period - 1
        print("계약 기간이 %s 달 남았습니다." %contract_period)

        #임대중인 경우 0보다 큼 임대중이 아닌경우 0보다 작음
        if lent_period < 0 :
            print("소속팀에서 뛰고 있습니다.")
        else:
            #남은 기간임으로 -1 해준 기간을 출력
            lent_period = lent_period - 1
            print("임대 기간이 %s 달 남았습니다." %lent_period)
        
        #계약기간 종료 재계약을 위해 계약 함수 호출
        if contract_period == 0:
            print("계약이 종료되었습니다.")
            #계약 함수가 결과를 돌려줌
            contract_period = player_contract()
            #결과가 -1일 경우 임대기간과 상관 없이 첫 화면으로 return
            if contract_period == -1: 
                return
        
        #lent_period = 0은 기간 만료 -1은 임대 안보냄
        if lent_period <= 0:
            print("임대할 수 있습니다.")
            lent_period = player_lent()



######################################################################

#기본 데이터값
player1 = Player("Messi", 33, "FW")
player2 = Player("Ronaldo", 30, "GK")
player3 = Player("Bouk", 15, "MF")


#전체 선수 목록
player_list = [player1, player2, player3]

#내 선수 목록
#my_player_list = [player1]

while 1:
    print("1. 선수 검색")
    print("2. 선수 계약/임대")
    #print("3. 선수 추가")
    #print("4. 선수 삭제")
    #print("5. 턴 종료")
    print("0. 프로그램 종료")

    #contract_period = 0
    #lent_period = 0

    select_menu = int(sys.stdin.readline())
    if select_menu == 1:
        #선수검색
        #숙제 검색 방법을 선택하세요 1. 이름, 2. 포지션
        #검색 방법 함수화 search_by_name, search_by_position
        print("이름 입력")
        search_name = sys.stdin.readline().lower().rstrip('\n')

        for i in range(0, len(player_list)):
            pname = player_list[i].player_name.lower()
            
            if(search_name == pname):
                print("Name: %s | Age: %s | Position: %s" % (player_list[i].player_name, player_list[i].player_age, player_list[i].player_position))

    elif select_menu == 2:
        #선수 목록에서 한명을 선택하고 계약
        #먼저 선수 선택을 해야함

        #계약하고 그 데이터를 선수에게 입력
        #Messi 계약 -> 
        contract_period = player_contract()
        lent_period = player_lent()
    
    elif select_menu == 3:
        #전체 선수 목록에 선수 추가
        print("")
    
    elif select_menu == 4:
        #전체 선수 목록에서 선수 삭제
        print("")
    
    elif select_menu == 5:
        #time pass
        time_pass(contract_period, lent_period)
        print("")
    
    elif select_menu == 0:
        break
    
    else:
        print("잘못 입력하셨습니다.(입력은 숫자 0-5까지)")

    # 숙제: #3, #4 선택지 2번은 선수 선택, 계약 정보 선수에게 입력
    








