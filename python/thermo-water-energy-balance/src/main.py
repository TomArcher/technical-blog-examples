import numpy as np

SIGMA = 5.670374419e-8
LV = 2.45e6
CP = 4186.0
RHO = 1000.0

def c_to_f(c):
    return c * 9.0/5.0 + 32.0

def f_to_c(f):
    return (f - 32.0) * 5.0/9.0

def c_to_k(C):
    return C + 273.15

def esat(C):
    return 610.94 * np.exp(17.625 * C / (C + 243.04))

def evap_flux(TwC, TairC, RH, wind, A, k_evap=2.5e-7, beta_wind=0.1):
    es = esat(TwC)
    ea = RH * esat(TairC)
    grad = np.maximum(es - ea, 0.0)
    return k_evap * A * grad * (1.0 + beta_wind * wind)

def q_solar(I, A, alpha):
    return alpha * A * I

def q_conv(TwK, TairK, A, h_c):
    return h_c * A * (TairK - TwK)

def q_rad(TwK, TskyK, A, epsilon):
    return epsilon * SIGMA * A * (TskyK**4 - TwK**4)

def q_evap(TwC, TairC, RH, wind, A, k_evap=2.5e-7, beta_wind=0.1):
    mdot = evap_flux(TwC, TairC, RH, wind, A, k_evap, beta_wind)
    return -LV * mdot

def diurnal(base, amp, hours, peak_shift=7.0):
    return base + amp * np.sin(2*np.pi * (hours - peak_shift) / 24.0)

def simulate(days=14, dt=3600.0, cover=False, seed_temp_C=24.0):
    # Geometry and bulk properties
    L, W, depth = 8.0, 4.0, 1.4  # meters
    A = L * W                    # surface area, m^2
    V = A * depth                # volume, m^3
    m = RHO * V                  # mass of water, kg
    C = m * CP                   # heat capacity, J/K

    # Surface exchange coefficients and optical properties
    alpha = 0.85                 # shortwave absorptivity (fraction)
    epsilon = 0.95               # longwave emissivity (dimensionless)
    h_c = 8.0                    # convective HTC, W/(m^2 K)
    k_evap = 2.5e-7              # bulk evaporation coefficient
    beta_wind = 0.1              # wind amplification factor

    # Apply cover effects: reduce evaporation and radiation, slightly 
    # lower convection
    if cover:
        k_evap = 0.3e-7          # strong reduction in evaporation losses
        epsilon = 0.75           # less longwave emission with cover
        h_c = 6.0                # modestly lower convection

    # Time discretization
    N = int(days * 24)           # number of hourly steps
    t = np.arange(N) * dt        # seconds
    hours = (t / 3600.0) % 24    # local hour of day for diurnal cycles

    # Synthetic diurnal weather forcing

    # hot mean with daily swing
    T_air_C = diurnal(37.0, 10.0, hours)                     

    # very dry afternoons
    RH = np.clip(diurnal(0.18, 0.10, hours), 0.05, 0.6)      

    # m/s
    wind = np.clip(diurnal(2.0, 1.5, hours), 0.2, 6.0)       

    # W/m^2
    I = np.maximum(0.0, 900.0 * np.sin(np.pi * (hours - 6.0) / 12.0))  

    # effective sky temp in Kelvin
    T_sky_K = c_to_k(T_air_C - 15.0)                         

    # State initialization
    Tw = np.zeros(N)
    Tw[0] = seed_temp_C

    # Time integration of energy balance
    for i in range(1, N):
        # Convert current water temp to Kelvin for radiation and 
        # convection calcs
        TwK = c_to_k(Tw[i-1])

        # Compute flux terms (Watts). Sign convention:
        # Positive adds heat to water. Negative removes heat 
        # from water.

        # shortwave absorbed
        Qs = q_solar(I[i-1], A, alpha)

        # convection with air
        Qc = q_conv(TwK, c_to_k(T_air_C[i-1]), A, h_c)

        # longwave net radiation
        Qr = q_rad(TwK, T_sky_K[i-1], A, epsilon)

        # evaporation
        Qe = q_evap(Tw[i-1], T_air_C[i-1], RH[i-1], 
                    wind[i-1], A, k_evap, beta_wind)

        # Net heat rate and temperature update

        # Watts
        Qnet = Qs + Qc + Qr + Qe

        # Celsius update
        Tw[i] = Tw[i-1] + (Qnet * dt) / C

    # Return time in hours and temperature in Celsius
    return t / 3600.0, Tw

def plot_runs_dual_axis(run_open, run_cov):
    import matplotlib.pyplot as plt

    hours_open, Tw_open_C, label_open = run_open
    hours_cov,  Tw_cov_C,  label_cov  = run_cov

    # Convert series to °F for the primary y-axis
    Tw_open_F = c_to_f(Tw_open_C)
    Tw_cov_F  = c_to_f(Tw_cov_C)

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(hours_open, Tw_open_F, label=label_open)
    ax.plot(hours_cov,  Tw_cov_F,  label=label_cov)

    ax.set_xlabel("Hour")
    ax.set_ylabel("Water temperature (°F)")
    ax.set_title("Two week warming under diurnal forcing")
    ax.legend(loc="best")

    # Secondary y-axis in °C mapped from the primary °F axis
    # functions = (forward, inverse) where forward maps primary->secondary
    # Primary is °F, secondary is °C, so use (f_to_c, c_to_f)
    ax2 = ax.secondary_yaxis('right', functions=(f_to_c, c_to_f))
    ax2.set_ylabel("Water temperature (°C)")

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Run two scenarios:
    # 1) Open surface without a cover
    # 2) Covered surface that reduces evaporation and radiation
    hours_open, Tw_open = simulate(days=14, cover=False)
    hours_cov,  Tw_cov  = simulate(days=14, cover=True)

    # Report total simulated hours and final temperatures in both units
    print(f"Simulated {len(hours_open)} hours")
    print(f"Final temperature open:  {c_to_f(Tw_open[-1]):.1f} °F ({Tw_open[-1]:.1f} °C)")
    print(f"Final temperature cover: {c_to_f(Tw_cov[-1]):.1f} °F ({Tw_cov[-1]:.1f} °C)")

    # Plot with Fahrenheit on the primary (left) y-axis and Celsius on the 
    # secondary (right) y-axis. Each tuple is (time_hours, temperature_C, label)
    plot_runs_dual_axis(
        (hours_open, Tw_open, "Open surface"),
        (hours_cov,  Tw_cov,  "With cover")
    )
