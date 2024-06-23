import random

names = [
    "Alia", "Brian", "Amelia", "Bam Bam", "Itachi", "Javelle", "Marie", "Gates", "Sniperwolf", "Python Papi"
]

print(f"All names: {names}\n")

idx = random.randint(0, len(names) - 1)
print(f"Picked names: {names[idx]}")