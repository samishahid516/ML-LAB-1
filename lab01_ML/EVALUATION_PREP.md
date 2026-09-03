# Lab # 01 — Evaluation Prep Notes
**Course:** AIC-301 Machine Learning | **Topic:** Pandas & Matplotlib (CLO1)

---

## 1. Core Concepts You Must Be Able to Explain

### Pandas
| Term | Meaning |
|---|---|
| **Series** | A single labeled column of data (one dimension). Think of it as one column of an Excel sheet with an index. |
| **DataFrame** | A 2D table made of multiple Series sharing the same index — rows and columns, like a full spreadsheet. |
| **Index** | The row labels of a Series/DataFrame. Defaults to 0, 1, 2, ... unless set explicitly. |
| **`df.head()`** | Shows the first 5 rows (or `n` rows if you pass a number) — a quick look at the data. |
| **`df.shape`** | Returns `(rows, columns)` as a tuple — no parentheses needed, it's an attribute not a method. |
| **`df.isnull().sum()`** | Counts missing/null values per column. `isnull()` alone returns a True/False DataFrame. |
| **`df.describe()`** | Gives count, mean, std, min, 25%/50%/75% quartiles, and max for numeric columns. |
| **`df.columns`** | Lists column names — useful for renaming or diagnosing `KeyError`s. |
| **`inplace=True`** | Modifies the DataFrame directly instead of returning a new copy. |
| **`drop_duplicates()`** | Removes duplicate rows. `keep='first'` (default), `'last'`, or `False` (drop all duplicates). |
| **Filtering / Boolean indexing** | `df[df['col'] > x]` — selects rows where a condition is True. Multiple conditions combine with `&` (and) / `|` (or), each wrapped in parentheses. |
| **`df.groupby()`** | Splits data into groups (e.g. by year or month) so you can aggregate (mean, sum, etc.) within each group. |

### Matplotlib
| Term | Meaning |
|---|---|
| **Figure** | The whole canvas/window that can hold one or more plots. |
| **Axes** | An individual plot inside a Figure (has its own x-axis, y-axis, title). Not to be confused with "Axis". |
| **Axis** | The actual number-line objects (x-axis, y-axis) that define scale/limits. |
| **Artist** | Anything drawn and visible on the figure (lines, text, bars, points). |
| **`plt.plot()`** | Draws a line graph connecting points — good for trends over a continuous variable like time. |
| **`plt.scatter()`** | Draws individual points without connecting lines — good for showing spread/distribution of raw data. |
| **`plt.bar()`** | Draws vertical bars — good for comparing distinct categories (e.g. months). |
| **`plt.title() / xlabel() / ylabel()`** | Add descriptive text to a single plot. |
| **`plt.legend()`** | Displays a key describing what each line/series represents (needs a `label=` in the plot call). |
| **`plt.subplots(nrows, ncols)`** | Creates a Figure and an array of Axes in one call — the modern, convenient way to build multi-plot figures. |
| **`plt.savefig()`** | Saves the current figure to a file (must be called **before** `plt.show()`, since `show()` can clear the figure). |

---

## 2. What Each Lab Task Actually Does

### Lab Task 1 (`lab_task1_pandas.py`)
1. Loads `Tempreture_1901_2016_Pakistan.csv` into a DataFrame.
2. Cleans column names (lowercase, no spaces/symbols) — mirrors the "column cleanup" section of the manual.
3. Displays `head()`, checks nulls with `isnull().sum()`, and computes summary stats with `describe()`.
4. Filters two subsets:
   - Summer months (June–August) → average ≈ **28.5°C**
   - Records after year 2000 with temperature > 25°C → **78 rows**

### Lab Task 2 (`lab_task2_matplotlib.py`)
Produces **3 separate PNG files**:
1. **`plot1_line_yearly_trend.png`** — Line plot of yearly average temperature (1901–2016). Shows a clear warming trend, sharper after ~2000.
2. **`plot2_scatter_monthly_readings.png`** — Scatter plot of every individual monthly reading vs. year. Shows the seasonal spread (cold months near the bottom, hot months near the top) staying wide but drifting slightly upward over time.
3. **`plot3_bar_monthly_average.png`** — Bar chart of average temperature per calendar month. Shows Pakistan's seasonal cycle: coldest in January, hottest in June/July.

---

## 3. Key Dataset Facts (memorize for viva)
- **Rows:** 1,392 (116 years × 12 months, 1901–2016)
- **Columns:** `temperature` (°C), `year`, `month`
- **No missing values**
- **Overall mean temp:** ~20.01°C | **Median:** ~21.17°C
- **Min:** ~5.91°C (a January) | **Max:** ~30.31°C (a summer month)
- **Hottest months on average:** June/July (~29°C) | **Coldest:** January (~8.5°C)

---

## 4. Likely Viva / Evaluation Questions

1. **Q: What's the difference between a Series and a DataFrame?**
   A: A Series is one labeled column; a DataFrame is a table made of multiple Series sharing an index.

2. **Q: Why do we clean column names before analysis?**
   A: Raw column names often have spaces, symbols, or inconsistent casing, which causes `KeyError`s and makes code harder to read/type.

3. **Q: How do you check for missing values, and what are your two main options for handling them?**
   A: `df.isnull().sum()`. Options: (1) drop rows/columns with nulls, or (2) impute — replace with a non-null value (e.g. mean/median).

4. **Q: What's the difference between `plt.plot()` and `plt.scatter()`?**
   A: `plot()` connects points with a line (good for continuous trends); `scatter()` shows unconnected individual points (good for spread/distribution/correlation).

5. **Q: What does `inplace=True` do?**
   A: Modifies the original DataFrame directly instead of returning a new copy that must be reassigned.

6. **Q: How would you filter rows where temperature > 25 AND year > 2000?**
   A: `df[(df['temperature'] > 25) & (df['year'] > 2000)]` — note the parentheses around each condition are required.

7. **Q: What does `groupby()` do, and why did we use it here?**
   A: It splits the DataFrame into groups by a column's values (e.g. year or month) so you can aggregate within each group — used here to compute yearly and monthly averages before plotting.

8. **Q: What trend does the yearly line plot reveal?**
   A: A gradual warming trend across the century, with a noticeably steeper rise after roughly 2000 — consistent with global warming patterns.

9. **Q: Why use `figsize` and `dpi` in `savefig()`?**
   A: `figsize` controls the plot's physical dimensions (in inches); `dpi` controls resolution/sharpness of the saved image.

10. **Q: What's the difference between `.shape` and `.describe()`?**
    A: `.shape` is an attribute giving `(rows, columns)` only; `.describe()` is a method giving statistical summaries (mean, std, quartiles, etc.) of numeric columns.

---

## 5. Quick Revision Checklist
- [ ] Can explain Series vs DataFrame vs Index
- [ ] Can write a boolean filter with multiple conditions
- [ ] Know the difference between Figure, Axes, and Axis
- [ ] Can explain why `plot()`, `scatter()`, and `bar()` are each used for different data shapes
- [ ] Know the dataset's mean/median/min/max off the top of your head
- [ ] Can explain what `groupby()` + `.mean()` does in one sentence
