
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset
df = pd.read_csv("dashboard_data.csv")

# Dashboard title
st.title("📊 Student Performance Dashboard")
st.write("Explore and analyze student academic performance.")

# Sidebar filters
st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

preparation = st.sidebar.multiselect(
    "Test Preparation",
    options=df["test preparation course"].unique(),
    default=df["test preparation course"].unique()
)

# Filter dataset
filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["test preparation course"].isin(preparation))
]

# KPI calculations
st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(filtered_df))

col2.metric(
    "Overall Average",
    round(filtered_df["average_score"].mean(), 2)
)

col3.metric(
    "Highest Score",
    filtered_df[["math score", "reading score", "writing score"]].max().max()
)

col4.metric(
    "Lowest Score",
    filtered_df[["math score", "reading score", "writing score"]].min().min()
)

# Average scores chart
st.subheader("Average Scores per Subject")

score_columns = [
    "math score",
    "reading score",
    "writing score"
]

average_scores = filtered_df[score_columns].mean()

chart_data = average_scores.reset_index()
chart_data.columns = ["Subject", "Average Score"]

fig = px.bar(
    chart_data,
    x="Subject",
    y="Average Score",
    text_auto=".2f",
    title="Average Student Scores"
)

st.plotly_chart(fig, use_container_width=True)

# Display dataset
st.subheader("Student Records")
st.dataframe(filtered_df, use_container_width=True)
