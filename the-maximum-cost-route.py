s1 = input().split()
n, m = int(s1[0]), int(s1[1])
map = []
map_with_cost = []
map_with_path = []

for i in range(n):
    map.append(input().split())
    map_with_cost.append([0] * m)
    map_with_path.append([""] * m)
    for j in range(m):
        map[i][j] = int(map[i][j])

map_with_cost[0][0] = map[0][0]

for i in range(1, m):
    map_with_cost[0][i] = map_with_cost[0][i-1] + map[0][i]
    map_with_path[0][i] = map_with_path[0][i-1] + "R"
for i in range(1, n):
    map_with_cost[i][0] = map_with_cost[i-1][0] + map[i][0]
    map_with_path[i][0] = map_with_path[i-1][0] + "D"

for i in range(1, n):
    for j in range(1, m):
        if map_with_cost[i-1][j] > map_with_cost[i][j-1]:
            map_with_path[i][j] = map_with_path[i-1][j] + "D"
            map_with_cost[i][j] = map_with_cost[i-1][j] + map[i][j]
        else:
            map_with_path[i][j] = map_with_path[i][j-1] + "R"
            map_with_cost[i][j] = map_with_cost[i][j-1] + map[i][j]

'''for i in range(n):
    print(f'{map[i]}    {map_with_cost[i]}    {map_with_path[i]}')'''

print(map_with_cost[n-1][m-1])
path = list(map_with_path[n-1][m-1])

print(*path)