import pandas as pd
import numpy as np

df = pd.read_csv("C:\spring 2026\causal-learn/tests\TestData/559-ws-training_processed.csv")

df = df[["cbg", "hr"]]

window_size = 12 * 12   # 144 rows
missing_scores = []

for start in range(len(df) - window_size):

    window = df.iloc[start:start+window_size]

    missing_fraction = window.isna().mean().mean()

    missing_scores.append(missing_fraction)

best_start = np.argmin(missing_scores)

print("Best start:", best_start)
print("Missing fraction:", missing_scores[best_start])

clean_df = df.iloc[best_start:best_start + window_size].copy()

print(clean_df.head())
print(clean_df.isna().sum())
print(clean_df.shape)

lags = [1, 2, 3, 6, 12]  # 5, 10, 15, 30, 60 minutes

for lag in lags:
    clean_df[f"cbg_lag{lag}"] = clean_df["cbg"].shift(lag)
    clean_df[f"hr_lag{lag}"] = clean_df["hr"].shift(lag)

clean_df = clean_df.dropna().copy()

print(clean_df.head())
print(clean_df.shape)
print(clean_df.columns)

clean_df.to_csv("ohio_cbg_hr_lagged.csv", index=False)
X = clean_df.to_numpy()
labels = clean_df.columns.tolist()