'''
과제2 (3)  238쪽 프로그램 9.3

prim의 방식으로 최소 비용 신장 트리 찾기

- 시작 노드는 사용자로부터 입력받음
- 신장 트리에 간선이 추가되는 순서대로 출력

'''

class Graph:
    def __init__(self):
        self.graph = {}     # 그래프의 기본 모양 (중복있음)
        self.v_list = []    # 현재까지 확장된 트리의 vertex 리스트
        self.e_list = []    # 현재 트리에서 선택할 수 있는 edge 리스트
        self.edge = []      # 실제로 추가된 edge
        self.total = 0      # edge의 총 cost

    def create(self, v1, v2, weight):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        # 각 정점마다 연결될 수 있는 간선을 전부 넣어줌
        self.graph[v1].append((v1, v2, weight))
        self.graph[v2].append((v2, v1, weight))

    # 간선 비용대로 정렬
    def sort_edge(self, network):
        temp = []
        for v1, v2, cost in network:
            temp.append((cost, v1 ,v2))
        temp.sort()
        return temp

    # 프림 알고리즘 구현
    def prim(self, start):
        # 시작 지점부터 v_list와 e_list에 추가함
        self.v_list.append(start)
        print('\nStart vertex =', self.v_list)
        self.e_list.extend(self.graph[start])
        self.e_list = self.sort_edge(self.e_list)

        while self.e_list:  # 더 선택할 수 있는 간선이 없을때까지 반복
            cost = self.e_list[0][0]
            v1 = self.e_list[0][1]
            v2 = self.e_list[0][2]
            print('\n(',v1,',',v2,')','cost = ',cost)

            # 사용한 간선 리스트에서 삭제
            del self.e_list[0]

            # 간선이 v_list에 이미 있는 정점를 가르킨다면 사이클을 형성하므로 연결안함
            if v1 in self.v_list and v2 in self.v_list:
                print("rejected for cycle")
                continue
            
            # 간선을 연결하고 합계 비용 계산
            self.edge.append((v1, v2, cost))
            self.total += cost

            # 확장된 정점에서 선택할 수 있는 간선이 v_list에 이미 있다면 중복이므로 빼고 추가
            extend_list = []
            for s1, s2, cost in self.graph[v2]:
                if s2 not in self.v_list:
                    extend_list.append((s1, s2, cost))
            extend_list = self.sort_edge(extend_list)

            # 현재 정점과 간선 리스트 확장
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

# 시작할 정점 입력
start = int(input("start node : "))
g.prim(start)
print()
print('Spanning tree vertices = ', g.v_list)
print('spanning tree edges = ', g.edge)
print('cost total = ', g.total)