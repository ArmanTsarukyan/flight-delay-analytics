"""
Flight Delay Analytics — Interactive Dashboard
Week 3 of the project: filters by route / airline / date over the data
already cleaned and merged in Weeks 1-2.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Flight Delay Analytics",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ Flight Delay Analytics")
st.markdown(
    "Explore what factors best predict operational delays across the "
    "30 highest-traffic U.S. airports (2024)."
)


@st.cache_data
def load_data():
    # TODO: replace with the actual processed dataset
    # df = pd.read_parquet("data/processed/flights_weather_2024.parquet")
    df = pd.DataFrame()
    return df


df = load_data()

if df.empty:
    st.info(
        "No processed data is connected to this dashboard yet. "
        "Complete Weeks 1-2 and update `load_data()` to point to the "
        "final dataset in `data/processed/`."
    )
else:
    # --- Filters (sidebar) ---
    st.sidebar.header("Filters")

    airlines = sorted(df["Reporting_Airline"].unique())
    selected_airlines = st.sidebar.multiselect(
        "Airline", airlines, default=airlines
    )

    origins = sorted(df["Origin"].unique())
    selected_origin = st.sidebar.multiselect(
        "Origin airport", origins, default=origins
    )

    date_range = st.sidebar.date_input(
        "Date range",
        value=(df["FlightDate"].min(), df["FlightDate"].max()),
    )

    # --- Apply filters ---
    filtered = df[
        df["Reporting_Airline"].isin(selected_airlines)
        & df["Origin"].isin(selected_origin)
    ]

    # --- Key metrics ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Flights analyzed", f"{len(filtered):,}")
    col2.metric("Average delay (min)", f"{filtered['DepDelay'].mean():.1f}")
    col3.metric(
        "% flights delayed >15min",
        f"{(filtered['DepDel15'].mean() * 100):.1f}%",
    )

    # --- Visualizations ---
    st.subheader("Average delay by airport")
    by_airport = (
        filtered.groupby("Origin")["DepDelay"].mean().sort_values(ascending=False)
    )
    fig = px.bar(by_airport, title="Average departure delay by airport (min)")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Delay patterns by time of day")
    # TODO: hourly aggregation using CRSDepTime / DepTimeBlk

    st.subheader("Delay vs. weather conditions")
    # TODO: scatter/heatmap of delay vs. NOAA variables
