import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[1, 1],
              [1, 0],
              [0, 1],
              [0, 0]])

y = np.array([[0],
              [1],
              [1],
              [0]])

# Inicialização de pesos aleatórios
input_neurons = 2
hidden_neurons = 3
output_neurons = 1

np.random.seed(1)

weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))

learning_rate = 0.1

epochs = 10000

for epoch in range(epochs):
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    predicted_output = sigmoid(output_layer_input)

    error = y - predicted_output

    # Backpropagation
    output_error = error * sigmoid_derivative(predicted_output)
    hidden_layer_error = output_error.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_layer_output)

    # Atualização de pesos
    weights_hidden_output += hidden_layer_output.T.dot(output_error) * learning_rate
    weights_input_hidden += X.T.dot(hidden_layer_error) * learning_rate

# Teste da rede treinada
test_input = np.array([[1, 1]])
hidden_layer_input = np.dot(test_input, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
predicted_output = sigmoid(output_layer_input)

print("Saída para [1, 1]:", predicted_output)