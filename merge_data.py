import pandas as pd
import glob
import os

path = "data/"  
files = glob.glob(os.path.join(path, "*.csv"))

all_dataframes = []

for file in files:
    city_name = os.path.basename(file).split("_")[0].lower()

    df = pd.read_csv(file)

    df["city"] = city_name
    date_cols = [col for col in df.columns if "date" in col.lower() or "review" in col.lower()]

    if len(date_cols) > 0:
        date_col = date_cols[0]  
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

        df["is_weekend"] = df[date_col].dt.weekday >= 5
    else:
        df["is_weekend"] = False

    all_dataframes.append(df)

merged_df = pd.concat(all_dataframes, ignore_index=True)

merged_df.to_csv("airbnb_merged.csv", index=False)

print("Gotovo! Spojene tablice spremljene u airbnb_merged.csv.")