# Sample Code: The Meeting Diet

This repository contains the companion code for the blog post:

👉 [The Meeting Diet: Max Value Under Time & Energy Budgets](https://tomarcher.io/posts/meeting-diet/) on [Signal & Syntax](https://tomarcher.io/).

This code demonstrates how to frame your weekly calendar as a **0/1 knapsack problem**. Each meeting has a *value*, a *time cost*, and an *energy cost*. The solver (using [PuLP](https://coin-or.github.io/pulp/)) selects the combination of meetings that maximizes total value while staying within time and energy budgets. The blog post walks through the problem setup, prompt engineering, and lessons learned. This sample provides the runnable Python code behind that exploration.

## 📋 Requirements

- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- `pip` for dependency management: `python -m ensurepip --upgrade`

## ⚙️ Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/TomArcher/technical-blog-examples.git
cd technical-blog-examples/meeting-diet
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the Sample

Run the main script:

```bash
python meeting_diet.py
```

You’ll see:

- A list of selected meetings under your constraints

- Totals for value, time, and energy

- A chart showing value-per-minute efficiency (attend vs decline)

## 🛠️ Customizing for Your Calendar

Update the meetings list in main() with your own events:

```python
meetings = [
    {"name": "Roadmap Sync",  "value": 10, "time": 50, "energy": 4},
    {"name": "Vendor Pitch",  "value":  3, "time": 30, "energy": 2},
    {"name": "1:1 Mentoring", "value":  8, "time": 45, "energy": 2},
]
```

- value = impact score (higher = more important)

- time = meeting length in minutes

- energy = subjective cognitive load (1–6 scale works well)

Then, adjust **TIME_BUDGET** and **ENERGY_BUDGET** to fit your week.

## 🤝 Contributing

Pull requests are welcome! If you spot an improvement, bug, or want to extend the sample (e.g., import from a calendar, handle overlaps, add mandatory meetings), feel free to open a PR.
