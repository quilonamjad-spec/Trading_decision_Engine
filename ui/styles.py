"""
====================================================
Trade Decision Engine (TDE)

UI Design System
Version : P1.1
====================================================
"""

import streamlit as st

# ====================================================
# COLOR PALETTE
# ====================================================

PRIMARY = "#2563EB"

SUCCESS = "#16A34A"

WARNING = "#D97706"

DANGER = "#DC2626"

BACKGROUND = "#F5F7FA"

CARD = "#FFFFFF"

BORDER = "#E5E7EB"

TEXT = "#111827"

TEXT_LIGHT = "#6B7280"

SHADOW = "0 4px 12px rgba(0,0,0,0.08)"

# ====================================================
# TYPOGRAPHY
# ====================================================

TITLE_SIZE = "22px"

PRICE_SIZE = "30px"

SECTION_TITLE = "14px"

BODY_SIZE = "13px"

SMALL_SIZE = "12px"

# ====================================================
# CARD
# ====================================================

CARD_RADIUS = "18px"

CARD_PADDING = "20px"

SECTION_GAP = "14px"

# ====================================================
# CSS
# ====================================================


def load_css():

    st.markdown(
        f"""
<style>

/* Entire App */

.main {{

    background-color:{BACKGROUND};

}}

/* Hide Streamlit Footer */

footer {{

visibility:hidden;

}}

header {{

visibility:hidden;

}}

/* Card */

.stock-card {{

background:{CARD};

border:1px solid {BORDER};

border-radius:{CARD_RADIUS};

padding:{CARD_PADDING};

box-shadow:{SHADOW};

transition:0.25s;

margin-bottom:20px;

}}

.stock-card:hover {{

transform:translateY(-4px);

box-shadow:0 10px 24px rgba(0,0,0,0.12);

}}

/* Header */

.stock-title {{

font-size:{TITLE_SIZE};

font-weight:700;

color:{TEXT};

}}

.stock-subtitle {{

font-size:{SMALL_SIZE};

color:{TEXT_LIGHT};

margin-bottom:10px;

}}

/* Price */

.stock-price {{

font-size:{PRICE_SIZE};

font-weight:700;

color:{TEXT};

margin-top:8px;

}}

.stock-change-red {{

color:{DANGER};

font-weight:600;

}}

.stock-change-green {{

color:{SUCCESS};

font-weight:600;

}}

.section-title {{

font-size:{SECTION_TITLE};

font-weight:700;

margin-top:18px;

margin-bottom:8px;

color:{TEXT};

}}

.section-text {{

font-size:{BODY_SIZE};

color:{TEXT_LIGHT};

}}

hr {{

border:none;

height:1px;

background:{BORDER};

margin-top:16px;

margin-bottom:16px;

}}

</style>
""",
        unsafe_allow_html=True,
    )
