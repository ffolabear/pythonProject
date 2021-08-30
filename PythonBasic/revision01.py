# 파이썬 기본 정리
# part 1

# 들은 강의 링크
# https://www.youtube.com/watch?v=kWiCuklohdY
# 이미 잘 아는 내용은 건너뛰고 다시 정리하고싶은 내용, 퀴즈만 기록

# Quiz)
# 변수명 : station
# 변수값 : 사당, 신도림, 인천공항 순으로 입력
# 출력문장 : OO행 열차가 들어오고 있습니다.
import math
from math import *

station = list()
station.append("사당")
station.append("신도림")
station.append("인천공항")

for i in station:
    print("{} 행 열차가 들어오고 있습니다.".format(i))

print('---------------------------------------------------------------------------------------------------------------')

# 수학 관련 함수
# 절댓값
print(abs(-5))

# ㅇ승
# 4를 2승
print(math.pow(4, 2))

# 둘중 최솟값
print(max(5, 12))
# 둘중 최댓값
print(min(5, 12))

# 반올림
print(round(3.14))  # 3
print(round(4.99))  # 5

# 내림
print(floor(4.99))  # 4
# 올림
print(ceil(3.14))  # 4
# 제곱근
print(sqrt(25))  # 5.0

print('---------------------------------------------------------------------------------------------------------------')

from random import *

# 0.0 ~ 1.0 미만의 난수 생성
print(random())
# 0.0 ~ 10.0 미만의 난수 생성
print(random() * 10)
# 정수부분만 보기
print(int(random() * 10))

# 1부터 보고싶어
print(int(random() * 10) + 1)

# 로또 숫자 뽑아보기
print(int(random() * 45) + 1)
# 1부터 46미만의 난수 생성
print(randrange(1, 46))

# 마지막 포함? 미포함? 햇갈린다
# 1부터 45 모두 포함
print(randint(1, 45))

print('---------------------------------------------------------------------------------------------------------------')

# Quiz) 당신은 최근에  코딩 스터디 모임을 새로 만들었습니다
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오
#
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함 (아무리 늦어도 28일 이내의 날짜로 선정)
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# 방법1
print("스터디 날짜 1 : ", int((random() * 28) + 1))
# 방법2
print("스터디 날짜 2 : ", randrange(1, 29))
# 방법3
print("스터디 날짜 3 : ", randint(1, 28))

print('---------------------------------------------------------------------------------------------------------------')

reginum = "991111-2020200"
print("성별 : ", reginum[7])
print("생년 : ", reginum[0:2])  # 마지막 인덱스는 포함하지 않음
print("생월 : ", reginum[2:4])  # 마지막 인덱스는 포함하지 않음
print("생일 : ", reginum[4:6])
print("생년월일 : ", reginum[0:6])
print("생년월일 : ", reginum[:6])  # 처음부터 6번째 직전까지
print("뒤 7자리 : ", reginum[7:14])
print("뒤 7자리 : ", reginum[7:])  # 7번쨰 부터 끝까지
print("뒤 7자리(뒤에서부터 계산) : ", reginum[-7:])  # 7번쨰 부터 끝까지

print()

str_func = "Python is Amazing"
# 소문자로
print(str_func.lower())
# 대문자로
print(str_func.upper())
# 문자가 대문자인지?
print(str_func[0].isupper())
# 문자의 길이
print(len(str_func))
# 특정 문자를 교체
print(str_func.replace("Python", "Java"))

index = str_func.index('n')
print(index)
# 두번째 'n'을 찾기 index+1 부터 탐색
index2 = str_func.index('n', index+1)
print(index2)

# 찾는 값이 없다면 -1을 리턴
print(str_func.find("Java"))
# 하지만 index로 찾으면 에러가 발생
# print(str_func.index("Java"))

# 특정 문자 갯수 세기
print(str_func.count('n'))

print('---------------------------------------------------------------------------------------------------------------')

# 문자열 합치기
print("a" + "b")
print("a", "b")

# 방법1
print("나는 %d 살입니다." % 20)
print("나는 %s 를 잘합니다." % "Java")
print("Apple은 %c 로 시작합니다." % 'A')
print("%s색 %s색" % ("파란", "노랑"))

print()

# 방법2
print("나는 {}살입니다.".format(20))
print("{}색 {}색".format("파란", "노랑"))
print("{0}색 {1}색".format("파란", "노랑"))
print("{1}색 {0}색".format("파란", "노랑"))

# 방법3
print("나는 {age}살, {color}색을 좋아합니다.".format(age=20, color="blue"))

# 방법4 (v 3.6이상)
age = 20
color = "green"
print(f"나는 {age}살, {color}색을 좋아합니다.")

print('---------------------------------------------------------------------------------------------------------------')

print("가나다라마바사\n아차자가카타파하")
print("가나다라마\"바사아차자\"가카타파하")
print("가나다라마\\바사아차자\\가카타파하")    # 역슬래시 하나일때는 오류 발생
print("Red Apple\rPine")
print("Red Apple\bPine")
print("Red Apple\tPine")


print('---------------------------------------------------------------------------------------------------------------')


# Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.
#
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!'로 구성
#                        (nav)                      (5)                   (1)             (!)
#
# 예) 생성된 비밀번호 : nav51!

site_address = "http://naver.com"
generated_pw = site_address[7:-4]
print(generated_pw[0:3] + str(len(generated_pw)) + str(generated_pw.count('e')) + '!')
print(generated_pw[0:3], len(generated_pw), generated_pw.count('e'), '!', sep='')


