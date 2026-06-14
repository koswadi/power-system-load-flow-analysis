import pandas as pd
import numpy as np


class YBusBuilder:
    def __init__(self, line_data_path):
        self.line_data = pd.read_csv(line_data_path)

    def build(self):
        n_bus = int(
            max(
                self.line_data["From_Bus"].max(),
                self.line_data["To_Bus"].max()
            )
        )

        ybus = np.zeros((n_bus, n_bus), dtype=complex)

        for _, row in self.line_data.iterrows():
            fb = int(row["From_Bus"]) - 1
            tb = int(row["To_Bus"]) - 1

            r = row["Resistance_pu"]
            x = row["Reactance_pu"]

            z = complex(r, x)
            y = 1 / z

            ybus[fb, fb] += y
            ybus[tb, tb] += y

            ybus[fb, tb] -= y
            ybus[tb, fb] -= y

        return ybus