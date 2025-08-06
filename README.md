# Brent Oil Price Analysis

This report establishes the analytical bedrock for a comprehensive Brent oil price modeling project. It meticulously defines a systematic data analysis workflow, detailing steps from data acquisition and pre-processing to model selection and validation. A critical component involves the compilation of a structured historical dataset of major geopolitical events, OPEC decisions, and global economic shocks, which are pivotal exogenous factors influencing oil markets. The report further addresses essential methodological considerations, including inherent assumptions and limitations of time series analysis, and critically distinguishes between statistical correlation and causal impact. This foundational work ensures a robust, methodologically sound framework for subsequent quantitative modeling and informed interpretation of Brent oil price dynamics.

---

## 🔧 Project Structure

```bash
Birhan-Energies-week10/
   .github/workflows/ci.yml,            
    data/raw/.gitkeep,                   
    data/processed/.gitkeep,              
    docs/README.md,                       
    models/.gitkeep,                      
    notebooks/1.0-eda.ipynb,             
    reports/final_report.md,         
    reports/visualizations/,           
    src/__init__.py,                      
    src/data_processing.py,              
    src/train.py,                         
    src/predict.py,                      
    src/api/main.py,                      
    src/api/pydantic_models.py,          
    tests/test_data_processing.py,        
    Dockerfile,                          
    docker-compose.yml            
```
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
