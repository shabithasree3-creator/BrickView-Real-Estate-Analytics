import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(page_title="CRUD Operations",page_icon="🛠",layout="wide")

conn=get_connection()
cur=conn.cursor()

st.title("🛠 CRUD Operations")

menu=st.radio("",["➕ Create","🔍 Retrieve","✏️ Update","❌ Delete"],horizontal=True,label_visibility="collapsed")

if menu=="➕ Create":

    st.subheader("➕ Add New Listing")

    c1,c2=st.columns(2)

    with c1:
        lid=st.text_input("Listing ID")
        city=st.text_input("City")
        ptype=st.selectbox("Property Type",["Apartment","Condo","House","Townhouse"])
        price=st.text_input("Price",placeholder="Enter Price")
        sqft=st.text_input("Sqft",placeholder="Enter Sqft")

    with c2:
        listed=st.date_input("Date Listed")
        agent=st.text_input("Agent ID")
        lat=st.text_input("Latitude",placeholder="Enter Latitude")
        lon=st.text_input("Longitude",placeholder="Enter Longitude")

    if st.button("Create Listing",use_container_width=True):

        if "" in [lid,city,price,sqft,agent,lat,lon]:

            st.warning("⚠ Please fill all required fields.")

        elif not pd.read_sql("select listing_id from listings where listing_id=%s",conn,params=(lid,)).empty:

            st.error("❌ Listing ID already exists.")

        else:

            try:

                cur.execute("insert into listings(listing_id,City,Property_type,Price,Sqft,Date_listed,Agent_ID,Latitude,Longitude) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(lid,city,ptype,float(price),float(sqft),listed,agent,float(lat),float(lon)))
                conn.commit()

                st.success("✅ Listing created successfully.")
            except ValueError:

                st.error("❌ Price, Sqft, Latitude and Longitude must be numeric.")

            except Exception as e:

                st.error(f"❌ {e}")
elif menu=="🔍 Retrieve":

    st.subheader("🔍 Retrieve Listings")

    option=st.radio("",["View All","Listing ID","City","Property Type"],horizontal=True,label_visibility="collapsed")

    if option=="View All":

        df=pd.read_sql("select * from listings order by listing_id",conn)
        st.success(f"✅ {len(df)} record(s) found.")
        st.dataframe(df,use_container_width=True)

    elif option=="Listing ID":

        lid=st.text_input("Enter Listing ID")

        if st.button("Search",use_container_width=True):

            df=pd.read_sql("select * from listings where listing_id=%s",conn,params=(lid.strip(),))

            if df.empty:
                st.error("❌ Listing not found.")
            else:
                st.success("✅ Listing found.")
                st.dataframe(df,use_container_width=True)

    elif option=="City":

        city=st.selectbox("Select City",pd.read_sql("select distinct City from listings order by City",conn)["City"])

        if st.button("Search",use_container_width=True):

            df=pd.read_sql("select * from listings where City=%s",conn,params=(city,))

            if df.empty:
                st.error("❌ No records found.")
            else:
                st.success(f"✅ {len(df)} record(s) found.")
                st.dataframe(df,use_container_width=True)

    else:

        ptype=st.selectbox("Select Property Type",["Apartment","Condo","House","Townhouse"])

        if st.button("Search",use_container_width=True):

            df=pd.read_sql("select * from listings where Property_type=%s",conn,params=(ptype,))

            if df.empty:
                st.error("❌ No records found.")
            else:
                st.success(f"✅ {len(df)} record(s) found.")
                st.dataframe(df,use_container_width=True)
elif menu=="✏️ Update":

    st.subheader("✏️ Update Listing")

    lid=st.selectbox("Select Listing ID",pd.read_sql("select listing_id from listings order by listing_id",conn)["listing_id"])

    row=pd.read_sql("select * from listings where listing_id=%s",conn,params=(lid,)).iloc[0]

    c1,c2=st.columns(2)

    with c1:
        city=st.text_input("City",row["City"])
        ptype=st.selectbox("Property Type",["Apartment","Condo","House","Townhouse"],index=["Apartment","Condo","House","Townhouse"].index(row["Property_type"]))
        price=st.text_input("Price",value=str(row["Price"]))
        sqft=st.text_input("Sqft",value=str(row["Sqft"]))

    with c2:
        listed=st.date_input("Date Listed",pd.to_datetime(row["Date_listed"]))
        agent=st.text_input("Agent ID",row["Agent_ID"])
        lat=st.text_input("Latitude",value=str(row["Latitude"]))
        lon=st.text_input("Longitude",value=str(row["Longitude"]))

    if st.button("Update Listing",use_container_width=True):

        if "" in [city,price,sqft,agent,lat,lon]:

            st.warning("⚠ Please fill all required fields.")

        else:

            try:

                cur.execute("update listings set City=%s,Property_type=%s,Price=%s,Sqft=%s,Date_listed=%s,Agent_ID=%s,Latitude=%s,Longitude=%s where listing_id=%s",(city,ptype,float(price),float(sqft),listed,agent,float(lat),float(lon),lid))
                conn.commit()

                if cur.rowcount:
                    st.success("✅ Listing updated successfully.")
                    
                else:
                    st.info("No changes were made.")

            except ValueError:

                st.error("❌ Price, Sqft, Latitude and Longitude must be numeric.")

            except Exception as e:

                st.error(f"❌ {e}")
else:

    st.subheader("❌ Delete Listing")

    if "delete_confirm" not in st.session_state:
        st.session_state.delete_confirm=False

    lid=st.selectbox("Select Listing ID",pd.read_sql("select listing_id from listings order by listing_id",conn)["listing_id"])

    df=pd.read_sql("select * from listings where listing_id=%s",conn,params=(lid,))
    st.dataframe(df,use_container_width=True)

    if not st.session_state.delete_confirm:

        if st.button("Delete Listing",type="primary",use_container_width=True):
            st.session_state.delete_confirm=True
            

    else:

        st.warning("⚠ Are you sure you want to delete this listing?")

        c1,c2=st.columns(2)

        with c1:

            if st.button("✅ Yes, Delete",use_container_width=True):

                try:

                    cur.execute("delete from property_attributes where listing_id=%s",(lid,))
                    cur.execute("delete from buyers where sale_id in(select sale_id from sales where listing_id=%s)",(lid,))
                    cur.execute("delete from sales where listing_id=%s",(lid,))
                    cur.execute("delete from listings where listing_id=%s",(lid,))

                    conn.commit()

                    st.session_state.delete_confirm=False

                    st.success("✅ Listing deleted successfully.")
                    

                except Exception as e:

                    st.error(f"❌ {e}")

        with c2:

            if st.button("❌ Cancel",use_container_width=True):
                st.session_state.delete_confirm=False
                st.rerun()
st.divider()

c1,c2=st.columns(2)

with c1:
    if st.button("🏠 Home",use_container_width=True):
        st.switch_page("app.py")

with c2:
    if st.button("📝 SQL Queries ➜",use_container_width=True):
        st.switch_page("pages/4_SQL_Queries.py")

conn.close()