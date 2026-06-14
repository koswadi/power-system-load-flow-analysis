from ybus_builder import YBusBuilder
from gauss_seidel import GaussSeidelSolver
from newton_raphson import NewtonRaphsonSolver
from power_flow import PowerFlowCalculator
from transmission_losses import TransmissionLossCalculator

import numpy as np


def main():

    print("=" * 50)
    print("POWER SYSTEM LOAD FLOW ANALYSIS")
    print("=" * 50)

    ybus = YBusBuilder(
        "data/sample_line_data.csv"
    ).build()

    print("\nY-Bus Matrix:")
    print(ybus)

    gs_solver = GaussSeidelSolver(ybus)

    voltages, iterations = gs_solver.solve()

    print("\nGauss-Seidel Results")
    print("--------------------")

    for i, v in enumerate(voltages, start=1):
        print(
            f"Bus {i}: "
            f"{abs(v):.4f} p.u."
        )

    print(f"\nIterations: {iterations}")

    power_flow = PowerFlowCalculator(
        ybus,
        voltages
    )

    results = power_flow.calculate()

    losses = TransmissionLossCalculator(
        results["powers"]
    ).calculate()

    print(
        f"\nEstimated Transmission Loss: "
        f"{losses:.4f} MW"
    )

    nr_solver = NewtonRaphsonSolver(ybus)

    v_nr, angle_nr, nr_iter = nr_solver.solve()

    print("\nNewton-Raphson Results")
    print("----------------------")

    print(
        f"Converged in {nr_iter} iterations"
    )

    print("\nAnalysis Completed")


if __name__ == "__main__":
    main()