import streamlit as st


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Market Scanner",
    page_icon="📈",
    layout="wide"
)


# ==========================================================
# Header
# ==========================================================

def draw_header():

    st.title("📈 Market Scanner")
    st.caption("Find today's highest quality trading opportunities.")


# ==========================================================
# Controls
# ==========================================================

def draw_controls():

    col1, col2 = st.columns([3, 1])

    with col1:

        universe = st.selectbox(
            "Select Universe",
            [
                "Nifty 50",
                "Nifty 100",
                "Nifty 500"
            ],
            index=2
        )

    with col2:

        st.write("")
        st.write("")

        scan = st.button(
            "🚀 Scan Market",
            use_container_width=True
        )

    return universe, scan


# ==========================================================
# Results Placeholder
# ==========================================================

def draw_placeholder():

    st.divider()

    st.info(
        "Press 'Scan Market' to analyse today's opportunities."
    )


# ==========================================================
# Main
# ==========================================================

def main():

    draw_header()

    universe, scan = draw_controls()

    if scan:

        st.success(f"Scanning {universe}...")

    else:

        draw_placeholder()


if __name__ == "__main__":

    main()
