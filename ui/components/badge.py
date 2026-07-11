"""
=========================================================
Trade Decision Engine (TDE)

Reusable Status Badge
Version : P2.3
=========================================================
"""

import streamlit as st


class Badge:

    COLORS = {

        "red": (
            "#FEE2E2",
            "#B91C1C",
        ),

        "green": (
            "#DCFCE7",
            "#166534",
        ),

        "yellow": (
            "#FEF3C7",
            "#92400E",
        ),

        "blue": (
            "#DBEAFE",
            "#1D4ED8",
        ),

        "gray": (
            "#E5E7EB",
            "#374151",
        ),

    }

    def render(self, text, color="gray"):

        bg, fg = self.COLORS.get(
            color,
            self.COLORS["gray"],
        )

        st.markdown(
            f"""
            <div style="
                display:inline-block;
                padding:6px 14px;
                border-radius:20px;
                background:{bg};
                color:{fg};
                font-size:14px;
                font-weight:600;
                text-align:center;
            ">
                {text}
            </div>
            """,
            unsafe_allow_html=True,
        )
