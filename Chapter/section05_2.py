# Section05-2
# 파이썬 흐름제어(제어문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 사용(while, for)

v1 = 1
while v1 < 11:
    print("v1이 11보다 작음")
    v1 += 1

# for문이 좀더 유연
# v2 라는 변수에 range함수의 값을 할당 (0 부터 4)
for v2 in range(5):
    print("v2 is : ", v2)

# 1부터 4까지
for v3 in range(1, 5):
    print("v3 is : ", v3)

print()
print()

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 합 : ', sum1)
# sum : 리스트를 입력받아서 그 안의 합을 더해줌
print('1 ~ 100 합 : ', sum(range(1, 101)))
# 1부터 100까지 중 3개 단위로 건너뜀
print('1 ~ 100 안에 3의 배수의 합 : ', sum(range(1, 101, 2)))


print()
print()


# break
# 조건에 맞을때 반복문을 중지시킬때 사용 -> 효율성을 증가

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
cnt = 1

for i in numbers:
    if i == 33:
        print("찾았다")
        break
    else:
        print("찾지못했음 ", i, " 탐색한 갯수 : ", cnt)
        cnt += 1

print()
print()


# 파이썬에는 for - else 구문이 있음
# 반복문이 정상 종료됐을때 실행

for i in numbers:
    if i == 999:
        print("찾았다")
        break
    else:
        print("찾지못했음 ", i)
else:
    print("찾는 숫자가 존재하지 않음")


print()
print()


# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

# 리스트 안에 있는 실수형을 찾고싶을때
for v in lt:
    if type(v) is float:
        continue
    print(" 실수가 아는 값들의 타입: ", type(v))