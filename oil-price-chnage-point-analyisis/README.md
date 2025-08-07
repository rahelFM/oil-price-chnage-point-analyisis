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