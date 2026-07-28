import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_connection

st.set_page_config(page_title="Visualizations",page_icon="📊",layout="wide")

conn=get_connection()

st.title("📊 Real Estate Visualizations")
st.caption("Interactive insights from BrickView")

c1,c2=st.columns(2)

with c1:
    df=pd.read_sql("select City,count(*) Total from listings group by City order by Total desc",conn)
    fig=px.treemap(df,path=["City"],values="Total",color="Total",
                   color_continuous_scale="Blues",
                   title="Properties by City")
    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig,use_container_width=True)

with c2:
    df=pd.read_sql("select Property_type,count(*) Total from listings group by Property_type",conn)
    fig=px.pie(df,names="Property_type",values="Total",hole=.45,title="Property Type Distribution",color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig,use_container_width=True)

c3,c4=st.columns(2)

with c3:
    df=pd.read_sql("select Property_type,Price from listings",conn)
    fig=px.box(df,x="Property_type",y="Price",color="Property_type",title="Property Price by Type",color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(showlegend=False,title_x=0.5)
    st.plotly_chart(fig,use_container_width=True)

with c4:
    df=pd.read_sql("select Name,deals_closed from agents order by deals_closed desc limit 10",conn)
    fig=px.bar(df,x="Name",y="deals_closed",title="Top 10 Agents by Deals Closed",text_auto=True,color="deals_closed",color_continuous_scale="Viridis")
    fig.update_layout(title_x=0.5,xaxis_title="Agent",yaxis_title="Deals Closed")
    st.plotly_chart(fig,use_container_width=True)


df=pd.read_sql("select date_format(date_sold,'%Y-%m') Month,count(*) Sales from sales group by Month order by Month",conn)
fig=px.line(df,x="Month",y="Sales",markers=True,title="Monthly Sales Trend")
fig.update_traces(line_color="#00CC96",line_width=4,marker_size=8)
fig.update_layout(title_x=0.5,xaxis_title="Month",yaxis_title="Sales")
st.plotly_chart(fig,use_container_width=True)
conn.close()
st.divider()
c1,c2=st.columns(2)
with c1:
    if st.button("🏠 Home",use_container_width=True):
        st.switch_page("app.py")
with c2:
    if st.button("🛠 CRUD ➜",use_container_width=True):
        st.switch_page("pages/3_CRUD.py")