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