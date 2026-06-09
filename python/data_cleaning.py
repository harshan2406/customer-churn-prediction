import pandas as pd

# Load dataset
df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Before Cleaning:")
print(df.shape)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df.fillna(0, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nAfter Cleaning:")
print(df.shape)

# Save cleaned dataset
df.to_csv(
    "../data/cleaned_churn.csv",
    index=False
)

print("\nCleaned file saved successfully!")