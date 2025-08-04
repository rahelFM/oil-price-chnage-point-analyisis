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
