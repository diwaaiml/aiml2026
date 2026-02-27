import pandas as pd

# -----------------------------
# Sample Data
# -----------------------------
data = {
    "Department": ["HR", "IT", "IT", "HR", "Finance","Doctor"],
    "Salary": [30000, 50000, 40000, 35000, 40000,None]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# -----------------------------
# 1. BASIC GROUPBY (mean)
# -----------------------------
print("\n1. Mean salary per department")
print(df.groupby("Department")["Salary"].mean())

# -----------------------------
# 2. SUM
# -----------------------------
print("\n2. Total salary per department")
print(df.groupby("Department")["Salary"].sum())

# -----------------------------
# 3. MULTIPLE AGGREGATIONS
# -----------------------------
print("\n3. Min, Max, Mean salary per department")
print(df.groupby("Department")["Salary"].agg(["min", "max", "mean"]))

# -----------------------------
# 4. NAMED AGGREGATIONS (BEST PRACTICE)
# -----------------------------
print("\n4. Named aggregations")
print(
    df.groupby("Department").agg(
        avg_salary=("Salary", "mean"),
        total_salary=("Salary", "sum")
    )
)

# -----------------------------
# 5. GROUPBY + RESET INDEX
# -----------------------------
print("\n5. Reset index after groupby")
print(df.groupby("Department")["Salary"].mean().reset_index())

# -----------------------------
# 6. GROUPBY MULTIPLE COLUMNS
# -----------------------------
print("\n6. Group by Department and Salary")
print(df.groupby(["Department", "Salary"]).count())

# -----------------------------
# 7. COUNT vs SIZE
# -----------------------------
print("\n7a. Count (non-null values)")
print(df.groupby("Department").count())

print("\n7b. Size (row count)")
print(df.groupby("Department").size())

# -----------------------------
# 8. TRANSFORM (same size output)
# -----------------------------
print("\n8. Add average salary per department to each row")
df["avg_salary"] = df.groupby("Department")["Salary"].transform("mean")
print(df)

# -----------------------------
# 9. FILTER (keep groups)
# -----------------------------
print("\n9. Departments with avg salary > 35000")
print(df.groupby("Department").filter(lambda x: x["Salary"].mean() > 35000))

# -----------------------------
# 10. APPLY (custom logic)
# -----------------------------
print("\n10. Highest salary in each department")
print(
    df.groupby("Department").apply(lambda x: x.nlargest(1, "Salary"))
)
