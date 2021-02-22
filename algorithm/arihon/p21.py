import itertools

n = int(input())
a = map(int, input().split())

combinations = itertools.combinations(a, 3)

answer = 0

for combination in combinations:
    if combination[0] + combination[1] > combination[2] and combination[1] + combination[2] > combination[0] and combination[2] + combination[0] > combination[1]:
        perimeter = combination[0] + combination[1] + combination[2]
        if answer < perimeter:
            answer = perimeter

print(answer)
