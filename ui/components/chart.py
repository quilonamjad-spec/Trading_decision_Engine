"""
=========================================================
Trade Decision Engine (TDE)

Mini Candlestick Chart
Version : P2.1
=========================================================
"""

import plotly.graph_objects as go


class MiniChart:

    def render(self, df):

        """
        Returns a compact Plotly candlestick chart.
        """

        # Last 20 candles only
        data = df.tail(20).copy()

        # ----------------------------
        # Candlestick
        # ----------------------------

        fig = go.Figure()

        fig.add_trace(

            go.Candlestick(

                x=data.index,

                open=data["Open"],

                high=data["High"],

                low=data["Low"],

                close=data["Close"],

                increasing_line_color="#22C55E",

                decreasing_line_color="#EF4444",

                increasing_fillcolor="#22C55E",

                decreasing_fillcolor="#EF4444",

                name="Price",

            )

        )

        # ----------------------------
        # EMA20 Overlay
        # ----------------------------

        if "EMA20" in data.columns:

            fig.add_trace(

                go.Scatter(

                    x=data.index,

                    y=data["EMA20"],

                    mode="lines",

                    line=dict(

                        color="#3B82F6",

                        width=2,

                    ),

                    name="EMA20",

                )

            )

        # ----------------------------
        # Layout
        # ----------------------------

        fig.update_layout(

            height=170,

            margin=dict(

                l=0,

                r=0,

                t=0,

                b=0,

            ),

            paper_bgcolor="#0E1117",

            plot_bgcolor="#0E1117",

            showlegend=False,

            xaxis=dict(

                visible=False,

                rangeslider=dict(visible=False),

            ),

            yaxis=dict(

                visible=False,

            ),

        )

        return fig
