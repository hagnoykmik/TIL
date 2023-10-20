# 최대 힙 구현
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


# 루트 노드 뽑기
def heap_pop():
    if len(heap) <= 2:
        return heap.pop()
    
    item = heap[1]
    heap[1] = heap.pop()
    parent = 1
    child = parent * 2

    # 새로운 루트 찾기
    while child < len(heap):
        # 오른쪽 자식이 더 클 경우
        if child + 1 < len(heap) and heap[child] < heap[child + 1]:
            child += 1
        
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        
        else:
            break

    return item

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