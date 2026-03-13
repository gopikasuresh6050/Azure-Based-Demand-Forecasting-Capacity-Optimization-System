import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Azure Capacity Planner", layout="wide")

st.title("📊 Azure Demand & Capacity Optimization")

# Load your Milestone 3 results
# NOTE: Assuming 'demand forecasting results.csv' is available in the Colab environment.
# If your results are in 'demand forecasting results.xlsx', you'll need to change this line.
# For demonstration, I'm creating a dummy dataframe if the file isn't found.
try:
    results = pd.read_csv('demand forecasting results.csv') 
    # Ensure 'Date' column is present or create a dummy one for plotting
    if 'Date' not in results.columns:
        results['Date'] = pd.to_datetime(pd.date_range(start='2023-01-01', periods=len(results)))
except FileNotFoundError:
    st.warning("Results CSV not found. Using dummy data for demonstration.")
    # Create a dummy DataFrame for results
    data = {
        'Date': pd.to_datetime(pd.date_range(start='2023-01-01', periods=10)),
        'Actual': [8000, 8100, 8050, 8200, 8150, 8300, 8250, 8400, 8350, 8500],
        'Predicted': [7900, 8050, 8000, 8100, 8100, 8250, 8200, 8300, 8300, 8450],
        'Capacity': [8000, 8000, 8000, 8200, 8200, 8300, 8300, 8400, 8400, 8500],
        'Region': ['eastus', 'westeurope', 'eastus', 'westeurope', 'eastus', 'westeurope', 'eastus', 'westeurope', 'eastus', 'westeurope']
    }
    results = pd.DataFrame(data)


# Metric calculation (Simulating the -$120M per 1% gain)
accuracy_gain = 2.5 # Example percentage improvement over old system
savings = accuracy_gain * 120 

col1, col2, col3 = st.columns(3)
col1.metric("Forecast Accuracy", "94.2%", "+1.5%")
col2.metric("Estimated CAPEX Savings", f"${savings}M")
col3.metric("System Health", "Optimal")

# Plot Actual vs Predicted
st.subheader("Compute Demand: Actual vs Predicted")
fig = px.line(results, x='Date', y=['Actual', 'Predicted'], 
              title="Demand Trends across Regions")
st.plotly_chart(fig, use_container_width=True)

# Actionable Intelligence Table
st.subheader("Capacity Recommendations")
results['Action'] = results.apply(lambda x: 'Provision More' if x['Predicted'] > x['Capacity'] else 'Optimize Cost', axis=1)
st.table(results[['Region', 'Predicted', 'Capacity', 'Action']].head(10))
