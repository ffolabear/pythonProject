# Section05-1
# 파이썬 흐름제어(조건문)
# 조건문 실습


# 조건문은 True 와 False가 중요

# 기본 형식

# 예1
if True:
    print("Yes")  # 들여쓰기 중요

# True일때만 실행되므로 실행되지 않음
if False:
    # 출력되지 않음.
    print("No")

# 예2
if False:
    # 여기는 실행되지 않음.
    print("You can't reach here")
else:
    # if문이 실행되지 않을때 실행되는 곳
    print("Oh, you are here")

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

# == 양 변이 같을 때 참.
print(a == b)

# != 양 변이 다를 때 참.
print(a != b)

# > 왼쪽이 클때 참.
print(a > b)

# >= 왼쪽이 크거나 같을 때 참.
print(a >= b)

# < 오른쪽이 클 때 참.
print(a < b)

# <= 오른쪽이 크거나 같을 때 참.
print(a <= b)

# 참 거짓 종류
# 참 : "내용", [값이 있는 리스트], (값이 있는 튜플), {값이 있는 닥셔너리}, 1
# 거짓 : "", [빈 리스트], (빈 튜플), {빈 딕셔너리}, 0, None

print()
print()

city = ""

if city:
    print("True 비어있지 않음:", city)
else:
    # 이쪽이 출력된다.
    print("False 비어있음")

city = "seoul"

if city:
    # 값이 있으므로 참
    print("True 비어있지 않음:", city)
else:
    print("False 비어있음")

print()
print()

# 논리연산자
# and, or, not

a = 1
b = 2
c = 3

# a가 b보가 크고 동시에 b가 c보다 크면 참
print('and : ', a > b and b > c)

# a가 b보가 크거나  b가 c보다 크면 참
print('or : ', a > b or b > c)

# a가 b보다 크지 않으면 참
print('not : ', not a > b)

# b가 c보다 크지 않으면 참
print('not : ', not b > c)

print()
print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용


print('ex1 : ', 3 + 12 > 7 + 3)
print('ex2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('ex3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('ex4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

# 다중 조건문
num = 90

if num >= 70:
    print("70 이상. 점수 : ", num)
elif num >= 60:
    print("60 이상. 점수 : ", num)
else:
    print("꽝")

# 중첩 조건문

age = 27
height = 175

# 20세 이상일때만 탐색
if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원가능")
