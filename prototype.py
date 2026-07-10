import streamlit as st
from ui.styles import load_css

load_css()

st.markdown("""

<div class="stock-card">

<div class="stock-title">

SBIN

</div>

<div class="stock-subtitle">

State Bank of India

</div>

<div class="stock-price">

₹1022.60

</div>

<div class="stock-change-red">

▼ -4.60 (-0.45%)

</div>

<hr>

<div class="section-title">

TREND

</div>

<div class="section-text">

Bearish

</div>

</div>

""",unsafe_allow_html=True)
