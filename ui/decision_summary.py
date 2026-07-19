import streamlit as st


def draw_decision_summary(stock):

    with st.container(border=True):

        col1, col2 = st.columns([12, 1])

        with col1:
            st.subheader("📊 Decision Summary")

        with col2:
            if st.button("✖", key="close_summary"):
                st.session_state.selected_stock = None
                st.rerun()

        st.divider()

        st.header(stock["ticker"])

        st.metric(
            "Trade Quality",
            f"{stock['score']}/100"
        )

        st.success(f"Recommendation : {stock['status']}")

        st.divider()

        st.subheader("Why this stock?")

        st.write("✔ Placeholder for Engine Explanation")

        st.write("✔ Placeholder for Indicator Summary")

        st.write("✔ Placeholder for Risk Assessment")

        st.divider()

        st.subheader("Warnings")

        st.info("None")
