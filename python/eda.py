import pandas as pd

df = pd.read_csv("../data/cleaned_churn.csv")

# Total Customers
total_customers = len(df)

# Churn Count
churn_count = df["Churn"].value_counts()

# Churn Rate
churn_rate = (
    len(df[df["Churn"] == "Yes"])
    / len(df)
) * 100

print("Total Customers:", total_customers)

print("\nChurn Count:")
print(churn_count)

print("\nChurn Rate:")
print(round(churn_rate, 2), "%")
print("\nContract Type vs Churn")

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

print(contract_churn)