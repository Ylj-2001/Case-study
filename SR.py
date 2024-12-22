##随机表示法（SR）
import numpy as np

def uniform_sphere_samples(n_samples, dimension):
    samples = np.random.normal(0, 1, (n_samples, dimension))
    samples /= np.linalg.norm(samples, axis=1)[:, np.newaxis]
    return samples

def transform_to_hyperplane(samples, coefficients, constant):
    dimension = samples.shape[1]
    transformed_samples = samples.copy()
    
    for i in range(samples.shape[0]):
        sample = samples[i]
        scale = (constant - np.dot(coefficients[:-1], sample[:-1])) / coefficients[-1]
        transformed_samples[i] = sample + scale * coefficients / np.linalg.norm(coefficients)
    
    return transformed_samples

n_samples = 1000
dimension = 3
coefficients = np.array([1, 1, 1])
constant = 1

sphere_samples = uniform_sphere_samples(n_samples, dimension)
hyperplane_samples = transform_to_hyperplane(sphere_samples, coefficients, constant)
