import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
import arviz as az
from arch import arch_model
from statsmodels.tsa.arima.model import ARIMA

class AdvancedModeling:
    def __init__(self, df, date_col='Date', price_col='Price'):
        self.df = df.copy()
        self.df[date_col] = pd.to_datetime(self.df[date_col])
        self.df.set_index(date_col, inplace=True)
        self.price_col = price_col
        self.df['log_return'] = np.log(self.df[price_col]).diff().dropna()
        self.model_results = {}

    def fit_arima(self, order=(1,1,1)):
        print(f"Fitting ARIMA{order} model...")
        model = ARIMA(self.df[self.price_col], order=order)
        fitted = model.fit()
        self.model_results['arima'] = fitted
        print(fitted.summary())
        return fitted

    def fit_garch(self, p=1, q=1):
        print(f"Fitting GARCH({p},{q}) model on log returns...")
        returns = self.df['log_return'].dropna() * 100  # scale to percentage
        am = arch_model(returns, vol='GARCH', p=p, q=q)
        res = am.fit(update_freq=5, disp='off')
        self.model_results['garch'] = res
        print(res.summary())
        return res

    def bayesian_change_point_detection(self, col='log_return', sample_size=500):
        print("Running Bayesian Change Point Detection with PyMC3...")
        y = self.df[col].dropna().values[-sample_size:]  # Limit to sample size for speed

        with pm.Model() as model:
            τ = pm.DiscreteUniform('τ', lower=0, upper=len(y) - 1)
            mu1 = pm.Normal('mu1', mu=0, sigma=1)
            mu2 = pm.Normal('mu2', mu=0, sigma=1)
            sigma = pm.HalfNormal('sigma', sigma=1)

            mu = pm.math.switch(τ >= np.arange(len(y)), mu1, mu2)
            obs = pm.Normal('obs', mu=mu, sigma=sigma, observed=y)

            trace = pm.sample(2000, tune=1000, cores=2, return_inferencedata=True, progressbar=True)

        az.plot_trace(trace, var_names=["τ", "mu1", "mu2"])
        plt.tight_layout()
        plt.show()

        change_point = int(trace.posterior['τ'].mean().values)
        print(f"Estimated Change Point Index: {change_point}")
        self.model_results['change_point'] = change_point
        return change_point

    def plot_garch_volatility(self):
        if 'garch' in self.model_results:
            res = self.model_results['garch']
            res.plot(annualize='D')
        else:
            print("Please run fit_garch() first.")
