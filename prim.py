'''
과제2 (3)  238쪽 프로그램 9.3

prim의 방식으로 최소 비용 신장 트리 찾기

- 시작 노드는 사용자로부터 입력받음
- 신장 트리에 간선이 추가되는 순서대로 출력

'''

class Graph:
    def __init__(self):
        self.graph = {}
        self.v_list = []
        self.e_list = []
        self.edge = []
        self.total = 0

    def create(self, v1, v2, weight):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        self.graph[v1].append((v1, v2, weight))
        self.graph[v2].append((v2, v1, weight))

    def sort_edge(self, network):
        temp = []
        for v1, v2, cost in network:
            temp.append((cost, v1 ,v2))
        temp.sort()
        return temp

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
        print('Spanning Tree =', self.v_list)
        self.e_list.extend(self.graph[start])
        self.e_list = self.sort_edge(self.e_list)

        while self.e_list:
            cost = self.e_list[0][0]
            v1 = self.e_list[0][1]
            v2 = self.e_list[0][2]
            print('\n(',v1,',',v2,')','cost = ',cost)
            del self.e_list[0]

            if v1 in self.v_list and v2 in self.v_list:
                print("rejected for cycle")
                continue
            
            self.edge.append((v1, v2, cost))
            self.total += cost

            extend_list = []
            for s1, s2, cost in self.graph[v2]:
                if s2 not in self.v_list:
                    extend_list.append((s1, s2, cost))
            extend_list = self.sort_edge(extend_list)

            self.e_list.extend(extend_list)
            self.e_list.sort()
            self.v_list.append(v2)
            
            print('Spanning Tree =',self.v_list)

g = Graph()
# (v1, v2, weight)
network = [(1,5,6),(1,6,8),(2,3,17),(2,6,9),(5,6,7),(3,7,15),(3,4,5),(3,8,3),(4,8,4),(6,7,10)]
node_list = []

for v1, v2, weight in network:
    g.create(v1, v2, weight)

print('network=', network)
print(g.graph)

start = int(input("start node : "))
g.prim(start)
print()
print('Spanning tree vertices = ', g.v_list)
print('spanning tree edges = ', g.edge)
print('cost total = ', g.total)