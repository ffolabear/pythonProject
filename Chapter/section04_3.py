# Section04-3
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합, 자료형


# Dictionary
# 순서 x, 중복 x, 수정 o, 삭제 o
# Key - Value (Json) -> ex) MongoDB


# 선언
# Key 를 가져오면 매핑된 데이터를 얻을 수 있음
# Key 는 중복되지 않지만 Value 는 중복될수 있음

a = {
    'name' : 'Kim',
    'phone' : '010-0000-0000',
    'birth' : 900000
        }

# 숫자를 Key에 할당할 수 있지만 비추천
b = {
    0: 'Hello Python',
    1: 'Hello Java'
}

c = {
  'arr' : [1, 2, 3, 4, 5]
}


print()
print()

# 출력
# 이런식으로 값을 얻을 수도 있지만 올바르지 않은 Key값을 가져올 수 있으므로 비추천
print(a['name'])

# 추천하는 방법
# 에러를 발생하지 않고 None을 리턴
print(a.get('name23'))

# 리스트를 반환 - 1번인덱스부터 2번 인덱스까지 출력
print(c['arr'][1:3])

# 딕셔너리 추가
# 순서가 없는 자료형이므로 순서는 다르게 출력될 수 있음
a['address'] = 'seoul'
print(a)

# 튜플과 리스트를 추가
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3, )
print(a)


# Keys, Values, Items
# Item ? -> Key와 그에 해당하는 Value  한 쌍을 뜻함

# Key만 가져오기
# dict_keys 란 이름으로 Key들의 리스트를 원소로 가지고 있는 튜플을 반환
print(a.keys())
print(type(a.keys()))

# 하지만 인덱싱이 불가능 하기 때문에 list로 형변환해줘야 가능함
temp1 = list(a.keys())
print(temp1[1:3])

print()
print()

# 그렇다면 Value 는?
print(a.values())

temp2 = list(a.values())
print(temp2[1:3])

print()
print()


# Item 도 동일함
print(a.items())


# 원하는 키또는 값이 있는지 찾기
print('country' in a)
print('name' in a)
print(234 in b)


print()
print()

# 집합 Sets
# 순서 x, 중복 x

# 선언
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6,3])

print(type(a))

# 중복을 혀용하지 않기 때문에 알아서 삭제됨
print(c)

# 형변환 후 슬라이싱이 가능
t = tuple(b)
print(t[1:3])

l = list(b)
print(l[1:3])

print()
print()

# Set 관련 함수

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7 ,8 ,9])\

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

print()
print()

# 합집합 - 중복되는 원소는 한번만 나옴
print(s1.union(s2))
print(s1 | s2)

print()
print()

# 차집합
print(s1.difference(s2))
print(s1 - s2)

print()
print()

# 추가
s3 =  set([7, 8, 10, 15])
s3.add(50)
# 중복되는 값을 추가해도 변함없음
s3.add(7)
print(s3)

# 제거
s3.remove(15)
print(s3)
print(type(s3))








