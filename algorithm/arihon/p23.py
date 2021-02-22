L = int(input())
n = int(input())
x = map(int, input().split())

central = L / 2

minimums = []
maximums = []

for ant in x:
    if ant >= central:
        minimum = L - ant
        maximum = ant
    else:
        maximum = L - ant
        minimum = ant

    minimums.append(minimum)
    maximums.append(maximum)

print(max(minimums), max(maximums))
