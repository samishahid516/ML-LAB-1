# AIC-301 Machine Learning Lab - Lab 01

Pakistan Average Temperature Analysis (1901–2016) using **Pandas** and **Matplotlib**.

## Dataset

[Pakistan Average Temperature 1901–2016 (Kaggle)](https://www.kaggle.com/datasets) — monthly temperature readings in Celsius.

## Lab Tasks

### Task 1 — Pandas Data Exploration

`lab_task1.py` loads the CSV, cleans column names, and prints:

- First 5 rows
- Missing values per column
- Summary statistics (mean, median, max, min)
- Summer (Jun–Aug) average temperature
- Records after 2000 with temperature > 25 °C

### Task 2 — Matplotlib Visualizations

`lab_task2.py` generates three plots:

![Yearly Trend](plot1_line_yearly_trend.png)

![Monthly Readings](plot2_scatter_monthly_readings.png)

![Monthly Average](plot3_bar_monthly_average.png)

## Requirements

```
pandas
matplotlib
```

## Usage

```bash
python lab_task1.py
python lab_task2.py
```
