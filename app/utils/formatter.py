def format_currency(value):

    try:
        return f"₹ {value:,.2f}"

    except:
        return value


def format_percentage(value):

    try:
        return f"{value:.2f}%"

    except:
        return value


def format_number(value):

    try:
        return f"{value:,.2f}"

    except:
        return value