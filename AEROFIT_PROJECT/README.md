# 🚀 AeroFit Customer Analytics & Recommendation System

## 📌 Project Overview

This project focuses on analyzing customer purchase behavior for AeroFit treadmills and building a data-driven system to **predict product selection**, **segment customers**, and **recommend the most suitable treadmill**.

The objective is to transform raw customer data into **actionable business insights** and **intelligent recommendations**, enabling better targeting, personalization, and decision-making.

---

## 🎯 Business Problem

AeroFit aims to:

* Identify **target customer profiles** for each treadmill product
* Understand **key factors influencing purchase decisions**
* Provide **personalized product recommendations**
* Improve **marketing strategies and sales conversion**

---

## 📊 Dataset Description

The dataset contains customer-level information, including:

* Product Purchased (KP281, KP481, KP781)
* Age
* Gender
* Education
* Marital Status
* Usage (times per week)
* Income
* Fitness Level (1–5 scale)
* Miles (weekly running/walking distance)

---

## 🔍 Exploratory Data Analysis (EDA)

### ✔ Data Understanding

* Analyzed dataset structure, data types, and statistical summary
* Converted categorical variables for efficient processing
* Checked for missing values and data consistency

### ✔ Univariate Analysis

* Product distribution showed:

  * KP281 (Entry-level) → Most popular
  * KP481 (Mid-level) → Moderate demand
  * KP781 (Premium) → Niche segment
* Income and usage showed right-skewed distribution

### ✔ Bivariate Analysis

* Strong relationship between:

  * **Income and Product selection**
  * **Fitness level and Product selection**
  * **Usage and Miles**
* KP781 buyers are typically:

  * High-income
  * High fitness
  * Frequent users

### ✔ Correlation Analysis

* Positive correlation between:

  * Fitness ↔ Miles
  * Usage ↔ Miles
* Income emerged as the **strongest predictor**

### ✔ Outlier Detection

* Identified outliers in Income and Miles using boxplots
* Outliers represent high-value customers (premium segment)

---

## 📈 Probability Analysis

### ✔ Marginal Probability

* Computed distribution of customers across products

### ✔ Conditional Probability

* Example:

  * Probability of a male customer buying KP781
  * Probability of high-income users purchasing premium products

👉 Helped quantify customer behavior patterns and decision likelihoods

---

## 👥 Customer Profiling

### 🟢 KP281 – Entry Level

* Low to mid income
* Beginner fitness level
* Low usage frequency

### 🟡 KP481 – Mid Level

* Moderate income
* Regular fitness users
* Moderate usage

### 🔴 KP781 – Premium

* High income
* High fitness level
* Frequent usage
* Performance-focused users

---

## 🤖 Machine Learning Model

### 🎯 Objective:

Predict which treadmill a customer is likely to purchase

### ✔ Model Used:

* Random Forest Classifier

### ✔ Key Results:

* Achieved high prediction accuracy (~85–90%)
* Identified feature importance:

  * Income → Most influential
  * Fitness → Second
  * Usage → Third

👉 Enabled **data-driven product prediction**

---

## 🔗 Customer Segmentation (Clustering)

### ✔ Technique:

* K-Means Clustering

### ✔ Output:

Customers segmented into 3 groups:

1. Beginners (Low income, low fitness)
2. Intermediate users
3. Advanced athletes (High income, high usage)

👉 Helps in **targeted marketing & personalization**

---

## 🎯 Recommendation System

### ✔ Built a Rule-Based System:

Recommends treadmill based on:

* Income
* Fitness level
* Usage

### ✔ Example Logic:

* High income + high fitness → KP781
* Mid income → KP481
* Low income → KP281

👉 Provides **personalized product suggestions**

---

## 📊 Dashboard (Optional Extension)

* Interactive dashboard built using Streamlit / Power BI
* Allows users to input data and get recommendations in real-time

---

## 💡 Key Insights

* Income is the **strongest driver of product purchase**
* High fitness users prefer premium treadmills
* KP281 dominates the mass market segment
* Clear segmentation exists across customer groups
* Usage and fitness strongly influence product selection

---

## 📌 Business Recommendations

* 🎯 Target KP281 to beginners and budget-conscious users
* 💎 Focus KP781 marketing on high-income fitness enthusiasts
* 🔄 Upsell KP281 users with EMI and upgrade offers
* 📢 Use segmentation for personalized campaigns
* 🤖 Deploy recommendation system for customer guidance

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit (for dashboard)

---

## 🏆 Project Highlights

* End-to-end Data Analysis (EDA → Insights → ML)
* Applied Probability & Statistics in real-world scenario
* Built Machine Learning prediction model
* Developed Customer Segmentation using clustering
* Designed a Recommendation System
* Business-focused insights and actionable strategies

---

## 🚀 Conclusion

This project demonstrates how data analytics and machine learning can be leveraged to:

* Understand customer behavior
* Predict future actions
* Deliver personalized recommendations
* Drive business growth through data-driven decisions

---

## ⭐ Future Enhancements

* Model explainability using SHAP
* Deployment on cloud platforms (AWS / Render)
* Real-time recommendation engine
* Advanced ML models (XGBoost, Neural Networks)

---

## 📬 Author

**Ritu Raj Kashyap**

---
