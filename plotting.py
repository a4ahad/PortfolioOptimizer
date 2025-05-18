import plotly.graph_objs as go
import streamlit as st
import plotly.express as px

# Function to plot stock data
def plot_stock_data(data):
    fig = go.Figure()
    # Looping through each ticker in the specified column range
    for ticker in data.columns:
        # Adding a line trace for each ticker
        fig.add_trace(go.Scatter(x=data.index, y=data[ticker], mode='lines', name=str(ticker)))
    # Updating the layout of the plot
    fig.update_layout(title='Stock Prices Over Time',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_dark',
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      font=dict(color='green'))
    # Displaying the plot in Streamlit
    st.plotly_chart(fig)

# Function to plot portfolio optimization results
def plot_optimization_results(results_df):
    fig = go.Figure(data=go.Scatter(x=results_df['Volatility'], y=results_df['Returns'], mode='markers'))
    # Update the layout of the plot
    fig.update_layout(title='Portfolio Optimization',
                      xaxis_title='Volatility (Risk)',
                      yaxis_title='Returns',
                      template='plotly_dark',
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      font=dict(color='green'))
    # Displaying the plot in Streamlit
    st.plotly_chart(fig)

# Function to plot a correlation heatmap
def plot_correlation_heatmap(data):
    corr = data.corr()
    # Create a heatmap of the correlation matrix
    fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', zmin=-1, zmax=1)
    # Update the layout of the plot
    fig.update_layout(title='Correlation Matrix Heatmap', title_x=0.5)
    # Displaying the plot in Streamlit
    st.plotly_chart(fig)