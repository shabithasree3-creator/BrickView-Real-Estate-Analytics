import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(page_title="Filters",page_icon="🔍",layout="wide")
conn=get_connection()

st.title("🔍 Advanced Filters")
st.caption("Filter Listings, Property Details, Agents, Sales and Buyers")

tab1,tab2,tab3,tab4,tab5=st.tabs(["🏠 Listings","🏡 Property","👨‍💼 Agents","💰 Sales","👤 Buyers"])

with tab1:
    df=pd.read_sql("select * from listings",conn)

    c1,c2=st.columns(2)
    with c1:
        city=st.selectbox("City",["All"]+sorted(df.City.dropna().unique()))
        price=st.slider("Price",int(df.Price.min()),int(df.Price.max()),(int(df.Price.min()),int(df.Price.max())))
    with c2:
        ptype=st.selectbox("Property Type",["All"]+sorted(df.Property_type.dropna().unique()))
        sqft=st.slider("Sqft",int(df.Sqft.min()),int(df.Sqft.max()),(int(df.Sqft.min()),int(df.Sqft.max())))

    filtered=df.copy()
    if city!="All":filtered=filtered[filtered.City==city]
    if ptype!="All":filtered=filtered[filtered.Property_type==ptype]
    filtered=filtered[(filtered.Price>=price[0])&(filtered.Price<=price[1])]
    filtered=filtered[(filtered.Sqft>=sqft[0])&(filtered.Sqft<=sqft[1])]

    m1,m2,m3=st.columns(3)
    m1.metric("Listings",len(filtered))
    m2.metric("Avg Price",f"₹{filtered.Price.mean():,.0f}" if len(filtered) else "₹0")
    m3.metric("Avg Sqft",f"{filtered.Sqft.mean():.0f}" if len(filtered) else "0")

    st.dataframe(filtered,use_container_width=True,hide_index=True)
    st.download_button("⬇ Download CSV",filtered.to_csv(index=False),"Listings.csv","text/csv")
with tab2:
    df=pd.read_sql("select l.listing_id,l.City,l.Property_type,p.attribute_id,p.bedrooms,p.bathrooms,p.floor_number,p.total_floors,p.year_built,p.is_rented,p.tenant_count,p.furnishing_status,p.metro_distance_km,p.parking_available,p.power_backup from property_attributes p join listings l on p.listing_id=l.listing_id",conn)
    df["is_rented"]=df["is_rented"].replace({1:"Rented",0:"Not Rented"})
    df["parking_available"]=df["parking_available"].replace({1:"Available",0:"Not Available"})
    df["power_backup"]=df["power_backup"].replace({1:"Available",0:"Not Available"})
    c1,c2,c3=st.columns(3)
    with c1:
        city=st.selectbox("City",["All"]+sorted(df.City.dropna().unique()),key="pcity")
        bed=st.selectbox("Bedrooms",["All"]+sorted(df.bedrooms.dropna().unique()),key="bed")
        bath=st.selectbox("Bathrooms",["All"]+sorted(df.bathrooms.dropna().unique()),key="bath")
    with c2:
        furnish=st.selectbox("Furnishing",["All"]+sorted(df.furnishing_status.dropna().unique()),key="fur")
        rent=st.selectbox("Rental Status",["All"]+sorted(df.is_rented.dropna().unique()),key="rent")
        parking=st.selectbox("Parking",["All"]+sorted(df.parking_available.dropna().unique()),key="park")
    with c3:
        backup=st.selectbox("Power Backup",["All"]+sorted(df.power_backup.dropna().unique()),key="back")
        year=st.slider("Year Built",int(df.year_built.min()),int(df.year_built.max()),(int(df.year_built.min()),int(df.year_built.max())))
        metro=st.slider("Maximum Metro Distance (km)",float(df.metro_distance_km.min()),float(df.metro_distance_km.max()),float(df.metro_distance_km.max()))
    filtered=df.copy()
    if city!="All":
        filtered=filtered[filtered.City==city]
    if bed!="All":
        filtered=filtered[filtered.bedrooms==bed]
    if bath!="All":
        filtered=filtered[filtered.bathrooms==bath]
    if furnish!="All":
        filtered=filtered[filtered.furnishing_status==furnish]
    if rent!="All":
        filtered=filtered[filtered.is_rented==rent]
    if parking!="All":
        filtered=filtered[filtered.parking_available==parking]
    if backup!="All":
        filtered=filtered[filtered.power_backup==backup]
    filtered=filtered[(filtered.year_built>=year[0])&(filtered.year_built<=year[1])]
    filtered=filtered[filtered.metro_distance_km<=metro]
    m1,m2,m3=st.columns(3)
    m1.metric("Properties",len(filtered))
    m2.metric("Avg Bedrooms",round(filtered.bedrooms.mean(),1) if len(filtered) else 0)
    m3.metric("Avg Bathrooms",round(filtered.bathrooms.mean(),1) if len(filtered) else 0)
    st.dataframe(filtered,use_container_width=True,hide_index=True)
    st.download_button("⬇ Download CSV",filtered.to_csv(index=False),"Property.csv","text/csv")
    st.divider()
c1,c2=st.columns(2)
with c1:
    if st.button("🏠 Home",use_container_width=True):
        st.switch_page("app.py")
with c2:
    if st.button("📊 Visualizations ➜",use_container_width=True):
        st.switch_page("pages/2_Visualizations.py")