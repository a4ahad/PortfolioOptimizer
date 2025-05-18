import streamlit as st
from datetime import datetime

# Function to create sidebar inputs
def sidebar_inputs():
    st.sidebar.title('Finance Tracker')
    # Input for stock symbols
    tickers = st.sidebar.text_input('Enter stock symbols (comma separated)', 'AMZN, MCD, MSFT, WMT, INTC')
    # Input for start date
    start_date = st.sidebar.date_input('Start Date', datetime(2024, 5, 1))
    # Input for end date
    end_date = st.sidebar.date_input('End Date', datetime(2024, 10, 31))
    # Slider for page size
    page_size = st.sidebar.slider('Page Size', min_value=1, max_value=10, value=5, step=1)
    # Slider for number of portfolios
    num_portfolios = st.sidebar.slider('Number of Portfolios', min_value=1000, max_value=10000, step=1000)
    return tickers, start_date, end_date, page_size, num_portfolios

# Function to display paginated data
def display_paginated_data(data, page_size):
    # Calculate the number of pages
    num_pages = len(data.columns) // page_size + 1
    # Input for selecting the page number
    page = st.sidebar.number_input('Page', min_value=1, max_value=num_pages, step=1)
    # Calculate the start and end columns for the current page
    start_col = (page - 1) * page_size
    end_col = min(page * page_size, len(data.columns))
    # Display the data for the current page
    st.write(data.iloc[:, start_col:end_col])
    return page