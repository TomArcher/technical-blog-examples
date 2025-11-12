import numpy as np
import matplotlib.pyplot as plt

# Define a simple loss function: f(x) = (x - 3)^2 + 2
def loss(x):
    return (x - 3)**2 + 2

def gradient(x):
    return 2 * (x - 3)

# Gradient descent
x = 0  # Start far from the minimum
learning_rate = 0.1
history = [x]

for _ in range(20):
    grad = gradient(x)
    x = x - learning_rate * grad
    history.append(x)

# Visualize
x_vals = np.linspace(-1, 7, 100)
plt.plot(x_vals, loss(x_vals), 'b-', label='Loss Function')
plt.plot(history, [loss(x) for x in history], 'ro-', 
          label='Learning Path')
plt.xlabel('Parameter Value')
plt.ylabel('Loss')
plt.legend()
plt.show()