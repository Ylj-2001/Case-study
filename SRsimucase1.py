import numpy as np
import csv

def generate_samples(num_samples):
    samples = []
    while len(samples) < num_samples:
        # 随机生成x1和x2的值
        x1 = np.random.uniform(0, 1)
        x2 = np.random.uniform(0, 1)
        
        # 使用约束条件计算x3的值
        x3 = 2*x1 + 0.5*x2 - 1
        
        # 检查x3是否在有效范围内
        if 0 < x3 < 1:
            samples.append((x1, x2, x3))
    
    return samples

# 生成数据点
data9S_points = generate_samples(90)
print(data9S_points)

# 写入CSV文件
with open('data9S_points.csv', 'w', newline='') as csvfile:
    fieldnames = ['x1', 'x2', 'x3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for point in data9S_points:
        writer.writerow({'x1': point[0], 'x2': point[1], 'x3': point[2]})