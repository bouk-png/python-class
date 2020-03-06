test_file = open('C:\\Users\\Princeton C33\\Desktop\\python\\text.txt')
text = test_file.read()
print(text)
#test_file.close()

test_file2 = open('C:\\Users\\Princeton C33\\Desktop\\python\\text1.txt', 'w')
# test_file2.write('this is test file 2 ok')
test_file2.close()

'''
#숙제 9장 3번문제 test1 test2를 만들고

test1에는 내용을 적고
test2에는 아무것도 적지 않고

test1에서 읽어드린 값을
test2파일에 쓰고 종료하기

숙제 9장 2번문제는 인터넷에 검색해보기
"문자열을 단어로 나누기"
그리고 하나씩 출력하기
'''