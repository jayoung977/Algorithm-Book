n, m = map(int, input().split())
room = []
for i in range(n):
    li = list(map(int, input().split()))
    room.append(li)
temp = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def virus(y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < m and nx >= 0 and ny < n and ny >= 0:
            if temp[ny][nx] == 0:
                temp[ny][nx] = 2
                virus(ny, nx)


def score():
    result = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1
    return result


max_num = 0


def dfs(cnt):
    global max_num

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = room[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        max_num = max(max_num, score())
        return

    else:
        for i in range(n):
            for j in range(m):
                if room[i][j] == 0:
                    room[i][j] = 1
                    cnt += 1
                    dfs(cnt)
                    room[i][j] = 0
                    cnt -= 1


dfs(0)
print(max_num)
