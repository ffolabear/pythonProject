# 파이썬 자료구조
# 2. 큐
# FIFO : 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조


# Enqueue: 큐에 데이터를 넣는 기능
# Dequeue: 큐에서 데이터를 꺼내는 기능

# 큐의 종류
# Queue(): 가장 일반적인 큐 자료 구조
# LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
# PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력


import queue

# 일반적인 큐

data_queue = queue.Queue()
data_queue.put("Queue1")
data_queue.put("Queue2")

print(data_queue.qsize())
print(data_queue.get())

print()

# 큐의 get 함수를 호출하면 나중에 입력된 데이터부터 하나씩 줄어듬
print(data_queue.qsize())
print(data_queue.get())

print()
print()

# LifoQueue 큐 (스택과 비슷한 구조)
lifo_queue = queue.LifoQueue()

lifo_queue.put((1, 'one'))
lifo_queue.put((2, 'two'))
lifo_queue.put((3, 'three'))

print(lifo_queue.qsize())

# lifo queue는 가장 마지막에 넣은것 부터 출력된다.
print(lifo_queue.get())
print(lifo_queue.get())
print(lifo_queue.get())
print(lifo_queue.qsize())

print()
print()

# Priority Queue 큐

p_queue = queue.PriorityQueue()

# 인자로 튜플을 넘겨주는데 그 첫번째 인자를 우선순위로 인식
p_queue.put((8, "third"))
p_queue.put((1, "second"))
p_queue.put((3, "first"))

print(p_queue.get())
print(p_queue.get())
print(p_queue.get())

# 연습 : 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기

list_queue = list()


def enque(data):
    list_queue.append(data)


def deque():
    return list_queue[len(list_queue) - 1]


def qsize():
    return len(list_queue)
