# ctu-quantum-computing-course

<img src="ctu.png" alt="alt text" width="200" align="right">

This repository contains the code examples and exercises for my lectures on quantum computing at the Czech Technical University in Prague. 
The course information is here: https://intranet.fel.cvut.cz/cz/education/bk/predmety/74/72/p7472006

The code is written in Python/Julia and covers various topics such as quantum random walks, quantum annealing, variational quantum algorithms and aspects of the applications of quantum computing in finance.

## What does each file do?

01. File [01_quantum_random_walk.py ](01_quantum_random_walk.py ) is an implementation of the quantum random walk on the line using only numpy.
02. File [02_classical_random_walk_probabilities.ipynb](02_classical_random_walk_probabilities.ipynb) shows how the probability to find a classical walker at a fixed vertex converges to 1 with O(N) iterations where N is the number of vertices (of a complete, symmetric graph).
![Convergence of CRW](figures/random_walk_complete.pdf)
