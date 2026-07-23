import numpy as np

data = np.array([20, 40, 60, 80, 100])
norm = (data - np.min(data)) / (np.max(data) - np.min(data))
print(norm)