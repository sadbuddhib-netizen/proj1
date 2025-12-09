# ---------------------------------------
# 📌 IMPORT LIBRARIES
# ---------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------
# 📌 LOAD THE CSV FILE
# ---------------------------------------
df = pd.read_csv("telecom_db_tables_converted.csv")

# ---------------------------------------
# 📌 SHOW DATA INFORMATION
# ---------------------------------------
print("\n----- DATA INFO -----")
print(df.info())

print("\n----- NUMERIC DESCRIPTION -----")
print(df.describe())

print("\n----- CATEGORICAL DESCRIPTION -----")
print(df.describe(include='object'))

# ---------------------------------------
# 📌 CHECK NULL VALUES
# ---------------------------------------
print("\n----- NULL VALUES IN EACH COLUMN -----")
print(df.isnull().sum())

# 📌 Visualize null values
plt.figure(figsize=(10,5))
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values Heatmap")
plt.show()

# ---------------------------------------
# 📌 DROP ROWS WITH NULL VALUES (OPTIONAL)
# ---------------------------------------
df_dropna = df.dropna()
print("\nShape after dropping null values:", df_dropna.shape)

# ---------------------------------------
# 📌 FILL NULL VALUES WITH MEAN
# ----------
