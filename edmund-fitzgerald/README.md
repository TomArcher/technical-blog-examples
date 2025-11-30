Here's the updated README for the Edmund Fitzgerald blog post:

```markdown
# Sample Code: The Wreck of the Edmund Fitzgerald - Modeling Decomposition in Extreme Environments

This repository contains the companion code for the blog post:

👉 [The Wreck of the Edmund Fitzgerald: Modeling Decomposition in Extreme Environments](https://tomarcher.io/posts/edmund-fitzgerald/) on [Signal & Syntax](https://tomarcher.io/).

This code demonstrates how physics and thermodynamics explain why Gordon Lightfoot's haunting lyric "The lake, it is said, never gives up her dead" is scientifically accurate. The examples model decomposition rates using the Arrhenius equation, gas compression via Boyle's Law, and buoyancy calculations to show why bodies at 530 feet in Lake Superior's 4°C water can never surface naturally. The blog post validates the model against historical maritime disasters and explores the brutal mathematics behind this limnological phenomenon.

## 📋 Requirements

- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`
- `matplotlib` for visualizations
- `numpy` for numerical computations

## ⚙️ Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/edmund-fitzgerald
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the Examples

Run the main simulation and visualizations:

```bash
# Run the Edmund Fitzgerald analysis
python analyze_edmund_fitzgerald.py

# Validate against historical disasters
python validate_historical_disasters.py

# Generate visualizations
python plot_density_evolution.py
python plot_surfacing_zones.py
```

## 📁 What's Included

### Core Physics Functions
- **decomposition_rate.py** - Temperature-dependent decomposition using Q10 coefficient
- **gas_volume_at_depth.py** - Boyle's Law gas compression calculations
- **body_density_with_gas.py** - Buoyancy calculations with gas production

### Environmental Modeling
- **lake_conditions.py** - Data structure for environmental conditions
- **superior_conditions.py** - Lake Superior's temperature and pressure profiles
- **gas_production_model.py** - Exponential gas production over time

### Simulation & Analysis
- **will_body_surface.py** - Main simulation combining all physics
- **analyze_edmund_fitzgerald.py** - Specific analysis for 530 feet depth
- **validate_historical_disasters.py** - Model validation against Titanic, Lusitania, etc.

### Visualizations
- **plot_density_evolution.py** - Body density changes over time at various depths
- **plot_surfacing_zones.py** - Contour map of surfacing possibility zones

## 📊 Key Findings

At the Edmund Fitzgerald's depth (162m/530ft) in 4°C water:
- Decomposition rate: ~10% of normal
- Gas compression: 6% of surface volume  
- Verdict: Bodies will never surface naturally
- Required gas for buoyancy: 18,355 mL (impossible to generate)

## 🤝 Contributing

Pull requests are welcome! If you spot an improvement, bug, or want to extend the model (salinity effects, current modeling, probabilistic variations), feel free to open a PR.
```

This README follows the same structure as your hash collisions example but is tailored to the Edmund Fitzgerald post's content and code structure.