
import pandas as pd

# Step 1: Read the student dataset
data = pd.read_csv("dataset/students.csv")

print("===== STUDENT PERFORMANCE DATA =====")
print(data)

# Step 2: Calculate total marks
data["total"] = (
    data["maths"] +
    data["science"] +
    data["english"]
)

# Step 3: Calculate average marks
data["average"] = data["total"] / 3

print("\n===== STUDENT MARKS WITH AVERAGE =====")
print(data)

# Step 4: Find the top-performing student
topper = data.loc[data["average"].idxmax()]

print("\n===== TOPPER DETAILS =====")
print(topper)

# Step 5: Calculate subject averages
print("\n===== SUBJECT AVERAGES =====")
print("Maths:", data["maths"].mean())
print("Science:", data["science"].mean())
print("English:", data["english"].mean())

# Step 6: Calculate overall pass percentage
passed = data[data["average"] >= 40]

pass_percentage = (len(passed) / len(data)) * 100

print("\n===== PASS PERCENTAGE =====")
print(pass_percentage, "%")

# Check pass or fail in every subject
data["result"] = data.apply(
    lambda row: "Pass" if
    row["maths"] >= 40 and
    row["science"] >= 40 and
    row["english"] >= 40
    else "Fail",
    axis=1
)

print("\n===== STUDENT RESULTS =====")
print(data[["name", "average", "result"]])

# Save analyzed data
data.to_csv("dataset/analyzed_students.csv", index=False)

print("\nAnalyzed data saved successfully!")


# Check whether each student passed or failed
data["result"] = data.apply(
    lambda row: "Pass" if
    row["maths"] >= 40 and
    row["science"] >= 40 and
    row["english"] >= 40
    else "Fail",
    axis=1
)

# Display student results
print("\n===== STUDENT RESULTS =====")
print(data[["name", "average", "result"]])

# Count passed and failed students
passed_count = (data["result"] == "Pass").sum()
failed_count = (data["result"] == "Fail").sum()

print("\nTotal Passed:", passed_count)
print("Total Failed:", failed_count)

# Save analyzed data
data.to_csv("dataset/analyzed_students.csv", index=False)

print("\nAnalyzed data saved successfully!")
