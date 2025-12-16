# 1 2
# 1 3
# 2 3
# 3 4
# 3 5
# 2 6
n = int(input())
# 列表只能靠索引去找边，使用字典更合适
unorderd_tu = {}
for i in range(n):
    u, v = input().split()
    if u not in unorderd_tu:
        unorderd_tu[u] = []
    unorderd_tu[u].append(v)
    if v not in unorderd_tu:
        unorderd_tu[v] = []
    unorderd_tu[u].append(v)
    
ordered_tu={}
for i in range(n):
    u,v = input()
    if u not in ordered_tu:
        ordered_tu[u] =[]
    ordered_tu[u].append(v)

