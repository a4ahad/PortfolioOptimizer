import numpy as np
import pandas as pd

# Function to calculate portfolio statistics
def calculate_portfolio_statistics(data):
    # Calculating daily returns and drop missing values
    returns = data.pct_change().dropna()
    # Calculating mean returns
    mean_returns = returns.mean()
    # Calculating covariance matrix
    cov_matrix = returns.cov()
    return mean_returns, cov_matrix

# Function to calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR)
def calculate_var_cvar(returns, confidence_level=0.95):
    # Calculate VaR at the given confidence level
    var = np.percentile(returns, (1 - confidence_level) * 100)
    # Calculate CVaR as the mean of returns below VaR
    cvar = returns[returns <= var].mean()
    return var, cvar

# Function to optimize the portfolio
def optimize_portfolio(mean_returns, cov_matrix, num_portfolios=10000):
    # Initialize an array to store the results
    results = np.zeros((5, num_portfolios))
    for i in range(num_portfolios):
        # Generate random weights for the portfolio
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        # Calculate portfolio return
        portfolio_return = np.sum(weights * mean_returns)
        # Calculate portfolio volatility
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        # Calculate portfolio returns
        portfolio_returns = np.dot(weights, mean_returns)
        # Calculate VaR and CVaR
        var, cvar = calculate_var_cvar(portfolio_returns)
        # Store the results
        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = results[0, i] / results[1, i]
        results[3, i] = var
        results[4, i] = cvar
    # Create a DataFrame from the results
    results_df = pd.DataFrame(results.T, columns=['Returns', 'Volatility', 'Sharpe Ratio', 'VaR', 'CVaR'])
    return results_df