import pandas as pd

df = pd.DataFrame({
    "team": ["A", "A", "B", "B", "B"],
    "player": ["p1", "p2", "p3", "p4", "p5"],
    "points": [10, 15, 7, 12, 9]
})
print(df.groupby("player")["points"].mean())