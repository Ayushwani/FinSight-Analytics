import sys
from pathlib import Path
from pprint import pprint

ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(ROOT))

from app.parsers.parser import parse_spl_file

data = parse_spl_file(
    "app/uploads/trial bal 31.3.26 Consolidated.SPL"
)

print("=" * 80)

print("L03")

print("=" * 80)

pprint(data["sections"]["L03"])

print()

print("=" * 80)

print("A21")

print("=" * 80)

pprint(data["sections"]["A21"])