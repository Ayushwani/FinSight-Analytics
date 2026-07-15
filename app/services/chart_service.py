import plotly.graph_objects as go
import plotly.express as px


class ChartService:

    def __init__(self, report):
        self.report = report

    ####################################################################
    # COMMON LAYOUT
    ####################################################################

    def _layout(self, title):

        return dict(

            template="plotly_white",

            title=dict(

                text=f"<b>{title}</b>",

                x=0.5,

                xanchor="center",

                font=dict(
                    size=22,
                    color="#1E3A8A"
                )
            ),

            font=dict(
                family="Segoe UI",
                size=14
            ),

            margin=dict(
                l=40,
                r=30,
                t=70,
                b=40
            ),

            hoverlabel=dict(
                bgcolor="white",
                font_size=14
            )
        )

    ####################################################################
    # FINANCIAL COMPARISON
    ####################################################################

    def financial_comparison(self):

        categories = [

            "Deposits",
            "Loans",
            "Profit",
            "Share Capital"

        ]

        fy = [

            self.report["FY Deposits"],
            self.report["FY Loans"],
            self.report["FY Profit"],
            self.report["FY Share Capital"]

        ]

        current = [

            self.report["Current Deposits"],
            self.report["Current Loans"],
            self.report["Current Profit"],
            self.report["Current Share Capital"]

        ]

        fig = go.Figure()

        fig.add_trace(

            go.Bar(

                name="Financial Year",

                x=categories,

                y=fy,

                marker_color="#9CA3AF",

                text=[f"₹ {x:,.0f}" for x in fy],

                textposition="outside",

                hovertemplate="<b>%{x}</b><br>FY : ₹ %{y:,.0f}<extra></extra>"

            )

        )

        fig.add_trace(

            go.Bar(

                name="Current",

                x=categories,

                y=current,

                marker_color="#2563EB",

                text=[f"₹ {x:,.0f}" for x in current],

                textposition="outside",

                hovertemplate="<b>%{x}</b><br>Current : ₹ %{y:,.0f}<extra></extra>"

            )

        )

        fig.update_layout(

            **self._layout("Financial Year vs Current Comparison"),

            barmode="group",

            height=520,

            legend=dict(

                orientation="h",

                y=1.10,

                x=0.30

            )

        )

        return fig.to_html(

            full_html=False,

            include_plotlyjs=False

        )

    ####################################################################
    # GROWTH ANALYSIS
    ####################################################################

    def growth_chart(self):

        labels = [

            "Deposit",

            "Loan",

            "Share Capital"

        ]

        values = [

            self.report["Deposit Growth"],

            self.report["Loan Growth"],

            self.report["Share Growth"]

        ]

        colors = [

            "#16A34A" if x >= 0 else "#DC2626"

            for x in values

        ]

        fig = go.Figure()

        fig.add_trace(

            go.Bar(

                x=labels,

                y=values,

                marker_color=colors,

                text=[f"{x:.2f}%" for x in values],

                textposition="outside",

                hovertemplate="%{x}<br>%{y:.2f}%<extra></extra>"

            )

        )

        fig.add_hline(

            y=0,

            line_dash="dash",

            line_color="black"

        )

        fig.update_layout(

            **self._layout("Growth Analysis"),

            yaxis_title="Growth (%)",

            height=470

        )

        return fig.to_html(

            full_html=False,

            include_plotlyjs=False

        )

    ####################################################################
    # LIQUIDITY
    ####################################################################

    def liquidity_chart(self):

        fig = px.pie(

            names=[

                "Cash",

                "Investments"

            ],

            values=[

                self.report["Cash"],

                self.report["Investments"]

            ],

            hole=.65,

            color_discrete_sequence=[

                "#2563EB",

                "#10B981"

            ]

        )

        fig.update_traces(

            textposition="inside",

            textinfo="percent+label",

            hovertemplate="<b>%{label}</b><br>₹ %{value:,.0f}<extra></extra>"

        )

        fig.update_layout(

            **self._layout("Liquidity Distribution"),

            height=470,

            showlegend=True

        )

        return fig.to_html(

            full_html=False,

            include_plotlyjs=False

        )

    ####################################################################
    # CREDIT DEPOSIT RATIO
    ####################################################################

    def compliance_gauge(self):

        cd = self.report["CD Ratio"]

        value = min(cd, 100)

        if cd < 60:

            bar = "#16A34A"

        elif cd < 80:

            bar = "#EAB308"

        else:

            bar = "#DC2626"

        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=value,

                number=dict(

                    suffix="%",

                    font=dict(size=40)

                ),

                gauge=dict(

                    axis=dict(

                        range=[0, 100]

                    ),

                    bar=dict(

                        color=bar,

                        thickness=0.35

                    ),

                    bgcolor="white",

                    borderwidth=2,

                    bordercolor="#E5E7EB",

                    steps=[

                        dict(

                            range=[0, 60],

                            color="#DCFCE7"

                        ),

                        dict(

                            range=[60, 80],

                            color="#FEF9C3"

                        ),

                        dict(

                            range=[80, 100],

                            color="#FEE2E2"

                        )

                    ]

                )

            )

        )

        fig.update_layout(

            **self._layout("Credit Deposit Ratio"),

            height=430

        )

        return fig.to_html(

            full_html=False,

            include_plotlyjs=False

        )