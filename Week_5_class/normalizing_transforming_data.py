import pandas as pd
from sklearn.preprocessing import StandardScaler
""" Handling outliers """

data = pd.read_csv(
    "/home/jude/scientific_computing/Week_5_class/sample_data.csv")

# Standardizing data - reduce the range so that the data fits within eg -1 , 0 and 1 - to prevent any piece of data from dominating e.g larger values dominating small values
scaler = StandardScaler()

# Makes the data fit within the range
df_scale = scaler.fit_transform(data[["temperature", "humidity"]])

print(df_scale)
