class SummaryService:

    def __init__(self, report):

        self.report = report

    # --------------------------------------------------

    def generate(self):

        summary = []

        # ---------------- Profit ----------------

        profit_growth = (
            (
                self.report["Current Profit"]
                - self.report["FY Profit"]
            )
            / self.report["FY Profit"]
        ) * 100

        if profit_growth >= 0:

            summary.append({

                "icon": "🟢",

                "title": "Profit",

                "message": f"Profit increased by {profit_growth:.2f}%"

            })

        else:

            summary.append({

                "icon": "🔴",

                "title": "Profit",

                "message": f"Profit declined by {abs(profit_growth):.2f}%"

            })

        # ---------------- Deposits ----------------

        if self.report["Deposit Growth"] >= 0:

            summary.append({

                "icon": "🟢",

                "title": "Deposits",

                "message": f'Deposits increased by {self.report["Deposit Growth"]:.2f}%'

            })

        else:

            summary.append({

                "icon": "🔴",

                "title": "Deposits",

                "message": f'Deposits declined by {abs(self.report["Deposit Growth"]):.2f}%'

            })

        # ---------------- Loans ----------------

        if self.report["Loan Growth"] >= 0:

            summary.append({

                "icon": "🟢",

                "title": "Loans",

                "message": f'Loans increased by {self.report["Loan Growth"]:.2f}%'

            })

        else:

            summary.append({

                "icon": "🔴",

                "title": "Loans",

                "message": f'Loans declined by {abs(self.report["Loan Growth"]):.2f}%'

            })

        # ---------------- Share Capital ----------------

        if self.report["Share Growth"] >= 0:

            summary.append({

                "icon": "🟢",

                "title": "Share Capital",

                "message": f'Share Capital increased by {self.report["Share Growth"]:.2f}%'

            })

        else:

            summary.append({

                "icon": "🔴",

                "title": "Share Capital",

                "message": f'Share Capital declined by {abs(self.report["Share Growth"]):.2f}%'

            })

        # ---------------- CRR ----------------

        if self.report["CRR Difference"] >= 0:

            summary.append({

                "icon": "🟢",

                "title": "CRR",

                "message": "CRR Requirement is Fully Maintained"

            })

        else:

            summary.append({

                "icon": "🔴",

                "title": "CRR",

                "message": "CRR Requirement is NOT Maintained"

            })

        # ---------------- SLR ----------------

        if self.report["SLR Difference"] >= 0:

            summary.append({

                "icon": "🟢",

                "title": "SLR",

                "message": "SLR Requirement is Fully Maintained"

            })

        else:

            summary.append({

                "icon": "🔴",

                "title": "SLR",

                "message": "SLR Requirement is NOT Maintained"

            })

        # ---------------- CD Ratio ----------------

        cd = self.report["CD Ratio"]

        if cd < 60:

            health = "Excellent"

            color = "🟢"

        elif cd < 75:

            health = "Good"

            color = "🟢"

        elif cd < 90:

            health = "Average"

            color = "🟡"

        else:

            health = "Weak"

            color = "🔴"

        summary.append({

            "icon": "📊",

            "title": "CD Ratio",

            "message": f"Current CD Ratio is {cd:.2f}%"

        })

        summary.append({

            "icon": color,

            "title": "Overall Health",

            "message": f"Overall Financial Health : {health}"

        })

        return summary