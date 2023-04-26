from collections import deque

N = int(input())
board = [[0]*N for i in range(N)]  #[[0]*N]*M 사용하지 말것, 모든 행 값 반복됨


apple_num = int(input())
for i in range(apple_num):
    row, col = map(int, input().split())
    board[row-1][col-1] = 2 #리스트는 0부터
# for li in board:
#     print(li)



dx = [0, 1, 0, -1] #[열+1,행+1,열-1,행-1]
dy = [1, 0, -1, 0]
directDict = dict()
queue = deque()
queue.append((0, 0))


change_num = int(input())
for i in range(change_num):
    X, C = input().split()
    directDict[int(X)] = C  #{X1:C1, X2:C2 ...}



x, y = 0, 0 #x:행 y:열
board[x][y] = 1  #초기값 board[0][0] =1 
cnt = 0
direction = 0

# ?
def turn(alpha):
    global direction
    if alpha == 'L': #왼쪽
        direction = (direction - 1) % 4
    else:  #D-오른쪽
        direction = (direction + 1) % 4


while True:
    cnt += 1  #초 
    x += dx[direction]   #[열+1,행+1,열-1,행-1] 초기값  direction 0 이니까 열+1
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N: #벽에 부딫히면 게임끝
        break

    if board[x][y] == 2:  #사과가 있으면
        board[x][y] = 1
        queue.append((x, y))
        if cnt in directDict:  #X초인 경우 
            turn(directDict[cnt])  #딕셔너리에서 C값 확인 및 turn 함수 실행

    elif board[x][y] == 0: #사과가 없으면
        board[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft() #꼬리 좌표 값을 뺴면서 tx, ty 로 출력
        board[tx][ty] = 0  #꼬리 좌표값 0으로 만듦 (꼬리 뻄)
        if cnt in directDict:   #X초인 경우 
            turn(directDict[cnt])   #딕셔너리에서 C값 확인 및 turn 함수 실행

    else:  #만약 자기자신에 부딪힐 경우도 게임 끝 board[x][y] == 1: 
        break

print(cnt)



        





