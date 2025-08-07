<<<<<<< HEAD
# 🛢️ Change Point Detection of Brent Oil Prices using Bayesian Models
## 🔍 Project Overview

This project investigates how major global events influence the dynamics of Brent crude oil prices over the last 20+ years using statistical and Bayesian time series modeling. Specifically, we use **Bayesian Change Point Detection** to identify structural shifts in the oil price time series and associate them with real-world events such as wars, economic crises, and policy decisions.

---

## 🧠 Objectives

- Load and analyze daily Brent oil prices from 2000 to 2024.
- Identify change points using **Bayesian inference** and **PyMC3**.
- Link detected change points to geopolitical or macroeconomic events.
- Visualize and interpret model results for actionable insight.

---

## 📁 Project Structure

.
├── data/
│ └── brent-daily.csv # Raw Brent oil price time series
├── notebooks/
│ └── exploratory_analysis.ipynb # EDA and trend exploration
├── results/
│ ├── change_point_plot.png # Final change point visualization
│ ├── posterior_summary.png # Posterior trace plots from MCMC
│ └── final_model_trace.nc # Saved PyMC3 trace
├── src/
│ ├── change_point_model.py # PyMC3 model definition and execution
│ └── utils.py # Helper functions (e.g., plotting)
├── final_report.pdf # Final analysis report
├── dashboard/ # (Optional) Flask/React dashboard
├── README.md # 📄 You are here
└── requirements.txt # Project dependencies

yaml
Copy
Edit

---

## ⚙️ How to Run the Code

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/brent-oil-change-point.git
cd brent-oil-change-point
2. Create and activate environment
bash
Copy
Edit
conda create -n oil-env python=3.9
conda activate oil-env
pip install -r requirements.txt
3. Run the model
bash
Copy
Edit
python src/change_point_model.py
4. View outputs
Results (plots, trace, etc.) will be saved in the results/ directory.

📊 Key Results
Bayesian change point model detected significant structural breaks in the oil price time series.

These shifts aligned with major global events, such as:

2008 Global Financial Crisis

2014 Oil Price Collapse

2020 COVID-19 pandemic

2022 Russia–Ukraine conflict

Model uncertainty and parameter traces visualized with arviz.

📦 Dependencies
pymc3

arviz

pandas, matplotlib, seaborn

numpy, scipy

See requirements.txt for full list.

📈 Dashboard (Optional)
An interactive dashboard is available in the dashboard/ folder. It can be run with:

bash
Copy
Edit
cd dashboard
python app.py
🧠 Author
Rahel Sileshi Abdisa – Data Scientist @ Birhan Energies
Project by: 10Academy

📄 License
This project is open source under the MIT License.
=======
# Brent Oil Price Change Point Analysis

## Overview
This project analyzes historical Brent crude oil prices to identify significant structural changes in price behavior linked to major geopolitical and economic events. Using Bayesian Change Point Detection with PyMC3, the analysis detects points where the statistical properties of oil prices shift, helping investors, policymakers, and analysts understand how events affect the oil market.
## Project Objectives
- Perform exploratory data analysis on Brent oil price data (daily prices from 1987 to 2022).
- Detect change points in oil price trends using Bayesian modeling.
- Associate detected change points with major events such as wars, economic crises, and policy decisions.
- Quantify the impact of these events on oil prices.
- Present findings in clear visualizations and an interactive dashboard.

## Dataset
- **Source:** Historical Brent oil prices from May 20, 1987, to September 30, 2022.
- **Format:** CSV file with columns:
  - `Date`: Date of price record (format varies, handled in preprocessing).
  - `Price`: Price of Brent crude oil per barrel (USD).

## Setup and Installation

1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/oil-price-change-point-analysis.git
   cd oil-price-change-point-analysis
Create and activate a Python virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install required dependencies:
pip install -r requirements.txt

Exploratory Data Analysis:
Run notebooks in notebooks/ folder to visualize trends and prepare data.

Project Structure
oil-price-change-point-analysis/
│
├── data/                # Raw and processed datasets (ignored by git)
├── notebooks/           # Jupyter notebooks for EDA and modeling
├── src/                 # Python scripts for modeling and utilities
├── requirements.txt     # Project dependencies
├── README.md            # This file
└── .gitignore           # Git ignore rules (includes /data)

## Future Work
Extend the model to include volatility changes and multiple change points.

Incorporate additional external factors such as OPEC production data, sanctions, and macroeconomic indicators.

Enhance dashboard functionality with real-time data updates and more interactive visualizations.

## References
PyMC3 Documentation

Bayesian Change Point Detection Tutorial

Brent Oil Historical Data Source
>>>>>>> 58e94655723cc97c7272ab5b027ac20d884d1b94
