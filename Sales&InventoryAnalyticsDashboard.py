import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Interactive Sales & Inventory Dashboard")
st.markdown("This dashboard helps managers analyze product performance and revenue trends.")



def get_data():
    dates = pd.date_range(start="2024-01-01", periods=100)
    products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

    data = {
        "Date": np.random.choice(dates, 200),
        "Product": np.random.choice(products, 200),
        "Units Sold": np.random.randint(1, 20, 200),
        "Price Per Unit": np.random.randint(20, 500, 200)
    }

    df = pd.DataFrame(data)
    df["Total Revenue"] = df["Units Sold"] * df["Price Per Unit"]
    return df


df = get_data()

st.sidebar.header("Filter Options")

selected_product = st.sidebar.multiselect(
    "Select Product:",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

df_selection = df.query("Product == @selected_product")

st.markdown("### Key Performance Indicators (KPIs)")

total_sales = df_selection["Total Revenue"].sum()
total_units = df_selection["Units Sold"].sum()
avg_price = df_selection["Price Per Unit"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_sales:,.0f}")
col2.metric("Units Sold", f"{total_units}")
col3.metric("🏷Avg. Price", f"${avg_price:.2f}")

st.markdown("---")

left_column, right_column = st.columns(2)

# גרף עמודות: מכירות לפי מוצר
sales_by_product = df_selection.groupby("Product")["Total Revenue"].sum().reset_index()
fig_product_sales = px.bar(
    sales_by_product,
    x="Product",
    y="Total Revenue",
    title="Sales by Product",
    color="Total Revenue",
    template="plotly_white"
)

# גרף קו: מכירות לאורך זמן
sales_over_time = df_selection.groupby("Date")["Total Revenue"].sum().reset_index()
fig_sales_time = px.line(
    sales_over_time,
    x="Date",
    y="Total Revenue",
    title="Revenue Trend Over Time",
    template="plotly_white"
)

# הצגת הגרפים
left_column.plotly_chart(fig_product_sales, use_container_width=True)
right_column.plotly_chart(fig_sales_time, use_container_width=True)

#  הצגת הטבלה
if st.checkbox("Show Raw Data"):
    st.dataframe(df_selection)