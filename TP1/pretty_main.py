"""
TP1 - Main
Runs all TSP methods and produces images/ + result.md
"""

import os
import matplotlib
matplotlib.use('Agg')  # non-interactive backend, no window popup
import matplotlib.pyplot as plt

from tsp_utils import (
    init_cities, distance_matrix, tour_length,
    generate_all_tours, force_brute,
    random_sample_search, nearest_neighbor,
)
from genetic_algorithm import (
    genetic_algorithm,
    cycle_crossover, pmx_crossover, order_crossover,
    displacement_mutation, exchange_mutation,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

N_CITIES    = 8
SAMPLE_SIZE = 500
IMAGES_DIR  = "images"
RESULT_FILE = "result.md"

GA_PARAMS = dict(
    n=N_CITIES,
    nb_tours=100,
    max_gen=500,
    mutation_rate=0.1,
)

GA_COMBOS = [
    ("Cycle + Displacement", cycle_crossover,  displacement_mutation),
    ("Cycle + Exchange",     cycle_crossover,  exchange_mutation),
    ("PMX + Displacement",   pmx_crossover,    displacement_mutation),
    ("PMX + Exchange",       pmx_crossover,    exchange_mutation),
    ("Order + Displacement", order_crossover,  displacement_mutation),
    ("Order + Exchange",     order_crossover,  exchange_mutation),
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

os.makedirs(IMAGES_DIR, exist_ok=True)


def save_tour_plot(cities, tour, title, filename):
    """Save a tour plot to images/<filename> and return the relative path."""
    fig, ax = plt.subplots(figsize=(5, 5))

    xs = [c.x for c in cities]
    ys = [c.y for c in cities]

    if tour:
        cx = [cities[t - 1].x for t in tour] + [cities[tour[0] - 1].x]
        cy = [cities[t - 1].y for t in tour] + [cities[tour[0] - 1].y]
        ax.plot(cx, cy, color="#4C72B0", linewidth=1.5, zorder=1)

    ax.scatter(xs, ys, color="#DD4444", s=60, zorder=2)

    for i, c in enumerate(cities):
        ax.annotate(str(i + 1), (c.x, c.y),
                    textcoords="offset points", xytext=(6, 4), fontsize=8)

    ax.set_title(title, fontsize=10)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.axis("off")

    path = os.path.join(IMAGES_DIR, filename)
    fig.savefig(path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return path


def fmt_tour(tour):
    return " → ".join(str(c) for c in tour) + f" → {tour[0]}"


# ---------------------------------------------------------------------------
# Section 1 – City generation & in-order tour
# ---------------------------------------------------------------------------

print("[1/5] City generation...")

cities    = init_cities(N_CITIES)
distances = distance_matrix(cities)

inorder_tour   = list(range(1, N_CITIES + 1))
inorder_length = tour_length(inorder_tour, distances)

img_inorder = save_tour_plot(cities, inorder_tour,
                             f"In-order tour  (length={inorder_length:.4f})",
                             "01_inorder.png")

# ---------------------------------------------------------------------------
# Section 2 – Brute force (its own city set to stay faithful to original)
# ---------------------------------------------------------------------------

print("[2/5] Brute force...")

cities_bf    = init_cities(N_CITIES)
distances_bf = distance_matrix(cities_bf)

all_tours      = generate_all_tours(N_CITIES)
best_tour_bf   = force_brute(distances_bf)
best_length_bf = tour_length(best_tour_bf, distances_bf)

img_bf = save_tour_plot(cities_bf, best_tour_bf,
                        f"Brute force  (length={best_length_bf:.4f})",
                        "02_brute_force.png")

# ---------------------------------------------------------------------------
# Section 3 – Random sampling
# ---------------------------------------------------------------------------

print("[3/5] Random sampling...")

best_tour_rs, best_length_rs = random_sample_search(N_CITIES, SAMPLE_SIZE, distances)

img_rs = save_tour_plot(cities, best_tour_rs,
                        f"Random sampling  ({SAMPLE_SIZE} samples, length={best_length_rs:.4f})",
                        "03_random_sampling.png")

# ---------------------------------------------------------------------------
# Section 4 – Nearest neighbour
# ---------------------------------------------------------------------------

print("[4/5] Nearest neighbour...")

best_nn_start = min(
    range(N_CITIES),
    key=lambda s: tour_length(nearest_neighbor(distances, start=s), distances),
)
best_tour_nn   = nearest_neighbor(distances, start=best_nn_start)
best_length_nn = tour_length(best_tour_nn, distances)

img_nn = save_tour_plot(cities, best_tour_nn,
                        f"Nearest neighbour  (start={best_nn_start+1}, length={best_length_nn:.4f})",
                        "04_nearest_neighbour.png")

# Per-start detail (text only, no extra plots to keep images/ clean)
nn_rows = []
for start in range(N_CITIES):
    t  = nearest_neighbor(distances, start=start)
    ln = tour_length(t, distances)
    nn_rows.append((start + 1, t, ln))

# ---------------------------------------------------------------------------
# Section 5 – Genetic algorithm
# ---------------------------------------------------------------------------

print("[5/5] Genetic algorithm...")

ga_results = []
best_ga_tour   = None
best_ga_length = float("inf")
best_ga_label  = ""

for label, crossover_fn, mutation_fn in GA_COMBOS:
    tour   = genetic_algorithm(crossover_fn=crossover_fn,
                               mutation_fn=mutation_fn,
                               distances=distances,
                               **GA_PARAMS)
    length = tour_length(tour, distances)
    ga_results.append((label, tour, length))

    if length < best_ga_length:
        best_ga_length = length
        best_ga_tour   = tour
        best_ga_label  = label

img_ga = save_tour_plot(cities, best_ga_tour,
                        f"GA best ({best_ga_label}, length={best_ga_length:.4f})",
                        "05_genetic_algorithm.png")

# ---------------------------------------------------------------------------
# Write result.md
# ---------------------------------------------------------------------------

print("Writing result.md...")

lines = []

def h(level, text):
    lines.append("#" * level + " " + text)
    lines.append("")

def p(text=""):
    lines.append(text)

def img_md(alt, path):
    lines.append(f"![{alt}]({path})")
    lines.append("")

def table(headers, rows):
    sep = " | ".join("---" for _ in headers)
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + sep + " |")
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    lines.append("")


h(1, "TP1 — Travelling Salesman Problem")
p(f"All results below use **{N_CITIES} cities** unless noted otherwise.")
p()

# --- Section 1 ---
h(2, "1. City generation & in-order tour")
p("Cities were generated randomly. The in-order tour visits them in index order.")
p()
p(f"**Tour:** {fmt_tour(inorder_tour)}")
p(f"**Length:** `{inorder_length:.4f}`")
p()
img_md("In-order tour", img_inorder)

# --- Section 2 ---
h(2, "2. Brute force (exhaustive search)")
p(f"All {len(all_tours)} possible tours were evaluated on a separate random city set.")
p()
p(f"**Best tour:** {fmt_tour(best_tour_bf)}")
p(f"**Length:** `{best_length_bf:.4f}`")
p()
img_md("Brute force best tour", img_bf)

# --- Section 3 ---
h(2, "3. Random sampling")
p(f"{SAMPLE_SIZE} random tours were sampled and the shortest one kept.")
p()
p(f"**Best tour:** {fmt_tour(best_tour_rs)}")
p(f"**Length:** `{best_length_rs:.4f}`")
p()
img_md("Random sampling best tour", img_rs)

# --- Section 4 ---
h(2, "4. Nearest neighbour heuristic")
p("The algorithm was run from every possible starting city.")
p()
table(
    ["Start city", "Tour", "Length"],
    [(r[0], fmt_tour(r[1]), f"{r[2]:.4f}") for r in nn_rows],
)
p(f"**Best start:** city {best_nn_start + 1}")
p(f"**Best tour:** {fmt_tour(best_tour_nn)}")
p(f"**Length:** `{best_length_nn:.4f}`")
p()
img_md("Nearest neighbour best tour", img_nn)

# --- Section 5 ---
h(2, "5. Genetic algorithm")
p(f"Parameters: population={GA_PARAMS['nb_tours']}, "
  f"generations={GA_PARAMS['max_gen']}, "
  f"mutation rate={GA_PARAMS['mutation_rate']}")
p()
table(
    ["Crossover + Mutation", "Length", "Tour"],
    [(label, f"{length:.4f}", fmt_tour(tour)) for label, tour, length in ga_results],
)
p(f"**Best combination:** {best_ga_label}")
p(f"**Best tour:** {fmt_tour(best_ga_tour)}")
p(f"**Length:** `{best_ga_length:.4f}`")
p()
img_md("Genetic algorithm best tour", img_ga)

# --- Summary ---
h(2, "Summary")
p("Comparison on the same 8-city set (brute force used its own random set).")
p()
table(
    ["Method", "Length", "Notes"],
    [
        ("In-order tour",     f"{inorder_length:.4f}", "trivial baseline"),
        ("Brute force",       f"{best_length_bf:.4f}", "different city set, guaranteed optimal"),
        ("Random sampling",   f"{best_length_rs:.4f}", f"{SAMPLE_SIZE} samples"),
        ("Nearest neighbour", f"{best_length_nn:.4f}", f"best of {N_CITIES} starts"),
        ("Genetic algorithm", f"{best_ga_length:.4f}", f"best of {len(GA_COMBOS)} operator combos"),
    ],
)

with open(RESULT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Done. See {RESULT_FILE} and {IMAGES_DIR}/")