# 파이썬 자료구조
# 7. 힙
# 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
#   - 완전 이진 트리: 노드를 삽입할 때 최하단 ⭐️ 왼쪽 ⭐ 노드부터 차례대로 삽입하는 트리

# 힙을 사용하는 이유
# 데이터를 입력과, 최대값과 최소값의 탐색시,  𝑂(𝑙𝑜𝑔𝑛) 의 시간복잡도를 가짐
# 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

# 힙은 최대값을 구하기 위한 구조 (최대 힙, Max Heap) 와,
# 최소값을 구하기 위한 구조 (최소 힙, Min Heap) 로 분류할 수 있음


# 힙의 조건
# ⭐️ 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
# ⭐ 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
# 완전 이진 트리 형태를 가짐

# 힙과 이진탐색트리의 차이점과 공통점

# 공통점
# 둘다 이진 트리

# 차이점
# 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
# 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
# (힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음)

# 이진 탐색 트리는 탐색을 위한 구조
# 힙은 최대/최소값 검색을 위한 구조

# ‼️ 힙의 주요 특징
# 부모 노드 인덱스 번호 : 자식 노드 인덱스 번호  // 2
# 왼쪽 자식 노드 인덱스 번호 : 부모 노드 인덱스 번호  * 2
# 오른쪽 자식 노드 인덱스 번호 : 부모 노드 인덱스 번호  * 2 + 1

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):

        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        # 마지막으로 넣은 원소의 인덱스 번호
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                inserted_idx]
            # Heap 의 기본 조건을 만족시키기 위해 바꾸는 작업을 계속해줘야 하므로 바꿔줌
            inserted_idx = parent_idx
        return True

    def move_down(self, popped_idx):

        # popped_idx 의 왼쪽, 오른쪽 자식 인덱스 번호
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # 1. 왼쪽 자식이 없는 경우 = 자식 노드가 없는 경우
        if left_child_popped_idx >= len(self.heap_array):
            # 바꿔줄 필요가 없음
            return False

        # 2. 왼쪽 자식만 있는 경우
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False

        # 3. 둘다 있는 경우
        else:
            # 왼쪽 자식 노드가 더 클 경우
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                # 왼쪽 자식노드가 부모 노드보다 크다면 바꿔줘야함
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            # 오른쪽 자식 노드가 더 클 경우
            else:
                # 오른쪽 자식노드가 부모 노드보다 크다면 바꿔줘야함
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    # 힙에서 특정 데이터의 삭제기능은 없음
    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        # 최댓값이자 루트 노드
        returned_data = self.heap_array[1]

        # 가장 마지막에 추가된 값(가장 마지막값)을 루트노드로 올려주기
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        # 추출된 데이터
        popped_idx = 1

        while self.move_down(popped_idx):

            # popped_idx 의 왼쪽, 오른쪽 자식 인덱스 번호
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # 2. 왼쪽 자식만 있는 경우
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    # 데이터를 바꿔준 다음 popped_idx 의 위치를 내려준다
                    popped_idx = left_child_popped_idx

            # 3. 둘다 있는 경우
            else:
                # 왼쪽 자식 노드가 더 클 경우
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # 왼쪽 자식노드가 부모 노드보다 크다면 바꿔줘야함
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx

                # 오른쪽 자식 노드가 더 클 경우
                else:
                    # 오른쪽 자식노드가 부모 노드보다 크다면 바꿔줘야함
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx

        return returned_data



heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())

print(heap.heap_array)
