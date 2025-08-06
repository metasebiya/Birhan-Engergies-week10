# Brent Oil Price Analysis

This project performs a comprehensive analysis of Brent crude oil prices using Bayesian Change Point Detection, Exploratory Data Analysis (EDA), and builds an interactive dashboard to visualize key trends.

---

## 🔧 Project Structure

brent-oil-analysis/
├── data/
│ └── BrentOilPrices.csv
├── notebooks/
│ └── brent_analysis.ipynb
├── src/
│ ├── init.py
│ ├── eda.py
│ └── bayesian_changepoint.py
├── dashboard/
│ ├── app.py
│ └── components/
├── README.md
├── requirements.txt
└── .env

markdown
Copy
Edit
---
## ✅ Features

### Task 1: Data Preparation
- Load data from Google Drive or local storage
- Clean missing values
- Parse dates and normalize formats

### Task 2: Time Series Analysis
- **Task 2.1**: Core EDA
  - Summary statistics
  - Price trend visualization
  - Log return computation
  - Stationarity checks (ADF test)
- **Task 2.2**: Bayesian Change Point Detection
  - PyMC3 implementation of change point models
  - Posterior inference
  - Regime segmentation

### Task 3: Interactive Dashboard
- Plotly + Dash or Flask + React frontend
- Visualize:
  - Change point regimes
  - Rolling mean/volatility
  - Log returns
- Export insights and key statistics

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/metasebiya/Birhan-Engergies-week10.git
cd Birhan-Engergies-week10
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### In Google Colab, mount your Drive and use:
```bash
from google.colab import drive
drive.mount('/content/drive')

# Example path usage
data_path = '/content/drive/MyDrive/BrentOil/data/BrentOilPrices.csv'
cd notebooks
jupyter notebook brent_analysis.ipynb

```
## 🚀 Launch the Dashboard
```bash
cd dashboard
python app.py
```
---

## 📁 Notes
 - Ensure PyMC3 dependencies are resolved for Bayesian modeling (MKL issue in Colab? Set MKL_THREADING_LAYER=GNU).
 - Use dotenv for managing credentials if needed.
 - Use **__init__.py** for packaging and class imports.
   
---

## 📊 Dashboard Enhancements (Optional)
 - Date range slider
 - Regime-specific summary stats
 - Forecasting toggle
 - Export charts as PNG/PDF
   
---

## 📜 License
MIT License
