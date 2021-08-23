# 파이썬 자료구조
# 4_1. 링크드 리스트

# 배열은 미리 할당된 공간에 순차적으로 연결된 공간에 데이터를 나열하는데 그 이상의 공간에 데이터를 저장할 수 없음
# 그것을 보완한 것이 링크드 리스트
# - 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

# 노드(Node): 데이터 저장 단위 (데이터값, 포인터) 로 구성
# 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# 장점
# 미리 데이터 공간을 미리 할당하지 않아도 됨

# 단점
# 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
# 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림(인덱스로 접근하는 것이 아니므로)
# 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요


# 유형 1
# 노드와 다음 노드를 카리키는 포인터로 구성된 유형

class Node:
    # 클래스가 만들어질때마다 초기화 시키는 함수
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 노드의 함수들을 포함한 클래스
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def info(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head is None:
            print("노드가 없습니다")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp

        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


linked_list = NodeMgmt(0)
linked_list.info()

print()

for i in range(1, 11):
    linked_list.add(i)

print()

linked_list.info()

print()
linked_list.delete(5)
linked_list.info()

print()
print()
print(linked_list.head.data)

print()
linked_list.delete(0)
linked_list.info()
