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

                if self.current_node.left is not None:
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

    def delete(self, value):

        # 삭제할 노드의 존재여부 파악
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched is False:
            return False

        # 1. 삭제할 노드가 leaf 노드일때
        if self.current_node.left is None and self.current_node.right is None:
            # leaf 노드가 부모보다 작으면 왼쪽, 크면 오른쪽
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            # del self.current_node

        # 2. 삭제할 노드의 자식 노드가 1개일때

        # 현재 노드가 왼쪽에만 자식 노드를 가지고 있을 경우
        if self.current_node.left is not None and self.current_node.right is None:
            # 삭제할 노드가 부모 노드의 왼쪽에 있는 경우
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        # 현재 노드가 오른쪽에만 자식 노드를 가지고 있을 경우
        elif self.current_node.left is None and self.current_node.right is not None:
            # 삭제할 노드가 부모 노드의 오른쪽에 있는 경우
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 3. 삭제할 노드의 자식 노드가 2개일때
        elif self.current_node.left is not None and self.current_node.right is not None:

            #    - 삭제할 Node의 오른쪽 자식 중, 왼쪽값(가장 작은 값)을 삭제할 Node의 부모 Node가 가리키도록 한다. ⭐
            #      - 삭제 노드의 왼쪽 노드 보다 크면서 오른쪽 노드중 가장 작은 값이기 때문

            #    - 삭제할 Node의 왼쪽 자식 중, 오른쪽 값(가장 큰 값을) 삭제할 Node의 부모 Node가 가리키도록 한다.
            #      - 삭제 노드의 왼쪽 노드 중 가장 크면서 오른쪽 노드들 보다 작기 때문

            # 3-1: 삭제할 Node가 부모 Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 자식 Node가 없을 때
            if value < self.parent.value:
                # 오른쪽을 봐야하므로 순회하기 위한 첫번째 노드 지정
                # change_node 는 노드(current_node)를 삭제함으로써 위치를 올려줘야하는 노드
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                # 가장 작은 노드를 찾기 위한 작업
                while self.change_node.left is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                # 3-1-1: 삭제할 Node가 부모 Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 자식 Node가 있을 때
                if self.change_node.right is not None:
                    # 삭제 노드의 오른쪽의 부모 노드 기준으로 가장 작은 노드이므로 올려줌
                    self.change_node_parent.left = self.change_node.right

                # 3-1-2: 삭제할 Node가 부모 Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 자식 Node가 없을때
                else:
                    # 자식 노드가 없다면 가장 작은 노드를 삭제하기 위해서먼저 부모의 관계만 끊어주면됨
                    self.change_node_parent.left = None

                # 삭제할 노드의 부모와 연결
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

            # 3-2: 삭제할 Node가 부모 Node의 오른쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 자식 Node가 없을 때
            #  - 3-1 의 경우와 반대지만 기본 전략이 같기 때문에 수정할 부분이 많지는 않음
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right is not None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None

                # 이 부분만 3-1과 다름
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True


# 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
import random

# 중복 방지를 위한 집합 사용
bst_nums = set()
while len(bst_nums) != 100:
     bst_nums.add(random.randint(0, 999))

print(bst_nums)

# 루트 노드에는 중간 값을 넣어줌
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print ('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)











