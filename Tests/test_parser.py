from pathlib import Path

FILE = Path("app/uploads/trial bal 31.3.26 Consolidated.SPL")

with open(FILE, "rb") as f:
    data = f.read()

# Decode
text = data.decode("latin1", errors="ignore")

# Remove printer control characters
text = text.replace("\x1b", "")
text = text.replace("\x0f", "")

lines = text.splitlines()

print("=" * 120)

for i, line in enumerate(lines):

    print(f"{i:03d} | {repr(line)}")

print("=" * 120)