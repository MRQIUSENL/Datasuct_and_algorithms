import random
L = [random.randint(1, 100) for _ in range(100)]
print("原列表:\n", L, "\n 整除过滤列表：\n", [i for i in L if i % 3 != 0])