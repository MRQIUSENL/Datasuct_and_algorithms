import heapq

class Node:
    def __init__(self,number,level,path,length,lb):
        self.number=number #编号(节点)
        self.level=level #层级(已经访问的城市数量,便于节点遍历程度计算，形成回路。)
        self.path=path #已访问节点路径eg：1->2->3->4->>>>n
        self.length=length #当前路径的长度
        self.lb=lb #下界 即：最小边权（乐观估计)
    
    def __lt__(self,other):
        return self.lb<other.lb
    

def calculate_lb(graph,path):
    lb=0
    n=len(graph)
    visited=set(path)
    
    for i in range (n):
        if i in visited:
            continue

        min_edge = min(graph[i][j] for j in range (n) if j!=i)
        lb+=min_edge
    return lb//2

def tsp_branch_bound(graph): #tbb
    n = len(graph)
    heap = []
    
    # 计算初始下界（从起点开始）
    lb = calculate_lb(graph, [0])
    root = Node(0, 1, [0], 0, lb)
    heapq.heappush(heap, root)

    best_path, best_length = None, float("inf")

    while heap:
        cnode = heapq.heappop(heap)

        if cnode.level == n:  # 已访问所有城市
            final_length = cnode.length + graph[cnode.path[-1]][0]  # 回到起点
            if final_length < best_length:
                best_path = [p + 1 for p in cnode.path] + [1]  # 转换回 1-based
                best_length = final_length
            continue

        # 遍历未访问的城市
        for next_city in range(n):
            if next_city not in cnode.path:
                new_path = cnode.path + [next_city]
                new_length = cnode.length + graph[cnode.path[-1]][next_city]
                new_lb = calculate_lb(graph, new_path)

                if new_lb < best_length:  # 剪枝条件
                    heapq.heappush(heap, Node(next_city, cnode.level + 1, new_path, new_length, new_lb))

    return best_path, best_length
