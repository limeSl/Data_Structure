'''
과제2 (1)       138쪽 5장 15번
16개 노드의 이중 연결리스트, 두 명의 플레이어 대각선 위치에서 시작 (0번, 8번)
시계방향으로 이동
상대방의 노드에 도착하면 승리

매턴 주사위 2개 던지기
(6,6) -> 이동방향 리버스
(5,5) -> 말의 위치 교환
(1,1) -> 뒤로 1칸 이동
그 외라면 주사위 눈의 합만큼 이동
'''

import random

class Node:
    def __init__(self, item):
        self.data = item
        self.rlink = None
        self.llink = None

class Player:
    def __init__(self, item):
        self.name = item
        self.course = True

class Linkedlist:
    def __init__(self, element = 0):
        self.head = Node(element)
        self.head.rlink = self.head
        self.head.llink = self.head
        if element:
            for i in range(element):
                self.add(0)
        
    def empty(self):
        return self.head.rlink == self.head

    def find(self, item):
        temp = self.head.rlink
        while temp != self.head:
            if temp.data == item: return temp
            temp = temp.rlink
        return None

    def view(self):
        temp = self.head.rlink
        print("[", end=' ')
        while temp != self.head:
            if temp.data:
                print("{0:<3}".format(temp.data), end= '')
            else:
                print("{0:<3}".format("□"), end='')
            temp = temp.rlink
        print("]")

    def add(self, item):
        node = Node(item)
        if self.empty():
            node.llink = self.head
            node.rlink = self.head
            self.head.rlink = node
            self.head.llink = node
        else:
            node.llink = self.head.llink
            node.rlink = self.head
            self.head.llink.rlink = node
            self.head.llink = node

    def move(self, item, index):

        #존재하던 요소라면 거기부터 이동
        crt = self.find(item.name)
        #없었다면 헤드부터
        if not crt: crt = self.head.rlink
        else: crt.data = 0

        #index가 음수값
        if index<0: 
            item.course = not item.course
            index = abs(index)
        
        for i in range(index):
            if item.course:
                crt = crt.rlink
                if crt == self.head:
                    crt = crt.rlink
            else:
                crt = crt.llink
                if crt == self.head:
                    crt = crt.llink

        #도착한 곳에 이미 데이터가 있다면
        if crt.data:
            global judged
            judged = True
        crt.data = item.name

    #서로의 데이터 값만 바꿔줌
    def trade(self, item1, item2):
        self.find(item1.name).data = item2.name
        self.find(item2.name).data = item1.name


#게임 초기 세팅
lst = Linkedlist(16)
p1 = Player("p1")
p2 = Player("p2")
players = [p1, p2]
lst.move(p1,0)
lst.move(p2,8)
turn = 0
judged = False

print("Game Start!")
lst.view()
print("___________________________________________________")

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    event = ""

    if dice1 == 6 and dice2 == 6:
        #reverse
        players[turn%2].course = not players[turn%2].course
        event = "reverse"
    elif dice1 == 5 and dice2 == 5:
        #trade
        lst.trade(players[0],players[1])
        event = "trade"
    elif dice1 == 1 and dice2 == 1:
        #back
        lst.move(players[turn%2], -1)
    else:
        lst.move(players[turn%2],dice1 + dice2)
    
    #매 턴 상태 출력
    print("\n",turn+1,"turn   (",dice1,",",dice2,") ",event)
    lst.view()

    #게임 종료
    if judged:
        print("\n" + players[turn%2].name + " is winner!")
        break

    turn += 1
    event = ""

input()