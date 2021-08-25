# 파이썬 자료구조
# 5. 헤쉬 테이블 기본 구현 - 충돌 개선 - Linear probing

# 해쉬 값이 충돌될때 해결방법

# Linear probing
# 폐쇄 해슁 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
# 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법


hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 이미 데이터가 저장되어있다는 뜻
    if hash_table[hash_address] != 0:
        # 순회하면서 빈공간을 찾은후 그 곳에 값을 넣어준다
        for index in range(hash_address, len(hash_table)):
            # 데이터가 안들어있는 상태
            if hash_table[index] == 0:
                # 리스트 형태의 값을 추가해준다
                hash_table[index] = [index_key, value]
                return
            # 만약 이미 값이 있는 키라면 값을 업데이트
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            # 중복된 키에 대한 데이터를 저장할떄 빈공간이 나올때까지 찾은후 저장하므로 0이라는 것은 저장되지 않았다는 뜻
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]


save_data('asdasd', 'apple')
save_data('erqwrw', 'apples')
save_data('wvwrrv', 'chicken')
save_data('vcvnte', 'dice')

print((hash('apple')) % 8)
print((hash('abc')) % 8)

print(hash_table)
