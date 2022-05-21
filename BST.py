'''
과제2 (4) 286p. 이진탐색트리

노드를 삭제할 때, 왼쪽 서브트리의 최대값과 오른쪽 서브트리의 최소값을 선택
전체트리의 높이가 낮아지는 것을 대체 노드로 선택
-> 동일할 경우 왼쪽 서브 트리의 노드를 선택

대체 노드를 이동하면 또다른 삭제 연산이 재귀적으로 발생

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.tree = None
        self.temp = None
        self.prev = None
        self.direction = None

    def insert(self, item):
        node = Node(item)
        if not self.tree: self.tree = node      # 빈 트리
        else:
            temp = self.tree                    # 현재 노드
            prev = None                         # 상위 노드
            while True:
                prev = temp
                if item < prev.data:            # 왼쪽 서브 트리로 이동
                    temp = temp.left
                    if not temp:
                        prev.left = node
                        return
                elif item > prev.data:
                    temp = temp.right
                    if not temp:
                        prev.right = node
                        return
                else: return                    # 중복 노드
    
    def delete_node(self, node, item):          # node는 삭제할 노드
        if node is None: return None
        if node.data > item:
            node.left = self.delete_node(node.left, item)
            return node
        elif node.data < item:
            node.right = self.delete_node(node.right, item)
            return node
        else:                                   # 삭제 노드 발견
            if node.left is None:               # 오른쪽 자식 노드만 존재
                return node.right
            elif node.right is None:            # 왼쪽 자식 노드만 존재
                return node.left
            elif node.left is None and node.right is None:      # 단말 노드
                return None
            else:                               # 자식이 2개인 노드 삭제
                if self.height(node.right) > self.height(node.left): # 오른쪽 서브트리가 더 깊은 경우
                    right_min = self.find_min(node.right)       # 오른쪽의 최소값
                    node.data = right_min.data
                    node.right = self.delete_node(node.right, right_min.data)
                    return node
                else:
                    left_max = self.find_max(node.left)         # 왼쪽의 최댓값
                    node.data = left_max.data
                    node.left = self.delete_node(node.left, left_max.data)
                    return node

    def find_delete(self, item):
        self.tree = self.delete_node(self.tree, item)
    
    def find_max(self, root):
        if not root: return Node
        node = root
        while node.right:
            node = node.right
        return node

    def find_min(self, root):
        if not root: return Node
        node = root
        while node.left:
            node = node.left
        return node

    def height(self, root):         # 루트부터 트리의 높이
        if root is None:
            return -1

        leftH = self.height(root.left) + 1
        rightH = self.height(root.right) + 1
        return max(leftH, rightH)

    def postorder(self,ptr):
        if ptr:
            self.postorder(ptr.left)
            self.postorder(ptr.right)
            print(ptr.data, end=' ')

bst = BST()
for i in [30, 20, 10, 40, 60, 50, 25]:
    bst.insert(i)
    bst.postorder(bst.tree)
    print()

print()

for i in [30, 25, 40, 50, 20, 60]:
    bst.find_delete(i)
    bst.postorder(bst.tree)
    print()