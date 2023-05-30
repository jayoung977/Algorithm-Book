import itertools

arr = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
permutations = list(set(itertools.permutations(arr)))
permutations.sort(reverse=True)
for i in range(len(permutations)):
    if i < 26:
        print(i+1, ':', permutations[i])
