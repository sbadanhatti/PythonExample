# Intel Core Ultra i9 185H vs 285K — Python Comparison Example
"""
This script compares the Intel Core Ultra 9 185H (14th gen, mobile, Meteor Lake)
against the Intel Core Ultra 9 285K (15th gen, desktop, Arrow Lake) using
Python dictionaries and common data operations.

It demonstrates:
- Storing structured hardware specs in dictionaries
- Iterating and comparing dictionary values
- Determining a winner per category
- Summarising results programmatically
"""

# ── Processor specs ──────────────────────────────────────────────────────────

intel_ultra_i9_185h = {
    "name": "Intel Core Ultra 9 185H",
    "generation": "14th Gen (Meteor Lake)",
    "segment": "Mobile",
    "cores_performance": 6,
    "cores_efficient": 8,
    "cores_low_power_efficient": 2,
    "total_cores": 16,
    "total_threads": 22,
    "base_clock_ghz": 2.3,
    "boost_clock_ghz": 5.1,
    "cache_mb": 24,
    "tdp_watts": 45,
    "max_tdp_watts": 115,
    "integrated_gpu": "Intel Arc Graphics (8 Xe-cores)",
    "max_ram_gb": 96,
    "ram_type": "DDR5 / LPDDR5x",
    "pcie_version": 5,
    "process_node_nm": 7,
    "release_year": 2023,
}

intel_ultra_i9_285k = {
    "name": "Intel Core Ultra 9 285K",
    "generation": "15th Gen (Arrow Lake)",
    "segment": "Desktop",
    "cores_performance": 8,
    "cores_efficient": 16,
    "cores_low_power_efficient": 0,
    "total_cores": 24,
    "total_threads": 24,
    "base_clock_ghz": 3.7,
    "boost_clock_ghz": 5.7,
    "cache_mb": 36,
    "tdp_watts": 125,
    "max_tdp_watts": 250,
    "integrated_gpu": "Intel Graphics (4 Xe-cores)",
    "max_ram_gb": 192,
    "ram_type": "DDR5",
    "pcie_version": 5,
    "process_node_nm": 3,
    "release_year": 2024,
}

# ── Helper: compare two specs ────────────────────────────────────────────────

# For these numeric specs a *higher* value is better
HIGHER_IS_BETTER = {
    "cores_performance",
    "cores_efficient",
    "cores_low_power_efficient",
    "total_cores",
    "total_threads",
    "base_clock_ghz",
    "boost_clock_ghz",
    "cache_mb",
    "max_ram_gb",
    "pcie_version",
    "release_year",
}

# For these numeric specs a *lower* value is better
LOWER_IS_BETTER = {
    "tdp_watts",
    "max_tdp_watts",
    "process_node_nm",
}


def compare_processors(cpu1: dict, cpu2: dict) -> None:
    """Print a side-by-side comparison of two processors and declare winners."""

    name1 = cpu1["name"]
    name2 = cpu2["name"]
    wins = {name1: 0, name2: 0, "tie": 0}

    print("=" * 70)
    print(f"{'SPEC':<30} {name1:<22} {name2:<22} {'WINNER'}")
    print("=" * 70)

    comparable_keys = (
        HIGHER_IS_BETTER | LOWER_IS_BETTER
    )

    for key in cpu1:
        if key in ("name", "generation", "segment",
                   "integrated_gpu", "ram_type"):
            continue  # skip non-numeric / info-only fields

        val1 = cpu1[key]
        val2 = cpu2[key]

        if key in comparable_keys and isinstance(val1, (int, float)):
            if key in HIGHER_IS_BETTER:
                if val1 > val2:
                    winner = name1
                elif val2 > val1:
                    winner = name2
                else:
                    winner = "Tie"
            else:  # lower is better
                if val1 < val2:
                    winner = name1
                elif val2 < val1:
                    winner = name2
                else:
                    winner = "Tie"

            if winner == "Tie":
                wins["tie"] += 1
            else:
                wins[winner] += 1
        else:
            winner = "N/A"

        label = key.replace("_", " ").title()
        print(f"{label:<30} {str(val1):<22} {str(val2):<22} {winner}")

    print("=" * 70)
    print("\nRESULTS:")
    print(f"  {name1}: {wins[name1]} wins")
    print(f"  {name2}: {wins[name2]} wins")
    print(f"  Ties: {wins['tie']}")

    if wins[name1] > wins[name2]:
        overall = name1
    elif wins[name2] > wins[name1]:
        overall = name2
    else:
        overall = "It's a tie"

    print(f"\nOverall winner (most category wins): {overall}")


# ── Info-only fields ─────────────────────────────────────────────────────────

def print_info_fields(cpu1: dict, cpu2: dict) -> None:
    """Print non-numeric / descriptive fields side by side."""
    info_keys = ["generation", "segment", "integrated_gpu", "ram_type"]
    name1, name2 = cpu1["name"], cpu2["name"]
    print("\n" + "=" * 70)
    print(f"{'INFO':<30} {name1:<22} {name2:<22}")
    print("=" * 70)
    for key in info_keys:
        label = key.replace("_", " ").title()
        print(f"{label:<30} {str(cpu1[key]):<22} {str(cpu2[key]):<22}")
    print("=" * 70)


# ── Main ─────────────────────────────────────────────────────────────────────

print(f"\nComparing: {intel_ultra_i9_185h['name']}  vs  {intel_ultra_i9_285k['name']}\n")

print_info_fields(intel_ultra_i9_185h, intel_ultra_i9_285k)
print()
compare_processors(intel_ultra_i9_185h, intel_ultra_i9_285k)

# ── Key takeaways ────────────────────────────────────────────────────────────
print("""
Key Takeaways
─────────────
• The 285K is a 15th-gen DESKTOP chip; the 185H is a 14th-gen MOBILE chip.
• The 285K wins on raw performance (more cores, higher clocks, larger cache).
• The 185H wins on power efficiency (lower TDP), making it ideal for laptops.
• Both support PCIe 5 and DDR5, but the 285K supports more RAM (192 GB vs 96 GB).
• The 185H includes a more capable integrated GPU (8 Xe-cores vs 4 Xe-cores).
• Choose 285K for a high-performance desktop build.
• Choose 185H for a thin-and-light or battery-focused laptop.
""")

# ── Quick dict operations demo ───────────────────────────────────────────────
print("=== Python Dict Operations Demo ===\n")

# Merge both specs into one dict for easy lookup
all_specs = {
    "185H": intel_ultra_i9_185h,
    "285K": intel_ultra_i9_285k,
}

# Find which CPU has more total cores
most_cores = max(all_specs, key=lambda k: all_specs[k]["total_cores"])
print(f"CPU with most cores: {all_specs[most_cores]['name']} "
      f"({all_specs[most_cores]['total_cores']} cores)")

# Find the more power-efficient CPU (lower TDP)
most_efficient = min(all_specs, key=lambda k: all_specs[k]["tdp_watts"])
print(f"More power-efficient CPU: {all_specs[most_efficient]['name']} "
      f"({all_specs[most_efficient]['tdp_watts']} W TDP)")

# Dictionary comprehension — extract clock speeds only
clock_speeds = {k: {"base": v["base_clock_ghz"], "boost": v["boost_clock_ghz"]}
                for k, v in all_specs.items()}
print(f"\nClock speeds summary: {clock_speeds}")

# Iterate and print all specs for the 285K
print(f"\nAll specs for {intel_ultra_i9_285k['name']}:")
for spec, value in intel_ultra_i9_285k.items():
    print(f"  {spec.replace('_', ' ').title()}: {value}")
