class RecommendationService:

    def __init__(self, report):
        self.report = report

    # --------------------------------------------------

    def generate(self):

        recommendations = []

        # ----------------------------------------
        # Deposit Growth
        # ----------------------------------------

        if self.report["Deposit Growth"] < 5:

            recommendations.append({

                "icon": "🏦",

                "title": "Improve Deposit Growth",

                "priority": "High",

                "color": "#DC2626",

                "message": (
                    "Deposit growth is below the desired level. "
                    "Focus on CASA deposits, new customer acquisition "
                    "and deposit campaigns."
                )

            })

        else:

            recommendations.append({

                "icon": "✅",

                "title": "Deposit Growth",

                "priority": "Low",

                "color": "#16A34A",

                "message": (
                    "Deposit growth is healthy. Continue current deposit strategy."
                )

            })

        # ----------------------------------------
        # Loan Growth
        # ----------------------------------------

        if self.report["Loan Growth"] < 0:

            recommendations.append({

                "icon": "💳",

                "title": "Increase Lending",

                "priority": "Medium",

                "color": "#F59E0B",

                "message": (
                    "Loan portfolio has declined. Consider expanding "
                    "retail and MSME lending."
                )

            })

        else:

            recommendations.append({

                "icon": "✅",

                "title": "Loan Portfolio",

                "priority": "Low",

                "color": "#16A34A",

                "message": (
                    "Loan growth is satisfactory."
                )

            })

        # ----------------------------------------
        # Profit
        # ----------------------------------------

        profit_growth = (

            (

                self.report["Current Profit"]

                - self.report["FY Profit"]

            )

            / self.report["FY Profit"]

        ) * 100

        if profit_growth < 0:

            recommendations.append({

                "icon": "📉",

                "title": "Improve Profitability",

                "priority": "High",

                "color": "#DC2626",

                "message": (
                    "Profit has declined. Review operating expenses "
                    "and improve interest income."
                )

            })

        else:

            recommendations.append({

                "icon": "📈",

                "title": "Profitability",

                "priority": "Low",

                "color": "#16A34A",

                "message": (
                    "Profit trend is healthy."
                )

            })

        # ----------------------------------------
        # CD Ratio
        # ----------------------------------------

        cd = self.report["CD Ratio"]

        if cd < 60:

            recommendations.append({

                "icon": "📊",

                "title": "Increase Credit Utilization",

                "priority": "Medium",

                "color": "#2563EB",

                "message": (
                    "Credit Deposit Ratio is conservative. "
                    "The bank has additional lending capacity."
                )

            })

        elif cd > 90:

            recommendations.append({

                "icon": "⚠️",

                "title": "Reduce Liquidity Risk",

                "priority": "High",

                "color": "#DC2626",

                "message": (
                    "Credit Deposit Ratio is high. "
                    "Monitor liquidity and funding position."
                )

            })

        else:

            recommendations.append({

                "icon": "✅",

                "title": "CD Ratio",

                "priority": "Low",

                "color": "#16A34A",

                "message": (
                    "Credit Deposit Ratio is within the recommended range."
                )

            })

        # ----------------------------------------
        # CRR
        # ----------------------------------------

        if self.report["CRR Difference"] < 0:

            recommendations.append({

                "icon": "🏛",

                "title": "Maintain CRR",

                "priority": "Critical",

                "color": "#B91C1C",

                "message": (
                    "Available CRR is below the required level. "
                    "Immediate action is required."
                )

            })

        # ----------------------------------------
        # SLR
        # ----------------------------------------

        if self.report["SLR Difference"] < 0:

            recommendations.append({

                "icon": "🏛",

                "title": "Maintain SLR",

                "priority": "Critical",

                "color": "#B91C1C",

                "message": (
                    "Available SLR is below the required level. "
                    "Immediate corrective action is recommended."
                )

            })

        return recommendations