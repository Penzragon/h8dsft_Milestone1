import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import plotly.express as px

st.set_option("deprecation.showPyplotGlobalUse", False)


def app():
    st.markdown(
        "<h1 style='text-align: center;'>🔬Hypothesis Testing🔬</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        """
    Pada bagian ini akan dilakukan uji hipotesis untuk mengetahui **apakah rata-rata pendapatan kotor dari kota dengan pendapat kotor paling besar memiliki perbedaan signifikan dengan kota dengan pendapatan kotor paling kecil**."""
    )

    sales = pd.read_csv("dataset/cleandata.csv")
    sales["datetime"] = pd.to_datetime(sales["datetime"])
    naypyitaw_income = (
        sales[sales.city == "Naypyitaw"]
        .groupby(sales.datetime.dt.date)
        .gross_income.sum()
    )
    mandalay_income = (
        sales[sales.city == "Mandalay"]
        .groupby(sales.datetime.dt.date)
        .gross_income.sum()
    )
    yangon_income = (
        sales[sales.city == "Yangon"].groupby(sales.datetime.dt.date).gross_income.sum()
    )

    if st.checkbox("Show Average Income"):
        col1, col2 = st.columns(2)
        with col1:
            mean_datetime_city = sales.groupby("city").gross_income.mean().reset_index()
            piechart = px.pie(
                mean_datetime_city,
                names="city",
                values="gross_income",
                title="Average Income",
            )
            piechart.update_traces(hovertemplate="%{label}<br>$%{value:.2f}")
            st.plotly_chart(piechart, use_container_width=True)

        with col2:
            boxplot = px.box(
                sales,
                y="city",
                x="gross_income",
                color="city",
                title="Gross Income Distribution by City",
                labels={"city": "City", "gross_income": "Gross Income"},
            )
            st.plotly_chart(boxplot, use_container_width=True)

        st.write(
            "**Naypyitaw** average income: **$"
            + str(round(sales[sales.city == "Naypyitaw"].gross_income.mean(), 2))
            + "**"
        )
        st.write(
            "**Mandalay** average income: **$"
            + str(round(sales[sales.city == "Mandalay"].gross_income.mean(), 2))
            + "**"
        )
        st.write(
            "**Yangon** average income: **$"
            + str(round(sales[sales.city == "Yangon"].gross_income.mean(), 2))
            + "**"
        )

    st.write(
        """
    Karena kota **Naypyitaw** adalah kota dengan pendapatan kotor paling besar dan kota **Yangon** adalah kota dengan pendapatan kotor paling kecil, maka:
    - Null Hypothesis (**H0**): μNaypyitaw = μYangon (Perbedaan rata-rata pendapatan Naypyitaw dan Yangon **tidak signifikan**)
    - Alternative Hypothesis (**H1**): μNaypyitaw != μYangon (Perbedaan rata-rata pendapatan Naypyitaw dan Yangon **signifikan**)
    """
    )

    st.markdown(
        "<h2 style='text-align: center;'>Two Sample T-Test</h2>", unsafe_allow_html=True
    )
    st.write(
        """
        Karena pada uji hipotesis ini menggunakan dua kelompok yang indepedent yaitu rata-rata pendapatan kota **Naypyitaw** dan rata-rata pendapatan kota **Yangon**, 
        maka akan menggunakan uji **Two Sample T-Test** dengan significant thershold **0.05**. Dan didapatkan t-statistic dan p-value sebagai berikut:
        """
    )

    significant_threshold = 0.05
    tstat, pval = stats.ttest_ind(naypyitaw_income, yangon_income)
    st.write("t-statistic: ", tstat)
    st.write("p-value: ", pval)

    if st.checkbox("Show Visualization"):
        kol1, kol2, kol3 = st.columns([1, 3, 1])
        with kol2:
            plt.figure(figsize=(10, 6))
            naypyitaw_population = np.random.normal(
                naypyitaw_income.mean(), naypyitaw_income.std(), 1000
            )
            yangon_population = np.random.normal(
                yangon_income.mean(), yangon_income.std(), 1000
            )
            ci = stats.norm.interval(
                0.95, loc=naypyitaw_income.mean(), scale=naypyitaw_income.std()
            )
            sns.histplot(
                naypyitaw_population, bins=50, label="Naypyitaw", color="red", kde=True
            )
            sns.histplot(
                yangon_population, bins=50, label="Yangon", color="blue", kde=True
            )
            plt.axvline(x=naypyitaw_income.mean(), color="red", label="Naypyitaw mean")
            plt.axvline(x=yangon_income.mean(), color="blue", label="Yangon mean")
            plt.axvline(
                naypyitaw_population.mean() + tstat * naypyitaw_population.std(),
                color="black",
                linestyle="dashed",
                linewidth=2,
                label="Alternative Hypothesis",
            )
            plt.axvline(
                naypyitaw_population.mean() - tstat * naypyitaw_population.std(),
                color="black",
                linestyle="dashed",
                linewidth=2,
            )
            plt.axvline(
                x=ci[0], color="green", linestyle="--", label="Confidence Interval"
            )
            plt.axvline(x=ci[1], color="green", linestyle="--")
            plt.title("Two Sample T-Test")
            plt.xlabel("Income")
            plt.ylabel("Frequency")
            plt.legend()
            st.pyplot()

    with st.expander("See Conclusion🔍"):
        if pval <= significant_threshold:
            st.markdown(
                "<h3 style='text-align: center;'>Reject the null hypothesis</h3>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<h3 style='text-align: center;'>Fail to reject the null hypothesis</h3>",
                unsafe_allow_html=True,
            )
        st.write(
            "Dari hasil uji hipotesis menggunakan **two sampe t-test** dengan significant threshold sebesar 0.05 p-value yang didapatkan adalah ",
            pval,
            ", karena p-value lebih besar dari significant threshold maka pada uji hipotesis ini **gagal menolak H0** karena **tidak cukup bukti** untuk menolak hipotesis tersebut.",
        )
        st.write(
            "Jadi, dapat disimpulkan bahwa perbedaan rata-rata pendapatan kotor kota Naypyitaw dengan kota Yangon **tidak signifikan**."
        )
