# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    # 원소가 없는 경우
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        print(array, target, start, mid - 1)
        return binary_search(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        print(array, target, mid + 1, end)
        return binary_search(array, target, mid + 1, end)


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = map(int, input().split())  # 10 7
# 전체 원소 입력 받기
array = list(map(int, input().split()))  # 1 3 5 7 9 11 13 15 17 19
# 1 3 5 6 9 11 13 15 17 19
# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
