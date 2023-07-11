'''
오늘 동빈이는 여행가신 부모님을 대신해서 떡집 일을 하기로 했다. 
오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 떡의 길이가 일정하지 않다.
대신에 한봉지 안에 들어가는 총 떡의 길이는 절단기로 잘라서 맞춰준다.

절단기 놀이 (H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.

예를 들어 높이가 19,14,10,17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면
자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다.
손님은 6cm만큼의 길이를 가져간다

손님이 왔을 떄 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 
절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

[입력 조건]
- 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000 )
- 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양 만큼 떡을 사갈 수 있다.
높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

[출력 조건]
- 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

[입력 예시]
4 6
19 15 10 17

[출력 예시]
15
'''
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜자르기(오른쪽 부분 탐색)
    else:
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        result = mid
        start = mid + 1
# 정답 출력
print(result)
