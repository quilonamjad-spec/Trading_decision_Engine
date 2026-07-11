"""
=========================================================
Trade Decision Engine (TDE)

Stock Card
Version : P2.0
=========================================================
"""

import streamlit as st
from ui.components.chart import MiniChart

class StockCard:

    def render(
        self,
        ticker,
        company,
        price,
        change,
        change_percent,
        trend,
        momentum,
        risk,
        df,
    ):

        # --------------------------
        # Card Container
        # --------------------------

        with st.container(border=True):

            # ==========================
            # Header
            # ==========================

            left, right = st.columns([4, 1])

            with left:
                st.subheader(ticker)
                st.caption(company)

            with right:
                st.markdown(
                    """
                    <div style="
                        background:#FEF3C7;
                        color:#92400E;
                        text-align:center;
                        padding:6px;
                        border-radius:12px;
                        font-weight:bold;">
                        WATCH
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # ==========================
            # Price
            # ==========================
            st.markdown(
                f"""
                <div style="
                    font-size:32px;
                    font-weight:700;
                    color:white;
                    margin-bottom:4px;
                ">
                    ₹ {price:,.2f}
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Price Change

            color = "#22C55E" if change >= 0 else "#EF4444"
            arrow = "▲" if change >= 0 else "▼"

            st.markdown(
                f"""
                <div style="
                color:{color};
                font-size:15px;
                font-weight:600;
                margin-bottom:8px;
                ">
                    {arrow} {abs(change):.2f} ({change_percent:.2f}%)
                </div>
                """,
                unsafe_allow_html=True,
            )
          

            # ==========================
            # Chart Placeholder
            # ==========================
            
            chart = MiniChart()

            fig = chart.render(df)

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displayModeBar": False
                },
            )

            st.divider()

            # ==========================
            # Analysis
            # ==========================

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### 📈")
                st.caption("TREND")
                st.write(trend)

            with col2:
                st.markdown("### 🚀")
                st.caption("MOMENTUM")
                st.write(momentum)

            with col3:
                st.markdown("### ⚖")
                st.caption("RISK")
                st.write(risk)

            st.divider()

            st.caption("Click card for detailed analysis (Coming Soon)")
