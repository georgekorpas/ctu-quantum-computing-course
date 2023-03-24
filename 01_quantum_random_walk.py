
import numpy as np
import matplotlib.pyplot as plt

# Define the coin operator C that implements the coin toss and can be applied to each state.
def coin_operator(pos_state):
    C = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)],
                  [1 / np.sqrt(2), -1 / np.sqrt(2)]])
    return np.dot(pos_state, C)

# Define the shift operator which shifts the position states based on their coin states.
def shift_operator(pos_state):
    new_pos_state = np.zeros(pos_state.shape, dtype=np.complex128)
    for i in range(pos_state.shape[0]):
        new_pos_state[i] = (pos_state[i - 1, 0], pos_state[(i + 1) % pos_state.shape[0], 1])
    return new_pos_state

# Define the quantum random walk for a given number of steps.
def quantum_random_walk(steps, size=100):
    pos_state = np.zeros((size, 2), dtype=np.complex128)
    pos_state[size // 2] = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)], dtype=np.complex128)
    for _ in range(steps):
        pos_state = coin_operator(pos_state)
        pos_state = shift_operator(pos_state)
    return pos_state

# Define the plot_probability_distribution function, which plots the probability distribution of the position states.
def plot_probability_distribution(pos_state):
    prob_distribution = np.sum(np.abs(pos_state) ** 2, axis=1)
    plt.plot(prob_distribution)
    plt.xlabel('Position')
    plt.ylabel('Probability')
    plt.title('Quantum Random Walk Probability Distribution')
    plt.show()

if __name__ == "__main__":
    steps = 50
    size = 100
    pos_state = quantum_random_walk(steps, size)
    plot_probability_distribution(pos_state)

# Save the figure for future use
# plt.savefig('quantum_random_walk.pdf', dpi=300)