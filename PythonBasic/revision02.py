# 파이썬 기본 정리
# part 2

# 들은 강의 링크
# https://www.youtube.com/watch?v=kWiCuklohdY
# 이미 잘 아는 내용은 건너뛰고 다시 정리하고싶은 내용, 퀴즈만 기록
import random

city = ["seoul", "Tokyo", "London"]
print(city.index("Tokyo"))
city.append("Boston")
print(city)

# 원하는 위치에 삽입
city.insert(1, "Paris")
print(city)

# 뒤에서 하나씩 원소 제거
print(city.pop())
print(city)

# 원하는 원소 갯수세기
city.append("Paris")
print(city.count("Paris"))

num = [1, 4, 42, 21, 5, 99]
print(num)

# 배열 정렬하기
num.sort()
print(num)

# 배열 뒤집기
num.reverse()
print(num)

# 모두 지우기
# num.clear()
# print(num)

# 배열 확장
city.extend(num)
print(city)

print('---------------------------------------------------------------------------------------------------------------')
# 딕셔너리

cabinet = {3: "AAA", 4: "BBB"}
print(cabinet[3])
print(cabinet[4])
print(cabinet.get(3))

# 키값을 잘못 입력시 에러발생
# print(cabinet[6])
print(cabinet.get(6))

# 딕셔너리안의 값 있는지 여부 확인
print(3 in cabinet)
print(99 in cabinet)

# 값의 추가
cabinet[77] = "CCC"
print(cabinet)

# 기존에 있는 키를 입력시 덮어씀
cabinet[3] = "XXX"
print(cabinet)

# 값의 삭제
del cabinet[77]
print(cabinet)

# 키의 목록만 출력
print(cabinet.keys())
# 밸류만 출력
print(cabinet.values())
# 키-밸류 쌍으로 출력
print(cabinet.items())

# 데이터 삭제
cabinet.clear()
print(cabinet)

print('---------------------------------------------------------------------------------------------------------------')
# 튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name, age, food) = ("FF", 12, menu[0])
print(name, age, food)

print('---------------------------------------------------------------------------------------------------------------')
# 세트
# 중복 안됨, 순서 없음

my_set = {1, 2, 2, 3, 3, 3}

# 중복을 허용하지 않음
print(my_set)

backend = {"Python", "Java", "JS"}
frontend = {"JS", "HTML", "SCSS"}

# 교집합
print(backend & frontend)
print(backend.intersection(frontend))

# 합집합
print(backend | frontend)
print(backend.union(frontend))

# 차집합
print(backend - frontend)
print(backend.difference(frontend))

frontend.add("CSS")
print(frontend)
frontend.remove("SCSS")
print(frontend)

print('---------------------------------------------------------------------------------------------------------------')
# 자료구조의 변경

menu = {"Americano", "latte", "Frappuccino"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
#
# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --

import random


def event():

    student = list(i for i in range(1, 21))
    random.shuffle(student)

    chicken = student[0]

    coffee = student[0:3]
    print("커피 당첨자는 {} 입니다.".format(coffee))
    print("치킨 당첨자는 {} 입니다.".format(chicken))

event()

print('---------------------------------------------------------------------------------------------------------------')