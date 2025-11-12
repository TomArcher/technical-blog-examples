from __future__ import annotations
import numpy as np
from typing import Dict, Iterable, Tuple

MPH_TO_FTS = 1.4666666667

def mph_to_fts(mph: np.ndarray | float) -> np.ndarray:
    """Convert mph to ft/s. Accepts scalar or arraylike."""
    v = np.asarray(mph, dtype=float)
    return v * MPH_TO_FTS

def required_headway_instant_stop(
    v_mph: np.ndarray | float,
    tau: float = 1.5,
    a_f: float = 19.7
) -> np.ndarray:
    """
    Minimum time headway (seconds) to avoid collision if the 
    lead car stops instantly. h = tau + v/(2*a_f), where v is 
    initial speed in ft/s and a_f is follower decel in ft/s^2.
    Accepts scalar or arraylike mph and returns ndarray.
    """
    v_fts = mph_to_fts(v_mph)
    return tau + v_fts / (2.0 * a_f)

def print_headway_table(
    speeds_mph: Iterable[float],
    conditions: Dict[str, float],
    tau: float = 1.5
) -> None:
    """
    Print a simple table of required headway by condition 
    and speed.
    """
    speeds = list(speeds_mph)
    for name, a_f in conditions.items():
        print(f"\n{name} pavement:")
        for mph in speeds:
            h = required_headway_instant_stop(mph, tau=tau, a_f=a_f)
            print(f"  {mph:>3.0f} mph \u2192 {h:.2f} s")

def plot_headway_curves(
    speeds_mph: Iterable[float],
    conditions: Dict[str, Tuple[float, str]],
    tau: float = 1.5,
    rule_sec: float = 3.0,
    title: str = (
        "Safe Following Time if the Lead Car Stops Instantly"
    ),
) -> None:
    """
    Plot headway vs speed for multiple road conditions.

    conditions: dict like
    {"Dry": (19.7, "green"), "Wet": (13.1, "orange"), ...}
    speeds_mph: iterable of speeds in mph
    """
    import matplotlib.pyplot as plt

    speeds = np.asarray(list(speeds_mph), dtype=float)

    plt.figure(figsize=(8, 4))
    for name, (a_f, color) in conditions.items():
        h = required_headway_instant_stop(
            speeds, tau=tau, a_f=a_f
        )
        plt.plot(speeds, h, "o-", color=color, label=name)

    plt.axhline(
        rule_sec,
        color="black",
        ls="--",
        label=f"{rule_sec:.0f}-second rule",
    )
    plt.xlabel("Speed (mph)")
    plt.ylabel("Minimum headway (seconds)")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main() -> None:
    # Headway at a few representative speeds
    speeds_table = [30, 50, 70]

    # Deceleration assumptions in ft/s^2
    # Print table uses simple dict[name] = a_f
    table_conditions = {
        "Dry": 19.7,
        "Wet": 13.1,
        "Icy": 6.6,
    }
    print_headway_table(speeds_table, table_conditions, tau=1.5)

    # Smoother range for plotting
    speeds_plot = np.linspace(20, 80, 13)

    # Plotting uses dict[name] = (a_f, color)
    plot_conditions = {
        "Dry": (19.7, "green"),
        "Wet": (13.1, "orange"),
        "Icy": (6.6, "blue"),
    }
    plot_headway_curves(speeds_plot, plot_conditions, tau=1.5, rule_sec=3.0)

if __name__ == "__main__":
    main()
