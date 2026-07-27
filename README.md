🏠 BrickView - Real Estate Analytics Platform
---
BrickView is a Real Estate Analytics Platform developed in Python, Streamlit and MySql which provides interactive dashboard for analysis of property listings, sales, agents and buyers with filters, visualizations, CRUD operations and Sql analytics.

---

## 📌 Project Summary

BrickView is created to explore the real estate data with ease and includes the following features:

- Interactive filtering of the property listings

- Visualization of the property listings

- Performing complete crud operations

- Insightful business questions through sql queries
- User friendly dashboard for exploring the data
---
### 🚀 Features
#### 📊 Dashboard
- Total Listings
- Total Sales
- Total Agents
- Total Buyers
- Recent Listings
- Top Agents
- Recent Sales
#### 🎛 Filters
- Filter by city
- Filter by property type
- Filter by price range
- Filter by agent
- Filter by date
#### 📈 Visualizations
- Properties by city
- Property type distribution
- Average price by property type
- Top performing agents
- Monthly sales trend
#### 🛠 CRUD Operations
- Create
- Read
- Update
- Delete
#### 💻 SQL Queries
- Property pricing analysis
- Sale performance analysis
- Agent performance analysis
- Buyer and loan analysis
- Market trend analysis
---
### 🗄 Database Tables
- Listings
- Property_Attributes
- Agents
- Sales
- Buyers
---
### 🛠 Technologies
- Python
- Streamlit
- MySQL
- Pandas
- Plotly Express
- MySQL-connector
---
### 📂 Project Structure
```text
BrickView/
│
├── app.py
├── database.py
├── requirements.txt
├── data/
│  ├── listings_final_expanded.json
│  ├── property_attributes_final_expanded.json
│  ├── agents_cleaned.json
│  ├── buyers_cleaned.json
│  └── sales_cleaned.csv
│
├── pages/
│  ├── 1_Filters.py
│  ├── 2_Visualizations.py
│  ├── 3_CRUD.py
│  └── 4_SQL_Queries.py
│
└── notebook/
└── BrickView_analysis.ipynb
```
---
## ⚙️ Installation
### Clone the repository
```bash

git clone https://github.com/shabithasree3-creator/BrickView-Real-Estate-Analytics.git
```
### Move into the project
```bash
cd BrickView-Real-Estate-Analytics
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Configure MySQL
Update the database credentials in the database.py:
```python
host="localhost"
user="root"
password="your_password"
database="brickview"
```
### Run the application
```bash
streamlit run app.py
```
---
## 📊 Sample Insights
- Average listing price analysis by city
- Furnished property has more listing price compared to unfurnished
- Property near metro has higher price
- Agent performance analysis based on sales and ratings
- Monthly sale trend analysis
- Buyer loan analysis
---
## 📷 Applications
- 🏠 Home Dashboard
- 🎛 Filters
- 📈 Visualizations
- 🛠 CRUD Operations
- 💻 SQL Query Analysis
---
## 🎯 Learning Outcomes
- Interactive web application development with streamlit
- Designing and implementing mysql database
- Joining and analyzing data with sql queries
- Efficient coding with python
- Building insightful visualization
---
## 👩‍💻 Author
Shabitha Sree
GitHub: https://github.com/shabithasree3-creator
---

## 📜 License

This project made for educational and learning purpose only.
