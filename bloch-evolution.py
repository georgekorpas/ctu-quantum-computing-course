import numpy as np
from qutip import basis, Bloch, sigmax, sigmay, sigmaz, sesolve
from qutip.solver import Options


class QuantumEvolution:
    def __init__(self, hamiltonian_func, initial_state, time_params, options=None):
        self.hamiltonian_func = hamiltonian_func
        self.psi0 = initial_state
        self.time_params = time_params
        self.options = options if options else Options()
        self.result = None

    def run_simulation(self):
        self.result = sesolve(self.hamiltonian_func, self.psi0, self.time_params['times'],
                              [sigmax(), sigmay(), sigmaz()], args=self.time_params, options=self.options)

    def visualize(self, filename=None):
        bloch = Bloch()
        bloch.add_points(self.result.expect, meth='l')
        bloch.add_states(self.psi0)
        bloch.add_states(self.result.states[-1])

        if filename:
            bloch.save(filename)

        bloch.show()


if __name__ == '__main__':
    psi0 = 1 / np.sqrt(2) * (basis(2, 0) + basis(2, 1))
    T = 100
    times = np.linspace(0, T, 100)
    time_params = {'T': T, 'times': times}
    options = Options(store_states=True)

    # Define the Hamiltonian using a lambda function
    hamiltonian_func = lambda t, args: (-(1 - t / args['T']) / 2) * sigmax() + (-(t / args['T']) / 2) * sigmaz()

    qe = QuantumEvolution(hamiltonian_func, psi0, time_params, options)
    qe.run_simulation()
    qe.visualize('bloch-evolution.pdf')
