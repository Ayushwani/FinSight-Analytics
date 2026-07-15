class HealthService:

    def __init__(self, report):

        self.report = report

    ##########################################################

    def calculate(self):

        score = 0

        ##############################################
        # Deposit Growth (20 Marks)
        ##############################################

        dg = self.report["Deposit Growth"]

        if dg >= 10:
            score += 20
        elif dg >= 5:
            score += 16
        elif dg >= 0:
            score += 12
        elif dg >= -5:
            score += 8
        else:
            score += 4

        ##############################################
        # Loan Growth (15 Marks)
        ##############################################

        lg = self.report["Loan Growth"]

        if 5 <= lg <= 15:
            score += 15
        elif 0 <= lg < 5:
            score += 12
        elif 15 < lg <= 20:
            score += 10
        else:
            score += 6

        ##############################################
        # Profit Growth (20 Marks)
        ##############################################

        profit_growth = (
            (
                self.report["Current Profit"]
                - self.report["FY Profit"]
            )
            /
            self.report["FY Profit"]
        ) * 100

        if profit_growth >= 20:
            score += 20
        elif profit_growth >= 10:
            score += 16
        elif profit_growth >= 0:
            score += 12
        else:
            score += 5

        ##############################################
        # CD Ratio (20 Marks)
        ##############################################

        cd = self.report["CD Ratio"]

        if 60 <= cd <= 80:
            score += 20
        elif 50 <= cd < 60:
            score += 16
        elif 80 < cd <= 90:
            score += 14
        else:
            score += 8

        ##############################################
        # CRR (10 Marks)
        ##############################################

        if self.report["CRR Difference"] >= 0:
            score += 10

        ##############################################
        # SLR (10 Marks)
        ##############################################

        if self.report["SLR Difference"] >= 0:
            score += 10

        ##############################################
        # Share Growth (5 Marks)
        ##############################################

        sg = self.report["Share Growth"]

        if sg >= 5:
            score += 5
        elif sg >= 0:
            score += 4
        else:
            score += 2

        ##############################################

        if score >= 90:

            rating = "Excellent"

            color = "#16A34A"

            emoji = "🟢"

        elif score >= 75:

            rating = "Very Good"

            color = "#22C55E"

            emoji = "🟢"

        elif score >= 60:

            rating = "Good"

            color = "#F59E0B"

            emoji = "🟡"

        elif score >= 40:

            rating = "Average"

            color = "#F97316"

            emoji = "🟠"

        else:

            rating = "Needs Attention"

            color = "#DC2626"

            emoji = "🔴"

        return {

            "score": score,

            "rating": rating,

            "color": color,

            "emoji": emoji

        }