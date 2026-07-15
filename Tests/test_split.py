import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from app.parsers.parser import parse_spl_file

rows = parse_spl_file(
    "app/uploads/trial bal 31.3.26 Consolidated.SPL"
)

print()

for i in range(25):

    print("="*80)

    print(rows[i]["left"])

    print("------")

    print(rows[i]["right"])