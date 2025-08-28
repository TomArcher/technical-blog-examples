from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpBinary

def solve_meeting_diet(meetings, time_budget, energy_budget):
    # Decision variables
    x = {
        m["name"]: LpVariable(cat=LpBinary, name=f"x_{i}")
        for i, m in enumerate(meetings)
    }

    # Model
    model = LpProblem("MeetingDiet", LpMaximize)
    model += lpSum(m["value"] * x[m["name"]] for m in meetings)

    # Constraints
    model += lpSum(
        m["time"] * x[m["name"]] for m in meetings
    ) <= time_budget

    model += lpSum(
        m["energy"] * x[m["name"]] for m in meetings
    ) <= energy_budget

    # Solve
    model.solve()

    # Gather results
    attend = [m for m in meetings if x[m["name"]].value() == 1]
    chosen_names = {m["name"] for m in attend}
    total_value = sum(m["value"] for m in attend)
    total_time = sum(m["time"] for m in attend)
    total_energy = sum(m["energy"] for m in attend)

    return attend, chosen_names, total_value, total_time, total_energy

def plot_meetings(
    meetings,
    chosen_names,
    title="Meeting Value Efficiency (Attend vs Decline)",
):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch

    # Compute value-per-minute ratios (avoid div-by-zero)
    names   = [m["name"] for m in meetings]
    ratios = [
        (m["value"] / m["time"]) if m["time"] else 0.0
        for m in meetings
    ]

    status = [
        "Attend" if m["name"] in chosen_names else "Decline"
        for m in meetings
    ]

    # Sort by ratio (desc) for a cleaner story
    order = sorted(
        range(len(meetings)),
        key=lambda i: ratios[i],
        reverse=True
    )
    names_sorted  = [names[i] for i in order]
    ratios_sorted = [ratios[i] for i in order]
    status_sorted = [status[i] for i in order]

    # Color map
    colors = {"Attend": "#2ca02c",  # green
              "Decline": "#d62728"}  # red
    bar_colors = [colors[s] for s in status_sorted]

    # Figure
    fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
    bars = ax.barh(names_sorted, 
                   ratios_sorted, 
                   color=bar_colors, 
                   edgecolor="black", 
                   linewidth=0.5)

    # Labels & title
    ax.set_xlabel("Value per Minute (higher is better)", labelpad=8)
    ax.set_title(title, pad=12, fontweight="bold")

    # Grid for readability
    ax.xaxis.grid(True, linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)

    # Show values at end of bars
    xmax = max(ratios_sorted) if ratios_sorted else 0.0
    pad = 0.02 * (xmax if xmax > 0 else 1.0)
    for bar, r in zip(bars, ratios_sorted):
        ax.text(bar.get_width() + pad, bar.get_y() + bar.get_height()/2,
                f"{r:.2f}", va="center", ha="left", fontsize=9)

    # Legend
    legend_handles = [
        Patch(
            facecolor=colors["Attend"],
            edgecolor="black",
            label="Attend",
        ),
        Patch(
            facecolor=colors["Decline"],
            edgecolor="black",
            label="Decline",
        ),
    ]

    ax.legend(
        handles=legend_handles,
        frameon=False,
        loc="lower right",
    )

    # Invert y to have highest ratio on top
    ax.invert_yaxis()

    # Tight layout; extra space for long labels
    plt.tight_layout()
    plt.subplots_adjust(left=0.28, right=0.95, top=0.9, bottom=0.12)
    plt.show()

def main():
    meetings = [
        {"name": "Weekly Staff",  "value": 7,  "time": 60, "energy": 3},
        {"name": "Design Review", "value": 9,  "time": 90, "energy": 6},
        {"name": "1:1 Mentoring", "value": 8,  "time": 45, "energy": 2},
        {"name": "Vendor Pitch",  "value": 4,  "time": 30, "energy": 2},
        {"name": "Roadmap Sync",  "value": 10, "time": 50, "energy": 4},
    ]

    TIME_BUDGET = 180
    ENERGY_BUDGET = 10

    attend, chosen_names, total_value, total_time, total_energy = (
        solve_meeting_diet(
            meetings,
            TIME_BUDGET,
            ENERGY_BUDGET,
        )
    )

    print("Selected meetings:")
    for m in attend:
        print(
            f" - {m['name']} "
            f"(v={m['value']}, t={m['time']}m, e={m['energy']})"
        )

    print(f"\nTotal value = {total_value}")
    print(f"Total time  = {total_time} minutes")
    print(f"Total energy= {total_energy} units")

    plot_meetings(meetings, chosen_names)

if __name__ == "__main__":
    main()
