import csv
import numpy as np

def generate_samples(num_samples):
    samples = []
    while len(samples) < num_samples:
        # 从[0,1]^3中生成样本
        x1, x2, x3 = np.random.uniform(0, 1, 3)
        
        # 检查约束条件
        if np.isclose(2*x1 + 0.5*x2 - x3, 1, atol=1e-5) and all(0 < x < 1 for x in [x1, x2, x3]):
            samples.append((x1, x2, x3))
    
    return samples

# 生成数据点
data9A_points = generate_samples(90)
print(data9A_points)

# 写入CSV文件
with open('data9A_points.csv', 'w', newline='') as csvfile:
    fieldnames = ['x1', 'x2', 'x3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for point in data9A_points:
        writer.writerow({'x1': point[0], 'x2': point[1], 'x3': point[2]})