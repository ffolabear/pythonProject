# 파이썬 자료구조
# 5. 헤쉬 테이블 기본 구현 - 충돌 개선 - Chaining

# 해쉬 값이 충돌될때 해결방법

# Chaining
# 개방 해슁 또는 Open Hashing 기법 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
# 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법


hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    # 해쉬값이 중복될떄 값을 구분해줄 값
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 0이 아니다 = 이미 값이 있다. = 중복된 해쉬값을 가진다.
    if hash_table[hash_address] != 0:
        # 해당 해쉬값 안에 있는 chaining 한 객체들의 길이 동안
        for index in range(len(hash_table[hash_address])):
            # 만약 그 안에서 key 값이 동일하다면 그냥 덮어 씀
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        # key 값이 같은것이 하나도 없으면 새로운 것을 추가해줌
        hash_table[hash_address].append([index_key, value])

    # 만약 데이터가 없다면
    else:
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


save_data('asdasd', 'apple')
save_data('erqwrw', 'apples')
save_data('wvwrrv', 'chicken')
save_data('vcvnte', 'dice')

print((hash('apple')) % 8)
print((hash('abc')) % 8)

print(hash_table)
