#数组times包含有结点u->v的权重w，朴素缔结特斯拉
def networkDelayTime(self, times, n, k):
    g = [[float('inf')] * n for i in range(n)] #将图的数组载入数组
    for u, v, w in times:
        g[u - 1][v - 1] = w
    dist = [float('inf')] * n #定义距离数组
    dist[k - 1] = 0#定义起始结点距离为0
    vis = set()
    for i in range(n):
        t = -1
        for j in range(n):
            if j not in vis and (t == -1 or dist[t] > dist[j]):
                t = j
        vis.add(t)#记录已经访问过的点
        for u in range(n):
            dist[u] = min(dist[u], dist[t] + g[t][u])#更新距离数组，利用假设中转结点和直线距离去比较