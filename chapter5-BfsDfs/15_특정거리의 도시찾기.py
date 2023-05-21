from collections import deque
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# print(graph)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# print(graph)
visited = [-1]*(n+1)

visited[x] = 0
q = deque([x])
# print(visited)
while q:
    now = q.popleft()
    # print('now:',now)
    for i in graph[now]:
        # print('i:', i)
        if visited[i] == -1:
            visited[i] = visited[now] + 1
            q.append(i)
iscity = False
for i in range(len(visited)):
    if visited[i] == k:
        iscity = True
        print(i)
if iscity == False:
    print(-1)





