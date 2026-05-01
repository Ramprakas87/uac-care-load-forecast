# ================================
# COMPLETE PRD LEVEL PROJECT (100% FINAL)
# ================================

import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error

import warnings
warnings.filterwarnings("ignore")

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Care Load Forecast Dashboard", layout="wide")

st.title("📊 Predictive Forecasting of Care Load & Placement Demand")

# ================================
# LOAD DATA
# ================================
df = pd.read_csv("HHS_Unaccompanied_Alien_Children_Program.csv")

df.columns = [
    "Date",
    "Apprehended",
    "CBP_Custody",
    "Transferred",
    "HHS_Care",
    "Discharged"
]

cols = ["Apprehended", "CBP_Custody", "Transferred", "HHS_Care", "Discharged"]

for col in cols:
    df[col] = df[col].astype(str).str.replace(",", "")
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.sort_values("Date")
df = df.ffill()

# ================================
# FEATURE ENGINEERING
# ================================
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.strftime("%b")

df["HHS_Rolling"] = df["HHS_Care"].rolling(7).mean()
df["Daily_Change"] = df["HHS_Care"].diff()

df["Placement_Rate"] = df["Discharged"] / df["HHS_Care"]
df["Placement_Rate"] = df["Placement_Rate"].fillna(0)

df["Estimated_Delay"] = df["HHS_Care"] / (df["Discharged"] + 1)

CAPACITY = df["HHS_Care"].max() * 1.2
df["Utilization"] = df["HHS_Care"] / CAPACITY

# ================================
# SIDEBAR
# ================================
st.sidebar.markdown("## 🔎 Filters")

if st.sidebar.button("🔄 Reset Filters"):
    st.session_state.clear()
    st.rerun()

start_date = st.sidebar.date_input("Start Date", df["Date"].min())
end_date = st.sidebar.date_input("End Date", df["Date"].max())

years = sorted(df["Year"].dropna().unique())
selected_years = st.sidebar.multiselect("Year", years, default=years)

filtered_df = df[
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date)) &
    (df["Year"].isin(selected_years))
]

month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
dynamic_months = [m for m in month_order if m in filtered_df["Month_Name"].unique()]

selected_month = st.sidebar.selectbox("Month", ["All"] + dynamic_months)

if selected_month != "All":
    filtered_df = filtered_df[filtered_df["Month_Name"] == selected_month]

quick_filter = st.sidebar.selectbox(
    "Quick Range",
    ["None", "Last 3 Months", "Last 6 Months", "Last 1 Year"]
)

if selected_years == years:
    if quick_filter == "Last 3 Months":
        filtered_df = filtered_df[
            filtered_df["Date"] >= filtered_df["Date"].max() - pd.DateOffset(months=3)
        ]
    elif quick_filter == "Last 6 Months":
        filtered_df = filtered_df[
            filtered_df["Date"] >= filtered_df["Date"].max() - pd.DateOffset(months=6)
        ]
    elif quick_filter == "Last 1 Year":
        filtered_df = filtered_df[
            filtered_df["Date"] >= filtered_df["Date"].max() - pd.DateOffset(years=1)
        ]

st.sidebar.markdown(f"📊 Records: {len(filtered_df)}")

# ================================
# KPIs
# ================================
st.subheader("📌 Key Performance Indicators")

latest = df.iloc[-1]
prev = df.iloc[-2]

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Care Load", int(latest["HHS_Care"]), int(latest["HHS_Care"] - prev["HHS_Care"]))
col2.metric("Avg Load", int(df["HHS_Care"].mean()))
col3.metric("Placement Rate", f"{df['Placement_Rate'].mean()*100:.2f}%")
col4.metric("Delay", f"{df['Estimated_Delay'].mean():.1f}")
col5.metric("Utilization", f"{df['Utilization'].mean()*100:.1f}%")

st.markdown(f"### 📊 Showing: Year {[int(y) for y in selected_years]} | Month {selected_month}")

# ================================
# VISUALS
# ================================
def style(fig):
    fig.update_layout(template="plotly_dark", hovermode="x unified")
    fig.update_traces(mode="lines")
    return fig

st.markdown("### 1️⃣ Care Load vs 7-Day Rolling Average")
st.markdown("*Actual daily values compared with smoothed trend to identify underlying patterns*")
st.plotly_chart(style(px.line(filtered_df, x="Date", y=["HHS_Care","HHS_Rolling"])), use_container_width=True)

st.markdown("### 2️⃣ Apprehensions vs Discharges")
st.markdown("*Intake volume compared with successful placements - key for capacity planning*")
st.plotly_chart(style(px.line(filtered_df, x="Date", y=["Apprehended","Discharged"])), use_container_width=True)

st.markdown("### 3️⃣ CBP Custody vs HHS Care Load")
st.markdown("*Pipeline from border custody to HHS system - shows transfer flow*")
st.plotly_chart(style(px.line(filtered_df, x="Date", y=["CBP_Custody","HHS_Care"])), use_container_width=True)

st.markdown("### 4️⃣ Monthly Average Care Load")
st.markdown("*Long-term trend analysis with monthly aggregation - identifies seasonal patterns*")

filtered_df["Date"] = pd.to_datetime(filtered_df["Date"], errors="coerce")
filtered_df = filtered_df.dropna(subset=["Date"])

filtered_df["Date"] = pd.to_datetime(filtered_df["Date"], errors="coerce")
filtered_df = filtered_df.dropna(subset=["Date"])

filtered_df = filtered_df.set_index("Date")

monthly = filtered_df.resample("M").mean(numeric_only=True).reset_index()

st.plotly_chart(style(px.line(monthly, x="Date", y="HHS_Care")), use_container_width=True)

st.markdown("### 5️⃣ Care Load Distribution")
st.markdown("*Histogram showing frequency of care load values - identifies typical ranges*")
st.plotly_chart(px.histogram(filtered_df, x="HHS_Care"), use_container_width=True)

st.markdown("### 6️⃣ Daily Change in Care Load")
st.markdown("*Day-to-day volatility and sudden fluctuations - tracks sudden surges*")
st.plotly_chart(style(px.line(filtered_df, x="Date", y="Daily_Change")), use_container_width=True)

st.markdown("### 7️⃣ Placement Rate Tracking")
st.markdown("*Percentage of children successfully discharged daily - system efficiency metric*")
st.plotly_chart(style(px.line(filtered_df, x="Date", y="Placement_Rate")), use_container_width=True)

st.markdown("### 8️⃣ System Utilization")
st.markdown("*Percentage of maximum capacity currently in use - capacity pressure indicator*")
st.plotly_chart(style(px.line(filtered_df, x="Date", y="Utilization")), use_container_width=True)

# ================================
# INSIGHTS
# ================================
st.subheader("📊 Key Insights")

st.markdown(f"""
- Current Care Load is **{int(latest['HHS_Care'])}**, showing recent trend movement.
- Average Placement Rate is **{df['Placement_Rate'].mean()*100:.2f}%**, indicating system efficiency.
- Utilization at **{df['Utilization'].mean()*100:.1f}%** suggests capacity pressure.
- Sudden fluctuations in apprehensions impact care load demand.
""")

# ================================
# ALERT SYSTEM
# ================================
st.subheader("⚠️ Risk Alerts")

if latest["Utilization"] > 0.85:
    st.error("🚨 High Capacity Utilization!")

if latest["Placement_Rate"] < 0.5:
    st.warning("⚠️ Low Placement Rate")

if latest["Daily_Change"] > 1000:
    st.warning("⚠️ Sudden Surge Detected")

# ================================
# FORECAST
# ================================
st.subheader("📈 Forecast")

ts = df.set_index("Date")["HHS_Care"]
ts_monthly = ts.resample("M").mean()

model = SARIMAX(ts_monthly, order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit()

forecast = results.get_forecast(steps=12)
forecast_mean = forecast.predicted_mean
conf_int = forecast.conf_int()

fig = go.Figure()
fig.add_trace(go.Scatter(x=ts_monthly.index, y=ts_monthly, name="Actual"))
fig.add_trace(go.Scatter(x=forecast_mean.index, y=forecast_mean, name="Forecast"))

fig.add_trace(go.Scatter(
    x=conf_int.index,
    y=conf_int.iloc[:, 0],
    line=dict(width=0),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=conf_int.index,
    y=conf_int.iloc[:, 1],
    fill='tonexty',
    name='Confidence Interval'
))

st.markdown("### 9️⃣ 12-Month Care Load Forecast")
st.markdown("*SARIMA predictions with 95% confidence intervals - predictive intelligence*")
st.plotly_chart(style(fig), use_container_width=True)

# ================================
# SCENARIO ANALYSIS
# ================================
st.subheader("🧠 Scenario Simulation")

growth = st.slider("Expected Growth %", 0, 50, 10)

future = forecast_mean * (1 + growth/100)

st.markdown("### 🔟 Scenario Analysis Chart")
st.markdown("*Projected care load with custom growth percentage applied - what-if planning*")
st.line_chart(future)

# ================================
# MODEL EVALUATION
# ================================
st.subheader("📊 Model Evaluation")

train = ts_monthly[:-12]
test = ts_monthly[-12:]

model = SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit()

pred = results.forecast(steps=12)

mae = mean_absolute_error(test, pred)
rmse = np.sqrt(mean_squared_error(test, pred))

st.write("MAE:", round(mae,2))
st.write("RMSE:", round(rmse,2))

# ================================
# DOWNLOAD
# ================================
st.subheader("📥 Download Data")

st.download_button(
    "Download Filtered Data",
    filtered_df.to_csv(index=False),
    file_name="filtered_data.csv"
)
