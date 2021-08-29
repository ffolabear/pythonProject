# 파이썬 기초
# oop 연습

# 연습1. width, height, color 속성을 가진 사각형 클래스를 만들고 객체 만들기
#  - 직사각형 : width=10, height=5, color='red'
#  - 정사각형 : width=7, height=7, color='blue'

class Quadrangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        return self.width * self.height


rectangle = Quadrangle(10, 5, 'red')
print(rectangle.width)
print(rectangle.height)
print(rectangle.color)
print(rectangle.get_area())

print()

square = Quadrangle(7, 7, 'blue')
print(square.width)
print(square.height)
print(square.color)
print(square.get_area())

# 연습2. 정삼각형 클래스만들기
# attribute : 한변의 길이, 삼각형 이름
# method : 정삼각형의 이름 출력
# 생성자에서 attribute 설정
# 소멸자 작성후 "Object is deleted." 출력

import math


class triangle:
    def __init__(self, leg, name):
        self.leg = leg
        self.name = name

    def getname(self):
        return self.name

    def __getarea(self):
        return math.sqrt(3) / 4 * math.pow(self.leg, 2)

    def __del__(self):
        print("Object is deleted.")


print()

tri1 = triangle(4, "trinity force")
# print(tri1.getarea())
print(tri1.getname())

print()


# 파이썬의 접근제한자

class access:
    def __init__(self):
        pass

    def _protected(self):
        return 'Protected'

    def __private(self):
        return 'Private'


# protected : 해당 속성앞에 '_' 로 표시
# 실제로 제약되지는 않고 경고 표시로 사용


# private : 해당 속성앞에 '__' 로 표시

acessTest = access()


print('1', acessTest._protected())

print()

# 호출할 수 없음
# print(acessTest.__private())
# _클래스명 + 변수 이름 으로 접근 가능
print('2', acessTest._access__private())
print(tri1._triangle__getarea)