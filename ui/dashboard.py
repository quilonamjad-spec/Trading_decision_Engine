import streamlit as st


class Dashboard:

    def show_stock_card(self, ticker, analysis):

        trend = analysis["trend"]
        momentum = analysis["momentum"]
        risk = analysis["risk"]

        with st.container(border=True):

            st.subheader(ticker)

            st.metric(
                "Current Price",
                f"₹ {trend['values']['price']}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("### 📈 Trend")

                st.write(trend["analysis"]["alignment"])

                st.caption(trend["analysis"]["price_vs_ema20"])

                st.caption(
                    f"{trend['analysis']['distance_ema20_pct']} %"
                )

            with col2:

                st.markdown("### 🚀 Momentum")

                st.write(
                    momentum["analysis"]["momentum_bias"]
                )

                st.caption(
                    momentum["analysis"]["histogram_state"]
                )

                st.caption(
                    momentum["analysis"]["strength"]
                )

            with col3:

                st.markdown("### ⚖ Risk")

                st.write(
                    risk["analysis"]["zone"]
                )

                st.caption(
                    f"RSI : {risk['values']['rsi']}"
                )

                st.caption(
                    f"Risk : {risk['analysis']['risk']}"
                )
