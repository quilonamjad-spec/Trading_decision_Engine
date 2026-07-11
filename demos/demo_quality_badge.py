import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st

from ui.components.quality_badge import QualityBadge

st.set_page_config(layout="centered")

badge = QualityBadge()

st.title("Quality Badge Demo")

badge.render("READY")
badge.render("READY (Minor Concerns)")
badge.render("READY (High Risk)")
badge.render("WAIT")
badge.render("AVOID")
