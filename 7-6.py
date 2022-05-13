'''
과제2 (2)       182쪽 7장 6번
최대 힙 프로그램을 "연결 리스트"로 구현

1. 원소가 입력될 때마다 최대 힙을 재구성
2. 재구성 결과를 트리 형태로 출력
3. '999'가 입력되면, 완전 이진 트리 순서로 노드 값을 출력

* 각 노드의 링크 필드를 (left, right, parent)로 정의
트리 생성 시점에 부모 노드에 대한 링크 설정
'''


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
        self.parent = None

class Heap:
    def __init__(self):
        self.root = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not self.root

    def view(self):
        pass

    def add_heap(self, item):
        self.count += 1
        i = self.tail
        #item이 부모보다 클때까지 (i//2)
        while i.parent != None and item > i.parent:
            i = i.parent
        #i가 도달한 자리에 item 넣기
        i.data = item

    def view(self):
        pass