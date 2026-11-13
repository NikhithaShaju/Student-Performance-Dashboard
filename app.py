
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("dataset/analyzed_students.csv")


@app.route("/")
def home():

    total_students = len(data)
    average_marks = round(data["average"].mean(), 2)

    pass_count = (data["result"] == "Pass").sum()
    fail_count = (data["result"] == "Fail").sum()

    pass_percentage = round(
        (pass_count / total_students) * 100, 2
    )

    topper = data.loc[data["average"].idxmax()]

    students = data.to_dict(orient="records")

    subject_averages = {
        "Maths": round(data["maths"].mean(), 2),
        "Science": round(data["science"].mean(), 2),
        "English": round(data["english"].mean(), 2)
    }

    return render_template(
        "index.html",
        total_students=total_students,
        average_marks=average_marks,
        pass_count=pass_count,
        fail_count=fail_count,
        pass_percentage=pass_percentage,
        topper=topper,
        students=students,
        subject_averages=subject_averages
    )


if __name__ == "__main__":
    app.run(debug=True)

