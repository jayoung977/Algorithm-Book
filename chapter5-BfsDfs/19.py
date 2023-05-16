from itertools import product
# n = int(input())
# li = list(map(int, input().split()))
# op = list(map(int, input().split()))

n = 6
li = [1, 2, 3, 4, 5, 6]
op = [2, 1, 1, 1]


do = ['+', '-', '*', '//']


def minus_divide(a, b):
    num = abs(a)
    return -(num // b)


op_list = []
for i in range(4):
    if op[i] > 0:
        for j in range(op[i]):
            op_list.append(do[i])

# print(op_list)
# print(len(list(product(op_list))))
print(list(product(op_list,  n-1)))


# result = 0
# for i in range(n-1):

#     if op_list[i] == '+':
#         result += (li[i] +li[i+1] )
