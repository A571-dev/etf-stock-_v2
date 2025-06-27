
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ETF & Stock Dashboard", layout="wide")

DATA_PATH = "ETF_Stock_Analyzer.xlsx"

@st.cache_data
def load_data():
    try:
        xl = pd.ExcelFile(DATA_PATH)
        full_df = xl.parse("Full Dataset")
        forecast_df = xl.parse("Forecast Leaders")
        return full_df, forecast_df
    except FileNotFoundError:
        st.error("Excel file not found. Please ensure 'ETF_Stock_Analyzer.xlsx' is in the same folder as this script.")
        return pd.DataFrame(), pd.DataFrame()

full_df, forecast_df = load_data()

st.title("📊 ETF & Stock Analyzer")

tab1, tab2, tab3 = st.tabs(["Full Dataset", "Top Performers", "Forecast Leaders"])

with tab1:
    st.subheader("All Tracked Investments")
    st.dataframe(full_df, use_container_width=True)

with tab2:
    st.subheader("Top Performing Investments")
    metric = st.selectbox("Rank by:", ["10Y CAGR", "5Y CAGR", "1Y Return"])
    if not full_df.empty:
        sorted_df = full_df.sort_values(by=metric, ascending=False)
        st.dataframe(sorted_df.head(20), use_container_width=True)

with tab3:
    st.subheader("AI Forecast Leaders")
    if not forecast_df.empty:
        sorted_forecast = forecast_df.sort_values(by="Forecasted 1Y Return", ascending=False)
        st.dataframe(sorted_forecast.head(20), use_container_width=True)
