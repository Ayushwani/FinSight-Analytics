from pathlib import Path
import re


class SPLParser:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

        self.lines = []

        self.rows = []

        self.sections = {}

    ############################################################

    def read_file(self):

        raw = self.file_path.read_bytes()

        text = raw.decode("latin1", errors="ignore")

        text = text.replace("\x1b", "")
        text = text.replace("\x0f", "")

        self.lines = text.splitlines()

    ############################################################

    def split_columns(self):

        for line in self.lines:

            if "|" in line:

                left, right = line.split("|", 1)

            else:

                left = line
                right = ""

            self.rows.append({

                "left": left.rstrip(),

                "right": right.rstrip()

            })

    ############################################################

    def is_section(self, text):

        return re.match(r"^[LA]\d{2}\s+", text.strip())

    ############################################################

    def clean_amount(self, value):

        value = value.replace(",", "")

        try:
            return float(value)

        except:
            return 0

    ############################################################

    def parse_account_line(self, line):

        m = re.match(

            r"^\s*(\d+)\s+(.*?)\s+([\d,]+\.\d+)$",

            line

        )

        if not m:

            return None

        return {

            "code": m.group(1),

            "name": m.group(2).strip(),

            "amount": self.clean_amount(m.group(3))

        }

    ############################################################

    def parse_total_line(self, line):

        m = re.match(

            r"^(.*?)Total\s+([\d,]+\.\d+)$",

            line.strip()

        )

        if not m:

            return None

        return self.clean_amount(

            m.group(2)

        )

    ############################################################

    def process_side(self, side):

        current = None

        for row in self.rows:

            text = row[side].strip()

            if not text:

                continue

            ##############################################

            if self.is_section(text):

                code = text[:3]

                title = text[3:].strip()

                if code not in self.sections:

                    self.sections[code] = {

                        "title": title,

                        "accounts": {},

                        "total": 0

                    }

                current = code

                continue

            ##############################################

            if current is None:

                continue

            ##############################################

            account = self.parse_account_line(text)

            if account:

                self.sections[current]["accounts"][

                    account["name"]

                ] = account["amount"]

                continue

            ##############################################

            total = self.parse_total_line(text)

            if total:

                self.sections[current]["total"] = total

    ############################################################

    def parse_grand_total(self):

        for row in self.rows[::-1]:

            left = row["left"]

            right = row["right"]

            m = re.search(

                r"([\d,]+\.\d+)",

                left

            )

            if m:

                return self.clean_amount(m.group(1))

        return 0

    ############################################################

    def parse(self):

        self.read_file()

        self.split_columns()

        self.process_side("left")

        self.process_side("right")

        return {

            "sections": self.sections,

            "grand_total": self.parse_grand_total()

        }


############################################################


def parse_spl_file(file_path):

    parser = SPLParser(file_path)

    return parser.parse()