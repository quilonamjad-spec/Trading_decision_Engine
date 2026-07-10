"""
=========================================================
Trade Decision Engine (TDE)

Reusable Stock Card
Version : P1.2
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

        change_class = (
            "stock-change-green"
            if change >= 0
            else "stock-change-red"
        )

        change_arrow = "▲" if change >= 0 else "▼"

        st.markdown(
            f"""
<div class="stock-card">

    <div style="display:flex;
                justify-content:space-between;
                align-items:center;">

        <div>

            <div class="stock-title">

                {ticker}

            </div>

            <div class="stock-subtitle">

                {company}

            </div>

        </div>

        <div style="
            background:#F3F4F6;
            padding:8px 14px;
            border-radius:20px;
            font-weight:600;
            font-size:13px;">

            WATCH

        </div>

    </div>


    <div class="stock-price">

        ₹ {price:.2f}

    </div>

    <div class="{change_class}">

        {change_arrow}
        {abs(change):.2f}
        ({change_percent:.2f}%)

    </div>


    <hr>


    <div style="
        height:130px;
        border:1px dashed #D1D5DB;
        border-radius:12px;
        display:flex;
        justify-content:center;
        align-items:center;
        color:#9CA3AF;
        margin-bottom:20px;">

        Mini Candlestick Chart

    </div>


    <div class="section-title">

        📈 TREND

    </div>

    <div class="section-text">

        {trend}

    </div>


    <hr>


    <div class="section-title">

        🚀 MOMENTUM

    </div>

    <div class="section-text">

        {momentum}

    </div>


    <hr>


    <div class="section-title">

        ⚖ RISK

    </div>

    <div class="section-text">

        {risk}

    </div>

</div>

""",
            unsafe_allow_html=True,
        )
