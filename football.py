import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("analysis_dataset.csv")

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

print("\nROWS AFTER CLEANING:", len(df))

# =====================================
# QUESTION 1
# WHICH POSITIONS COMMAND THE HIGHEST VALUES?
# =====================================

position_values = (
    df.groupby("sub_position")["market_value_in_eur"]
    .mean()
    .sort_values(ascending=False)
    / 1_000_000
)

plt.figure(figsize=(12, 6))

position_values.plot(kind="bar")

plt.title("Average Market Value by Position")
plt.xlabel("Position")
plt.ylabel("Average Market Value (€ Millions)")

plt.tight_layout()

plt.savefig("position_values.png")

plt.show()

# =====================================
# QUESTION 2
# WHICH LEAGUES HAVE THE HIGHEST VALUES?
# =====================================

league_values = (
    df.groupby("current_club_domestic_competition_id")
    ["market_value_in_eur"]
    .mean()
    .sort_values(ascending=False)
    / 1_000_000
)

plt.figure(figsize=(10, 6))

league_values.plot(kind="bar")

plt.title("Average Market Value by League")
plt.xlabel("League")
plt.ylabel("Average Market Value (€ Millions)")

plt.tight_layout()

plt.savefig("league_values.png")

plt.show()

# =====================================
# QUESTION 3
# HOW DOES AGE AFFECT VALUE?
# =====================================

age_values = (
    df[df["age"] <= 40]
    .groupby("age")["market_value_in_eur"]
    .mean()
    / 1_000_000
)

plt.figure(figsize=(10, 6))

plt.plot(
    age_values.index,
    age_values.values,
    marker="o"
)

plt.title("Average Market Value by Age")
plt.xlabel("Age")
plt.ylabel("Average Market Value (€ Millions)")

plt.tight_layout()

plt.savefig("age_values.png")

plt.show()

# =====================================
# QUESTION 4
# WHICH YOUNG PLAYERS APPEAR UNDERVALUED?
# =====================================

X = df[
    [
        "age",
        "goals",
        "assists",
        "minutes"
    ]
]

y = df["market_value_in_eur"]

model = LinearRegression()

model.fit(X, y)

r2_score = model.score(X, y)

print("\nMODEL R² SCORE:", round(r2_score, 3))

# Generate predictions

df["predicted_value"] = model.predict(X)

df["difference"] = (
    df["predicted_value"]
    - df["market_value_in_eur"]
)

# =====================================
# FILTER YOUNG PLAYERS
# =====================================

young = df[df["age"] <= 23]

undervalued = young.sort_values(
    "difference",
    ascending=False
)

top20 = undervalued[
    [
        "name",
        "age",
        "goals",
        "assists",
        "minutes",
        "market_value_in_eur",
        "predicted_value",
        "difference"
    ]
].head(20)

print("\nTOP 20 MODEL-IDENTIFIED POTENTIALLY UNDERVALUED YOUNG PLAYERS\n")

print(top20)

# =====================================
# VISUALISE UNDERVALUED PLAYERS
# =====================================

top10 = top20.head(10)

plt.figure(figsize=(12, 6))

plt.barh(
    top10["name"],
    top10["difference"] / 1_000_000
)

plt.title(
    "Top 10 Potentially Undervalued Young Players"
)

plt.xlabel(
    "Predicted Value - Actual Value (€ Millions)"
)

plt.tight_layout()

plt.savefig(
    "undervalued_players.png"
)

plt.show()

# =====================================
# SAVE RESULTS
# =====================================

top20.to_csv(
    "top20_undervalued_players.csv",
    index=False
)

df.to_csv(
    "model_results.csv",
    index=False
)

# =====================================
# FINAL OUTPUT
# =====================================

print("\nFILES SAVED")

print("position_values.png")
print("league_values.png")
print("age_values.png")
print("undervalued_players.png")

print("top20_undervalued_players.csv")
print("model_results.csv")
