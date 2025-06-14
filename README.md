## 🏥 Hospital Readmission Reduction Analysis

### 📌 Overview

This project investigates hospital readmission trends across U.S. hospitals using data from the **Hospital Readmissions Reduction Program (HRRP)**. It explores relationships among **readmissions, discharges, and predicted rates** through detailed statistical and visual analyses to improve healthcare quality and performance.

---

### 🎯 Objectives

* Clean and preprocess hospital-level readmission data
* Identify hospitals and states with the highest readmission rates
* Compare actual vs predicted vs expected readmissions
* Perform statistical testing and uncover contributing conditions
* Offer data-driven recommendations to reduce readmissions

---

### 📂 Dataset Details

**Source:** HRRP Hospital Readmissions Dataset
**Key Columns:**

* Hospital Name
* State
* Measure Name (e.g., Heart Failure, Pneumonia)
* Number of Readmissions
* Number of Discharges
* Predicted and Expected Readmission Rates

---

### 🧰 Tech Stack

* **Python**
* **Pandas, NumPy** – for data wrangling
* **Matplotlib, Seaborn** – for static visualizations
* **SciPy** – for statistical testing (t-test)
* **Scikit-learn** – for evaluation metrics like MAE

---

### ⚙️ Project Workflow

#### 1. 🧹 Data Preprocessing

* Replaced missing values like “Not Available” or “Too Few to Report” with 0
* Converted numeric columns for proper analysis

#### 2. 📊 Exploratory Data Analysis

* Aggregated and visualized average readmission rates
* Compared states and hospitals by total readmissions
* Analyzed condition-wise trends using “Measure Name”

#### 3. 📈 Visualizations

* **Bar Plots:** Top 10 hospitals and conditions by average readmissions
* **Pie Charts:** Disease-wise share of total readmissions
* **Scatter Plots:** Comparison of actual, predicted, and expected rates
* **Box Plots:** Detected outliers in hospital metrics
* **Heatmaps:** Correlation among all numerical features

#### 4. 🧮 Statistical Analysis

* **Mean Absolute Error (MAE):** Measured prediction error
* **T-test:** Found significant difference between actual and predicted values

  * *Result:* **p-value < 0.05** → statistically significant deviation

---

### 📊 Key Insights

* Conditions like **Heart Failure** and **Pneumonia** are major contributors to readmissions.
* Some **states consistently show higher average readmission rates**.
* Several **hospitals exceed expected readmission rates**, flagging quality issues.
* Prediction errors suggest a need for better forecasting models.

---

### 📈 Results Summary

| Metric         | Result                                          |
| -------------- | ----------------------------------------------- |
| MAE            | Low–Moderate                                    |
| T-test p-value | < 0.05                                          |
| Conclusion     | Prediction errors are statistically significant |

---

### 💡 Future Improvements

* Implement ML models like **Linear Regression**, **XGBoost**, or **Random Forest** for better prediction
* Add **patient-level** or **temporal data** for longitudinal tracking
* Develop **interactive dashboards** for hospital performance monitoring
* Use **clustering algorithms** to group hospitals with similar behaviors

---

### 👨‍💻 Owner

**Khushboo Verma**

This project reflects real-world healthcare analytics to support better hospital practices, reduce readmissions, and guide healthcare policy.

---

### 🚀 Final Note

Through a combination of **statistical analysis, EDA, and compelling visual storytelling**, this project uncovers the hidden patterns in hospital readmissions. It sets the foundation for predictive modeling and smarter healthcare decisions aimed at improving patient outcomes and hospital efficiency.
