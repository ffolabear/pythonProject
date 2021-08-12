# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
# 문자열을 출력할때 ' " 둘다 사용할 수 있음
print("큰따옴표 : ", "Hello Python!")
print("작은 따옴표 : ", 'Hello Python!')
print("큰 따옴표 3개 : ", """Hello Python!""")
print("작은 따옴표 3개 : ", '''Hello Python!''')
print()

# Seperator 옵션 사용


print('T', 'E', 'S', 'T' ,sep='')
print('2021','08', '19', sep='-')
print('ffdev','google.com', sep='@')
print()

# End 옵션 사용
print('Welcome To' , end=' ')
print('the black paradise' , end=' ')
print('piano Notes')
print()

# 잘까먹는 내용
# Format

# 중괄호 and 중괄호 .format을 통해서 매핑시켜줌
print('{} and {}'.format('You','Me'))
print('{0} and {1} and {2}'.format('You','Me','We'))
print('{2} and {0} and {1}'.format('You','Me','We'))

print('{a} and {b}'.format(a="Me", b="You"))

# 까먹지 말자
# %s : 문자
# %d : 정수
# %f : 실수

print("%s's favorite number is %d" % ('FF', 456))

# 5자리의 정수가 올것이라고 지정
# 4자리의 정수부분과 2자리의 실수부분을 가진 실수가 올것
print("Test1 : %5d, Price: %4.2f" % (776, 6544.1411))
print("Test1 : {0: 5d}, Price : {1: 4.2f}".format(776, 45635.123))
print("Test1 : {a: 5d}, Price : {b: 4.2f}".format(a= 776, b=23423.23))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
# 'you' 출력하기
print("1 : 'you'")
print("2 : \'you\'")
print('3 : "you"')
print("""4 : 'you'""")
print('5 : \\you\\')
print('6 : \\you\\\n')
print('7 : \\you\\\n\n\n\n')
print('8 : \t\t\t\t\t\tyou')
print("Test")