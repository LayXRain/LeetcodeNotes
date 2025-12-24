from collections import defaultdict
n = int(input())
circles = []
for _ in range(n):
    x, y, r = map(int, input().split())
    circles.append((x, y, r, r * r))
circles.sort(key=lambda c: -c[3])
neighbors = defaultdict(list)
for i in range(n):
    x1, y1, r1, _ = circles[i]
    for j in range(i + 1, n):
        x2, y2, r2, _ = circles[j]
        dx = x1 - x2
        dy = y1 - y2
        if dx * dx + dy * dy < (r1 + r2) * (r1 + r2):
            neighbors[i].append(j)
            neighbors[j].append(i)
suffix_sum = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + circles[i][3]
max_area = 0
ban = [False] * n 
def dfs(pos, current_sum):
    global max_area
    if current_sum > max_area:
        max_area = current_sum
    if pos >= n or current_sum + suffix_sum[pos] <= max_area:
        return
    dfs(pos + 1, current_sum)
    if not ban[pos]:
        conflict = []
        for j in neighbors[pos]:
            if not ban[j]:
                ban[j] = True
                conflict.append(j)
        dfs(pos + 1, current_sum + circles[pos][3])
        for j in conflict:
            ban[j] = False
dfs(0, 0)
print(max_area)