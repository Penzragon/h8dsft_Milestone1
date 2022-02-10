from re import X
import streamlit as st
import pandas as pd
import plotly.express as px


def app():
    @st.cache
    def get_data():
        temp = pd.read_csv("dataset/cleandata.csv")
        temp["datetime"] = pd.to_datetime(temp["datetime"])
        return temp

    sales = get_data()

    st.markdown(
        "<h1 style='text-align: center;'>💲Visualization Dashboard💲</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align: center;'>Dataset yang digunakan dalam project ini adalah dataset yang sebelumnya sudah dilakukan preprocessing dari dataset penjualan sebuah supermarket dari January 2019 sampai Maret 2019. </p>",
        unsafe_allow_html=True,
    )

    with st.expander("About Dataset❔"):
        if st.checkbox("Show Dataset"):
            st.write(sales)
        st.write(
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
        )
    barcity = px.histogram(
        sales,
        y="city",
        x="gross_income",
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

    mask = (
        (sales.datetime.dt.date >= dates[0]) & (sales.datetime.dt.date <= dates[1])
        if city == "All City"
        else (
            (sales.datetime.dt.date >= dates[0])
            & (sales.datetime.dt.date <= dates[1])
            & (sales.city == city)
        )
    )

    df = sales[mask]

    kolom1, kolom2, kolom3, kolom4, kolom5 = st.columns([1, 1, 1, 1, 1])
    with kolom1:
        st.write("Total Invoice🛒")
        st.title(df.ID.count())
    with kolom2:
        st.write("Total Item Sold🛍️")
        st.title(df.quantity.sum())
    with kolom3:
        st.write("Total Purchased Amount💸")
        st.title("$" + "{:,.0f}".format(df.total.sum()))
    with kolom4:
        st.write("Total Gross Income💰")
        st.title("$" + "{:,.0f}".format(df.gross_income.sum()))
    with kolom5:
        st.write("Average Rating⭐")
        st.title(round(df.rating.mean(), 2))

    ### Area Chart ###
    areaplot = px.area(
        df.groupby(df.datetime.dt.date).gross_income.mean(),
        labels={"datetime": "Date", "value": "Gross Income"},
        title="Average Gross Income by Day",
    )
    st.plotly_chart(areaplot, use_container_width=True)
    with st.expander("Get Insight 🧠"):
        st.write(
            (
                "Pendapatan rata-rata terbesar supermarket "
                + ("kota **" + city + "** " if city != "All City" else "")
                + "adalah sebesar **$"
                + "{:,.2f}".format(
                    df.groupby(df.datetime.dt.date).gross_income.mean().max()
                )
                + "** yang berada pada tanggal **"
                + str(
                    df.groupby(df.datetime.dt.date)
                    .gross_income.mean()
                    .idxmax()
                    .strftime("%d %B %Y")
                )
                + "** sedangkan pendapatan rata-rata terkecilnya berada pada tanggal **"
                + str(
                    df.groupby(df.datetime.dt.date)
                    .gross_income.mean()
                    .idxmin()
                    .strftime("%d %B %Y")
                )
                + "** yaitu sebesar **$"
                + "{:,.2f}".format(
                    df.groupby(df.datetime.dt.date).gross_income.mean().min()
                )
                + "**."
            ).capitalize()
        )

    ### Hour Plot and Gender Plot ###
    col3, col4 = st.columns(2)
    with col3:
        barplot = px.bar(
            df.groupby(df.datetime.dt.hour).gross_income.sum(),
            labels={"datetime": "Hour", "value": "Gross Income"},
            title="Gross Income by Hour",
        )
        barplot.update_layout(
            xaxis=dict(
                tickmode="linear",
                tick0=10,
                dtick=1,
            )
        )
        st.plotly_chart(barplot, use_container_width=True)
        with st.expander("Get Insight 🧠"):
            st.write(
                (
                    ("Di **" + city + "**, " if city != "All City" else "")
                    + "Supermarket memiliki jumlah pendapatan terbesar yang berada pada **jam "
                    + str(df.groupby(df.datetime.dt.hour).gross_income.sum().idxmax())
                    + "** dengan jumlah pendapatan sebesar **$"
                    + "{:,.0f}".format(
                        df.groupby(df.datetime.dt.hour).gross_income.sum().max()
                    )
                    + "** dan jumlah pendapatan terkecil sebesar **$"
                    + "{:,.0f}".format(
                        df.groupby(df.datetime.dt.hour).gross_income.sum().min()
                    )
                    + "** yang berada pada **jam "
                    + str(df.groupby(df.datetime.dt.hour).gross_income.sum().idxmin())
                    + "**."
                ).capitalize()
            )

    with col4:
        genderbar = px.histogram(
            df,
            y="gender",
            color="customer_type",
            title="Number of Customer by Gender and Customer Type",
        )
        st.plotly_chart(genderbar, use_container_width=True)
        with st.expander("Get Insight 🧠"):
            st.write(
                (
                    "Pada tanggal **"
                    + str(dates[0].strftime("%d %B %Y"))
                    + "** sampai **"
                    + str(dates[1].strftime("%d %B %Y"))
                    + "** pengunjung supermarket "
                    + ("di kota **" + city + "** " if city != "All City" else "")
                    + "paling banyak adalah **"
                    + str(df.groupby("gender").size().idxmax())
                    + "** dengan jumlah **"
                    + str(df.groupby("gender").size().max())
                    + "** pengunjung dan jumlah member supermarket paling banyak adalah **"
                    + str(df.groupby(["customer_type", "gender"]).size().idxmax()[1])
                    + "** sebanyak **"
                    + str(df.groupby(["customer_type", "gender"]).size().max())
                    + "** member."
                ).capitalize()
            )

    ### for product line and payment ###
    col5, col6 = st.columns(2)
    with col5:
        productdf = df.groupby("product_line").size().reset_index(name="count")
        pieplotproduct = px.pie(
            productdf,
            values="count",
            names="product_line",
            title="Product Line Sold",
        )
        st.plotly_chart(pieplotproduct, use_container_width=True)
        with st.expander("Get Insight 🧠"):
            idmax = df.groupby("product_line").size().idxmax()
            st.write(
                (
                    "Produk yang paling banyak dibeli di supermarket "
                    + ("kota **" + city + "** " if city != "All City" else "")
                    + "adalah produk berkategori **"
                    + str(df.groupby("product_line").size().idxmax())
                    + "** yang dibeli sebanyak **"
                    + str(df.groupby("product_line").size().max())
                    + "x** dengan **"
                    + str(df[df.product_line == idmax].quantity.sum())
                    + " item** yang terjual dan menyumbang pendapatan sebesar **$"
                    + "{:,.0f}".format(df[df.product_line == idmax].gross_income.sum())
                    + "**."
                ).capitalize()
            )

    with col6:
        paymentdf = df.groupby("payment").size().reset_index(name="count")
        pieplotpayment = px.pie(
            paymentdf, values="count", names="payment", title="Payment Method Used"
        )
        st.plotly_chart(pieplotpayment, use_container_width=True)
        with st.expander("Get Insight 🧠"):
            idmax = df.groupby("payment").size().idxmax()
            st.write(
                (
                    "Di supermarket "
                    + ("kota **" + city + "** " if city != "All City" else "")
                    + "metode pembayaran yang paling sering digunakan adalah metode pembayaran menggunakan **"
                    + str(df.groupby("payment").size().idxmax())
                    + "** dengan jumlah penggunaan sebanyak **"
                    + str(df.groupby("payment").size().max())
                    + "x** dan total pembelian sebesar **$"
                    + "{:,.0f}".format(df[df.payment == idmax].total.sum())
                    + "**."
                ).capitalize()
            )
