class ComplianceService:

    def __init__(self, report):
        self.report = report

    def generate(self):

        compliance = []

        # -----------------------------
        # CRR
        # -----------------------------

        if self.report["CRR Difference"] >= 0:

            crr_status = "Maintained"
            crr_color = "#16a34a"
            crr_icon = "✅"

        else:

            crr_status = "Shortfall"
            crr_color = "#dc2626"
            crr_icon = "❌"

        compliance.append({

            "title": "Cash Reserve Ratio (CRR)",

            "required": self.report["Required CRR"],

            "available": self.report["Available CRR"],

            "difference": self.report["CRR Difference"],

            "status": crr_status,

            "color": crr_color,

            "icon": crr_icon

        })

        # -----------------------------
        # SLR
        # -----------------------------

        if self.report["SLR Difference"] >= 0:

            slr_status = "Maintained"
            slr_color = "#16a34a"
            slr_icon = "✅"

        else:

            slr_status = "Shortfall"
            slr_color = "#dc2626"
            slr_icon = "❌"

        compliance.append({

            "title": "Statutory Liquidity Ratio (SLR)",

            "required": self.report["Required SLR"],

            "available": self.report["Available SLR"],

            "difference": self.report["SLR Difference"],

            "status": slr_status,

            "color": slr_color,

            "icon": slr_icon

        })

        return compliance