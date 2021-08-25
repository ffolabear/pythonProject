# 파이썬 자료구조
# 5. 헤쉬 테이블  - 충돌 개선


# 파이썬의 hash() 함수는 실행할 때마다, 값이 달라질 수 있음
# 유명한 해쉬 함수들이 있음: SHA(Secure Hash Algorithm, 안전한 해시 알고리즘)
# 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능


# SHA-1
import hashlib

data = 'test'.encode()
print(data)
hash_object = hashlib.sha1()

# 해쉬값이 오브젝트에 들어있는 상태
hash_object.update(data)
hex_digit = hash_object.hexdigest()
print(hex_digit)

# 데이터 -> 바이트로 인코딩 -> 16진수로 변환

print()

# SHA-256
hash_object_256 = hashlib.sha256()

hash_object_256.update(data)
hex_digit = hash_object_256.hexdigest()
print(hex_digit)

# 어떤 데이터를 넣던 고정된 길이의 일관된 값을 얻기 떄문에 사용한다.
# 얻은 해쉬값으로 원래 데이터를 추론할수없기 때문에 안전하다.

# 헤쉬 테이블에 적용해보기

hash_table = list([0 for i in range(8)])


# 이 부분만 변경해주면됨
def get_key(data):
    hash_256 = hashlib.sha256()
    hash_256.update(data.encode())
    hex_digit_256 = hash_256.hexdigest()
    return int(hex_digit_256, 16)


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


