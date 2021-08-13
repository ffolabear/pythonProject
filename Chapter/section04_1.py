# Section04
# 파이썬 데이터 타입(자료형)
# 문자열, 문자열 연산, 슬라이싱
# 문자열 중요성(가장 많은 분야에서 사용)

str1 = 'I am a boy'
str2 = "Nice"
str3 = ''
str4 = str()
str5 = str('ace')

print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))
print(len(str5))

# 이스케이프문자 문자열에 넣어보기
es1 = "Do you have a \"car\""
print(es1)

es2 = "Tab\tTab\tTab\t"
print(es2)

# Raw String - 경로를 표시할떄 많이 사용
raw1 = r'C:\Program\Test\Bin'
print(raw1)
raw2 = r"\\a\\a"
print(raw2)


# 멀티라인 출력
mul = \
""" 
문자열 
멀티라인 
테스트
"""

print(mul)


# 문자열 연산
sto1 = '*'
sto2 = 'abc'
sto3 = 'def'
sto4 = "NiceMan"

print(sto1 * 100)
print(sto1 + sto3)

# 문자열은 immutable 이므로 in 연산자를 사용할 수 있음
# sto2 에 'a' 문자가 있음?
print('a' in sto2)
print('z' in sto2)


print()
print()

# 문자열의 형변환

cast1 = str(77)
print(cast1 + 'a')
print(type(cast1))

print()
print()


# 문자열 함수

a = 'orange'
b = 'melon'

# a가 전부 소문자인가?
print(a.islower())

# a가 s로 끝나는가?
print(a.endswith('s'))

# 전부 대문자로 출력
print(a.capitalize())

# 특정 부분을 찾아서 교체
print(a.replace('o', '3'))

# reversed를 사용하려면 list로 형변환을 해줘야함
print(list(reversed(b)))

print()
print()

# 슬라이싱

c = 'elephant'
d = 'psychology'

# 0번쨰 부터 3번쨰 전까지! 출력
print(c[0:3])

# 0번 인덱스부터 시작하므로 마지막 element의 인덱스 번호는 길이 -1
# 그러므로 끝까지 출력하고 싶으면 len을 사용해도됨
print(c[0:len(c)])

# 처음부터 끝까지 출력
print(c[0:])

# 처음부터 4번째 인덱스 전까지
print(c[:4])

# 0부터 4번쨰 인덱스 전까지 출력하는데 한 원소를 건너뜀
print(d[0:4])
print(d[0:4:2])

# 1부터 시작해서 끝에서 두번째 원소 전까지
print(d[1:-2])

# 시작부터 끝까지 출력하는데 스킵은 역순으로
print(d[::-1])
print(d[::-2])