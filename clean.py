import pandas as pd

# === set your CSV path or URL here ===
CSV_PATH = "Dataset/global_air_pollution_cleaned.csv"   # e.g. "./global_air_pollution_cleaned.csv" or a https:// URL
TARGET   = "Malaysia"

# --- load & clean ---
df = pd.read_csv(CSV_PATH)
# standardize column names just in case
df.columns = [c.strip() for c in df.columns]
val_col = "Mean Overall AQI"
name_col = "Country"

# coerce to numeric and drop rows without values
df[val_col] = pd.to_numeric(df[val_col], errors="coerce")
df = df.dropna(subset=[val_col])

# normalize country names for matching
df["_key"] = df[name_col].str.strip().str.casefold()
target_key = TARGET.strip().casefold()

if target_key not in set(df["_key"]):
    raise SystemExit(f"'{TARGET}' was not found in the CSV’s '{name_col}' column.")

# sort DESC so rank 1 is the worst (highest AQI)
df_sorted = df.sort_values(val_col, ascending=False, kind="mergesort").reset_index(drop=True)

# --- compute ranks ---
# simple order (1..N, no tie handling beyond order)
df_sorted["rank_simple"] = range(1, len(df_sorted) + 1)

# competition ranking (1,1,3 style for ties)
# rank(method="min") gives the first position for a tie group
df_sorted["rank_competition"] = df_sorted[val_col].rank(method="min", ascending=False).astype(int)

# pick Malaysia row
row = df_sorted.loc[df_sorted["_key"] == target_key].iloc[0]
country = row[name_col]
value = row[val_col]
r_simple = int(row["rank_simple"])
r_comp = int(row["rank_competition"])
total = len(df_sorted)

print(f"{country}: Mean Overall AQI = {value:.2f}")
print(f"Rank (simple order):      {r_simple} of {total}  (1 = highest AQI)")
print(f"Rank (competition, ties): {r_comp} of {total}  (1 = highest AQI)")
