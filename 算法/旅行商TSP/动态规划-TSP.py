def tsp_dp_with_path(graph):
    n = len(graph)
    # 初始化 dp 表，大小为 2^n * n
    dp = [[float('inf')] * n for _ in range(1 << n)]
    # 初始化 parent 表，用于记录路径
    parent = [[-1] * n for _ in range(1 << n)]
    # 初始条件：从起点出发，不需要移动
    dp[1][0] = 0

    # 遍历所有可能的 mask
    for mask in range(1 << n):
        for u in range(n):
            # 如果 u 不在 mask 中，跳过
            if not (mask & (1 << u)):
                continue
            # 遍历所有未访问过的节点 v
            for v in range(n):
                if mask & (1 << v):
                    continue
                # 更新 dp[mask | (1 << v)][v] 和 parent[mask | (1 << v)][v]
                if dp[mask | (1 << v)][v] > dp[mask][u] + graph[u][v]:
                    dp[mask | (1 << v)][v] = dp[mask][u] + graph[u][v]
                    parent[mask | (1 << v)][v] = u

    # 找到最小权重的路径
    final_mask = (1 << n) - 1
    min_cost = float('inf')
    last_node = -1
    for u in range(1, n):
        if dp[final_mask][u] + graph[u][0] < min_cost:
            min_cost = dp[final_mask][u] + graph[u][0]
            last_node = u

    # 回溯路径
    path = []
    mask = final_mask
    u = last_node
    while u != -1:
        path.append(u + 1)  # 转换为 1-based 节点编号
        next_u = parent[mask][u]
        mask ^= (1 << u)  # 移除当前节点
        u = next_u

    # 添加起点
    path.append(1)
    # 反转路径，使其从起点开始
    path = path[::-1]

    return min_cost, path

# 示例图
graph = [
    [0, 7, 5, 3, 6],  # 节点 1
    [7, 0, 8, 2, 4],  # 节点 2
    [5, 8, 0, 9, 2],  # 节点 3
    [3, 2, 9, 0, 5],  # 节点 4
    [6, 4, 2, 5, 0]   # 节点 5
]

# 计算最小权重和路径
min_cost, path = tsp_dp_with_path(graph)
print(f"最小权重为: {min_cost}")
print(f"游历节点路径为: {' -> '.join(map(str, path))}")