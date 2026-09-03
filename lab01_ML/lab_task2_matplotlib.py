"""
AIC-301 Machine Learning Lab - Lab # 01
Lab Task 2: Matplotlib Visualizations
Dataset: Pakistan Average Temperature 1901-2016 (Kaggle)
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Tempreture_1901_2016_Pakistan.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "").str.replace("(", "").str.replace(")", "")
df.rename(columns={"temperature__celsius": "temperature"}, inplace=True)

yearly_avg = df.groupby("year")["temperature"].mean()
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthly_avg = df.groupby("month")["temperature"].mean().reindex(month_order)

def plot_line(data, title, xlabel, ylabel, saveas):
    plt.figure(figsize=(10, 5)); plt.plot(data.index, data.values, color="tab:red", linewidth=1.5, label="Yearly Avg Temp")
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend(loc="upper left"); plt.tight_layout()
    plt.savefig(saveas, dpi=150); print(f"Saved {saveas}"); plt.show()

def plot_scatter(x, y, title, xlabel, ylabel, saveas):
    plt.figure(figsize=(10, 5)); plt.scatter(x, y, color="tab:blue", s=8, alpha=0.5, label="Monthly reading")
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend(loc="upper left"); plt.tight_layout()
    plt.savefig(saveas, dpi=150); print(f"Saved {saveas}"); plt.show()

def plot_bar(data, title, xlabel, ylabel, saveas):
    plt.figure(figsize=(10, 5)); plt.bar(data.index, data.values, color="tab:green")
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.xticks(rotation=45, ha="right"); plt.tight_layout()
    plt.savefig(saveas, dpi=150); print(f"Saved {saveas}"); plt.show()

plot_line(yearly_avg, "Pakistan: Yearly Average Temperature (1901-2016)", "Year", "Temperature (Celsius)", "plot1_line_yearly_trend.png")
plot_scatter(df["year"], df["temperature"], "Pakistan: All Monthly Temperature Readings (1901-2016)", "Year", "Temperature (Celsius)", "plot2_scatter_monthly_readings.png")
plot_bar(monthly_avg, "Pakistan: Average Temperature by Month (1901-2016)", "Month", "Temperature (Celsius)", "plot3_bar_monthly_average.png")
