from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [-1]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


que = deque([x])
visited[x] = 0
while que:
    v = que.popleft()
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v]+1
            que.append(i)

check = False
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
