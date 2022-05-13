'''
과제2 (3)  238쪽 프로그램 9.3

prim의 방식으로 최소 비용 신장 트리 찾기

- 시작 노드는 사용자로부터 입력받음
- 신장 트리에 간선이 추가되는 순서대로 출력

'''
class Node:
    def __init__(self, data = None):
        self.data = data
        self.edge_list=[]

class Graph:
    def __init__(self):
        self.graph = {}
        self.v_list = []
        self.edge = []
        self.total = 0

    def create(self, v1, v2, weight):
        if v1 not in self.graph:
            self.graph[v1] = []
        self.graph[v1].append((v2, weight))

    def sort_edge(self, network):
        temp = []
        for v1, v2, cost in network:
            temp.append((cost, v1 ,v2))
        temp.sort()
        return temp
    
    '''
    def find(self, v2):
        for v1, lst in self.v_list.items():
            if v2 == v1: return v1
            if v2 in self.v_list[v1]: return v1
        return -1
    '''

    def union(self, s1, s2):
        if s1 < s2:
            self.v_list[s1].append(s2)
            self.v_list[s1].extend(self.v_list[s2])
            del self.v_list[s2]
        else:
            self.v_list[s2].append(s1)
            self.v_list[s2].extend(self.v_list[s1])
            del self.v_list[s1]

    def prim(self, start):
        self.v_list.append(start)
        print('set list=', self.v_list)
        sort_network = self.sort_edge(network)
        for cost, v1, v2 in sort_network:
            s1 = self.find(v1)
            s2 = self.find(v2)
            if s1 == s2:
                continue
            self.edge.append((v1, v2, cost))
            self.total += cost
            self.union(s1, s2)
        

g = Graph()
# (v1, v2, weight)
network = [(1,5,6),(1,6,8),(2,3,17),(2,6,9),(5,6,7),(3,7,15),(3,4,5),(3,8,3),(4,8,4),(6,7,10)]
node_list = []

for v1, v2, weight in network:
    g.create(v1, v2, weight)
    if node_list[0]//2 == 0:
        pass


print('network=', network)

start = input("start node : ")
g.prim(start)
print(g.graph)
print(g.v_list)
print(g.edge)
print(g.total)
