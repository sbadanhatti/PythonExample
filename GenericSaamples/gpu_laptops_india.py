# Latest GPUs Available in Indian Laptop Market
"""
This script provides information about the latest GPUs available in laptops
sold in the Indian market (2024-2025).
Data is organized using Python dictionaries and lists to demonstrate
real-world usage of these data structures.
"""

# 1. Latest NVIDIA Laptop GPUs available in India
"""
NVIDIA GeForce RTX 40-series (Ada Lovelace architecture) are the latest
mobile GPUs available in Indian market laptops.
"""
print("=== Latest NVIDIA GPUs in Indian Laptop Market ===")

nvidia_laptop_gpus = [
    {
        "model": "GeForce RTX 4090 Laptop GPU",
        "architecture": "Ada Lovelace",
        "vram_gb": 16,
        "cuda_cores": 9728,
        "tdp_range_w": "80-150",
        "approx_price_inr": "350000+",
        "example_laptops": ["ASUS ROG Strix SCAR 18", "MSI GT77 HX Titan", "Razer Blade 18"],
    },
    {
        "model": "GeForce RTX 4080 Laptop GPU",
        "architecture": "Ada Lovelace",
        "vram_gb": 12,
        "cuda_cores": 7424,
        "tdp_range_w": "60-150",
        "approx_price_inr": "250000-350000",
        "example_laptops": ["ASUS ROG Zephyrus M16", "Lenovo Legion Pro 7i", "Dell Alienware m18"],
    },
    {
        "model": "GeForce RTX 4070 Laptop GPU",
        "architecture": "Ada Lovelace",
        "vram_gb": 8,
        "cuda_cores": 4608,
        "tdp_range_w": "35-115",
        "approx_price_inr": "150000-250000",
        "example_laptops": ["ASUS ROG Strix G16", "MSI Raider GE78 HX", "HP OMEN 16"],
    },
    {
        "model": "GeForce RTX 4060 Laptop GPU",
        "architecture": "Ada Lovelace",
        "vram_gb": 8,
        "cuda_cores": 3072,
        "tdp_range_w": "35-115",
        "approx_price_inr": "100000-160000",
        "example_laptops": ["Lenovo Legion 5i Gen 8", "ASUS TUF Gaming A15", "Acer Predator Helios 300"],
    },
    {
        "model": "GeForce RTX 4050 Laptop GPU",
        "architecture": "Ada Lovelace",
        "vram_gb": 6,
        "cuda_cores": 2560,
        "tdp_range_w": "35-115",
        "approx_price_inr": "80000-120000",
        "example_laptops": ["ASUS Vivobook Pro 15", "MSI Cyborg 15", "Acer Nitro V 15"],
    },
]

for gpu in nvidia_laptop_gpus:
    print(f"\nModel       : {gpu['model']}")
    print(f"Architecture: {gpu['architecture']}")
    print(f"VRAM        : {gpu['vram_gb']} GB GDDR6")
    print(f"CUDA Cores  : {gpu['cuda_cores']}")
    print(f"TDP Range   : {gpu['tdp_range_w']} W")
    print(f"Price (INR) : ₹{gpu['approx_price_inr']}")
    print(f"Laptops     : {', '.join(gpu['example_laptops'])}")

print()

# 2. Latest AMD Laptop GPUs available in India
"""
AMD Radeon RX 7000M series (RDNA 3 architecture) are AMD's latest
mobile GPUs available in the Indian market.
"""
print("=== Latest AMD GPUs in Indian Laptop Market ===")

amd_laptop_gpus = [
    {
        "model": "Radeon RX 7900M",
        "architecture": "RDNA 3",
        "vram_gb": 16,
        "compute_units": 36,
        "tdp_range_w": "120-165",
        "approx_price_inr": "200000+",
        "example_laptops": ["ASUS ROG Strix Scar 16 (AMD Edition)"],
    },
    {
        "model": "Radeon RX 7700S",
        "architecture": "RDNA 3",
        "vram_gb": 8,
        "compute_units": 32,
        "tdp_range_w": "50-100",
        "approx_price_inr": "120000-180000",
        "example_laptops": ["Lenovo Legion Slim 5", "HP OMEN Transcend 14"],
    },
    {
        "model": "Radeon RX 7600S",
        "architecture": "RDNA 3",
        "vram_gb": 8,
        "compute_units": 28,
        "tdp_range_w": "50-75",
        "approx_price_inr": "90000-130000",
        "example_laptops": ["ASUS ROG Zephyrus G14 (2024)", "Acer Swift X 14"],
    },
    {
        "model": "Radeon RX 7600M XT",
        "architecture": "RDNA 3",
        "vram_gb": 8,
        "compute_units": 32,
        "tdp_range_w": "45-120",
        "approx_price_inr": "80000-120000",
        "example_laptops": ["MSI Cyborg 14", "Lenovo IdeaPad Gaming 3"],
    },
]

for gpu in amd_laptop_gpus:
    print(f"\nModel         : {gpu['model']}")
    print(f"Architecture  : {gpu['architecture']}")
    print(f"VRAM          : {gpu['vram_gb']} GB GDDR6")
    print(f"Compute Units : {gpu['compute_units']}")
    print(f"TDP Range     : {gpu['tdp_range_w']} W")
    print(f"Price (INR)   : ₹{gpu['approx_price_inr']}")
    print(f"Laptops       : {', '.join(gpu['example_laptops'])}")

print()

# 3. Latest Intel Arc Laptop GPUs available in India
"""
Intel Arc series (Alchemist architecture) represents Intel's
dedicated laptop GPUs available in the Indian market.
"""
print("=== Latest Intel Arc GPUs in Indian Laptop Market ===")

intel_arc_laptop_gpus = [
    {
        "model": "Arc A770M",
        "architecture": "Alchemist",
        "vram_gb": 16,
        "xe_cores": 32,
        "tdp_range_w": "60-120",
        "approx_price_inr": "100000-150000",
        "example_laptops": ["Acer Swift X 16", "Samsung Galaxy Book3 Pro 360"],
    },
    {
        "model": "Arc A550M",
        "architecture": "Alchemist",
        "vram_gb": 8,
        "xe_cores": 24,
        "tdp_range_w": "60-80",
        "approx_price_inr": "80000-110000",
        "example_laptops": ["Lenovo IdeaPad Slim 5i", "HP Envy 16"],
    },
    {
        "model": "Arc A370M",
        "architecture": "Alchemist",
        "vram_gb": 4,
        "xe_cores": 8,
        "tdp_range_w": "35-50",
        "approx_price_inr": "60000-90000",
        "example_laptops": ["Dell Inspiron 16 Plus", "Acer Aspire 5"],
    },
]

for gpu in intel_arc_laptop_gpus:
    print(f"\nModel      : {gpu['model']}")
    print(f"Architecture: {gpu['architecture']}")
    print(f"VRAM       : {gpu['vram_gb']} GB GDDR6")
    print(f"Xe-Cores   : {gpu['xe_cores']}")
    print(f"TDP Range  : {gpu['tdp_range_w']} W")
    print(f"Price (INR): ₹{gpu['approx_price_inr']}")
    print(f"Laptops    : {', '.join(gpu['example_laptops'])}")

print()

# 4. Summary: GPU Comparison by Performance Tier
"""
A quick lookup dictionary to find GPUs by performance tier,
useful for purchase decisions in the Indian market.
"""
print("=== GPU Tiers for Indian Laptop Buyers ===")

gpu_tiers = {
    "Flagship (₹2,00,000+)": [
        "NVIDIA RTX 4090 Laptop GPU",
        "NVIDIA RTX 4080 Laptop GPU",
        "AMD Radeon RX 7900M",
    ],
    "High-End (₹1,20,000 - ₹2,00,000)": [
        "NVIDIA RTX 4070 Laptop GPU",
        "AMD Radeon RX 7700S",
        "Intel Arc A770M",
    ],
    "Mid-Range (₹80,000 - ₹1,20,000)": [
        "NVIDIA RTX 4060 Laptop GPU",
        "AMD Radeon RX 7600S",
        "AMD Radeon RX 7600M XT",
        "Intel Arc A550M",
    ],
    "Budget (Under ₹80,000)": [
        "NVIDIA RTX 4050 Laptop GPU",
        "Intel Arc A370M",
    ],
}

for tier, gpus in gpu_tiers.items():
    print(f"\n{tier}:")
    for gpu in gpus:
        print(f"  - {gpu}")

print()

# 5. Quick lookup: find all laptops for a given GPU
"""
Using a dictionary comprehension to build a reverse lookup:
GPU model -> list of available laptops.
"""
print("=== Quick GPU-to-Laptop Lookup ===")

all_gpus = nvidia_laptop_gpus + amd_laptop_gpus + intel_arc_laptop_gpus
gpu_to_laptops = {gpu["model"]: gpu["example_laptops"] for gpu in all_gpus}

search_gpu = "GeForce RTX 4060 Laptop GPU"
print(f"Laptops with {search_gpu}:")
for laptop in gpu_to_laptops.get(search_gpu, ["No laptops found"]):
    print(f"  - {laptop}")
