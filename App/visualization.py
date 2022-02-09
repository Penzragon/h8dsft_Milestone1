import streamlit as st
import pandas as pd
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

barcity = px.histogram(
    sales,
    x="city",
    y="gross_income",
    color="city",
    labels={"city": "City", "gross_income": "Gross Income"},
    title="Gross Income by City",
)
st.plotly_chart(barcity, use_container_width=True)

col1, col2 = st.columns([3, 1])
with col1:
    dates = st.slider(
        "Select a range of dates",
        min_value=sales.datetime.dt.date.min(),
        max_value=sales.datetime.dt.date.max(),
        value=(sales.datetime.dt.date.min(), sales.datetime.dt.date.max()),
    )

with col2:
    city = st.selectbox("Select a city", ["All City"] + list(sales.city.unique()))

mask = (sales.datetime.dt.date >= dates[0]) & (sales.datetime.dt.date <= dates[1])

if city == "All City":
    df = sales[mask]

    ### for line chart and bar chart ###
    col3, col4 = st.columns(2)
    with col3:
        lineplot = px.line(
            df.groupby(df.datetime.dt.date).gross_income.mean(),
            labels={"datetime": "Date", "value": "Gross Income"},
            title="Average Gross Income by Day",
        )
        st.plotly_chart(lineplot, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Supermarket memiliki rata-rata pendapatan terbesar pada **"
                + str(df.groupby(df.datetime.dt.date).gross_income.mean().idxmax())
                + "** sedangkan pada **"
                + str(df.groupby(df.datetime.dt.date).gross_income.mean().idxmin())
                + "** adalah saat dimana supermarket memiliki rata-rata pendapatan terkecil."
            )

    with col4:
        barplot = px.bar(
            df.groupby(df.datetime.dt.hour).gross_income.sum(),
            labels={"datetime": "Hour", "value": "Gross Income"},
            title="Gross Income by Hour",
        )
        st.plotly_chart(barplot, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Supermarket memiliki jumlah pendapatan terbesar yang berada pada **jam "
                + str(df.groupby(df.datetime.dt.hour).gross_income.sum().idxmax())
                + "** dan jumlah pendapatan terkecil berada pada **jam "
                + str(df.groupby(df.datetime.dt.hour).gross_income.sum().idxmin())
                + "**."
            )

    ### for product line and payment ###
    col5, col6 = st.columns(2)
    with col5:
        productdf = df.groupby("product_line").size().reset_index(name="count")
        pieplotproduct = px.pie(
            productdf, values="count", names="product_line", title="Product Line Sold"
        )
        st.plotly_chart(pieplotproduct, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Produk yang paling banyak terjual di supermarket adalah produk berkategori **"
                + str(df.groupby("product_line").size().idxmax())
                + "** dengan jumlah penjualan sebanyak **"
                + str(df.groupby("product_line").size().max())
                + "x**."
            )

    with col6:
        paymentdf = df.groupby("payment").size().reset_index(name="count")
        pieplotpayment = px.pie(
            paymentdf, values="count", names="payment", title="Payment Method Used"
        )
        st.plotly_chart(pieplotpayment, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Di supermarket metode pembayaran yang paling sering digunakan adalah metode pembayaran menggunakan **"
                + str(df.groupby("payment").size().idxmax())
                + "** dengan jumlah penggunaan sebanyak **"
                + str(df.groupby("payment").size().max())
                + "x**."
            )

    col7, col8, col9 = st.columns([1, 2, 1])
    with col8:
        genderbar = px.histogram(
            df,
            x="gender",
            color="customer_type",
            title="Number of Customer by Gender and Customer Type",
        )
        st.plotly_chart(genderbar, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Pada tanggal **"
                + str(dates[0])
                + "** sampai **"
                + str(dates[1])
                + "** pengunjung supermarket paling banyak adalah **"
                + str(df.groupby("gender").size().idxmax())
                + "** dengan jumlah **"
                + str(df.groupby("gender").size().max())
                + "** pengunjung. Jumlah member supermarket paling banyak adalah **"
                + str(df.groupby(["customer_type", "gender"]).size().idxmax()[1])
                + "** sebanyak **"
                + str(df.groupby(["customer_type", "gender"]).size().max())
                + "** member."
            )

else:
    df = sales[mask][sales[mask].city == city]

    ### for line chart and bar chart ###
    col3, col4 = st.columns(2)
    with col3:
        lineplot = px.line(
            df.groupby(df.datetime.dt.date).gross_income.mean(),
            labels={"datetime": "Date", "value": "Gross Income"},
            title="Average Gross Income by Day",
        )
        st.plotly_chart(lineplot, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Supermarket di **"
                + str(city)
                + "** memiliki rata-rata pendapatan terbesar pada **"
                + str(df.groupby(df.datetime.dt.date).gross_income.mean().idxmax())
                + "** sedangkan pada **"
                + str(df.groupby(df.datetime.dt.date).gross_income.mean().idxmin())
                + "** adalah saat dimana supermarket memiliki rata-rata pendapatan terkecil."
            )

    with col4:
        barplot = px.bar(
            df.groupby(df.datetime.dt.hour).gross_income.sum(),
            labels={"datetime": "Hour", "value": "Gross Income"},
            title="Gross Income by Hour",
        )
        st.plotly_chart(barplot, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Di **"
                + str(city)
                + "**, supermarket memiliki jumlah pendapatan terbesar yang berada pada **jam "
                + str(df.groupby(df.datetime.dt.hour).gross_income.sum().idxmax())
                + "** dan jumlah pendapatan terkecil berada pada **jam "
                + str(df.groupby(df.datetime.dt.hour).gross_income.sum().idxmin())
                + "**."
            )

    ### for product line and payment ###
    col5, col6 = st.columns(2)
    with col5:
        productdf = df.groupby("product_line").size().reset_index(name="count")
        pieplotproduct = px.pie(
            productdf, values="count", names="product_line", title="Product Line Sold"
        )
        st.plotly_chart(pieplotproduct, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Produk yang paling banyak terjual di supermarket kota **"
                + str(city)
                + "** adalah produk berkategori **"
                + str(df.groupby("product_line").size().idxmax())
                + "** dengan jumlah penjualan sebanyak **"
                + str(df.groupby("product_line").size().max())
                + "x**."
            )

    with col6:
        paymentdf = df.groupby("payment").size().reset_index(name="count")
        pieplotpayment = px.pie(
            paymentdf, values="count", names="payment", title="Payment Method Used"
        )
        st.plotly_chart(pieplotpayment, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Di kota **"
                + str(city)
                + "**, metode pembayaran yang paling sering digunakan adalah metode pembayaran menggunakan **"
                + str(df.groupby("payment").size().idxmax())
                + "** dengan jumlah penggunaan sebanyak **"
                + str(df.groupby("payment").size().max())
                + "x**."
            )

    col7, col8, col9 = st.columns([1, 2, 1])
    with col8:
        genderbar = px.histogram(
            df,
            x="gender",
            color="customer_type",
            title="Number of Customer by Gender and Customer Type",
        )
        st.plotly_chart(genderbar, use_container_width=True)
        with st.expander("See Insight"):
            (
                "Pada tanggal **"
                + str(dates[0])
                + "** sampai **"
                + str(dates[1])
                + "** pengunjung supermarket kota **"
                + str(city)
                + "** paling banyak adalah **"
                + str(df.groupby("gender").size().idxmax())
                + "** dengan jumlah **"
                + str(df.groupby("gender").size().max())
                + "** pengunjung. Jumlah member supermarket paling banyak adalah **"
                + str(df.groupby(["customer_type", "gender"]).size().idxmax()[1])
                + "** sebanyak **"
                + str(df.groupby(["customer_type", "gender"]).size().max())
                + "** member."
            )
