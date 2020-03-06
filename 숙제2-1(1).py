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

#1. 선수 검색 #(*숙제!*)
def search_player(player_list):
    pass

#2. 선수 계약 
def player_contract(player_list, pi, my_list): #pi는 플레이어 인덱스
    #계약 할 것인가 물어보기 1은 yes 0은 no
    print("계약하시겠습니까?")
    print("yes: 1 | no: 0")
    y = int(sys.stdin.readline())
    if y == 1:
        print("계약 기간을 입력해 주세요.")
        contract_p = int(sys.stdin.readline())

        #(*숙제!*) 1보다 작은 값을 입력했다면 잘못 입력했다고 표시하고 함수 종료!
        
        print("계약 기간은 %s달입니다." %contract_p)
        player_list[pi].set_contract_period(contract_p)
        my_list.append(player_list[pi])
        return
        #return contract_p
    elif y == 0:
        print("계약을 포기하셨습니다.")
        return

#3. 선수 임대 
def player_lent(my_list):
    #임대 할 것인가 물어보기 1은 yes 0은 no
    print("임대하시겠습니까?")
    print("yes: 1 | no: 0")
    x = int(sys.stdin.readline())
    if x == 1:
        print("임대 기간을 입력해 주세요")
        lent_p = int(sys.stdin.readline())

        #(*숙제!*) 임대 기간도 계약과 같지만 계약 기간보다 임대기간이 작거나 같아야 된다는 조건 추가

        print("임대 기간은 %s달입니다." %lent_p)
        return lent_p
    elif x == 0:
        print("선수가 팀으로 복귀하였습니다.")
        return -1
        
#4. 전체 선수 목록에 선수 추가
def add_player(player_list):
    print("선수를 추가하시겠습니까?")
    print("yes: 1 | no: 0")
    i = int(sys.stdin.readline())
    if i == 1:
        print("추가하실 선수 이름을 입력해주세요.")
        name = sys.stdin.readline().rstrip('\n')
        print("추가하실 선수 나이를 입력해주세요.")
        age = int(sys.stdin.readline())
        print("추가하실 선수 포지션을 입력해주세요")
        position = sys.stdin.readline().rstrip('\n')
        New_player = Player(name, age, position)
        player_list.append(New_player)
        print("선수가 추가되었습니다.")
        print("")
    elif i == 0:
        print("선수를 추가하지 않았습니다.")
        print("")
        return -1

#5. 전체 선수 목록에서 선수 삭제
def remove_player(player_list):
    print("선수를 삭제하시겠습니까?")
    print("yes: 1 ㅣ no: 0")
    j = int(sys.stdin.readline())
    if j == 1:
        print("삭제하실 선수 이름을 입력해주세요.")
        
        delete_player = sys.stdin.readline().lower().rstrip('\n')
        i = 0
        for i in range(0, len(player_list)):
            pname = player_list[i].player_name.lower()
            
            if(delete_player == pname):
                del player_list[i]
                print("선수가 삭제되었습니다.")
                print("")
                return
        
        if i == len(player_list):
            print("해당 이름을 가진 선수가 없습니다.")
            print("")

    elif j == 0:
        print("선수를 삭제하지 않았습니다.")
        print("")
        return -1

#6. 선수 목록 보기
def show_all_players(player_list):
    print("선수 목록을 출력합니다.")
    for i in player_list:
        print("Name: %s | Age: %s | Position: %s" % (i.player_name, i.player_age, i.player_position))
    print("")

#7. 내 선수 목록
def show_my_players(player_list):
    print("선수 목록을 출력합니다.")
    for i in player_list:
        print("Name: %s | Age: %s | Position: %s" % (i.player_name, i.player_age, i.player_position))
    print("")

#8. 턴 종료 (1달이 지나게 함)
#내 선수들의 계약기간과 임대기간이 이 함수를 실행할때마다 -1이 되어야함

def time_pass(contract_period, lent_period):
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


    '''
    주석코드도 ㅇㅋ
    '''


    #계약기간 종료 재계약을 위해 계약 함수 호출
    if contract_period == 0:
        print("계약이 종료되었습니다.")
        print("")
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
#기본 선수들을 객체로 만들었다
player1 = Player("Messi", 33, "FW")
player2 = Player("Ronaldo", 30, "GK")
player3 = Player("Bouk", 15, "MF")

'''
#index로 순서 찾기
name_list = ["son", "ha", "kim", "lee"]
print(name_list.index("kim"))
'''

#전체 선수 목록
player_list = [player1, player2, player3]

#내 선수 목록
my_player_list = []

while 1:
    print("1. 선수 검색")
    print("2. 선수 계약")
    print("3. 선수 임대")
    print("4. 선수 추가")
    print("5. 선수 삭제")
    print("6. 선수 목록")
    print("7. 내 선수 목록")
    #print("8. 턴 종료")
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
            #pname이라는 변수에 플레이어리스트의 i번째 선수이름을 작은 글자 값을 넣어줬다.
            pname = player_list[i].player_name.lower()
            
            if(search_name == pname):
                print("Name: %s | Age: %s | Position: %s" % (player_list[i].player_name, player_list[i].player_age, player_list[i].player_position))
                print("")

    elif select_menu == 2:
        #선수 목록에서 한명을 선택하고 계약
        #먼저 선수 선택을 해야함

        #계약하고 그 데이터를 선수에게 입력
        #Messi 계약 -> 
        print("계약할 선수의 이름을 입력해 주세요.")
        contract_player = sys.stdin.readline().lower().rstrip('/n')
        for i in range(0, len(player_list)):
            pname = player_list[i].player_name.lower()
            
            if(contract_player == pname):
                player_contract(player_list, i, my_player_list)
                
                
                print("")
                return
        
        if i == len(player_list):
            print("해당 이름을 가진 선수가 없습니다.")
            print("")

        
        lent_period = player_lent()
    
    elif select_menu == 4:
        add_player(player_list)

   
    elif select_menu == 5:
        #전체 선수 목록에서 선수 삭제
        remove_player(player_list)
    
    elif select_menu == 6:
        show_all_players(player_list)
    
    elif select_menu == 7:
        show_my_players(my_player_list)

    elif select_menu == 8:
        #time pass
        time_pass(contract_period, lent_period)
        print("")
    
    elif select_menu == 0:
        break
    
    else:
        print("잘못 입력하셨습니다.(입력은 숫자 0-5까지)")
        print("")
    # 숙제: #3, #4 선택지 2번은 선수 선택, 계약 정보 선수에게 입력
    

#2/17 숙제

# 2번 3번 8번 + 모든 코드 (가능한 많이 기능 위주로) 주석달기
# 기본 선수 추가하기 10명?(이건 마음껏)
# 내 선수 목록에 아무 선수도 없다면 len(my_player_list)가 0이면 아무도 없다고 출력
# 6번에 포지션별 목록 보기 






