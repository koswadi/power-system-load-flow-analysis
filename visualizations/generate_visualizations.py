print("Script started...")
import os
import matplotlib.pyplot as plt

print("Current directory:", os.getcwd())
print("Script location:", os.path.abspath(__file__))


# Membuat folder visualizations jika belum ada
os.makedirs("visualizations", exist_ok=True)

# =====================================================
# Voltage Profile
# =====================================================

voltages = [1.05, 1.02, 1.01, 0.99, 0.975]

plt.figure(figsize=(8, 4))
plt.plot(range(1, 6), voltages, marker="o")
plt.xlabel("Bus Number")
plt.ylabel("Voltage (p.u.)")
plt.title("Voltage Profile")
plt.grid(True)

output_file = os.path.abspath("voltage_profile.png")
print("Saving to:", output_file)

plt.savefig(output_file, dpi=300)
plt.close()

# =====================================================
# Transmission Losses
# =====================================================

lines = ["1-2", "1-3", "2-3", "2-4", "2-5", "3-4", "4-5"]
losses = [0.30, 0.45, 0.25, 0.28, 0.35, 0.20, 0.30]

plt.figure(figsize=(8, 4))
plt.bar(lines, losses)
plt.xlabel("Transmission Line")
plt.ylabel("Loss (MW)")
plt.title("Transmission Losses")

plt.savefig("transmission_losses.png", dpi=300)
plt.close()

# =====================================================
# Convergence Curve
# =====================================================

iterations = [1, 2, 3, 4, 5, 6]
mismatch = [0.12, 0.05, 0.018, 0.006, 0.0015, 0.0001]

plt.figure(figsize=(8, 4))
plt.plot(iterations, mismatch, marker="o")
plt.xlabel("Iteration")
plt.ylabel("Power Mismatch")
plt.title("Convergence Curve")
plt.grid(True)

plt.savefig("convergence_curve.png", dpi=300)
plt.close()

# =====================================================
# Bus Angle Profile
# =====================================================

angles = [0, -2.5, -4.2, -3.1, -5.0]

plt.figure(figsize=(8, 4))
plt.bar(range(1, 6), angles)

plt.xlabel("Bus Number")
plt.ylabel("Angle (Degrees)")
plt.title("Bus Angle Profile")

plt.savefig("bus_angle_profile.png", dpi=300)
plt.close()

# =====================================================
# Power Flow Results
# =====================================================

power_flow = [120, 95, 85, 70, 60]

plt.figure(figsize=(8, 4))
plt.plot(range(1, 6), power_flow, marker="o")

plt.xlabel("Bus Number")
plt.ylabel("Power (MW)")
plt.title("Power Flow Results")
plt.grid(True)

plt.savefig("power_flow_results.png", dpi=300)
plt.close()

print("All visualizations generated successfully.")
