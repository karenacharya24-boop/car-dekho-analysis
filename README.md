# 🚗 Car Dekho Used Car Market Analysis

An exploratory data analysis (EDA) project analyzing used car market trends, price distributions, brand retention, and depreciation factors using Python.

---

## 📌 Project Overview
This project processes marketplace data from CarDekho to answer key business questions regarding vehicle manufacturing years, pricing extremes, brand value retention, and primary factors driving depreciation.

---

## 📂 Repository Structure
* `car_analysis.py` — Main Python script containing data cleaning, exploratory analysis, and dashboard visualizations.
* `1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv` — Dataset file.
* `README.md` — Project documentation.

---

## 📊 Key Findings

* **Year Range:** 2003 to 2018
* **Selling Price Range:** ₹0.10 Lakh (₹10,000) to ₹35.00 Lakhs
* **Total Records:** 299 listings (after removing duplicates)
* **Most Sold Vehicle:** Honda City (26 listings)
* **Fuel Distribution:** Petrol (239), Diesel (58), CNG (2)
* **Transmission Type:** Manual (259), Automatic (40)
* **Single-Owner Vehicles:** 290 listings (`Owner == 0` denotes first owner)
* **Most Depreciated Vehicle (%):** Toyota Camry (89.46% value lost)
* **Top Retaining Brands:** Hyundai, Honda, Maruti (<25% average value loss)
* **Primary Depreciation Factors:** Vehicle Age ($r = 0.85$) and Kilometers Driven ($r = 0.51$)

