from datetime import date
from turtle import width
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

sales = pd.read_csv("dataset/cleandata.csv")
sales["datetime"] = pd.to_datetime(sales["datetime"])

st.markdown(
    "<h1 style='text-align: center;'>Visualization Dashboard</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p style='text-align: center;'>Dataset yang digunakan dalam project ini adalah dataset yang sebelumnya sudah dilakukan preprocessing dari dataset penjualan sebuah supermarket dari January 2019 sampai Maret 2019. </p>",
    unsafe_allow_html=True,
)

with st.expander("About Dataset"):
    if st.checkbox("Show Dataset"):
        st.write(sales)

    """
    Dataset ini berisi 1000 baris dengan 15 kolom yang diantaranya adalah ID, city, customer_type, gender, product_line, price, quantity, tax, total, payment, cogs, margin_percentage, gross_income, rating, dan datetime.
    
    Berikut adalah keterangan dari kolom pada dataset:

    | Feature                 | Description                                                                                                                                                    |
    | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ID                      | Computer generated sales slip invoice identification number                                                                                                    |
    | city                    | Location of supercenters                                                                                                                                       |
    | customer_type           | Type of customers, recorded by Members for customers using member card and Normal for without member card                                                      |
    | gender                  | Gender type of customer                                                                                                                                        |
    | product_line            | General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel |
    | price                   | Price of each product in $                                                                                                                                     |
    | quantity                | Number of products purchased by customer                                                                                                                       |
    | tax                     | 5% tax fee for customer buying                                                                                                                                 |
    | total                   | Total price including tax                                                                                                                                      |
    | payment                 | Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)                                                                |
    | cogs                    | Cost of goods sold                                                                                                                                             |
    | margin_percentage       | Gross margin percentage                                                                                                                                        |
    | gross_income            | Gross income                                                                                                                                                   |
    | rating                  | Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)                                                                    |
    | datetime                | Date of purchase (Record available from January 2019 to March 2019) and Purchase time (10am to 9pm)                                                            |

    Dataset asli dapat dilihat di [Kaggle](https://www.kaggle.com/aungpyaeap/supermarket-sales).
    """

line = px.line(
    sales.groupby(sales.datetime.dt.date).gross_income.mean(),
    title="Gross Income by Day",
    labels={"datime": "Date", "value": "Gross Income"},
)
st.plotly_chart(line)

dates = st.slider(
    "Select a range of dates",
    min_value=sales.datetime.dt.date.min(),
    max_value=sales.datetime.dt.date.max(),
    value=(sales.datetime.dt.date.min(), sales.datetime.dt.date.max()),
)

mask = (sales.datetime.dt.date >= dates[0]) & (sales.datetime.dt.date <= dates[1])

city = st.radio("Select a city", ["All City"] + list(sales.city.unique()))

if city == "All City":
    sales[mask]
else:
    sales[mask][sales[mask].city == city]
