'''
힙의 특징
-> 자식노드로 부모노드를 찾을 수 있고, 부모노드로 자식노드를 찾을 수 있다
-> 완전 이진 트리라서 가능(순서대로 채우는 것)
-> 그래서 인덱스는 1부터 사용가능

<규칙>
자식노드(idx) // 2 == 부모노드
부모노드 * 2, (부모노드 * 2)+ 1 == 자식노드
'''

# 힙 삽입 연산
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1  # 배열의 마지막 인덱스
    parent = child // 2    # child를 2로 나눈 몫

    # 자식노드가 부모노드보다 작으면 자리 바꾸기 
    # 루트 노드이거나 최소힙 조건을 만족하지 못하면 종료
    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

# 힙 삭제 연산(루트 노드 뽑고나서 다시 루트 노드 채우기)
def heap_pop():
    # 루트 노드만 남은 경우 바로 반환
    if len(heap) <= 2:
        return heap.pop()
    
    item = heap[1]  # 루트 노드 백업
    heap[1] = heap.pop() # 마지막 노드를 루트 노드로 이용(다른데 하면 깨지니까)
    parent = 1
    child = parent * 2

    while child < len(heap): # 자식이 하나라도 있으면 자식과 부모 값 비교
        # 오른쪽 자식이 더 작은 경우
        if child + 1 < len(heap) and heap[child] > heap[child + 1]:
            child += 1 # 비교 대상을 오른쪽 자식으로 갱신

        # 자식이 더 작으면 교환
        if heap[child] < heap[parent]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        
        # 최소힙을 만족하면 탈출
        else:
            break

    return item # 백업했던 루트 노드 반환



heap = [0]
heap_push(2)
heap_push(5)
heap_push(7)
heap_push(3)
heap_push(4)
heap_push(6)
print(heap)

while len(heap) >= 2:
    print(heap_pop())
