# ⚽ What Factors Drive Football Player Market Value?

![Python](https://img.shields.io/badge11-blue)
![SQLite](https://img.shieldsSQLite-Database-green)
![Pandas](https://img.shields.io/badge/Pandas-Datas-orange)
![Scs://img.shields.io/badge/Scikit--Learn-Regression-red]
![Statusimg.shields.io/badge/Status-Completed-brightgreen]

A data analysis project using **SQL, Python, and machine learning** to investigate how **age, position, league, and on-field performance** influence professional football player market values.

---

## 🎯 Research Question

> **What factors best predict a football player's market value?**

Using data from over **5,000 professional football players** from the **2025 season**, this project combines SQL-based data extraction, Python visualisation, and regression modelling to identify the key drivers of player valuation.

---

## 🔍 Key Findings

✅ **Wingers commanded the highest average market values**, outperforming all other positions.

✅ **Premier League players had the highest average valuations**, significantly exceeding most other major leagues.

✅ **Player value peaked during the early-to-mid twenties**, before declining steadily with age.

✅ A regression model using **age, goals, assists, and minutes played** explained approximately **36% of variation in market value** (**R² = 0.363**).

✅ Several young players were identified as **potentially undervalued**, with the model estimating substantially higher values than their observed market values.

---

## 🛠 Technologies Used

- SQL (SQLite)
- Python
- Pandas
- Matplotlib
- Scikit-Learn

---

## 📊 Dataset

This project uses football player, appearance, game, and competition data from the Transfermarkt database.

The final analysis dataset was created using SQL joins across multiple tables:

- Players
- Appearances
- Games
- Competitions

After data cleaning and filtering, the final dataset contained:

- **5,257 players**
- **2025 season data**
- Player position
- League
- Market value
- Age
- Goals
- Assists
- Minutes played

---

## 🗄 SQL Workflow

The project began by importing multiple football datasets into SQLite.

Key SQL techniques used:

- `JOIN`
- `GROUP BY`
- `ORDER BY`
- `AVG()`
- `SUM()`
- `WHERE`
- `HAVING`

SQL was used to answer three analytical questions:

### Which positions command the highest market values?

Wingers and attacking midfielders had the highest average market values, while goalkeepers had the lowest.

### Which leagues contain the most valuable players?

The Premier League had the highest average player valuation, significantly exceeding most other major leagues.

### How does age influence market value?

Market values were highest among players in their early-to-mid twenties before declining with age.

The full SQL queries used in this project can be found in:

```text
queries.sql
```

---

## 🐍 Python Workflow

Python was used to:

- Clean exported SQL data
- Create visualisations
- Perform regression analysis
- Identify potentially undervalued players

Libraries used:

```python
pandas
matplotlib
scikit-learn
```

---

## 📈 Visualisations

### Average Market Value by Position

position_values.png

This visual shows that attacking positions command the highest average market values, particularly right wingers, left wingers, and attacking midfielders.

---

### Average Market Value by League

league_values.png

The Premier League contains the highest average player market values, highlighting its financial strength relative to other leagues.

---

### Average Market Value by Age

age_values.png

Player value tends to peak during the early-to-mid twenties before declining with age.

---

### Top 10 Potentially Undervalued Young Players

undervalued_players.png

This visual highlights players whose model-predicted value exceeded their actual market value by the largest margin.

---

## 🤖 Machine Learning Model

A Linear Regression model was trained to predict player market value using:

- Age
- Goals
- Assists
- Minutes Played

### Features

```python
age
goals
assists
minutes
```

### Target

```python
market_value_in_eur
```

### Model Performance

**R² Score: 0.363**

This suggests that age and basic performance metrics explain approximately **36.3%** of variation in market value.

The remaining variation is likely explained by factors not included in the dataset, such as:

- Contract length
- Injury history
- International reputation
- Commercial value
- Club finances
- Future potential

---

## 🎯 Research Conclusions

The analysis suggests that player market value is influenced by several factors.

### Position

Attacking players command higher values than defensive players.

### League

The Premier League has the highest average player valuations.

### Age

Players reach peak value during their early-to-mid twenties.

### Performance

Goals, assists and minutes played contribute to player value, but explain only part of the valuation process.

### Undervalued Talent

Several young players were identified whose performance levels suggest they may be priced below the values predicted by the model.

---

## 🚀 Future Improvements

Potential future developments include:

- Random Forest regression
- XGBoost models
- Expected Goals (xG) metrics
- Player transfer fee analysis
- Power BI dashboard
- Tableau dashboard
- Interactive web application
