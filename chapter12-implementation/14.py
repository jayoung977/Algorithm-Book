from itertools import permutations


def solution(n, weak, dist):
    weak_length = len(weak)
    # 배열을 두배 늘려주면 방향 고민할 필요 없다
    for i in range(weak_length):
        weak.append(weak[i] + n)
    # print(weak) 
    # [1, 5, 6, 10, 13, 17, 18, 22]

    answer = int(1e9)  # 점검 불가능한 경우 가정
    dist_order = list(map(list, permutations(dist, len(dist)))) # ✅ 무조건 list형으로 만들어줄 것!!!!
    # print(dist_order)
    # [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    for i in range(weak_length):
        # 시작점을 하나씩 바꾸면서, weak의 길이만큼 잘라서 사용
        start = [weak[j] for j in range(i, i + weak_length)]
        # print(start)
        # [1, 5, 6, 10]
        # [5, 6, 10, 13]
        # [6, 10, 13, 17]
        # [10, 13, 17, 18]
        for order in dist_order:  # 탐색  # order - [1, 2, 3, 4]
            result = 1  # 친구 활용 개수
            check_len = start[0] + order[result - 1]  # 첫번째 친구가 확인할 수 있는 최대 거리
            for k in range(weak_length):
                if start[k] > check_len:  # 확인가능한 최대거리를 넘은 경우
                    result += 1  # 활용되는 dist의 친구 수 추가
                    # 더 이상 투입 인원이 없는 경우
                    if result > len(order):  #len(order):4
                        break
                    # 다음 친구가 확인할 수 있는 거리 업데이트
                    check_len = start[k] + order[result - 1]
                    # 두번째 check_len = start[1] + order[2 - 1]

            answer = min(answer, result)  #order마다 반복
    
    if answer > len(dist): #if result > len(order): 여서 result = len(order)+1인경우
        return -1
    return answer

solution(12, [1,5,6,10], [1,2,3,4])