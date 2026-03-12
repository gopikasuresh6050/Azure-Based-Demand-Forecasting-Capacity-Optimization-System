# Azure Demand Forecasting & Capacity Optimization System

## Project Overview
This project focuses on analyzing cloud resource usage and forecasting demand to optimize capacity and reduce operational costs. The system evaluates relationships between usage patterns and cost behavior using statistical analysis and predictive modeling techniques. The dataset was enriched and transformed into a model-ready format through feature engineering. Machine learning models were developed to forecast future Azure resource demand based on historical usage data.

---

## Objectives
- Analyze usage and cost trends  
- Perform correlation analysis  
- Forecast future demand  
- Optimize capacity provisioning  
- Improve cost efficiency  

---

## Dataset Description
The dataset contains **540 records** with the following features:

- Timestamp  
- Region  
- Service  
- Usage_Units  
- Provisioned_Capacity  
- Cost_USD  
- Availability_%  
- Holiday  
- Economic_Index  
- Seasonal_Factor  

### Feature Engineering
Additional derived features were created including:

- Time-based seasonality indicators (Day, Month, Week, Quarter, DayOfWeek)  
- Infrastructure utilization metric  
- Lag variables (Lag_1, Lag_7, Lag_30)  
- Rolling mean features (7-day and 30-day trends)  
- Demand spike indicator  

Categorical variables were encoded and the dataset was transformed into a consistent **time-series format suitable for machine learning model development.**

---

## Key Findings
- A strong negative correlation **(-0.98)** was observed between **Usage_Units** and **Cost_USD**  
- This indicates an inverse relationship within the dataset  
- The behavior suggests structured or simulated data patterns rather than real-world billing dynamics  

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Google Colab  

---

## Analysis Performed
- Data Cleaning  
- Correlation Analysis  
- Visualization  
- Feature Engineering  
- Demand Pattern Evaluation  
- Data Transformation  
- Machine Learning Model Training  
- Forecast Accuracy Evaluation  

---

## Model Development
A **Random Forest regression model** was implemented to forecast future Azure resource demand using historical usage data and engineered features.

The dataset was split into **training and testing sets while maintaining time-series order**. The categorical feature **Seasonal_Factor** was encoded to improve model performance.

### Model Performance Metrics
- **Mean Absolute Error (MAE):** 281.48  
- **Root Mean Squared Error (RMSE):** 520.38  

The model predictions were compared against actual demand values, and the results were exported to **forecast_results.xlsx** for further evaluation.

---

## Future Improvements
- Implement additional forecasting models such as **ARIMA, XGBoost, and LSTM**  
- Deploy the model for **real-time Azure demand prediction**  
- Integrate forecasting outputs with a **dashboard (Power BI / Streamlit)**  
- Automate **model retraining and monitoring pipeline**

---

## Project Status
- **Milestone 1:** Environment setup and dataset preparation ✔  
- **Milestone 2:** Data processing and feature engineering ✔  
- **Milestone 3:** Machine learning model development and evaluation ✔
