class RatioService:

    def __init__(self, report):
        self.report = report

    ###########################################################

    def calculate(self):

        ratios = []

        # -------------------------------
        # Profit Growth
        # -------------------------------

        profit_growth = (
            (
                self.report["Current Profit"]
                - self.report["FY Profit"]
            )
            / self.report["FY Profit"]
        ) * 100

        ratios.append({

            "title": "Profit Growth",

            "value": f"{profit_growth:.2f}%",

            "icon": "📈",

            "status": (
                "Excellent"
                if profit_growth >= 20
                else "Average"
            )

        })

        # -------------------------------
        # Deposit Growth
        # -------------------------------

        dg = self.report["Deposit Growth"]

        ratios.append({

            "title": "Deposit Growth",

            "value": f"{dg:.2f}%",

            "icon": "💰",

            "status": (
                "Growing"
                if dg >= 0
                else "Declining"
            )

        })

        # -------------------------------
        # Loan Growth
        # -------------------------------

        lg = self.report["Loan Growth"]

        ratios.append({

            "title": "Loan Growth",

            "value": f"{lg:.2f}%",

            "icon": "🏦",

            "status": (
                "Healthy"
                if lg >= 0
                else "Declining"
            )

        })

        # -------------------------------
        # Share Growth
        # -------------------------------

        sg = self.report["Share Growth"]

        ratios.append({

            "title": "Share Growth",

            "value": f"{sg:.2f}%",

            "icon": "📊",

            "status": (
                "Increasing"
                if sg >= 0
                else "Decreasing"
            )

        })

        # -------------------------------
        # CD Ratio
        # -------------------------------

        cd = self.report["CD Ratio"]

        if cd < 60:
            cd_status = "Excellent"
        elif cd < 75:
            cd_status = "Good"
        elif cd < 90:
            cd_status = "Average"
        else:
            cd_status = "High"

        ratios.append({

            "title": "CD Ratio",

            "value": f"{cd:.2f}%",

            "icon": "📉",

            "status": cd_status

        })

        # -------------------------------
        # CRR Coverage
        # -------------------------------

        crr = (
            self.report["Available CRR"]
            /
            self.report["Required CRR"]
        ) * 100

        ratios.append({

            "title": "CRR Coverage",

            "value": f"{crr:.2f}%",

            "icon": "🏛",

            "status": "Maintained"

        })

        # -------------------------------
        # SLR Coverage
        # -------------------------------

        slr = (
            self.report["Available SLR"]
            /
            self.report["Required SLR"]
        ) * 100

        ratios.append({

            "title": "SLR Coverage",

            "value": f"{slr:.2f}%",

            "icon": "🏛",

            "status": "Maintained"

        })

        # -------------------------------
        # Cash to Deposits
        # -------------------------------

        cash_ratio = (
            self.report["Cash"]
            /
            self.report["Current Deposits"]
        ) * 100

        ratios.append({

            "title": "Cash to Deposits",

            "value": f"{cash_ratio:.2f}%",

            "icon": "💵",

            "status": "Liquidity"

        })

        # -------------------------------
        # Investment Ratio
        # -------------------------------

        invest_ratio = (
            self.report["Investments"]
            /
            self.report["Current Deposits"]
        ) * 100

        ratios.append({

            "title": "Investment Ratio",

            "value": f"{invest_ratio:.2f}%",

            "icon": "💼",

            "status": "Strong"

        })

        # -------------------------------
        # Working Capital Ratio
        # -------------------------------

        wc_ratio = (
            self.report["Working Capital"]
            /
            self.report["Current Deposits"]
        )

        ratios.append({

            "title": "Working Capital Ratio",

            "value": f"{wc_ratio:.2f}",

            "icon": "🏢",

            "status": "Healthy"

        })

        return ratios