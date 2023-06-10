
from collections import deque
n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input())))
# print(data)
# distance = [[-1]*m for _ in range(n)]
q = deque([[0, 0]])
# distance[0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y = q.popleft()
    # print('x,y', x, y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny < m and ny >= 0:
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                # distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny])
print(data[-1][-1])
