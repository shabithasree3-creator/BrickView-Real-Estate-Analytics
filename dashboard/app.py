import streamlit as st
import pandas as pd
from database import get_connection
#page config
st.set_page_config(
    page_title="BrickView",
    page_icon="🏠",
    layout="wide"
)
conn = get_connection()
st.title("🏠 BrickView")
st.caption("Real Estate Analytics Dashboard")
st.divider()
#KPI Cards
total_listings = pd.read_sql("select count(*) as total from listings",conn).iloc[0]["total"]
avg_price = pd.read_sql("select round(avg(price),0) as avg_price from listings",conn).iloc[0]["avg_price"]
total_sales = pd.read_sql("select count(*) as total from sales",conn).iloc[0]["total"]
total_agents = pd.read_sql("select count(*) as total from agents",conn).iloc[0]["total"]
avg_days = pd.read_sql("select round(avg(days_on_market),1) as avg_days from sales",conn).iloc[0]["avg_days"]
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("🏠 Listings", f"{total_listings:,}")
c2.metric("💰 Avg Price", f"₹{avg_price:,.0f}")
c3.metric("📈 Sales", f"{total_sales:,}")
c4.metric("👥 Agents", f"{total_agents:,}")
c5.metric("📅 Avg Days", avg_days)
st.divider()
st.subheader("🚀 Quick Access")
q1, q2, q3, q4 = st.columns(4)
with q1:
    st.info("🔍 **Filters**")
    st.write("Filter properties.")
    if st.button("Open Filters", use_container_width=True):
        st.switch_page("pages/1_Filters.py")
with q2:
    st.info("📊 **Visualizations**")
    st.write("Interactive charts and business insights.")
    if st.button("Open Visualizations", use_container_width=True):
        st.switch_page("pages/2_Visualizations.py")
with q3:
    st.info("✏️ **CRUD Operations**")
    st.write("Create, retrieve, update and delete records.")
    if st.button("Open CRUD", use_container_width=True):
        st.switch_page("pages/3_CRUD.py")
with q4:
    st.info("💻 **SQL Queries**")
    st.write("Run analytical SQL reports.")
    if st.button("Open SQL Queries", use_container_width=True):
        st.switch_page("pages/4_SQL_Queries.py")
st.divider()
left, right = st.columns([2, 1])
#recent listings
with left:
    st.subheader("📋 Recent Listings")
    recent = pd.read_sql("""select listing_id,City,Property_type,Price from listings order by Date_listed desc limit 5""", conn)
    st.dataframe(recent,use_container_width=True,hide_index=True)
#top agents
with right:
    st.subheader("⭐ Top Agents")
    agents = pd.read_sql("""select Name,rating,deals_closed from agents order by rating desc, deals_closed desc limit 5""", conn)
    st.dataframe(agents,use_container_width=True,hide_index=True)
st.divider()
