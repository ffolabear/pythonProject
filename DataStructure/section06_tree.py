# 파이썬 자료구조
# 6. 트리
# 트리: Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
# 이진 트리 (Binary Tree) 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

# Node: 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
# Root Node: 트리 맨 위에 있는 노드
# Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄

# Parent Node: 어떤 노드의 다음 레벨에 연결된 노드
# Child Node: 어떤 노드의 상위 레벨에 연결된 노드
# Leaf Node (Terminal Node): Child Node가 하나도 없는 노드

# Sibling (Brother Node): 동일한 Parent Node를 가진 노드
# Depth: 트리에서 Node가 가질 수 있는 최대 Level


# 이진 트리와 이진 탐색 트리 (Binary Search Tree)

# 이진 트리: 노드의 최대 Branch가 2인 트리
# 이진 탐색 트리 (Binary Search Tree, BST): 이진 트리에서 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 큰 값의 조건을 가지는 이진트리

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    # 루트노드 = head
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        # 순회해서 데이터가 들어갈 자리를 찾아야하므로 순회할 첫 값 지정
        self.current_node = self.head
        while True:
            # 현재 노드보다 작다 =  현재 노드를 기준으로 왼쪽으로 가야함
            if value < self.current_node.value:
                if self.current_node is not None:
                    self.current_node = self.current_node.left
                else:
                    # 해당 위치에 노드가 없다면 그냥 새로운 노드를 만들어준다
                    self.current_node.left = Node(value)
                    # while True 이므로 반복문 중지
                    break
            # 현재 노드보다 크거나 같다 =  현재 노드를 기준으로 오른쪽으로 가야함
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False


head = Node(1)
bst = NodeMgmt(head)
for i in range(2, 11):
    bst.insert(i)

print(bst.search(2))
