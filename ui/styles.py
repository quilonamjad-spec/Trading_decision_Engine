import streamlit as st


def load_css():

    st.markdown("""

<style>

/* Card */

div[data-testid="stVerticalBlockBorderWrapper"]{

    border-radius:18px;

    border:1px solid #30363d;

    background:#0f1722;

}

/* Metric */

div[data-testid="metric-container"]{

    background:#151d2b;

    border-radius:12px;

    padding:10px;

}

/* Buttons */

.stButton>button{

    width:100%;

    border-radius:10px;

    height:45px;

    font-weight:bold;

}

</style>

""",unsafe_allow_html=True)