import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_churn.csv")

# Churn Distribution
df["Churn"].value_counts().plot(
    kind="bar"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")

plt.show()
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

contract_churn.plot(
    kind="bar",
    stacked=True
)

plt.title("Contract Type vs Churn")
plt.xlabel("Contract")
plt.ylabel("Customers")

plt.show()