import sys

def output(my_list):
    print("몇 번째 선수를 출력할지 선택해 주세요")
    x = int(sys.stdin.readline())
    return my_list[x]
    #매개변수로 리스트를 넣어줘 그 리스트의 x번쨰 출력하기
