from eda import EDA  # Assuming your EDA class is in another file
from advanced_modeling import AdvancedModeling

if __name__ == '__main__':
    import pandas as pd

    # Load from Google Drive
    file_path = '../data/raw/BrentOilPrices.csv'
    df = pd.read_csv(file_path)

    # Step 1: EDA
    eda = EDA(df, date_col='Date', price_col='Price')
    eda.plot_price()
    eda.plot_log_return()
    eda.check_stationarity()

    # Step 2: Modeling
    modeler = AdvancedModeling(df, date_col='Date', price_col='Price')
    modeler.fit_arima(order=(1, 1, 1))
    modeler.fit_garch()
    modeler.bayesian_change_point_detection()
    modeler.plot_garch_volatility()