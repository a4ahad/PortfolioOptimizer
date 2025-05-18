# Portfolio Optimization with Risk Management to Support
Strategic Business Decision-Making


This is a project work for the AMOD-5610, it is a Streamlit application for optimizing stock portfolios. After unzipping the files, please follow the steps below to set up and run the project on Windows, Mac, and Linux.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository or download the project files.

2. Open a terminal (Command Prompt on Windows, Terminal on Mac and Linux).

3. Navigate to the project directory.

4. Create a virtual environment (optional but recommended):
   ```
   python -m venv env
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     .\env\Scripts\activate
     ```
   - On Mac and Linux:
     ```
     source env/bin/activate
     ```

6. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should include the following packages:
   ```
   streamlit
   yfinance
   pandas
   numpy
   plotly
   scipy
   ```

   If you don't have a `requirements.txt` file, you can create one with the above content or install the packages individually:
   ```
   pip install streamlit yfinance pandas numpy plotly scipy
   ```

## Running the Application

1. Ensure you are in the project directory.

2. Run the Streamlit application:
   ```
   streamlit run main.py
   ```

3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Custom CSS

To customize the appearance of the application, you can modify the `styles.css` file.

## References

- Streamlit Documentation
- yfinance Documentation
- Plotly Documentation
- Pandas Documentation
- NumPy Documentation
- SciPy Documentation

## Authors

- Md Abdul Ahad
- Ekpereamaka Nwachukwu