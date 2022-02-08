# Milestones 1

Milestones ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Phase 0.

---

By [Rifky Aliffa](https://github.com/Penzragon)

## Dataset

Dataset yang digunakan dalam project ini adalah dataset penjualan sebuah supermarket di Myanmar dari January 2019 sampai Maret 2019. Dataset ini berisi 1000 baris dengan 13 kolom yang diantaranya adalah Invoice id, Branch, City, Customer type, Gender, Product line, Unit price, Quantity, Tax, Total, Date, Payment, COGS, Gross margin percentage, Gross income, dan Rating. Dataset dapat dilihat di [Kaggle](https://www.kaggle.com/aungpyaeap/supermarket-sales)

Keterangan pada kolom pada dataset ini adalah:

| Feature                 | Description                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Invoice id              | Computer generated sales slip invoice identification number                                                                                                    |
| Branch                  | Branch of supercenter (3 branches are available identified by A, B and C)                                                                                      |
| City                    | Location of supercenters                                                                                                                                       |
| Customer type           | Type of customers, recorded by Members for customers using member card and Normal for without member card                                                      |
| Gender                  | Gender type of customer                                                                                                                                        |
| Product line            | General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel |
| Unit price              | Price of each product in $                                                                                                                                     |
| Quantity                | Number of products purchased by customer                                                                                                                       |
| Tax                     | 5% tax fee for customer buying                                                                                                                                 |
| Total                   | Total price including tax                                                                                                                                      |
| Date                    | Date of purchase (Record available from January 2019 to March 2019)                                                                                            |
| Time                    | Purchase time (10am to 9pm)                                                                                                                                    |
| Payment                 | Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)                                                                |
| COGS                    | Cost of goods sold                                                                                                                                             |
| Gross margin percentage | Gross margin percentage                                                                                                                                        |
| Gross income            | Gross income                                                                                                                                                   |
| Rating                  | Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)                                                                    |

## Objectives

Tujuan yang ingin dicapai pada project ini adalah:

- Mencari tahu kota manakah yang memiliki pendapatan kotor paling besar.
- Melakukan uji hipotesis untuk mengetahui apakah rata-rata pendapatan kotor dari tiap kota memiliki perbedaan yang signifikan.
