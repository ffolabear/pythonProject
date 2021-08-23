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
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    # 일반 링크드리스트와 다르게 앞뒤를 다르게 연결해줘야함
                    node.next = node.next.next
                    node.next.next.prev = node
                    del temp
                    return
                else:
                    node = node.next

    # 예제: 특정값 앞에 데이터를 추가하는 함수 만들기
    # 조건: tail 에서부터 탐색
    def insert_before(self, target,data):
        if self.head is None:
            Node(data)

        else:
            node = self.tail

            while node.prev:
                if node.prev.data == target:
                    # 만약 이전 노드가 head 라면
                    if node.prev == self.head:
                        old_head = self.head
                        new = Node(data)

                        # 새로운 노드를 head로 만들어주기
                        self.head = new
                        new.next = old_head

                        # 이전 head를 연결해주는 작업
                        old_head.prev = new

                    # 만약 이전 노드가 head가 아니라면
                    else:
                        new = Node(data)


                else:
                    node = node.prev








    # 예제: 특정값 뒤에 데이터를 추가하는 함수 만들기
    def insert_after(self, data):
        if self.head is None:
            Node(data)

    def info(self):
        node = self.head
        while node.next:
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
