# Azure Demand Forecasting & Capacity Optimization System

# Project Overview
This project focuses on analyzing cloud resource usage and forecasting demand to optimize capacity and reduce operational costs. The system evaluates relationships between usage patterns and cost behavior using statistical analysis and predictive modeling techniques.the dataset has been enriched and transformed into a model-ready format through feature engineering.

# Objectives
- Analyze usage and cost trends
- Perform correlation analysis
- Forecast future demand
- Optimize capacity provisioning
- Improve cost efficiency

# Dataset Description
The dataset contains 540 records with the following features:
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
- time-based seasonality indicators (Day, Month, Week, Quarter, DayOfWeek)  
- Infrastructure utilization metric  
- Lag variables (Lag_1, Lag_7, Lag_30)  
- Rolling mean features (7-day and 30-day trends)  
- Demand spike indicator  

Categorical variables such as Region and Service were encoded and the dataset was transformed into a consistent time-series format suitable for machine learning model development.

# Key Findings
- A strong negative correlation (–0.98) was observed between Usage_Units and Cost_USD.
- This indicates an inverse relationship within the dataset.
- The behavior suggests structured or simulated data patterns rather than real-world billing dynamics.
- 

# Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab

# Analysis Performed
- Data Cleaning
- Correlation Analysis
- Visualization
- Demand Pattern Evaluation
- Feature Engineering
- Data Transformation

# Future Improvements
- Implement ARIMA/LSTM forecasting models
- Real-time Azure integration  
- Dashboard using Power BI or Streamlit
- Real-time Azure integration
- Dashboard using Power BI or Streamlit
