import streamlit as st

from ui.components.quality_badge import QualityBadge
from ui.components.chart import MiniChart


class StockCard:

    def __init__(self):

        self.badge = QualityBadge()
        self.chart = MiniChart()

    # ---------------------------------------------------

    def render(

        self,

        ticker,
        company,

        price,
        change,
        pct_change,

        trade,

        df

    ):

        with st.container(border=True):

            # ==========================================
            # Header
            # ==========================================

            col1, col2 = st.columns([4,1])

            with col1:

                st.markdown(

                    f"""
                    <div style="font-size:28px;
                                font-weight:700;
                                color:white;">
                        {ticker}
                    </div>

                    <div style="font-size:14px;
                                color:#BDBDBD;">
                        {company}
                    </div>
                    """,

                    unsafe_allow_html=True

                )

            with col2:

                st.button(
                    "★",
                    key=f"watch_{ticker}",
                    use_container_width=True
                )

            st.markdown("")

            # ==========================================
            # Price
            # ==========================================

            colour = "#2ECC71" if change >= 0 else "#E74C3C"

            arrow = "▲" if change >= 0 else "▼"

            st.markdown(

                f"""
                <div style="font-size:40px;
                            font-weight:700;
                            color:white;">

                    ₹ {price:,.2f}

                </div>

                <div style="font-size:18px;
                            color:{colour};">

                    {arrow} {abs(change):.2f}
                    ({pct_change:.2f}%)

                </div>
                """,

                unsafe_allow_html=True

            )

            st.markdown("")

            # ==========================================
            # Quality Badge
            # ==========================================

            self.badge.render(
                trade["status"]
            )

            # ==========================================
            # Trade Score
            # ==========================================

            st.markdown(

                f"""
                <div style="text-align:center;
                            margin-top:10px;">

                    <div style="
                        font-size:32px;
                        font-weight:700;
                        color:#FFD54F;">

                        {trade["grade"]}

                    </div>

                    <div style="
                        font-size:48px;
                        font-weight:800;
                        color:white;">

                        {trade["score"]}/100

                    </div>

                    <div style="
                        font-size:22px;
                        color:#FFD54F;">

                        {trade["stars"]}

                    </div>

                    <div style="
                        font-size:14px;
                        color:#AAAAAA;
                        letter-spacing:1px;">

                        TRADE QUALITY

                    </div>

                </div>

                """,

                unsafe_allow_html=True

            )

            st.divider()
