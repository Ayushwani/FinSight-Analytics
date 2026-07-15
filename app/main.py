from app.services.summary_service import SummaryService
from app.services.health_service import HealthService

from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import shutil

from datetime import datetime

from app.parsers.parser import parse_spl_file
from app.services.financial_calculator import FinancialCalculator
from app.services.chart_service import ChartService

from app.utils.formatter import (
    format_currency,
    format_percentage
)

app = FastAPI(title="Visualization Tool")

# -------------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)

UPLOAD_FOLDER = "app/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# -------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# -------------------------------------------------------

@app.post("/upload", response_class=HTMLResponse)
async def upload_files(

        request: Request,

        fy_file: UploadFile = File(...),
        current_file: UploadFile = File(...),

        ndtl: float = Form(...),

        crr_percent: float = Form(...),

        slr_percent: float = Form(...)
):

    fy_path = os.path.join(
        UPLOAD_FOLDER,
        fy_file.filename
    )

    current_path = os.path.join(
        UPLOAD_FOLDER,
        current_file.filename
    )

    with open(fy_path, "wb") as f:
        shutil.copyfileobj(
            fy_file.file,
            f
        )

    with open(current_path, "wb") as f:
        shutil.copyfileobj(
            current_file.file,
            f
        )

    # ---------------------------------------------------

    fy_data = parse_spl_file(fy_path)

    current_data = parse_spl_file(current_path)

    # ---------------------------------------------------

    calculator = FinancialCalculator(
        fy_data,
        current_data,
        ndtl,
        crr_percent,
        slr_percent
    )

    report = calculator.calculate()

    # ---------------------------------------------------
    # Charts
    # ---------------------------------------------------

    charts = ChartService(report)

    comparison_chart = charts.financial_comparison()

    growth_chart = charts.growth_chart()

    liquidity_chart = charts.liquidity_chart()

    # ---------------------------------------------------
    # Executive Summary
    # ---------------------------------------------------

    summary = SummaryService(report).generate()

    # ---------------------------------------------------
    # Overall Health Score
    # ---------------------------------------------------

    health = HealthService(report).calculate()

    # ---------------------------------------------------
    # AI Insights
    # ---------------------------------------------------

    insights = []

    if report["Deposit Growth"] > 0:
        insights.append(
            f"Deposits increased by {report['Deposit Growth']:.2f}% compared to FY."
        )
    else:
        insights.append(
            f"Deposits decreased by {abs(report['Deposit Growth']):.2f}% compared to FY."
        )

    if report["Loan Growth"] > 0:
        insights.append(
            f"Loan portfolio grew by {report['Loan Growth']:.2f}%."
        )
    else:
        insights.append(
            f"Loan portfolio declined by {abs(report['Loan Growth']):.2f}%."
        )

    profit_growth = (
        (
            report["Current Profit"]
            - report["FY Profit"]
        )
        / report["FY Profit"]
    ) * 100

    if profit_growth > 0:
        insights.append(
            f"Profit improved by {profit_growth:.2f}%."
        )
    else:
        insights.append(
            f"Profit reduced by {abs(profit_growth):.2f}%."
        )

    if report["CD Ratio"] < 60:
        insights.append(
            "Credit Deposit Ratio is conservative. Bank has lending capacity."
        )

    elif report["CD Ratio"] < 80:
        insights.append(
            "Credit Deposit Ratio is within the healthy range."
        )

    else:
        insights.append(
            "Credit Deposit Ratio is high. Liquidity should be monitored."
        )

    if report["CRR Difference"] >= 0:
        insights.append(
            "CRR requirement is fully maintained."
        )
    else:
        insights.append(
            "CRR requirement is NOT maintained."
        )
    if report["SLR Difference"] >= 0:
        insights.append(
            "SLR requirement is fully maintained."
         )
    else:
        insights.append(
            "SLR requirement is NOT maintained."
     )

    # ---------------------------------------------------
    # Performance Summary
    # ---------------------------------------------------

    performance = []

    performance.append(
        "🟢 Deposits Growing"
        if report["Deposit Growth"] > 0
        else "🔴 Deposits Declining"
    )

    performance.append(
        "🟢 Loans Growing"
        if report["Loan Growth"] > 0
        else "🔴 Loans Declining"
    )

    performance.append(
        "🟢 Healthy CD Ratio"
        if 60 <= report["CD Ratio"] <= 80
        else "🟡 Review CD Ratio"
    )

    performance.append(
        "🟢 CRR Maintained"
        if report["CRR Difference"] >= 0
        else "🔴 CRR Shortfall"
    )

    performance.append(
        "🟢 SLR Maintained"
         if report["SLR Difference"] >= 0
        else "🔴 SLR Shortfall"
    )

    # ---------------------------------------------------
    # Format Values
    # ---------------------------------------------------

    display = report.copy()

    currency_fields = [

        "FY Deposits",
        "Current Deposits",

        "FY Loans",
        "Current Loans",

        "FY Share Capital",
        "Current Share Capital",

        "FY Profit",
        "Current Profit",

        "Cash",

        "Investments",

        "Working Capital",

        "Required CRR",
        "Available CRR",
        "CRR Difference",

        "Required SLR",
        "Available SLR",
        "SLR Difference"

    ]

    percentage_fields = [

        "CD Ratio",

        "Deposit Growth",

        "Loan Growth",

        "Share Growth"

    ]

    for key in currency_fields:

        if key in display:

            display[key] = format_currency(
                display[key]
            )

    for key in percentage_fields:

        if key in display:

            display[key] = format_percentage(
                display[key]
            )

    # ---------------------------------------------------
    generated_time = datetime.now().strftime(
    "%d %B %Y, %I:%M %p"
)
    
    return templates.TemplateResponse(

        request=request,

        name="dashboard.html",

        context={

            "analysis": display,

            "comparison_chart": comparison_chart,

            "growth_chart": growth_chart,

            "liquidity_chart": liquidity_chart,

            "summary": summary,

            "health": health,

            "insights": insights,

            "performance": performance,

            "generated_time": generated_time

        }

    )