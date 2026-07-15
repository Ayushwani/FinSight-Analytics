class FinancialCalculator:

    def __init__(self, fy, current, ndtl, crr, slr):

        self.fy = fy
        self.current = current

        self.ndtl = ndtl
        self.crr = crr
        self.slr = slr

    ###########################################################

    def get_section_total(self, data, section):

        if section not in data["sections"]:
            return 0

        return data["sections"][section]["total"]

    ###########################################################

    def get_account(self, data, section, account):

        if section not in data["sections"]:
            return 0

        accounts = data["sections"][section]["accounts"]

        return accounts.get(account, 0)

    ###########################################################

    def calculate(self):

        result = {}

        ###################################################
        # Deposits
        ###################################################

        result["FY Deposits"] = self.get_section_total(
            self.fy,
            "L03"
        )

        result["Current Deposits"] = self.get_section_total(
            self.current,
            "L03"
        )

        ###################################################
        # Loans
        ###################################################

        result["FY Loans"] = self.get_section_total(
            self.fy,
            "A21"
        )

        result["Current Loans"] = self.get_section_total(
            self.current,
            "A21"
        )

        ###################################################
        # Share Capital
        ###################################################

        result["FY Share Capital"] = self.get_section_total(
            self.fy,
            "L01"
        )

        result["Current Share Capital"] = self.get_section_total(
            self.current,
            "L01"
        )

        ###################################################
        # Profit
        ###################################################

        result["FY Profit"] = self.get_section_total(
            self.fy,
            "L99"
        )

        result["Current Profit"] = self.get_section_total(
            self.current,
            "L99"
        )

        ###################################################
        # Cash
        ###################################################

        result["Cash"] = self.get_section_total(
            self.current,
            "A01"
        )

        ###################################################
        # Investments
        ###################################################

        investments = 0

        for code in ["A10", "A11", "A13"]:

            investments += self.get_section_total(
                self.current,
                code
            )

        result["Investments"] = investments

        ###################################################
        # Working Capital
        ###################################################

        result["Working Capital"] = (
            result["Current Deposits"]
            +
            result["Current Share Capital"]
        )

        ###################################################
        # CD Ratio
        ###################################################

        if result["Current Deposits"]:

            result["CD Ratio"] = round(

                result["Current Loans"]
                /
                result["Current Deposits"]
                *
                100,

                2

            )

        else:

            result["CD Ratio"] = 0

        ###################################################
        # Deposit Growth
        ###################################################

        if result["FY Deposits"]:

            result["Deposit Growth"] = round(

                (
                    result["Current Deposits"]
                    -
                    result["FY Deposits"]
                )
                /
                result["FY Deposits"]
                *
                100,

                2

            )

        else:

            result["Deposit Growth"] = 0

        ###################################################
        # Loan Growth
        ###################################################

        if result["FY Loans"]:

            result["Loan Growth"] = round(

                (
                    result["Current Loans"]
                    -
                    result["FY Loans"]
                )
                /
                result["FY Loans"]
                *
                100,

                2

            )

        else:

            result["Loan Growth"] = 0

        ###################################################
        # Share Growth
        ###################################################

        if result["FY Share Capital"]:

            result["Share Growth"] = round(

                (
                    result["Current Share Capital"]
                    -
                    result["FY Share Capital"]
                )
                /
                result["FY Share Capital"]
                *
                100,

                2

            )

        else:

            result["Share Growth"] = 0

        ###################################################
        # CRR
        ###################################################

        result["Required CRR"] = round(

            self.ndtl
            *
            self.crr
            /
            100,

            2

        )

        result["Available CRR"] = result["Cash"]

        result["CRR Difference"] = round(

            result["Available CRR"]
            -
            result["Required CRR"],

            2

        )

        ###################################################
        # SLR
        ###################################################

        result["Required SLR"] = round(

            self.ndtl
            *
            self.slr
            /
            100,

            2

        )

        result["Available SLR"] = result["Investments"]

        result["SLR Difference"] = round(

            result["Available SLR"]
            -
            result["Required SLR"],

            2

        )

        return result
    ###########################################################
    # Generate Final Report
    ###########################################################

    def generate_report(self):

        analysis = self.calculate()

        return {
            "message": "Financial Analysis Completed Successfully",
            "Analysis": analysis
        }