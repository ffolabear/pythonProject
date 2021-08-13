# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트 튜플

# List
# 순서o, 중복o, 수정o, 삭제o
# 여러개의 데이터를 담는 그릇


# 선언
a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'Pen', 'Orange', 'Banana']
e = [10, 100, ['Pen', 'Orange', 'Banana']]



# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
# 역순으로 나오는 첫번째 요소의 뒤에서 두번째 요소
print(e[-1][-2])


# 슬라이싱
print(d[0:3])        # d의 0부터 2번 원소까지
print(e[2][1:3])     # e의 2번 원소의 1번부터 2번 원소까지

# 배열의 연산
# 배열과 배열을 더해서 하나의 배열로 만들수있음

print(c + d)
print(c * 3)
print(str(c[0]) + ' hihiyoyo')

print()
print()

# 리스트의 수정 삭제
c[0] = 77
print(c)

# 1번 원소를 대체
c[1:2] = [100, 1000, 100000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[0]
print(c)

del c[-1]
print(c)

print()
print()


# 리스트 함수
y = [5 , 2, 3, 1, 4]

# 배열의 끝부분에 삽입
y.append(6)
print(y)

# 배열의 정렬
y.sort()
print(y)

# 역순
y.reverse()
print(y)

# 원하는 위치에 삽입
# 2번 인덱스에 7을 삽입
y.insert(2,7)
print(y)

# 값의 삭제
# 2번 인덱스를 지우는 것이 아니라 2의 값을 가진 인덱스의 값을 삭제
y.remove(2)
print(y)

# 마지막에 있는 원소 꺼내기
print(y.pop())
print(y)

# 연장
ex = [77 ,88]
y.extend(ex)
print(y)

# append 와 비교
y.append(ex)
print(y)

# append에는 배열 자체가 인덱스에 들어가지만
# extend는 안에 있는 원소가 추가로 인덱스에 들어간다.
# 삭제는 del, remove, pop 으로 가능


print()
print()



# 튜플
# 순서 o, 중복 o, 수정 x, 삭제 x
# 변경되면 안되는 데이터에 사용

aa = ()
bb = (1, )
cc = (1, 2, 3, 4)
ee = (10, 100, ('a', 'b', 'c'))

# 삭제할 수 없기 때문에 해당 코드는 에러발생
# del c(2)


# 인덱싱
# 튜플의 데이터를 불러올때는 list와 형태는 같다
print(cc[3])
print(cc[2])
print(ee[2][1])


# 슬라이싱
print(ee[2:])
# 2번 인덱스에서 0번째 인덱스부터 1번째 인덱스까지 출력
print(ee[2][0:2])


# 튜플의 연산
print(cc + ee)
print(cc * 2)


# 튜플의 함수
z = (5, 2 ,1, 3, 4, 3)
print(z)

# 3이 z 안에 있느가?
print(3 in z)

# 1이 있는 인덱스를 반환
print(z.index(1))

# 1의 값을 가진 인덱스가 몇개가 있는가?
print(z.count(3))