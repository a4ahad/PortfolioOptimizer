# 📊 Portfolio Optimizer with Risk Management
### Strategic Business Decision-Making Tool | AMOD-5610 Project

![Streamlit App Preview](trent_logo.png)  
*A modern Streamlit application for stock portfolio optimization and risk analysis*

---

## 🌟 Features
- **Multi-Asset Portfolio Optimization** - Analyze up to 10 stocks simultaneously
- **Risk Metrics** - VaR (Value at Risk) and CVaR calculations
- **Interactive Visualizations** - Efficient frontier, correlation heatmaps
- **Real-time Data** - Powered by Yahoo Finance API
- **Responsive Design** - Works on all devices

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-3F4F75?logo=plotly&logoColor=white)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation
```bash
# Clone repository
git clone https://github.com/a4ahad/PortfolioOptimizer.git
cd PortfolioOptimizer

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```


### Running the Application

```bash
streamlit run main.py
```

> 🌐 Open your browser to `http://localhost:8501`

---

## 📂 Project Structure

PortfolioOptimizer/
├── main.py                     # Streamlit application
├── styles.css                 # Custom styling
├── requirements.txt      # Dependencies

├── README.md            # Documentation
└── trent_logo.png         # Institutional logo

---

## 🧑‍💻 Development

### Customizing Styles

Edit `styles.css` to modify the application appearance:


```css
/* Example customization */
[data-testid="stSidebar"] {
    background-color: #154734;
}
```
### Dependencies

The `requirements.txt` includes:
```
streamlit>=1.0
yfinance>=0.2
pandas>=1.3
plotly>=5.0
scipy>=1.7
```

---

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
    
- [yFinance Documentation](https://aroussi.com/post/python-yahoo-finance)
    
- [Modern Portfolio Theory (Investopedia)](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
    

---

## 👥 Authors

<table> <tr> <td align="center"> <a href="https://github.com/a4ahad"> <img src="https://via.placeholder.com/100" width="100px;" alt="Md Abdul Ahad"/> <br /> <sub><b>Md Abdul Ahad</b></sub> </a> </td> <td align="center"> <a href="#"> <img src="https://via.placeholder.com/100" width="100px;" alt="Ekpereamaka Nwachukwu"/> <br /> <sub><b>Ekpereamaka Nwachukwu</b></sub> </a> </td> </tr> </table>
