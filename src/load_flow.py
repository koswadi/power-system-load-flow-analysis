from ybus_matrix import build_ybus
from gauss_seidel import run_gauss_seidel
from newton_raphson import run_newton_raphson
from loss_calculation import calculate_losses

print("=" * 50)
print("POWER SYSTEM LOAD FLOW ANALYSIS")
print("=" * 50)

print("\nY-BUS MATRIX")
print(build_ybus())

print("\nGAUSS-SEIDEL RESULTS")
print(run_gauss_seidel())

print("\nNEWTON-RAPHSON RESULTS")
print(run_newton_raphson())

losses, total = calculate_losses()

print("\nTRANSMISSION LOSSES")
print(losses)

print(f"\nTOTAL LOSS = {total:.2f} MW")