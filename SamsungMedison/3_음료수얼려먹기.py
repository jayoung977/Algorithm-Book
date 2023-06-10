n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny < m and ny >= 0:
            if data[nx][ny] == 0:
                data[nx][ny] = 1
                virus(nx, ny)


result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            result += 1
            virus(i, j)

print(result)
