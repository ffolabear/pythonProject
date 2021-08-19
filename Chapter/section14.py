# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들

# python object Referrence

print('EX-1')
print(dir())
print(__name__)
print()

# id vs __eq__ (==) 증명
x = {'name': 'Kim', 'age': 33, 'city': 'seoul'}
y = x

print('EX2-1 - ', id(x), id(y))

# 값이 같은가?
print('EX2-2 - ', x == y)
# id 값이 같은가?
print('EX2-3 - ', x is y)

print('EX2-4 - ', x, y)

print()
print()

# 그럼 x의 값을 변경하면 x를 참조하는 y는?
x['class'] = 10
# y가 x를 참조하기 때문에 같은 값을 출력
print('EX2-4 - ', x, y)

print()
print()

# x와 같은 값을 가진 객체를 만들었을떄 관계
z = {'name': 'Kim', 'age': 33, 'city': 'seoul', 'class': 10}

# 같은 값을 가지는것 확인
print('EX2-6 - ', x, z)
# 값은 같지만 다른 주소를 가짐
print('EX2-7 - ', x is z)
print('EX2-7 - ', x is not z)
# 값은 같지만 주소가 다름
print('EX2-7 - ', x == z)

# 객체 생성후 완전 불변 -> 즉, id는 객체 주소(정체성)를 비교
#   == (__eq__)  는 값비교 (하지만 is 가 더 빠름)
# 데이터가 많을떄는 is 로 먼저 비교하는 것이 효율적

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

# 튜플또한 동일
# 생각해보면 튜플은 불변객체이기 때문에 다른것이 당연
print('EX3-1 - ', id(tuple1), id(tuple2))
print('EX3-2 - ', tuple1 is tuple2)
# 하지만 값은 같으므로 True 출력
print('EX3-3 - ', tuple1 == tuple2)
print('EX3-2 - ', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy


# Shallow Copy

tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

# 당연히 둘은 같은 주소를 참조하므로 값은 동일
print('EX4-1 - ', tl1 == tl2)
# 주소도 마찬가지
print('EX4-2 - ', tl1 is tl2)
# 형변환을 해주면 새로운 객체를 만들어서 사용. 안전한 복사
print('EX4-3 - ', tl1 is tl3)
# 하지만 여전히 값은 같음
print('EX4-4 - ', tl1 == tl3)

print()
print()

# 증명
tl1.append(1000)
tl1[1].remove(105)
# tl1 = [10, [100], (5, 10, 15), 10000]

# 같은 주소 = 같은 값
print('EX4-4 -5 ', tl1)
print('EX4-4 -6 ', tl2)
# 형변환을 통해서 얻은 새로운 객체
print('EX4-4 -7 ', tl3)

print()
print()

# 튜플은 불변 -> 튜플을 수정하게되면 새로운 객체를 생성한다
# 값의 참조와 불러오는 부분에서 오류발생할 수 있음
print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)
print(id(tl1[2]))
# tl1 = [10, [100, 110, 120], (5, 10, 15, 110, 120), 1000]

print('EX4-4 -8 ', tl1)
print('EX4-4 -9 ', tl2)
print('EX4-4 -10 ', tl3)

print()
print()


#  Deep Copy

class Basket:
    def __init__(self, product=None):
        if product is None:
            self._products = []
        else:
            self._products = list(product)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

# 복사의 방법과 관련없이 셋다 다른 id를 가짐
print('EX5-1 - ', id(basket1), id(basket2), id(basket3))
# 하지만 shallow copy로 복사한 객체는 안에 있는 상품들의 주소는 같음
print('EX5-2 - ', id(basket1._products), id(basket2._products), id(basket3._products))

print()
print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

# 얕은 복사를 한 객체의 상품은 동일
print('EX5-3 - ', basket1._products)
print('EX5-4 - ', basket2._products)
print('EX5-5 - ', basket3._products)

print()
print()


# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    return x


x = 10
y = 5

# 일반적인 정수형은 변하지 않는다
print('EX6-1 - ', mul(x, y))
print('EX6-1 - x : ', x, ' y : ', y)
print()

# 가변형일 경우 a 는 데이터가 변경 -> 원본의 주소를 넘김!!!!!!
# 데이터가 많을때 일일히 객체를 복사하는 것은 비효율적이므로

a = [10, 100]
b = [5, 10]
print('EX6-2 - ', mul(a, b))
print('EX6-2 - a : ', a, ' b : ', b)

print()

c = (10, 100)
d = (5, 10)
print('EX6-3 - ', mul(c, d))
print('EX6-3 - c : ', c, ' d : ', d)

# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본생성 X -> 참조 변환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
# 슬라이싱을 통한 복사
tt3 = tt1[:]

print()
print()

# 어차피 불변형이면 바뀔일이 없으므로 값이 같으면 같은 주소를 가진다
print('EX7-1 - ', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 - ', tt3 is tt1, id(tt3), id(tt1))

print()
print()

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

# 같은 값이므로 True 출력, 불변객체 이므로 같은 주소
print('EX7-3 - ', tt4 is tt5, id(tt4), id(tt5))
print('EX7-4 - ', ss1 is ss1, id(ss1), id(ss2))
