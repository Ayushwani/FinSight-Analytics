def find_value(data, keywords):
    """
    Search dictionary for keywords.
    Returns first matching value.
    """

    for key, value in data.items():

        key_upper = key.upper()

        for keyword in keywords:

            if keyword.upper() in key_upper:
                return value

    return 0


def calculate_growth(old_value, current_value):

    if old_value == 0:
        return 0

    return ((current_value - old_value) / old_value) * 100


def calculate_all_ratios(
        fy_data,
        current_data,
        ndtl,
        crr_percent,
        slr_percent
):

    results = {}

    # ---------------------------------------------------
    # SHARE CAPITAL
    # ---------------------------------------------------

    fy_share_capital = find_value(
        fy_data,
        [
            "CAPITAL TOTAL",
            "SHARE CAPITAL",
            "PAID UP SHARE"
        ]
    )

    current_share_capital = find_value(
        current_data,
        [
            "CAPITAL TOTAL",
            "SHARE CAPITAL",
            "PAID UP SHARE"
        ]
    )

    # ---------------------------------------------------
    # DEPOSITS
    # ---------------------------------------------------

    fy_deposit = find_value(
    fy_data,
    [
        "TOTAL DEPOSITS",
        "DEPOSITS",
        "CURRENT DEPOSIT",
        "SAVING DEPOSIT"
    ]
)

    current_deposit = find_value(
    current_data,
    [
        "TOTAL DEPOSITS",
        "DEPOSITS",
        "CURRENT DEPOSIT",
        "SAVING DEPOSIT"
    ]
)

    # ---------------------------------------------------
    # LOANS
    # ---------------------------------------------------

    fy_loan = find_value(
    fy_data,
    [
        "TOTAL LOANS",
        "LOAN",
        "ADVANCE",
        "CASH CREDIT"
    ]
)

    current_loan = find_value(
    current_data,
    [
        "TOTAL LOANS",
        "LOAN",
        "ADVANCE",
        "CASH CREDIT"
    ]
)

    # ---------------------------------------------------
    # PROFIT
    # ---------------------------------------------------

    fy_profit = find_value(
        fy_data,
        [
            "PROFIT",
            "NET PROFIT"
        ]
    )

    current_profit = find_value(
        current_data,
        [
            "PROFIT",
            "NET PROFIT"
        ]
    )

    # ---------------------------------------------------
    # WORKING CAPITAL
    # ---------------------------------------------------

    trial_balance_total = sum(current_data.values())

    ain = find_value(
        current_data,
        ["AIN INTEREST RECEIVABLE ON NPA"]
    )

    account_802 = find_value(
        current_data,
        ["DEPOSIT UNCLAIM RECEIVABLE"]
    )

    account_92 = find_value(
        current_data,
        ["BANK GUARANTEE RECEIVABLE"]
    )

    account_147 = find_value(
        current_data,
        ["ADVANCE INCOME TAX"]
    )

    contra_total = (
            ain +
            account_802 +
            account_92 +
            account_147
    )

    working_capital = (
            trial_balance_total -
            contra_total
    )

    # ---------------------------------------------------
    # CD RATIO
    # ---------------------------------------------------

    if current_deposit != 0:

        cd_ratio = (
                           current_loan /
                           current_deposit
                   ) * 100

    else:
        cd_ratio = 0

    # ---------------------------------------------------
    # GROWTH %
    # ---------------------------------------------------

    deposit_growth = calculate_growth(
        fy_deposit,
        current_deposit
    )

    loan_growth = calculate_growth(
        fy_loan,
        current_loan
    )

    share_growth = calculate_growth(
        fy_share_capital,
        current_share_capital
    )

    # ---------------------------------------------------
    # CRR
    # ---------------------------------------------------

    required_crr = (
            ndtl *
            (crr_percent / 100)
    )

    a01 = find_value(
        current_data,
        ["CASH IN HAND"]
    )

    a02 = find_value(
        current_data,
        ["BALANCE WITH RBI"]
    )

    a03 = find_value(
        current_data,
        ["BALANCE WITH OTHER BANK"]
    )

    available_crr = (
            a01 +
            a02 +
            a03
    )

    crr_difference = (
            available_crr -
            required_crr
    )

    # ---------------------------------------------------
    # SLR
    # ---------------------------------------------------

    required_slr = (
            ndtl *
            (slr_percent / 100)
    )

    a13 = find_value(
        current_data,
        [
            "INVESTMENT",
            "SLR"
        ]
    )

    slr_difference = (
            a13 -
            required_slr
    )

    # ---------------------------------------------------
    # STORE RESULTS
    # ---------------------------------------------------

    results["FY Deposit"] = fy_deposit
    results["Current Deposit"] = current_deposit

    results["FY Loan"] = fy_loan
    results["Current Loan"] = current_loan

    results["FY Share Capital"] = fy_share_capital
    results["Current Share Capital"] = current_share_capital

    results["CD Ratio %"] = round(cd_ratio, 2)

    results["Deposit Growth %"] = round(
        deposit_growth,
        2
    )

    results["Loan Growth %"] = round(
        loan_growth,
        2
    )

    results["Share Growth %"] = round(
        share_growth,
        2
    )

    results["Working Capital"] = round(
        working_capital,
        2
    )

    results["Required CRR"] = round(
        required_crr,
        2
    )

    results["Available CRR"] = round(
        available_crr,
        2
    )

    results["CRR Difference"] = round(
        crr_difference,
        2
    )

    results["Required SLR"] = round(
        required_slr,
        2
    )

    results["Available SLR"] = round(
        a13,
        2
    )

    results["SLR Difference"] = round(
        slr_difference,
        2
    )

    results["FY Profit"] = fy_profit
    results["Current Profit"] = current_profit

    return results