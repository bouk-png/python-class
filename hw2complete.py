import sys

#숙제 에러 방지, 턴 종료

class Player:
    def __init__(self, name, age, position):
        self.player_name = name
        self.player_age = age
        self.player_position = position
        self.player_lent_period = -1
    #player 라는 클래스를 만들어 객체인 축구선수들이 상속받을 여러 가지 옵션들을 넣어줌

    def set_contract_period(self, contract_period):
        self.player_contract_period = contract_period
    #선수가 이적을 하거나 재계약을 할 때 필요한 함수이다. 

    def set_lent_period(self, lent_period):
        self.player_lent_period = lent_period
    #선수가 임대 될 때 발동되는 함수이다.

    def set_team(self, team):
        self.player_team = team
    #선수의 팀에 관한 함수이다.

class Team:
    pass

#1. 선수 검색
def search_player(ultimate_player_list):#선수를 검색하는 함수이다. (이름, 포지션, 나이 등으로 검색 ok) 
    #########숙제 검색 방법을 선택하세요 1. 이름, 2. 포지션##########
    #검색 방법 함수화 search_by_name, search_by_position
    print("1: 이름으로 검색 ㅣ 2: 나이로 검색 ㅣ 3: 포지션으로 검색")
    x = sys.stdin.readline().rstrip('\n')
    if x in ["1", "2", "3"]:
        x = int(x)
        if x == 1:
            #1. 이름으로 검색하기
            print("이름 입력")
            search_name = sys.stdin.readline().lower().rstrip('\n')
            #search name은 입력받은 이름을 넣어준 변수

            found_count = 0
            for i in range(0, len(ultimate_player_list)):        #선수를 검색하는 함수
                #pname이라는 변수에 플레이어리스트의 i번째 선수이름을 작은 글자 값을 넣어줬다.
                pname = ultimate_player_list[i].player_name.lower()      #파이썬이 엔터값과 띄어스기를 인식하지 않게 해주기 위해서            
                if search_name == pname:                       #lower()을 넣어주었다
                    print("Name: %s | Age: %s | Position: %s" % (ultimate_player_list[i].player_name, ultimate_player_list[i].player_age, ultimate_player_list[i].player_position))
                    found_count = found_count + 1

            if found_count == 0:
                print("해당 이름을 가진 선수가 없거나 잘못 입력하셨습니다.")
            print()

        elif x == 2:
            #2. 나이로 검색하기
            print("나이 입력")
            #*******에러 방지하기**********
            search_age = int(sys.stdin.readline())
            #search_age 는 사용자로부터 입력받은 나이값을 저장하고 있는 변수
            
            for i in range(0, len(ultimate_player_list)):
                #i는 현재 리스트의 i번째 선수
                page = int(ultimate_player_list[i].player_age)
                #page는 i번째 선수의 나이
                if(search_age == page):
                    print("Name: %s | Age: %s | Position: %s" % (ultimate_player_list[i].player_name, ultimate_player_list[i].player_age, ultimate_player_list[i].player_position))
                    
            print("")

        elif x == 3:
            #3. 포지션으로 검색하기
            print("포지션 입력")
            #*******에러 방지하기**********
            search_position = sys.stdin.readline().lower().rstrip('\n')

            for i in range(0, len(ultimate_player_list)):
                pposition = ultimate_player_list[i].player_position.lower()
                if search_position == pposition:
                    print("Name: %s | Age: %s | Position: %s" % (ultimate_player_list[i].player_name, ultimate_player_list[i].player_age, ultimate_player_list[i].player_position))
            print("")        
    else:
        print("잘못 입력하셨습니다.")
        print()
        return

#2. 선수 계약 
def player_contract(ultimate_player_list, my_list): #pi는 플레이어 인덱스
    #선수 목록에서 한명을 선택하고 계약
    #먼저 선수 선택을 해야함

    #계약하고 그 데이터를 선수에게 입력
    #Messi 계약 -> 
    print("계약할 선수의 이름을 입력해 주세요.")

    #######숙제 계약할 선수가 이미 나와 계약중이면 "이미 계약한 선수 입니다"라고 출력후 continue########

    contract_player = sys.stdin.readline().lower().rstrip('\n')
    
    #*******에러 방지하기**********

    cont_index = 0
    not_found = 0
    for i in range(0, len(ultimate_player_list)):
        pname = ultimate_player_list[i].player_name.lower()
        if(contract_player == pname):
            #player_contract(ultimate_player_list, i, my_player_list)
            cont_index = i
            print("")
            break
        not_found = not_found + 1
    
    if not_found == len(ultimate_player_list):
        print("해당 이름을 가진 선수가 없습니다.")
        print("")
        return
    else:
        #계약 할 것인가 물어보기 1은 yes 0은 no     #선수를 한 명 검색하여 선택하고 그 선수와 계약을 하게 하는 함수 
        print("계약하시겠습니까?")                  #우선 계약을 할 건지 묻고
        print("yes: 1 | no: 0")                    #계약 기간을 입력받는다(계약 기간이 1달 미만이면 함수 종료)

        #*******에러 방지하기**********
        y = sys.stdin.readline().rstrip('\n')            #계약할 선수를 입력받아 그 선수를 찾아 계약한다
        if y in ["1", "0"]:
            y = int(y)
        else:
            print("잘못 입력하셨습니다")
            print()
                
        if y == 1:
            print("계약 기간을 입력해 주세요.")
            #contract_p는 사용자로부터 계약 기간을 입력받는 변수
            #player_contract_period는 선수의 계약기간을 저장하는 변수
            #set_contract_period는 선수의 계약기간을 설정하는 함수
            #contract_period는 set_contract_period 함수를 사용할 때 내부적으로 사용하는 매개변수 이름

            #*******에러 방지하기**********

            contract_p = sys.stdin.readline().rstrip('\n')
            if contract_p.isdigit():
                contract_p = int(contract_p)
                if contract_p < 1:
                    print("잘못 입력하셨습니다")
                    print()
                    return -1
            else:
                print("잘못 입력하셨습니다")
                print()
                return -1

            print("계약 기간은 %s달입니다." %contract_p)
            print()
            ultimate_player_list[cont_index].set_contract_period(contract_p)
            my_list.append(ultimate_player_list[cont_index])
            return
            #return contract_p
        elif y == 0:
            print("계약을 포기하셨습니다.")
            print()
            return

#3. 선수 임대 
def player_lent(my_player_list):                       #선수 임대 함수
    if len(my_player_list) < 1:
        print("임대할 선수가 없어요.")
        print("")
        return

    print("임대할 선수의 이름을 입력해 주세요.")

    #*******에러 방지하기**********

    #사용자로부터 임대할 선수의 이름을 저장하고 있는 변수
    lent_player = sys.stdin.readline().lower().rstrip('\n')
        
    #루프를 돌려서 임대할 선수의 이름과 같은 선수를 my_player_list에서 찾고 i 값을 찾는 것
    lent_index = -1
    not_found = 0

    for i in range(0, len(my_player_list)):
        lpname = my_player_list[i].player_name.lower()

        if (lent_player == lpname):            
            lent_index = i
            print("")
            break
        not_found = not_found + 1
        
    if not_found == len(my_player_list):
        print("당신한테는 그런 선수 없습니다.")
        print("")
        return

    #선수가 이미 임대중인 경우
    if my_player_list[lent_index].player_lent_period > 0:
        print("선수가 이미 임대 중입니다.")
        return
    #임대중이 아니면 lent하기
    elif my_player_list[lent_index].player_lent_period <= 0:
        #임대 할 것인가 물어보기 1은 yes 0은 no      #임대 여부를 묻는다
        print("임대하시겠습니까?")                   #임대를 하겠다고 하면 임대 기간을 입력 받고
        print("yes: 1 | no: 0")                     #임대 기간이 계약 기간보다 크면 함수 종료

        #*******에러 방지하기**********

        x = int(sys.stdin.readline())               
        if x == 1:
            print("임대 기간을 입력해 주세요")       

        #*******에러 방지하기**********

            lent_p = int(sys.stdin.readline())        
            cont_p = my_player_list[lent_index].player_contract_period
            
            if lent_p > cont_p:
                print("임대 기간은 계약 기간보다 작거나 같아야 합니다.")
                print()
                return -1
                
            print("임대 기간은 %s달입니다." %lent_p)
            my_player_list[lent_index].set_lent_period(lent_p)
            return

        elif x == 0:
            print("임대하지 않으셨습니다.")
            print()
            return -1
        
#4. 전체 선수 목록에 선수 추가                      
def add_player(player_list):                        #전체 선수 목록에 선수를 추가하는 함수
    print("선수를 추가하시겠습니까?")                #선수 초기화할 때 넣어줘야 하는 조건들(이름, 나이 포지션)입력
    print("yes: 1 | no: 0")                         #리스트에 그 선수를 추가
    
    #*******에러 방지하기**********

    i = int(sys.stdin.readline())
    if i == 1:
        print("추가하실 선수 이름을 입력해주세요.")
        name = sys.stdin.readline().rstrip('\n')
        print("추가하실 선수 나이를 입력해주세요.")

        #*******에러 방지하기**********

        age = int(sys.stdin.readline())
        print("추가하실 선수 포지션을 입력해주세요")
        position = sys.stdin.readline().rstrip('\n')
        new_player = Player(name, age, position)
        player_list.append(new_player)
        print("선수가 추가되었습니다.")
        print("")
    elif i == 0:
        print("선수를 추가하지 않았습니다.")
        print("")
        return -1

#5. 전체 선수 목록에서 선수 삭제
def remove_player(player_list):                     #전체 선수 목록에 있던 선수를 삭제하는 함수
    print("선수를 삭제하시겠습니까?")                 #초기화할 선수 이름 입력
    print("yes: 1 ㅣ no: 0")                        #선수 검색 

    #*******에러 방지하기**********

    j = int(sys.stdin.readline())                   #리스트에서 그 선수를 삭제
    if j == 1:                                      
        print("삭제하실 선수 이름을 입력해주세요.")
        
        #*******에러 방지하기**********

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
            print("해당 이름을 가진 선수가 없습니다.")  #만약 선수가 전체 선수 목록에 없다면 선수가 없다고 출력
            print("")

    elif j == 0:
        print("선수를 삭제하지 않았습니다.")            
        print("")
        return -1

#6. 선수 목록 보기
def show_all_players(player_list):          #선수 목록에 있는 선수들의 이름, 나이, 포지션을 출력 
    print("선수 목록을 출력합니다.")
    #print("Name     | Age       | Position  ")
    for i in player_list:
        print("Name: %s | Age: %s | Position: %s" % (i.player_name, i.player_age, i.player_position))
    print("")

#7. 내 선수 목록
def show_my_players(player_list):           #내가 위에 있는 계약 함수를 통해 계약한 선수들을 출력함
    if len(my_player_list) < 1:
        print("선수 목록 없음.")
        print("")
        return
    print("선수 목록을 출력합니다.")
    #######숙제 계약기간, 임대기간 출력할것 임대기간이 0이라면 "팀에서 뛰는 중"으로 출력##########
    for i in player_list:
        print("Name: %s | Age: %s | Position: %s | Contract: %s | Lent: %s " % (i.player_name, i.player_age, i.player_position, i.player_contract_period, i.player_lent_period))
    print("")

#8. 턴 종료 (1달이 지나게 함)
#내 선수들의 계약기간과 임대기간이 이 함수를 실행할때마다 -1이 되어야함
def time_pass(up_list, my_player_list):
    #for문을 돌려서 각각 선수마다 계약기간과 임대기간(있으면 없으면 x) -1해줘야함
    #my_player_list[i].set_contract_period(my_player_list[i].player_contract_period - 1)
    
    #print(" %s 선수의 계약 기간이 %s 달 남았습니다." % (이름, 계약기간))
    #임대 기간이 있으면 임대기간도 얼마나 남았는지 출력

    #임대중인 경우 0보다 큼 임대중이 아닌경우 0보다 작음
    for x in range(0, len(my_player_list)):
        tplayer = my_player_list[x]
        #계약기간과 임대기간 둘다 남은 경우
        if tplayer.player_lent_period > 0 and tplayer.player_contract_period > 0:
            tplayer.set_lent_period(tplayer.player_lent_period - 1)
            tplayer.set_contract_period(tplayer.player_contract_period - 1)
        elif tplayer.player_lent_period <= 0 and tplayer.player_contract_period > 0:
            tplayer.set_contract_period(tplayer.player_contract_period - 1)

        print("Name: %s | Age: %s | Position: %s | Contract: %s | Lent: %s " % (tplayer.player_name, tplayer.player_age, tplayer.player_position, tplayer.player_contract_period, tplayer.player_lent_period))

        if (tplayer.player_lent_period == 0) and (tplayer.player_contract_period > 0):
            print("선수 임대가 종료되었습니다.") #다시 임대하시겠습니까?는 필요 없음 메뉴에서 임대하라고 하면 됨
            tplayer.set_lent_period(tplayer.player_lent_period - 1)

        elif (tplayer.player_lent_period <= 0) and (tplayer.player_contract_period == 0):
            print("계약이 종료되었습니다.")
            print("")
            del my_player_list[x]
            x = x - 1
    print()

######################################################################

#기본 데이터값
#기본 선수들을 객체로 만들었다
while 1:
    player1 = Player("Messi", 33, "RW")
    player2 = Player("Ronaldo", 30, "GK")
    player3 = Player("Bouk", 15, "CM")
    player4 = Player("Zidane", 47, "CAM")
    player5 = Player("Ronaodinho", 39, "LW")
    player6 = Player("Xavi", 40, "CM")
    player7 = Player("Henry", 42, "ST")
    player8 = Player("Iniesta", 35, "CM")
    player9 = Player("Kaka", 37, "CAM")
    player10 = Player("Cannavaro", 46, "CB")
    player11 = Player("Busquets", 32, "CDM")
    player12 = Player("Varane", 27, "CB")
    player13 = Player("Alba", 29, "LB")
    player14 = Player("neymar", 28, "LW")
    player15 = Player("SUPER SON", 28, "CF")
    player16 = Player("Werner", 21, "ST")
    player17 = Player("Van dijk", 29, "CB")
    player18 = Player("De Bruyne", 28, "CAM")
    player19 = Player("Aguero", 33, "ST")
    player20 = Player("Salah", 29, "LW")
    player21 = Player("Kane", 29, "ST")
    player22 = Player("Casemiro", 28, "CDM")
    player23 = Player("Varane", 29, "MF")
    player24 = Player("Alba", 30, "LB")
    player25 = Player("Anhold", 23, "RWB")
    player26 = Player("Kante", 27, "CDM")
    player27 = Player("Anhold", 21, "RB")
    break

#전체 선수 목록
ultimate_player_list = [
    player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, 
    player11, player12, player13, player14, player15, player16, player17, player18, player19, player20, 
    player21, player22, player23, player24, player25, player26, player27
    ]

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
    print("8. 턴 종료")
    print("0. 프로그램 종료")

    select_menu = sys.stdin.readline().rstrip('\n')
    if select_menu in ["1", "2", "3", "4", "5", "6", "7", "8", "0"]:
        select_menu = int(select_menu)
        if select_menu == 1:
            #선수검색
            search_player(ultimate_player_list)

        elif select_menu == 2:
            player_contract(ultimate_player_list, my_player_list)
            
        elif select_menu == 3:
            player_lent(my_player_list)
            
        elif select_menu == 4:
            add_player(player_list)
    
        elif select_menu == 5:
            #전체 선수 목록에서 선수 삭제
            remove_player(player_list)
        
        elif select_menu == 6:
            show_all_players(ultimate_player_list)
        
        elif select_menu == 7:
            show_my_players(my_player_list)

        elif select_menu == 8:
            time_pass(ultimate_player_list, my_player_list)
        
        elif select_menu == 0:
            break
    
    else:
        print("잘못 입력하셨습니다.(입력은 숫자 0-8까지)")
        print()
    