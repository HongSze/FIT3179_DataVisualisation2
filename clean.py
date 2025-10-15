import pandas as pd
df = pd.read_csv("country_year_avg_aqi.csv")  # columns: Country, Year, Avg_AQI
wide = df.pivot(index="Country", columns="Year", values="Avg_AQI").reset_index()
# Rename year columns to YYYYY so we can address them easily in Vega-Lite
wide.columns = ["Country"] + [f"Y{int(c)}" for c in wide.columns[1:]]
wide.to_csv("global_air_pollution_years_cleaned.csv", index=False)
