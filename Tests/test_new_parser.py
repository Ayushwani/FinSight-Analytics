import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from app.parsers.parser import parse_spl_file

data = parse_spl_file(
    "app/uploads/trial bal 31.3.26 Consolidated.SPL"
)

print("=" * 80)

print(data.keys())

print()

print("Sections Found")

print(data["sections"].keys())

print()

print("L03")

print(data["sections"]["L03"])

print()

print("A21")

print(data["sections"]["A21"])

print()

print("Grand Total")

print(data["grand_total"])