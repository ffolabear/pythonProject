# Section02-1
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# 파이썬에 대한 철학
# import this
from os import PRIO_PGRP
import sys

# 파이썬 기본 인코딩
# 입력과 출력 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)


# 출력문
print("My name is FF")

# 변수 선언
# 변수에 값을 할당
# myname = 'FF'
myname = 'FFF'

# 조건문
if myname == 'FF':
    print('OK')
else:
    print('Wrong')

#  반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)
    print()

# 한글 변수선언
이름 = '좋은사람'
print(이름)

# 함수선언

def 인사():
    print("안녕")

인사()

def greeting():
    print("Hello Python")

greeting()


# 클래스
class Cookie:
    pass

# 객체 생성
Cookie = Cookie()

print(id(Cookie))
print(dir(Cookie))

