import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
import streamlit as st

from ui.components.quality_badge import QualityBadge

badge = QualityBadge()

st.title("Quality Badge Demo")

badge.render("READY")

badge.render("READY (Minor Concerns)")

badge.render("READY (High Risk)")

badge.render("WAIT")

badge.render("AVOID")
