import pandas as pd

df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Rows and Columns:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())