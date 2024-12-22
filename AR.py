##接受拒绝方法（AR）
import numpy as np
import matplotlib.pyplot as plt

def target_distribution(x):
    # 目标分布（例如标准正态分布）
    return np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)

def candidate_distribution(x):
    # 候选分布（例如均匀分布在[-10, 10]）
    return 1/20 if -10 <= x <= 10 else 0

def sample_candidate():
    # 从候选分布中生成样本（例如均匀分布在[-10, 10]）
    return np.random.uniform(-10, 10)

def accept_reject_sampling(num_samples, M):
    samples = []
    while len(samples) < num_samples:
        x_star = sample_candidate()
        u = np.random.uniform(0, 1)
        if u <= target_distribution(x_star) / (M * candidate_distribution(x_star)):
            samples.append(x_star)
    return np.array(samples)

# 参数设置
num_samples = 1000
M = 2.5  # 选择合适的比例常数

# 生成样本
samples = accept_reject_sampling(num_samples, M)

# 绘制生成的样本直方图与目标分布对比
x = np.linspace(-5, 5, 1000)
plt.hist(samples, bins=30, density=True, alpha=0.5, label='Samples')
plt.plot(x, target_distribution(x), label='Target Distribution')
plt.legend()
plt.show()
