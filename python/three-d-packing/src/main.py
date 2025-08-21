"""
truck_packing.py (fixed axes)

Simple shelf-style 3D truck packing (baseline) with consistent axes and plotting.

Coordinate system (RIGHT-HANDED, used consistently in packing and plotting):
- x: left -> right  (width)
- y: bottom -> top  (height)
- z: back -> front  (depth)

Origin (0,0,0) is the truck's back-left-bottom inside corner.

Heuristic (baseline):
- Sort items by volume (and weight) descending.
- Pack along x (width) to form a "row".
- When a row overflows width, start a new row by advancing z (depth).
- When depth overflows, start a new "layer" by advancing y (height).
- Skip items that no longer fit in remaining height.

NOTE:
- This is NOT the guillotine/rotation solver from the docstring of your original;
  it’s the same simple shelf heuristic you had, but with consistent axes and a fixed plot.
- If you want full 6-axis rotations + guillotine splitting, I can layer that in next.
"""

from dataclasses import dataclass
from typing import List, Tuple, Dict

@dataclass
class Dimensions:
    height: float
    width: float
    depth: float

@dataclass
class Placement:
    name: str
    size: Dimensions
    weight: float
    
    # (x, y, z) = (width, height, depth)
    position: Tuple[float, float, float] 

def pack_truck(
    truck: Dimensions,
    items: Dict[str, Dict]
) -> Tuple[List[Placement], List[str], List[str]]:
    placements: List[Placement] = []
    skipped: List[str] = []
    notes: List[str] = []

    # Shelf-style cursor positions using (x, y, z) 
    # with y=height and z=depth
    x, y, z = 0.0, 0.0, 0.0

    # Tallest item in this layer (height consumed)
    current_layer_height = 0.0  

    # Deepest item in the current row
    row_depth = 0.0

    # Sort by volume then weight (desc) to be more 
    # stable/deterministic
    items_sorted = sorted(
        items.items(),
        key=lambda kv: (
            kv[1]["height"] * kv[1]["width"] * kv[1]["depth"],
            kv[1]["weight"],
        ),
        reverse=True,
    )

    for name, item in items_sorted:
        h, w, d, wt = (item["height"], 
                      item["width"], 
                      item["depth"], 
                      item["weight"])

        # If it doesn't fit in the current row across width,
        # wrap to next row (advance depth z)
        if x + w > truck.width:
            x = 0.0
            z += row_depth
            row_depth = 0.0

        # If it doesn't fit within remaining depth,
        # start a new layer (advance height y)
        if z + d > truck.depth:
            z = 0.0
            y += current_layer_height
            current_layer_height = 0.0

        # If it doesn't fit within remaining height, skip
        if y + h > truck.height:
            skipped.append(name)
            notes.append(f"{name} skipped: too tall for remaining truck height.")
            continue

        # Place the item
        placements.append(
            Placement(
                name=name,
                size=Dimensions(h, w, d),
                weight=wt,
                position=(x, y, z),
            )
        )

        # Update cursors
        x += w
        row_depth = max(row_depth, d)
        current_layer_height = max(current_layer_height, h)

    return placements, skipped, notes

# ---------- Visualization ----------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random

def _cuboid_faces_mpl_from_internal(x, y, z, w, h, d):
    """
    Internal coords: x=width, y=height, z=depth
    Matplotlib axes: X=width, Y=depth, Z=height
    Map (x,y,z) -> (X,Y,Z) = (x, z, y)
    """
    # 8 vertices in internal space
    v000 = (x,     y,     z    )
    v100 = (x + w, y,     z    )
    v110 = (x + w, y + h, z    )
    v010 = (x,     y + h, z    )
    v001 = (x,     y,     z + d)
    v101 = (x + w, y,     z + d)
    v111 = (x + w, y + h, z + d)
    v011 = (x,     y + h, z + d)

    def to_mpl(v):
        xi, yi, zi = v
        return [xi, zi, yi]  # (X=width, Y=depth, Z=height)

    V = list(map(to_mpl, [v000, v100, v110, v010, v001, v101, v111, v011]))
    # faces as quads using transformed verts
    return [
        [V[0], V[1], V[2], V[3]],  # back  (z)
        [V[4], V[5], V[6], V[7]],  # front (z + d)
        [V[0], V[1], V[5], V[4]],  # bottom
        [V[3], V[2], V[6], V[7]],  # top
        [V[1], V[2], V[6], V[5]],  # right
        [V[0], V[3], V[7], V[4]],  # left
    ]

def plot_truck_packing(truck: Dimensions, placements: List[Placement]):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Truck wireframe: bottom (Z=0), top (Z=truck.height)
    # Use (X,Y,Z) = (width, depth, height)
    # Bottom rectangle (Z=0)
    ax.plot([0, truck.width, truck.width, 0, 0],
            [0, 0,           truck.depth,  truck.depth, 0],
            [0, 0,           0,            0,           0],
            "k-", linewidth=1)

    # Top rectangle (Z=truck.height)
    ax.plot([0, truck.width, truck.width, 0, 0],
            [0, 0,           truck.depth,  truck.depth, 0],
            [truck.height]*5,
            "k-", linewidth=1)

    # Vertical edges
    for X, Y in [
        (0, 0),
        (truck.width, 0),
        (truck.width, truck.depth),
        (0, truck.depth),
    ]:
        ax.plot([X, X], [Y, Y], [0, truck.height], "k-", linewidth=1)

    # Draw items
    for p in placements:
        x, y, z = p.position          # internal
        h, w, d = p.size.height, p.size.width, p.size.depth
        faces = _cuboid_faces_mpl_from_internal(x, y, z, w, h, d)
        color = [random.random(), random.random(), random.random()]
        poly = Poly3DCollection(faces, facecolors=color, 
                                edgecolors="k", 
                                linewidths=0.8, 
                                alpha=0.7)
        ax.add_collection3d(poly)

        # Label at center (map to mpl coords)
        Xc, Yc, Zc = x + w/2, z + d/2, y + h/2
        ax.text(Xc, Yc, Zc, p.name, color="k", ha="center", va="center")

    # Labels & limits (match mapped axes)
    ax.set_xlabel("Width (X)")
    ax.set_ylabel("Depth (Y)")
    ax.set_zlabel("Height (Z)")
    ax.set_xlim(0, truck.width)
    ax.set_ylim(truck.depth, 0)
    ax.set_zlim(0, truck.height)

    # Proportional box aspect
    max_range = max(truck.width, truck.depth, truck.height)
    ax.set_box_aspect((truck.width / max_range,
                       truck.depth / max_range,
                       truck.height / max_range))

    # Optional: set a helpful view angle
    ax.view_init(elev=20, azim=-60)

    plt.title("Truck Packing (X=Width, Y=Depth, Z=Height)")
    plt.tight_layout()
    plt.show()

# ---------- Demo ----------
if __name__ == "__main__":
    truck = Dimensions(height=100.0, width=100.0, depth=240.0)

    items_input = {
        "crateA": {"height": 50, "width": 40, "depth": 60, "weight": 80},
        "crateB": {"height": 30, "width": 30, "depth": 30, "weight": 40},
        "crateC": {"height": 20, "width": 60, "depth": 40, "weight": 50},
        "crateD": {"height": 80, "width": 40, "depth": 50, "weight": 90},
        "crateE": {"height": 10, "width": 90, "depth": 30, "weight": 20},
        "crateF": {"height": 40, "width": 40, "depth": 40, "weight": 60},
    }

    placements, skipped, notes = pack_truck(truck, items_input)

    print("== PACK PLAN ==")
    for i, p in enumerate(placements, 1):
        x, y, z = p.position
        print(
            f"{i:02d}. {p.name}: pos=({x:.1f},{y:.1f},{z:.1f}) "
            f"size(HxWxD)=({p.size.height:.1f}x{p.size.width:.1f}x"
            f"{p.size.depth:.1f}) "
            f"weight={p.weight:.1f}"
        )

    if skipped:
        print("\nSkipped:", skipped)
    if notes:
        print("\nNotes:")
        for n in notes:
            print("-", n)

    # Visualize the simulated pack
    try:
        plot_truck_packing(truck, placements)
    except Exception as e:
        print("\n(Visualization skipped; matplotlib may not be installed.)")
        print(e)
