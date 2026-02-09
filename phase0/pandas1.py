import pandas as pd

data = {
    "Department": ["HR", "IT", "IT", "HR", "Finance"],
    "Salary": [30000, 50000, 40000, 35000, 40000]
}

df = pd.DataFrame(data)
# print(df)
# print(df.groupby("Department").mean())
# print(df.groupby("Department")["Salary"].sum())
# print(df.groupby("Department")["Salary"].agg(["min", "max", "mean"]))
# print(df.groupby(["Department", "Salary"]).count())
# print(df.groupby("Department")["Salary"].mean().reset_index())
# print(df.groupby("Department").count())
print(df.groupby("Department").agg(
    avg_salary=("Salary", "mean"),
    total_salary=("Salary", "sum")
))