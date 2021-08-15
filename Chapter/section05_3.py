# Section05-3
# 파이썬 흐름제어(제어문)
# 반복문 실습


# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

# 비열은 반복적인 작업이 가능하다
for name in names:
    print("You are", name)

# 예제2
word = 'dreams'

for s in word:
    print('word : ', s)

# 예제3
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

# 기본값은 키가 호출되기 때문에 값을 얻으려면 키값 변수를 넣어줘야함
for key in my_info:
    print("myinfo : ", key)

print()

for key in my_info.values():
    print("myinfo : ", key)

print()

for key in my_info.keys():
    print("myinfo : ", key)

print()

for key in my_info.items():
    print("myinfo : ", key)

# 예제5
name = 'KennRY'

# 문자열도 iterable
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# 각종 자료구조 변환

name = "FFolabear"
print(list(reversed(name)))
print(tuple(reversed(name)))
