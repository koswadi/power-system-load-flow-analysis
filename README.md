# Power System Load Flow Analysis Using Python

## Overview

This project demonstrates the implementation of power system load flow analysis using Python.

The objective is to calculate:

- Bus voltage magnitudes
- Voltage angles
- Active power flow
- Reactive power flow
- Transmission losses

The project includes two classical numerical approaches:

1. Gauss-Seidel Method
2. Newton-Raphson Method

## Engineering Concepts

### Bus Types

- Slack Bus
- PQ Bus
- PV Bus

### Power Flow Analysis

Power flow analysis is used to determine the steady-state operating condition of an electrical power system.

### Y-Bus Matrix

The bus admittance matrix represents network connectivity and electrical characteristics.

## Numerical Methods

### Gauss-Seidel

Advantages:

- Easy implementation
- Low memory requirement

Limitations:

- Slow convergence

### Newton-Raphson

Advantages:

- Fast convergence
- High accuracy

Limitations:

- More computational complexity

## Repository Structure

```text
power-system-load-flow-analysis/

├── data/
├── src/
├── visualizations/
├── reports/
└── examples/
```

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib

## Sample Results

Voltage Profile:

Bus 1 : 1.050 p.u.
Bus 2 : 1.020 p.u.
Bus 3 : 1.010 p.u.
Bus 4 : 0.990 p.u.
Bus 5 : 0.975 p.u.

Total Transmission Loss:

2.13 MW

## Author

Electrical Engineering Portfolio Project