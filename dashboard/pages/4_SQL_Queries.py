import streamlit as st
import pandas as pd
from database import get_connection
st.set_page_config(page_title="SQL Queries",page_icon="📝",layout="wide")
conn=get_connection()
st.title("📝 SQL Queries")
questions=[
"1. What is the average listing price by city?",
"2. What is the average price per square foot by property type?",
"3. How does furnishing status impact property prices?",
"4. Do properties closer to metro stations command higher prices?",
"5. Are rented properties priced differently from non-rented ones?",
"6. How do bedrooms and bathrooms affect pricing?",
"7. Do properties with parking and power backup sell at higher prices?",
"8. How does year built influence listing price?",
"9. Which cities have the highest average property prices?",
"10. How are properties distributed across price buckets?",
"11. What is the average days on market by city?",
"12. Which property types sell the fastest?",
"13. What percentage of properties are sold above listing price?",
"14. What is the sale-to-list price ratio by city?",
"15. Which listings took more than 90 days to sell?",
"16. How does metro distance affect time on market?",
"17. What is the monthly sales trend?",
"18. Which properties are currently unsold?",
"19. Which agents have closed the most sales?",
"20. Who are the top agents by total sales revenue?",
"21. Which agents close deals fastest?",
"22. Does experience correlate with deals closed?",
"23. Do agents with higher ratings close deals faster?",
"24. What is the average commission earned by each agent?",
]
choice=st.selectbox("Select SQL Question",questions)
if choice==questions[0]:

    query="select city,round(avg(price),2) as average_price from listings group by city;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[1]:

    query="select property_type,round(avg(price/sqft),2) as price_per_sqft from listings group by property_type;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[2]:

    query="select furnishing_status,round(avg(price),2) as average_price from property_attributes pa join listings l on pa.listing_id=l.listing_id group by furnishing_status order by average_price;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[3]:

    query="select round(metro_distance_km,0) as distance_km,round(avg(price),2) as avg_price from property_attributes pa join listings l on pa.listing_id=l.listing_id group by distance_km order by distance_km;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[4]:

    query='select case when is_rented=1 then "Rented" else "Non-Rented" end as rental_status,round(avg(price),2) as average_price from property_attributes pa join listings l on pa.listing_id=l.listing_id group by is_rented;'
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)
elif choice==questions[5]:

    query="select bedrooms,bathrooms,round(avg(price),2) as average_price from property_attributes pa join listings l on pa.listing_id=l.listing_id group by bedrooms,bathrooms order by bedrooms,bathrooms;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)
elif choice==questions[6]:

    query='select case when parking_available=1 then "Available" else "Not Available" end as parking_status,case when power_backup=1 then "Available" else "Not Available" end as power_backup_status,round(avg(price),2) as average_price from property_attributes pa join listings l on pa.listing_id=l.listing_id group by parking_available,power_backup order by parking_available,power_backup;'
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[7]:

    query="select year_built,round(avg(price),2) as average_price from property_attributes pa join listings l on pa.listing_id=l.listing_id group by year_built order by year_built;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[8]:

    query="select city,round(avg(price),2) as average_price from listings group by city order by average_price desc;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[9]:

    query="select price_bucket,min(price) as min_price,max(price) as max_price,count(*) as property_count,round(avg(price),2) as average_price from (select price,ntile(5) over(order by price) as price_bucket from listings)t group by price_bucket order by price_bucket;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)
elif choice==questions[10]:

    query="select city,round(avg(days_on_market),2) as average_days_on_market from sales s join listings l on s.listing_id=l.listing_id group by city order by average_days_on_market;"
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[11]:

    query = """select property_type, round(avg(Days_on_Market), 2) as Time_to_Sell from listings l join sales s on l.listing_id = s.listing_id group by property_type order by Time_to_Sell;"""
    st.code(query, language="sql")
    st.dataframe(pd.read_sql(query, conn), use_container_width=True)

elif choice==questions[12]:

    query = """
select round(sum(case when sale_price > price then 1 else 0 end)*100.0/count(*), 2) as percentage_of_properties_above_listing_price from sales s join listings l on s.listing_id = l.listing_id;
"""
    st.code(query, language="sql")
    st.dataframe(pd.read_sql(query, conn), use_container_width=True)

elif choice==questions[13]:

    query = """
select city, round(avg(sale_price), 2)/round(avg(price), 2) as sale_to_listing_price_ratio from sales s join listings l on s.listing_id = l.listing_id group by city order by sale_to_listing_price_ratio desc;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[14]:

    query="""
select listing_id, days_on_market from sales where days_on_market > 90 order by days_on_market desc;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[15]:

    query="""
select metro_distance_km, round(avg(days_on_market), 2) as average_days_on_market from property_attributes pa join sales s on pa.listing_id = s.listing_id group by metro_distance_km order by metro_distance_km;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[16]:

    query="""
select monthname(date_sold) as sale_month, count(*) as total_sales from sales group by sale_month order by sale_month;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[17]:

    query="""
select l.listing_id, l.city, l.property_type, l.price from listings l left join sales s on l.listing_id = s.listing_id where s.listing_id is null;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[18]:

    query="""
select a.name, count(s.sale_id) as total_sales from agents a join listings l on a.agent_id = l.agent_id join sales s on l.listing_id = s.listing_id group by a.name order by total_sales desc limit 1;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[19]:

    query="""
select a.name, round(sum(s.sale_price), 2) as total_sales_revenue from agents a join listings l on a.agent_id = l.agent_id join sales s on l.listing_id = s.listing_id group by a.name order by total_sales_revenue desc limit 3;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[20]:

    query="""
select name, avg_closing_days from agents order by avg_closing_days asc limit 3;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[21]:

    query="""
select name,experience_years,deals_closed from agents order by experience_years;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[22]:

    query="""
select name,rating, avg_closing_days from agents order by rating desc, avg_closing_days asc;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[23]:

    query="""
select a.name, round(avg(s.sale_price*a.commission_rate), 2) as avg_commission_earned from agents a join listings l on a.agent_id = l.agent_id join sales s on l.listing_id = s.listing_id group by a.agent_id, a.name order by avg_commission_earned desc;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

elif choice==questions[24]:

    query="""
select a.name, count(l.listing_id) as active_listings from agents a join listings l on a.agent_id = l.agent_id left join sales s on l.listing_id = s.listing_id where s.listing_id is null group by a.name order by active_listings desc limit 3;
"""
    st.code(query,language="sql")
    st.dataframe(pd.read_sql(query,conn),use_container_width=True)

else:
    print("Invalid choice")
st.divider()
c1,c2=st.columns(2)
with c1:
    if st.button("🏠 Home",use_container_width=True):
        st.switch_page("app.py")
with c2:
    if st.button("🛠 CRUD",use_container_width=True):
        st.switch_page("pages/3_CRUD.py")
conn.close()