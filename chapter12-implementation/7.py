N = input()
middle_num = int(len(N)/2)
first_sum = sum(list(map(int,list(N[:middle_num]))))
second_sum = sum(list(map(int,list(N[middle_num:]))))

if(first_sum == second_sum):
    print('LUCKY')
else:
    print('READY')
