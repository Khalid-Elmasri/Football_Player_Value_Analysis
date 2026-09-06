-- =====================================
-- Question 1
-- Which positions command the highest values?
-- =====================================

SELECT
    sub_position,
    ROUND(AVG(market_value_in_eur),0) AS avg_value
FROM players
WHERE market_value_in_eur IS NOT NULL
GROUP BY sub_position
ORDER BY avg_value DESC;


-- =====================================
-- Question 2
-- Which leagues have the highest values?
-- =====================================

SELECT
    current_club_domestic_competition_id,
    ROUND(AVG(market_value_in_eur),0) AS avg_value
FROM players
WHERE market_value_in_eur IS NOT NULL
GROUP BY current_club_domestic_competition_id
ORDER BY avg_value DESC;


-- =====================================
-- Question 3
-- How does age affect market value?
-- =====================================

SELECT
    CAST(
        (julianday('now') - julianday(date_of_birth))
        / 365.25 AS INTEGER
    ) AS age,
    ROUND(AVG(market_value_in_eur),0) AS avg_value
FROM players
WHERE market_value_in_eur IS NOT NULL
GROUP BY age
ORDER BY age;


-- =====================================
-- Final Analysis Dataset
-- =====================================

CREATE TABLE analysis_dataset AS
SELECT
    p.player_id,
    p.name,
    p.sub_position,
    p.current_club_domestic_competition_id,
    p.market_value_in_eur,
    CAST(
        (julianday('now') - julianday(p.date_of_birth))
        / 365.25 AS INTEGER
    ) AS age,
    SUM(a.goals) AS goals,
    SUM(a.assists) AS assists,
    SUM(a.minutes_played) AS minutes
FROM players p
JOIN appearances a
    ON p.player_id = a.player_id
JOIN games g
    ON a.game_id = g.game_id
WHERE g.season = 2025
GROUP BY p.player_id
HAVING minutes > 500;