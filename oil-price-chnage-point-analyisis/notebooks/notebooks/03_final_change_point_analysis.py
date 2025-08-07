import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt

def main():
    # Load data
    df = pd.read_csv("D:\\KAIM5\\week 10\\oil-price-chnage-point-analyisis\\data\\BrentOilPrices.csv", parse_dates=["Date"])
    df = df.dropna()
    df = df.sort_values("Date")
    prices = df["Price"].values
    dates = df["Date"].values

    # Normalize prices
    log_prices = np.log(prices)
    returns = np.diff(log_prices)

    # Model
    with pm.Model() as model:
        # Prior for change point
        tau = pm.DiscreteUniform("tau", lower=0, upper=len(returns) - 1)

        # Priors for pre- and post-change point means and stds
        mu1 = pm.Normal("mu1", mu=0, sigma=1)
        mu2 = pm.Normal("mu2", mu=0, sigma=1)
        sigma1 = pm.HalfNormal("sigma1", sigma=1)
        sigma2 = pm.HalfNormal("sigma2", sigma=1)

        # Define the likelihood with change point
        mu = pm.math.switch(tau >= np.arange(len(returns)), mu1, mu2)
        sigma = pm.math.switch(tau >= np.arange(len(returns)), sigma1, sigma2)

        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=returns)

        # Inference
        trace = pm.sample(2000, tune=1000, return_inferencedata=True, random_seed=42)

    # Save results
    az.to_netcdf(trace, "../../results/final_model_trace.nc")

    # Plot posterior
    az.plot_posterior(trace, var_names=["tau", "mu1", "mu2", "sigma1", "sigma2"])
    plt.tight_layout()
    plt.savefig("../../results/posterior_summary.png")
    plt.show()

    # Plot change point over time
    tau_mean = int(trace.posterior["tau"].mean().values)
    change_date = dates[tau_mean + 1]

    plt.figure(figsize=(12, 5))
    plt.plot(dates[1:], returns, label="Log Returns")
    plt.axvline(x=change_date, color="red", linestyle="--", label=f"Change Point: {change_date.date()}")
    plt.legend()
    plt.title("Change Point Detection on Brent Oil Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.grid()
    plt.savefig("../../results/change_point_plot.png")
    plt.show()

    print(f"Estimated Change Point Date: {change_date.date()}")

# This is the fix for Windows multiprocessing
if __name__ == "__main__":
    main()
