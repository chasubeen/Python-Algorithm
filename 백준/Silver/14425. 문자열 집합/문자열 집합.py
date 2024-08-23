from sys import stdin
input = stdin.readline

## node를 클래스로 정의
class Node(object):
    def __init__(self, isEnd):
        self.isEnd = isEnd # 마지막 문자열인가(리프 노드)
        self.childNode = {} # 자식 노드 저장

### 트라이 트리
class Trie(object):
    def __init__(self):
        self.parent = Node(None) # 부모 노드 저장 변수

    # 트리 그리기
    def insert(self, string):
        nowNode = self.parent
        temp_lenght = 0
        for char in string:
            # 자식 노드에 없는 문자면 새로 생성
            if char not in nowNode.childNode:
                nowNode.childNode[char] = Node(char)
            # 자식 노드로 이동
            nowNode = nowNode.childNode[char]
            temp_lenght += 1
            # 이번이 마지막 문자면
            if temp_lenght == len(string):
                nowNode.isEnd = True

    # 트리 탐색
    def search(self, string):
        nowNode = self.parent
        temp_lenght = 0
        for char in string:
            if char in nowNode.childNode:
                nowNode = nowNode.childNode[char]
                temp_lenght += 1
                if temp_lenght == len(string) and nowNode.isEnd == True:
                    return True
            else:
                return False
        return False

## 입력
N, M = map(int, input().split())
myTrie = Trie()  # Trie 생성

for _ in range(N):
    word = input().strip()
    myTrie.insert(word)  # 단어 삽입

result = 0
for _ in range(M):
    word = input().strip()
    if myTrie.search(word):  # 단어 찾기
        result += 1
print(result)