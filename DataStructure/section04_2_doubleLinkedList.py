# 파이썬 자료구조
# 4_2. 더블 링크드 리스트

# 이중 연결 리스트
# 일반 링크드리스트와 다르게 현재 노드의 다음 포인터와 이전 노드를 가리키는 포인터가 같이 존재

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head is None:
            Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            # 새롭게 연결해줄 노드
            new = Node(data)

            node.next = new
            new.prev = node
            self.tail = new

    def delete(self, data):
        if self.head is None:
            print("노드가 없습니다.")

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head

            while node.data != data:
                node = node.next

            node_prev = node.prev

            node.prev.next = node.next
            node.next.prev = node_prev
            del node
            return

    # 예제: 특정값을 머리에서부터 탐색
    def search_from_head(self, data):

        if self.head is None:
            print("노드가 존재하지않습니다.")
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    # 예제: 특정값을 꼬리에서부터 탐색
    def search_from_tail(self, data):

        if self.head is None:
            print("노드가 존재하지않습니다.")
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    # 예제: 특정값 앞에 데이터를 추가하는 함수 만들기
    # 조건: tail 에서부터 탐색
    def insert_before(self, target, data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.tail

            while node.data != target:
                node = node.prev
                if node is None:
                    return False

            # 현재 상황
            # ⬅ 탐색방향
            # node.prev(prev_new) | new | node

            new = Node(data)
            prev_new = node.prev
            prev_new.next = new

            new.prev = prev_new
            new.next = node

            node.prev = new
            return True

    # 예제: 특정값 뒤에 데이터를 추가하는 함수 만들기
    # 조건: head 에서부터 탐색
    def insert_after(self, target, data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.head

            while node.data != target:
                node = node.next
                if node is None:
                    return False
            # 현재 상황
            # 탐색방향 ➡
            # node | new | node.next (next_new)

            new = Node(data)

            next_new = node.next
            new.next = next_new
            new.prev = node
            node.next = new

            if new.next is None:
                self.tail = new
            return True

    def info(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


double_list = NodeMgmt(0)

print(" >> 1 ~ 10까지 데이터 추가")
for i in range(1, 11):
    double_list.insert(i)

double_list.info()
print()

print(" >> 0 ~ 10중 6을 제거")
double_list.delete(6)
double_list.info()

print()

print(" >> 0 ~ 10중 head 값 0을 제거")
double_list.delete(0)
double_list.info()

# head 를 지우자 1로 head가 바뀐것을 볼 수있음
print()
print(double_list.head.data)

print()

double_list.insert_before(4, 12)
double_list.info()
print()

double_list.insert_after(4, 44)
double_list.info()

print()
print(double_list.search_from_head(44).data)
print(double_list.search_from_tail(44))
print(double_list.tail.data)

