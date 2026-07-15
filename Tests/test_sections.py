import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from app.parsers.parser import parse_spl_file

data = parse_spl_file(
    "app/uploads/trial bal 31.3.26 Consolidated.SPL"
)

print()

print(data.keys())

print()

print("L03")

print(data["L03"]["title"])

print()

print("First 15 rows")

for row in data["L03"]["rows"][:15]:

    print(row)