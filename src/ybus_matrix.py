import numpy as np

def build_ybus():
    """
    Example 5-bus Y-Bus matrix
    """

    ybus = np.array([
        [20-50j, -10+25j, -5+15j, -3+5j, -2+5j],
        [-10+25j, 25-60j, -8+20j, -4+10j, -3+5j],
        [-5+15j, -8+20j, 20-50j, -5+10j, -2+5j],
        [-3+5j, -4+10j, -5+10j, 15-35j, -3+10j],
        [-2+5j, -3+5j, -2+5j, -3+10j, 10-25j]
    ])

    return ybus


if __name__ == "__main__":
    print(build_ybus())