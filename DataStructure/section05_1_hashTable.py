# 파이썬 자료구조
# 5. 헤쉬 테이블 기본구현

# 키(Key)에 데이터(Value)를 저장하는 데이터 구조
# Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
# 파이썬은 딕셔너리를 통해 해쉬테이블을 사용하면됨


# 주요 용어
# 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
# 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
# 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
# 해쉬 값(Hash Value), 해쉬 주소(Hash Address): Key 를 해싱 함수로 연산해서 알아낸 해쉬값을 사용해서 해쉬 테이블에서 찾은 해당 Key에 대한 데이터
# 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간

# 키 -> 해쉬함수 -> 해쉬값 -> 해쉬 주소 -> 해쉬 테이블 -> 키에 대한 값

# 장점
# 데이터 저장/읽기 속도가 빠르다. (검색 속도가 빠르다.)
# 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움

# 단점
# 일반적으로 저장공간이 좀더 많이 필요하다.
# 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함

# 주요 용도
# 검색이 많이 필요한 경우
# 저장, 삭제, 읽기가 빈번한 경우
# 캐쉬 구현시 (중복 확인이 쉽기 때문)

# 해쉬함수 만들고 사용해보기

# 데이터를 저장할 공간 미리 만들어주기
hash_table = list([0 for i in range(10)])
print(hash_table)


# 나누기를 통한 해쉬값 구하기 : Division 기법
def hash_func(key):
    return key % 5


# 문자열 데이터일 경우 아스키코드로 변환하고 값을 나눠줌
data1 = 'Apple'
data2 = 'Butter'
data3 = 'Child'
data4 = 'Duck'

print(ord(data1[0]), " | hash : ", ord(data1[0]) % 5)
print(ord(data2[0]), " | hash : ", ord(data2[0]) % 5)
print(ord(data3[0]), " | hash : ", ord(data3[0]) % 5)
print(ord(data4[0]), " | hash : ", ord(data4[0]) % 5)


# 저장할 키값 : data
# 키의 value값 : value
# 해쉬함수를 통해서 생성한 키값 : hash_address

# 해쉬 테이블에 값을 저장하는 함수
def save_date(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


# 해쉬테이블의 값을 읽는 함수
def read_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


save_date("AAA", '01011111111')
save_date("BBB", '01022222222')
save_date("CCC", '01033333333')

# 연습1: 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)


list_hash = list([0 for i in range(8)])


# key를 만드는 함수
def getKey(data):
    return hash(data)


# 해쉬 함수
def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(getKey(data))
    list_hash[hash_address] = value


def read_data(data):
    hash_address = hash_function(getKey(data))
    return list_hash[hash_address]


save_data('asdasd', 'apple')
save_data('erqwrw', 'beetle')
save_data('wvwrrv', 'chicken')
save_data('vcvnte', 'dice')

print(list_hash)
print(read_data('wvwrrv'))