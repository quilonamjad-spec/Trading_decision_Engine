import streamlit as st


class QualityBadge:

    def render(self, status: str):

        badge = {
            "READY": (
                "#1E8E3E",
                "🟢 READY"
            ),

            "READY (Minor Concerns)": (
                "#D4A017",
                "🟡 READY (Minor Concerns)"
            ),

            "READY (High Risk)": (
                "#E67E22",
                "🟠 READY (High Risk)"
            ),

            "WAIT": (
                "#1976D2",
                "🔵 WAIT"
            ),

            "AVOID": (
                "#C62828",
                "🔴 AVOID"
            )
        }

        color, text = badge.get(
            status,
            ("#757575", "⚪ UNKNOWN")
        )

        st.markdown(
            f"""
            <div style="
                background:{color};
                color:white;
                padding:12px;
                border-radius:14px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                letter-spacing:0.5px;
                margin-top:8px;
                margin-bottom:12px;
                box-shadow:0 2px 6px rgba(0,0,0,0.15);
            ">
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )
