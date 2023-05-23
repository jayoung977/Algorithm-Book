n,m = map(int,input().split())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

temp = [[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >=0 and ny < m and ny >=0:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1
    return score


result = 0
def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        #바이러스 퍼뜨림
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        #점수 계산하기
        #가장 높은 점수 반환하기
        result = max(result,get_score())
    else:
        #벽 세우기
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    cnt += 1
                    dfs(cnt)
                    data[i][j] = 0
                    cnt -= 1
dfs(0)
print(result)