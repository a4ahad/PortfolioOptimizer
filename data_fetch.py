import streamlit as st
import yfinance as yf
import pandas as pd

# Cache the function to improve performance
@st.cache_data
def fetch_data(tickers, start_date, end_date):
    # Split the tickers string into a list and remove any extra spaces
    tickers_list = [ticker.strip() for ticker in tickers.split(',') if ticker.strip()]
    
    # Creates an empty DataFrame to store all the data
    all_data = pd.DataFrame()
    
    # Loop through each ticker and fetch its data
    for ticker in tickers_list:
        # Download the adjusted closing prices for the given date range
        data = yf.download(ticker, start=start_date, end=end_date)[['Adj Close']]
        
        # Rename the column to the ticker symbol
        data = data.rename(columns={'Adj Close': ticker})
        
        # Format the index (dates) to 'YYYY-MM-DD'
        data.index = data.index.strftime('%Y-%m-%d')
        
        # Concatenate the new data to the all_data DataFrame
        all_data = pd.concat([all_data, data], axis=1)
    
    # Return the combined data
    return all_data