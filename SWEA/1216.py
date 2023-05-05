# from collections import deque


# def recursive(r,q):
#     if len(q) == 1:
#         return 1


for i in range(1, 2):
    n = int(input())
    arr = []
    for j in range(100):
        row = list(input())
        arr.append(row)
        answer = 0
        li = []
        for l in range(100):
            for r in row[l:]:
                li.append(r)
                if li == li[::-1]:
                    answer = max(answer, len(li))
    arr_rev = list(map(list, zip(*arr)))
    for row in arr_rev:
        li = []
        for l in range(100):
            for r in row[l:]:
                li.append(r)
                if li == li[::-1]:
                    answer = max(answer, len(li))
    print(answer)

    # queue = deque(row)
    # for l in range(100):
    #     l = 99 - l

    #     if row[:l] == row[:l]
