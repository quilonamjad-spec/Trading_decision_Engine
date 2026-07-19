
import streamlit as st
import pandas as pd

from ui.components.stock_card_v2 import StockCard


class CommandCenter:
    """
    ============================================================
    Trade Decision Engine
    Command Center v2.0
    ============================================================
    """

    def __init__(self):

        self.card = StockCard()

    # ==========================================================
    # Main Render
    # ==========================================================

    def render(

        self,
    
        dashboard,
    
        dashboard_engine,
    
        market_engine,
    
        trade_engine,
    
        ema,
    
        macd,
    
        rsi
    
    ):

        st.title("Trade Decision Engine")

                # -----------------------------------
                # Engine References
                # -----------------------------------

                self.dashboard = dashboard

                self.dashboard_engine = dashboard_engine

                self.market_engine = market_engine

                self.trade_engine = trade_engine

                self.ema = ema

                self.macd = macd

                self.rsi = rsi

                if "idea_result" not in st.session_state:

                    st.session_state.idea_result = None

                if "idea_ticker" not in st.session_state:

                    st.session_state.idea_ticker = ""

        st.caption("AI Powered Trading Decision Support System")

        st.divider()

        # -----------------------------------
        # Market Overview
        # -----------------------------------

        self.morning_briefing(dashboard)

        st.divider()

        # -----------------------------------
        # Top Opportunities
        # -----------------------------------

        self.today_focus(dashboard)

        st.divider()

        self.my_watch()

        st.divider()

        self.my_ideas()

        st.divider()

        self.keep_an_eye_on(dashboard)

        st.divider()

        # -----------------------------------
        # Ranked Opportunities
        # -----------------------------------

        self.stock_table(dashboard)

        # -----------------------------------
        # Decision Dialog
        # -----------------------------------

        if "selected_stock" in st.session_state:

            self.show_decision_dialog()
    # ==========================================================
    # Market Overview
    # ==========================================================

    def morning_briefing(self, dashboard):

        st.subheader("🌅 Good Morning")

        bias = dashboard.get("market_bias","MIXED")
        confidence = dashboard.get("market_score",0)

        if bias == "BUY":
            st.success(f"🟢 BUY DAY | Confidence : {confidence}/100")
        elif bias == "SELL":
            st.error(f"🔴 SELL DAY | Confidence : {confidence}/100")
        else:
            st.warning(f"🟡 MIXED DAY | Confidence : {confidence}/100")

        st.caption("Today's Focus contains the highest conviction opportunities. Keep an Eye On contains secondary opportunities.")

    # ==========================================================
    # Today's Focus
    # ==========================================================

    def today_focus(self, dashboard):

        st.subheader("🎯 Today's Focus")

        top5 = dashboard["stocks"][:5]
        cols = st.columns(5)

        for col, stock in zip(cols, top5):
            with col:
                with st.container(border=True):
                    ticker = stock["ticker"].replace(".NS","")
                    st.markdown(f"### {ticker}")
                    st.write(stock["status"])
                    st.markdown(f"## {stock['score']}/100")
                    col1, col2 = st.columns(2)

                    with col1:
                        if st.button("🔍 Analyze", key=f"focus_{ticker}"):

                            st.session_state["selected_stock"] = stock
                            st.rerun()

                    with col2:
                        if st.button("⭐ Watch", key=f"watch_{ticker}"):

                            already_exists = any(
                                s["ticker"] == stock["ticker"]
                                for s in st.session_state.watch_list
                            )

                            if not already_exists:
                                st.session_state.watch_list.append(stock)

                            st.rerun()
    # ==========================================================
    # My Watch
    # ==========================================================

    def my_watch(self):

        st.subheader("⭐ My Watch")

        watch = st.session_state.watch_list

        if len(watch) == 0:

            st.info("No stocks added.")

            return

        cols = st.columns(min(5, len(watch)))

        for col, stock in zip(cols, watch):

            with col:

                with st.container(border=True):

                    ticker = stock["ticker"].replace(".NS", "")

                    st.markdown(f"### {ticker}")

                    st.write(stock["status"])

                    st.markdown(f"## {stock['score']}/100")

                    st.write("")

                    st.caption(
                        f"Analyzed : {stock.get('timestamp', 'Latest Market Data')}"
                    )

                    st.write("")

                    st.markdown(
                        f"### {stock['trade']['stars']}"
                    )

                    st.write("")

                    c1, c2, c3 = st.columns(3)

                    # ---------------------------------
                    # Add to Watch
                    # ---------------------------------

                    with c1:

                        if st.button(

                            "⭐ Add",

                            key="idea_watch"

                        ):

                            already_exists = any(

                                s["ticker"] == stock["ticker"]

                                for s in st.session_state.watch_list

                            )

                            if not already_exists:

                                st.session_state.watch_list.append(stock)

                                st.success("Added.")

                    # ---------------------------------
                    # Full Analysis
                    # ---------------------------------

                    with c2:

                        if st.button(

                            "🔍 Details",

                            key="idea_analysis"

                        ):

                            st.session_state.selected_stock = stock

                            st.rerun()

                    # ---------------------------------
                    # Clear
                    # ---------------------------------

                    with c3:

                        if st.button(

                            "🗑 Clear",

                            key="idea_clear"

                        ):

                            st.session_state.idea_result = None

                            st.session_state.idea_ticker = ""

                            st.rerun()

    # ==========================================================
    # My Ideas
    # ==========================================================

    def my_ideas(self):

        st.subheader("💡 My Ideas")

        col1, col2 = st.columns([4, 1])

        with col1:

            ticker = st.text_input(

                "Enter NSE Stock",

                value=st.session_state.idea_ticker,

                placeholder="Example: RELIANCE"

            )

        with col2:

            st.write("")

            st.write("")

            analyze = st.button(

                "Analyze",

                key="idea_analyze"

            )

        if analyze:

            ticker = ticker.strip().upper()

            st.session_state.idea_ticker = ticker

            if ticker == "":

                st.warning("Please enter a stock symbol.")

                return

            with st.spinner(f"Analyzing {ticker}..."):

                result = self.dashboard_engine.analyze_single_stock(

                    ticker=ticker,

                    market_data_engine=self.market_engine,

                    trade_engine=self.trade_engine,

                    ema=self.ema,

                    macd=self.macd,

                    rsi=self.rsi

                )

            if result["success"]:

                st.session_state.idea_result = result["stock"]

            else:

                st.session_state.idea_result = None

                st.error(result["message"])   

            # -----------------------------------------------------
            # Display Analysis
            # -----------------------------------------------------

            if st.session_state.idea_result is None:

                return

            stock = st.session_state.idea_result

            st.divider()

            st.subheader("📊 Analysis Result")

            with st.container(border=True):

                ticker = stock["ticker"].replace(".NS", "")

                st.markdown(f"## {ticker}")

                st.write(stock["status"])

                st.markdown(f"### {stock['score']}/100")

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(

                        "Grade",

                        stock["grade"]

                    )

                with col2:

                    st.metric(

                        "Confidence",

                        f"{stock['confidence']}%"

                    )

                with col3:

                    st.metric(

                        "Direction",

                        stock["direction"]

                    )

                st.write("")

                c1, c2 = st.columns(2)

                with c1:

                    if st.button(

                        "⭐ Add to Watch",

                        key="idea_watch"

                    ):

                        already_exists = any(

                            s["ticker"] == stock["ticker"]

                            for s in st.session_state.watch_list

                        )

                        if not already_exists:

                            st.session_state.watch_list.append(stock)

                            st.success("Added to My Watch")

                with c2:

                    if st.button(

                        "🔍 Full Analysis",

                        key="idea_analysis"

                    ):

                        st.session_state.selected_stock = stock

                        st.rerun()
    # ==========================================================
    # Keep an Eye On
    # ==========================================================

    def keep_an_eye_on(self, dashboard):

        st.subheader("👀 Keep an Eye On")

        watch = dashboard["stocks"][5:10]
        if not watch:
            st.info("No secondary opportunities.")
            return

        cols = st.columns(min(5,len(watch)))

        for col, stock in zip(cols, watch):
            with col:
                with st.container(border=True):
                    st.markdown(f"**{stock['ticker'].replace('.NS','')}**")
                    st.caption(stock["status"])
                    st.write(f"{stock['score']}/100")

    # ==========================================================
    # Top 5 Opportunities
    # ==========================================================

    def top_opportunities(self, dashboard):

        st.subheader("🏆 Top 5 Opportunities")

        top5 = dashboard["stocks"][:5]

        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

        cols = st.columns(5)

        for col, medal, stock in zip(cols, medals, top5):

            with col:

                with st.container(border=True):

                    ticker = stock["ticker"].replace(".NS", "")

                    st.markdown(
                        f"<h4 style='text-align:center'>{medal} {ticker}</h4>",
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Status
                    # --------------------------

                    status = stock["status"]

                    if "READY" in status:
                        st.success(status)

                    elif "WAIT" in status:
                        st.warning(status)

                    else:
                        st.error(status)

                    # --------------------------
                    # Trade Score
                    # --------------------------

                    st.markdown(
                        f"""
                        <div style='text-align:center;
                                    font-size:28px;
                                    font-weight:bold;
                                    padding-top:5px;'>
                            {stock["score"]}/100
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Grade
                    # --------------------------

                    st.markdown(
                        f"""
                        <div style='text-align:center;
                                    color:#FFD54F;
                                    font-size:18px;
                                    font-weight:bold;'>
                            {stock["grade"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Stars
                    # --------------------------

                    st.markdown(
                        f"""
                        <div style='text-align:center;
                                    font-size:20px;
                                    padding-top:5px;
                                    padding-bottom:10px;'>
                            {stock["trade"]["stars"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Analyze Button
                    # --------------------------

                    if st.button(

                        "🔍 Analyze",

                        key=f"analyze_{ticker}"

                    ):

                        st.session_state["selected_stock"] = stock

                        st.rerun()

    # ==========================================================
    # Decision Card
    # ==========================================================

    def show_decision_dialog(self):

        if "selected_stock" not in st.session_state:
            return

        st.divider()

        st.subheader("📊 Decision Analysis")

        stock = st.session_state["selected_stock"]

        self.card.render(

            ticker=stock["ticker"].replace(".NS", ""),

            company=stock["ticker"],

            price=stock["price"],

            change=stock["change"],

            pct_change=stock["pct_change"],

            trade=stock["trade"],

            df=stock["df"]

        )

     # ==========================================================
    # Ranked Opportunities
    # ==========================================================

    def stock_table(self, dashboard):

        st.subheader("📈 Ranked Opportunities")

        rows = []

        for stock in dashboard["stocks"]:

            rows.append({

                "Ticker": stock["ticker"].replace(".NS", ""),

                "Score": stock["score"],

                "Grade": stock["grade"],

                "Status": stock["status"],

                "Direction": stock["direction"],

                "Confidence": stock["confidence"]

            })

        df = pd.DataFrame(rows)

        st.dataframe(

            df,

            hide_index=True,

            use_container_width=True

        )
