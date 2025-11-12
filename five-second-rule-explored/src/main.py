import math
from dataclasses import dataclass
from typing import Optional, Union

Number = Union[float, int]

@dataclass
class TransferParams:
    # Transfer efficiency components and approach rate
    alpha: float = 0.5    # baseline stickiness
    moisture: float = 0.8 # 0..1, wetter transfers more
    surface: float = 0.5  # 0..1, rougher holds more
    beta: float = 0.8     # per second, how quickly you approach
                          # the ceiling

    @property
    def k(self) -> float:
        return self.alpha * self.moisture * self.surface

def germs(
    t: Number,
    rho: float,
    A: float,
    p: TransferParams = TransferParams()
) -> float:
    """
    Expected bacteria on food after t seconds.
    G(t) = rho * A * p.k * (1 - exp(-p.beta * t))
    """
    return (
        rho * A * p.k
        * (1 - math.exp(-p.beta * float(t)))
    )

def safe_time(
    L: float,
    rho: float,
    A: float,
    p: TransferParams = TransferParams()
) -> float:
    """
    Time until bacteria count first reaches threshold L.
    Returns math.inf if L is above the asymptote.
    """
    gmax = rho * A * p.k
    if L >= gmax:
        return math.inf
    return -math.log(1 - L / gmax) / p.beta

def plot_results(
    rho: float,
    A: float,
    p: TransferParams = TransferParams(),
    t_max: float = 10.0,
    L: Optional[float] = None
) -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    times = np.linspace(0, t_max, 200)
    values = [germs(t, rho, A, p) for t in times]

    plt.plot(times, values, label="G(t): germs on food")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Bacteria count")
    plt.title("Germ transfer to food over time")

    if L is not None:
        plt.axhline(
            L, color="red", linestyle="--", label=f"Threshold L={L}"
        )
        t_star = safe_time(L, rho, A, p)
        if math.isfinite(t_star):
            plt.axvline(
                t_star,
                color="red",
                linestyle=":",
                label=f"t* ≈ {t_star:.2f}s"
            )

    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    # Scenario settings
    rho = 100.0  # germs per cm^2 on the floor
    A = 4.0      # cm^2 of food touching the floor
    # tweak alpha, moisture, surface, beta as needed
    p = TransferParams()

    # Quick checks
    for t in (1, 5, 10):
        print(f"Germs after {t}s: {germs(t, rho, A, p):.2f}")

    L = 50.0
    t_star = safe_time(L, rho, A, p)
    safe_msg = (
        f"Safe time for L={L} germs: "
        f"{'never' if math.isinf(t_star) else f'{t_star:.2f}s'}"
    )
    print(safe_msg)

    # Visual
    plot_results(rho, A, p, t_max=10.0, L=L)

if __name__ == "__main__":
    main()
