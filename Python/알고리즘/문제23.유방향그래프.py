from pprint import pprint

# 정점의 갯수 n
# 간선의 갯수 m
n, m = map(int, input().split())

# 첫번째 행과 첫번째 열은 인덱스를 나타냄
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
list_ = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    # 유방향 인접 행렬
    graph[u][v] = 1
    # 유방향 인접 리스트
    list_[u].append(v)
pprint(graph)
pprint(list_)
