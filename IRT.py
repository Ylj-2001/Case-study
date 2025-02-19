import numpy as np
import csv
import pandas as pd
from scipy.optimize import fsolve

# 修正好格子点数据
data0 = pd.read_csv('la100.csv',header=None)
data0 = np.array(data0)

def generate_samples(num_samples):
    samples = []
    while len(samples) < num_samples:
        u1 = data0[len(samples),0]
        u2 = data0[len(samples),1]
        # 计算x12的值
        x1 = (1/(2.5))*u1
        # 计算x2的值
        x2 = (1/3)*u2*((1-4*((x1)**2))**(0.5))
        # 使用约束条件计算x3的值
        x3 = (1 - 4*x1**(2) -9* x2**(2))**(0.5) 
        samples.append((x1, x2, x3))
    
    return samples

# 生成数据点
data102I_points = generate_samples(100)
print(data102I_points)

# 写入CSV文件
with open('data102I_points.csv', 'w', newline='') as csvfile:
    fieldnames = ['x1', 'x2', 'x3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for point in data102I_points:
        writer.writerow({'x1': point[0], 'x2': point[1], 'x3': point[2]})