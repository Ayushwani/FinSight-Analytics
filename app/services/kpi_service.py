class KPIService:

    def __init__(self, report):

        self.report = report

    def generate(self):

        profit_growth = (
            (
                self.report["Current Profit"]
                - self.report["FY Profit"]
            )
            / self.report["FY Profit"]
        ) * 100

        kpis = []

        # ----------------------------------------
        # Deposits
        # ----------------------------------------

        dg = self.report["Deposit Growth"]

        if dg >= 0:
            trend = "🟢 Up"
            status = "Healthy Growth"
        else:
            trend = "🔴 Down"
            status = "Needs Attention"

        kpis.append({

            "title": "Deposits",

            "icon": "💰",

            "value": self.report["Current Deposits"],

            "trend": f"{trend} {abs(dg):.2f}%",

            "status": status

        })

        # ----------------------------------------
        # Loans
        # ----------------------------------------

        lg = self.report["Loan Growth"]

        if lg >= 0:
            trend = "🟢 Up"
            status = "Healthy Growth"
        else:
            trend = "🔴 Down"
            status = "Declining"

        kpis.append({

            "title": "Loans",

            "icon": "🏦",

            "value": self.report["Current Loans"],

            "trend": f"{trend} {abs(lg):.2f}%",

            "status": status

        })

        # ----------------------------------------
        # Profit
        # ----------------------------------------

        if profit_growth >= 0:
            trend = "🟢 Up"
            status = "Excellent"
        else:
            trend = "🔴 Down"
            status = "Loss"

        kpis.append({

            "title": "Profit",

            "icon": "📈",

            "value": self.report["Current Profit"],

            "trend": f"{trend} {abs(profit_growth):.2f}%",

            "status": status

        })

        # ----------------------------------------
        # CD Ratio
        # ----------------------------------------

        cd = self.report["CD Ratio"]

        if cd < 60:
            trend = "🟡 Conservative"
            status = "Below Ideal"

        elif cd <= 80:
            trend = "🟢 Healthy"
            status = "Optimal"

        else:
            trend = "🔴 High"
            status = "Monitor"

        kpis.append({

            "title": "CD Ratio",

            "icon": "📊",

            "value": f"{cd:.2f}%",

            "trend": trend,

            "status": status

        })

        return kpis