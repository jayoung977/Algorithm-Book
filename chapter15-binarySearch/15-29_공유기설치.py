'''
도현이의 집 N개가 수직선 위에 있습니다.
각각의 집 좌표는 x1,c2,...xn이고, 집 여러 개가 같은 좌표를 가지는 일은 없습니다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 합니다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고
가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치하려고 합니다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 
최대로 하는 프로그램을 작성하세요

[입력 조건]
- 첫째 줄에 집의 개수 N(2 <= N <= 200,000)과 공유기의 개수 C(2<= C <= N)가 하나 이상의 
빈칸을 사이에 두고 주어집니다.
- 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi(1 <= xi <= 1,000,000,000)가 한 줄에 하나씩
주어집니다.

[출력 조건]
- 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력합니다.

[입력 예시]
5 3
1 
2
8
4
9

[출력 예시]
3
'''
n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

# 이진 탐색을 위한 시작점과 끝점 설정
start = 1  # 가능한 최소 거리(min_gap)
end = array[-1] - array[0]  # 가능한 최대 거리(max_gap)
result = 0

# 이진 탐색 수행(반복적)
while (start <= end):
    mid = (start + end) // 2  # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = array[0]
    count = 1
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n):  # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:  # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid  # 최적의 결과를 저장
    else:  # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1
print(result)
