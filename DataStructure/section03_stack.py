# 파이썬 자료구조
# 3. 스택
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
# push(): 데이터를 스택에 넣기
# pop(): 데이터를 스택에서 꺼내기

# 함수를 처리하는 과정에서 스택을 사용하고 있음
# ex) 재귀함수

def recursive(data):
    if data < 0:
        print("end")
    else:
        print(data)
        recursive(data - 1)
        print("data : ", data)


recursive(5)

print()
print()

# 장점
# 구조가 단순해서, 구현이 쉽다.
# 데이터 저장/읽기 속도가 빠르다.

# 단점 (일반적인 스택 구현시)
# 데이터 최대 갯수를 미리 정해야 한다.
# 파이썬의 경우 재귀 함수는 1000번까지만 호출이 가능함
# 저장 공간의 낭비가 발생할 수 있음
# 미리 최대 갯수만큼 저장 공간을 확보해야 함

# 리스트를 활용해서 구현하는 것이 일반적임. 이 경우, 위에서 열거한 단점이 있을 수 있음


# 리스트로 스택 기능 사용해보기

list_stack = list()
list_stack.append(1)
list_stack.append(2)
list_stack.append(2)

print(list_stack)

# 가장 마지막에 넣은 값을 가져옴
print(list_stack.pop())

# pop을 하면 뽑은 값은 제거된다.
print(list_stack)

print()
print()

# 리스트로 직접 구현해보기

new_stack = list()


def new_push(data):
    new_stack.append(data)


def new_pop():
    data = new_stack[-1]
    del new_stack[-1]
    return data


for i in range(1, 10):
    new_push(i)
print(new_stack)

print(new_pop())
print(new_pop())
print(new_stack)
