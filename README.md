# Azure Demand Forecasting & Capacity Optimization System

# Project Overview
This project focuses on analyzing cloud resource usage and forecasting demand to optimize capacity and reduce operational costs. The system evaluates relationships between usage patterns and cost behavior using statistical analysis and predictive modeling techniques.

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

# Key Findings
- A strong negative correlation (–0.98) was observed between Usage_Units and Cost_USD.
- This indicates an inverse relationship within the dataset.
- The behavior suggests structured or simulated data patterns rather than real-world billing dynamics.

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

# Future Improvements
- Implement ARIMA/LSTM forecasting models
- Real-time Azure integration
- Dashboard using Power BI or Streamlit
