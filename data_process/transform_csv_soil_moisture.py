import pandas as pd

df = pd.read_csv('../df/SMAP_L3_SM_P_E_20251003_R19240_001.csv')

# Check for nulls
print(df.isnull().sum())

# Remove rows with NaN values and generate a new clean CSV
df = df.dropna()

# Keep only a sample (10% of the original dataset) to simplify mean calculation
df = df.sample(frac=0.1, random_state=1)

df.to_csv('../df/SMAP_L3_SM_P_E_20251003_R19240_001_cleaned.csv', index=False)

# Analyze cleaned CSV
df = pd.read_csv('../df/SMAP_L3_SM_P_E_20251003_R19240_001_cleaned.csv')
print(df.describe())

# Return data from Sergipe
LAT_MIN = -11.5
LAT_MAX = -9.5
LON_MIN = -38.5
LON_MAX = -36.0

sergipe_mask = (
    (df["Latitude"] >= LAT_MIN) &
    (df["Latitude"] <= LAT_MAX) &
    (df["Longitude"] >= LON_MIN) &
    (df["Longitude"] <= LON_MAX)
)

df_sergipe = df[sergipe_mask]

print(df_sergipe.describe())

# Return the average soil moisture in Sergipe
print(f"{(df_sergipe['Soil_Moisture'].mean() * 100):.2f}")