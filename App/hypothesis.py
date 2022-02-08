import streamlit as st

st.markdown(
    "<h1 style='text-align: center;'>Hypothesis Testing</h1>", unsafe_allow_html=True
)

"""
Pada bagian ini akan dilakukan uji hipotesis untuk mengetahui **apakah rata-rata pendapatan kotor dari kota dengan pendapat kotor paling besar memiliki perbedaan signifikan dengan kota dengan pendapatan kotor paling kecil** menggunakan two sample t-test dengan significant threshold sebesar 0.05.

Karena kota **Naypyitaw** adalah kota dengan pendapatan kotor paling besar dan kota **Yangon** adalah kota dengan pendapatan kotor paling kecil, maka:
- Null Hypothesis (**H0**): μNaypyitaw = μYangon (Perbedaan rata-rata pendapatan Naypyitaw dan Yangon **tidak signifikan**)
- Alternative Hypothesis (**H1**): μNaypyitaw != μYangon (Perbedaan rata-rata pendapatan Naypyitaw dan Yangon **signifikan**)
"""
