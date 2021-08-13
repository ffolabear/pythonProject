# Section04-1.py
# 데이터 타입
# Section04-1.py
# 데이터 타입


# 변수에 값 할당하기
str1 = "Nice"
bool1 = False
str2 = "Good"
float1 = 10.3
int1 = 7

# 딕셔너리 : key - value
dic1 = {
    "name" : "Kim",
    "age" : 25,
}

list1 = [3, 5 , 7]
tuple1 = 3, 5, 7
set1 = {7, 8, 9}


print(type(str1))
print(type(bool1))
print(type(float1))
print(type(int1))
print(type(dic1))
print(type(list1))
print(type(tuple1))
print(type(set1))


i1 = 39
i2 = 967

# 자바와 다르게 큰 숫자도 사용할 수 있음
i3 = 99999999999999999999999999999999
i4 = 77777777777777777777777777777777

f1 = 1.234
f2 = 3.784
f3 = .5     # 0.5
f4 = 10.    # 10.0

print(i1 * i2)
print(i3 * i4)
print(f1 ** f2)    # f1의 f2 승

# 정수 + 실수 형변환
result = i1 + f3
print(result, type(result))

print()
print()

# 형변환
a = 5.
b = 4

print(type(a), type(b))

result2 = a + b
print(type(result2))
print(type(int(result2)))
print(float(i2))
print(complex(i2))

# True 는 1 False 는 0
print(int(True))
print(int(False))
print(complex(False))

y = 100
y += 100
print(y)


# 수치 연산 함수
print(abs(-7))

# 100을 8로 나워서 몫은 n에 나머지는 m에
n, m = divmod(100, 8)

print(n)
print(m)

import math

print(math.ceil(5.1))           # 올림
print(math.floor(3.45454))      # 버림

