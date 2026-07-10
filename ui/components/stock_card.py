"""
=========================================================
Trade Decision Engine (TDE)

Stock Card
Version : P2.0
=========================================================
"""

import streamlit as st


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

            st.markdown(f"## ₹ {price:.2f}")

            if change >= 0:
                st.success(f"▲ {change:.2f} ({change_percent:.2f}%)")
            else:
                st.error(f"▼ {abs(change):.2f} ({change_percent:.2f}%)")

            st.divider()

            # ==========================
            # Chart Placeholder
            # ==========================

            st.info("📈 Mini Candlestick Chart (Coming Next)")

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
