# Importing necessary libraries
import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
from scipy.optimize import minimize

# Loading custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Fetching stock data
@st.cache_data
def fetch_data(tickers, start_date, end_date):
    tickers_list = [ticker.strip() for ticker in tickers.split(',') if ticker.strip()]
    all_data = pd.DataFrame()
    for ticker in tickers_list:
        data = yf.download(ticker, start=start_date, end=end_date)[['Adj Close']]
        data = data.rename(columns={'Adj Close': ticker})
        data.index = data.index.strftime('%Y-%m-%d')
        all_data = pd.concat([all_data, data], axis=1)
    return all_data

# Calculating portfolio statistics
def calculate_portfolio_statistics(data):
    returns = data.pct_change().dropna()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    variance = returns.var()
    std_dev = returns.std()
    return mean_returns, cov_matrix, variance, std_dev

# Calculating VaR and CVaR
def calculate_var_cvar(returns, confidence_level=0.95):
    var = np.percentile(returns, (1 - confidence_level) * 100)
    cvar = returns[returns <= var].mean()
    return var, cvar

# Optimizing portfolio and calculate efficient frontier
def optimize_portfolio(mean_returns, cov_matrix, num_portfolios=10000):
    results = np.zeros((5, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        portfolio_return = np.sum(weights * mean_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        portfolio_returns = np.dot(weights, mean_returns)
        var, cvar = calculate_var_cvar(portfolio_returns)
        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = results[0, i] / results[1, i]
        results[3, i] = var
        results[4, i] = cvar
        weights_record.append(weights)
    results_df = pd.DataFrame(results.T, columns=['Returns', 'Volatility', 'Sharpe Ratio', 'VaR', 'CVaR'])
    return results_df, weights_record

# Corrected plotting stock data function
def plot_stock_data(data, start_col, end_col):
    fig = go.Figure()
    for ticker in data.columns[start_col:end_col]:
        fig.add_trace(go.Scatter(x=data.index, y=data[ticker], mode='lines', name=str(ticker)))
    fig.update_layout(title='Stock Prices Over Time',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_dark',
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      font=dict(color='green'),
                      legend=dict(x=1.05, y=1))
    st.plotly_chart(fig)

# Scatter plot starts
# Plotting optimization results with efficient frontier and highlighted company positions
def plot_optimization_results(results_df, weights_record, mean_returns, cov_matrix):
    fig = go.Figure()

    # Plotting the scatter points for the portfolios
    fig.add_trace(go.Scatter(
        x=results_df['Volatility'],
        y=results_df['Returns'],
        mode='markers',
        marker=dict(
            color=results_df['Sharpe Ratio'],
            colorscale='Viridis',
            showscale=True,
            size=5,
            opacity=0.7
        ),
        text=[f"Portfolio {i+1}" for i in range(len(results_df))],
        hoverinfo='text'
    ))

    # Calculating and plotting the efficient frontier line
    frontier_y = []
    frontier_x = []
    
    for possible_return in np.linspace(results_df['Returns'].min(), results_df['Returns'].max(), num=100):
        constraints = (
            {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
            {'type': 'eq', 'fun': lambda w: np.sum(w * mean_returns) - possible_return}
        )
        res = minimize(lambda w: np.sqrt(np.dot(w.T, np.dot(cov_matrix, w))), 
                       x0=np.ones(len(mean_returns)) / len(mean_returns), 
                       method='SLSQP', 
                       bounds=[(0.0, 1.0)] * len(mean_returns), 
                       constraints=constraints)
        frontier_y.append(possible_return)
        frontier_x.append(res.fun)
    
    fig.add_trace(go.Scatter(
        x=frontier_x,
        y=frontier_y,
        mode='lines',
        name='Efficient Frontier',
        line=dict(color='red', width=2)
    ))

    # Highlight company positions by color highlighting and add intersection points where return and volatility meet
    company_names = ['AMZN', 'MCD', 'MSFT', 'WMT', 'INTC']
    for i in range(len(mean_returns)):
        fig.add_trace(go.Scatter(
            x=[results_df.iloc[i]['Volatility']],
            y=[results_df.iloc[i]['Returns']],
            mode='markers+text',
            marker=dict(color='blue', size=10),
            text=[company_names[i]],
            textposition="top center",
            name=company_names[i]
        ))

    fig.update_layout(
        title='Portfolio Optimization',
        xaxis_title='Volatility (Risk)',
        yaxis_title='Returns',
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(color='green'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig)
# Scatter plot ends

# Plotting correlation heatmap
def plot_correlation_heatmap(data):
    corr = data.corr()
    fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', zmin=-1, zmax=1, labels=dict(color="Correlation"))
    fig.update_layout(title='Correlation Matrix Heatmap', title_x=0.5)
    st.plotly_chart(fig)

# Sidebar inputs
st.sidebar.title('Trent University')
st.sidebar.image('trent_logo.png', width=100)
tickers = st.sidebar.text_input('Enter stock symbols (comma separated)', 'AMZN, MCD, MSFT, WMT, INTC')
start_date = st.sidebar.date_input('Start Date', datetime(2024, 5, 1))
end_date = st.sidebar.date_input('End Date', datetime(2024, 10, 31))
page_size = st.sidebar.slider('Page Size', min_value=1, max_value=10, value=5, step=1)
num_portfolios = st.sidebar.slider('Number of Portfolios', min_value=1000, max_value=10000, step=1000)

# Loading CSS and display logo
load_css("styles.css")

# Fetching stock data based on user input
stock_data = fetch_data(tickers, start_date, end_date)

# Displaying and plotting paginated data
st.title('Portfolio Optimizer')
st.markdown("#### Project carried out by Md Abdul Ahad and Ekpereamaka Nwachukwu")
st.subheader('Stock Data')

num_pages = len(stock_data.columns) // page_size + 1
page = st.sidebar.number_input('Page', min_value=1, max_value=num_pages, step=1)
start_col = (page - 1) * page_size
end_col = min(page * page_size, len(stock_data.columns))
st.write(stock_data.iloc[:, start_col:end_col])
plot_stock_data(stock_data.iloc[:, start_col:end_col], start_col=start_col, end_col=end_col)

# Explanation for Stock Prices Over Time
st.markdown("""
**Figure 1: Stock Prices Over Time**
This figure shows the adjusted closing prices of the selected stocks over the specified date range. Each line represents a different stock.
""")

# Calculating portfolio statistics and optimizing the portfolio
mean_returns, cov_matrix, variance, std_dev = calculate_portfolio_statistics(stock_data)
results_df, weights_record = optimize_portfolio(mean_returns, cov_matrix, num_portfolios)

# Display optimized portfolio and plots
st.subheader('Optimized Portfolio')
st.write(results_df)

# Explanation for Optimized Portfolio
st.markdown("""
**Table 1: Optimized Portfolio**
This table displays the optimized portfolio statistics for the selected stocks. The columns include:
- **Returns**: The expected return of the portfolio.
- **Volatility**: The risk or standard deviation of the portfolio returns.
- **Sharpe Ratio**: The risk-adjusted return of the portfolio.
- **VaR**: Value at Risk, a measure of the potential loss in value of the portfolio.
- **CVaR**: Conditional Value at Risk, an average of the losses that occur beyond the VaR threshold.
""")

plot_optimization_results(results_df, weights_record, mean_returns, cov_matrix)

# Explanation for Portfolio Optimization Plot
st.markdown("""
**Figure 2: Portfolio Optimization**
This scatter plot shows the relationship between the volatility (risk) and returns of the optimized portfolios. Each point represents a different portfolio with a unique combination of stock weights. The red line represents the efficient frontier, and the highlighted points indicate the positions of individual companies.
""")

# Plotting correlation heatmap
st.subheader('Correlation Matrix Heatmap')
plot_correlation_heatmap(stock_data)

# Explanation for Correlation Matrix Heatmap
st.markdown("""
**Figure 3: Correlation Matrix Heatmap**
This heatmap shows the correlation coefficients between the returns of the selected stocks. A value close to 1 indicates a strong positive correlation, while a value close to -1 indicates a strong negative correlation.
""")

# Displaying maximum and minimum Sharpe ratios
max_sharpe_ratio = results_df['Sharpe Ratio'].max()
min_sharpe_ratio = results_df['Sharpe Ratio'].min()

st.write(f"Maximum Sharpe Ratio: {max_sharpe_ratio}")
st.write(f"Minimum Sharpe Ratio: {min_sharpe_ratio}")