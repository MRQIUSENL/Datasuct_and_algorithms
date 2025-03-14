import heapq

class Node:
    def __init__(self, number, level, path, length, lb):
        self.number = number  # 编号(节点)
        self.level = level    # 层级(已经访问的城市数量)
        self.path = path      # 已访问节点路径
        self.length = length  # 当前路径的长度
        self.lb = lb          # 下界

    def __lt__(self, other):
        return self.lb < other.lb  # 优先扩展下界更小的节点

def calculate_lb(graph, path):
    n = len(graph)
    visited = set(path)
    lb = 0

    # 计算已访问路径的实际长度
    for i in range(len(path) - 1):
        lb += graph[path[i]][path[i + 1]]

    # 计算未访问城市的最小边权
    for i in range(n):
        if i not in visited:
            min_edge = min(graph[i][j] for j in range(n) if j != i)
            lb += min_edge

    return lb

def tsp_branch_bound(graph):
    n = len(graph)
    heap = []

    # 计算初始下界（从起点开始）
    lb = calculate_lb(graph, [0])
    root = Node(0, 1, [0], 0, lb)
    heapq.heappush(heap, root)

    best_path, best_length = None, float("inf")

    while heap:
        cnode = heapq.heappop(heap)
        print(cnode.path,cnode.length,cnode.lb)
        if cnode.level == n:  # 已访问所有城市
            final_length = cnode.length + graph[cnode.path[-1]][0]  # 回到起点
            if final_length < best_length:
                best_path = [p + 1 for p in cnode.path] + [1]  # 转换回 1-based
                best_length = final_length
            continue

        # 遍历未访问的城市
        for next_city in range(n):
            print(next_city)
            if next_city not in cnode.path:
                new_path = cnode.path + [next_city]
                new_length = cnode.length + graph[cnode.path[-1]][next_city]
                new_lb = calculate_lb(graph, new_path)
                print(new_path,new_length,new_lb)
                if new_lb < best_length:  # 剪枝条件
                    heapq.heappush(heap, Node(next_city, cnode.level + 1, new_path, new_length, new_lb))

    return best_path, best_length

# 测试
graph = [
    [0, 7, 5, 3, 6],  # 节点 1
    [7, 0, 8, 2, 4],  # 节点 2
    [5, 8, 0, 9, 2],  # 节点 3
    [3, 2, 9, 0, 5],  # 节点 4
    [6, 4, 2, 5, 0]   # 节点 5
]
best_path, best_length = tsp_branch_bound(graph)
print("最优路径:", best_path)
print("最优长度:", best_length)