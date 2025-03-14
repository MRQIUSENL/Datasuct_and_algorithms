#迪杰斯特拉算法

import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n  # 初始化距离数组
    dist[start] = 0            # 起点到自身的距离为 0
    heap = [(0, start)]        # 优先队列，存储 (距离, 节点)

    while heap:
        current_dist, u = heapq.heappop(heap)  # 取出当前距离最小的节点
        if current_dist > dist[u]:  # 如果当前距离不是最短，跳过
            continue

        # 遍历邻居节点
        for v, weight in enumerate(graph[u]):
            if weight == 0:  # 如果没有边，跳过
                continue
            if dist[u] + weight < dist[v]:  # 松弛操作
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))  # 将邻居节点加入优先队列

    return dist

# 测试
graph = [
    [0, 7, 5, 3, 6],  # 节点 1
    [7, 0, 8, 2, 4],  # 节点 2
    [5, 8, 0, 9, 2],  # 节点 3
    [3, 2, 9, 0, 5],  # 节点 4
    [6, 4, 2, 5, 0]   # 节点 5
]
start = 0  # 起点为节点 1
distances = dijkstra(graph, start)
print("从节点 1 到各节点的最短路径长度:", distances)