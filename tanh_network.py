import math
import random

def tanh(x):
    return math.tanh(x)


weights_input_hidden = [[random.uniform(-0.5, 0.5) for _ in range(2)] for _ in range(2)]
bias_hidden = [0.5, 0.5]
weights_hidden_output = [random.uniform(-0.5, 0.5) for _ in range(2)]
bias_output = 0.7

inputs = [random.uniform(-1, 1) for _ in range(2)]

hidden_layer = [tanh(sum(weights_input_hidden[i][j] * inputs[j] for j in range(2)) + bias_hidden[i]) for i in range(2)]

output = tanh(sum(weights_hidden_output[i] * hidden_layer[i] for i in range(2)) + bias_output)

print(f"Input: x1={inputs[0]:.3f}, x2={inputs[1]:.3f}")
print(f"Hidden Layer: h1={hidden_layer[0]:.3f}, h2={hidden_layer[1]:.3f}")
print(f"Output: O= {output:.3f}")
