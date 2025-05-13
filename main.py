
from flask import Flask, render_template, request, redirect, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

DATA_FILE = "data/ho_ten.xlsx"

@app.route("/", methods=["GET", "POST"])
def nhap_ho_ten():
    if request.method == "POST":
        ten = request.form.get("ten", "")
        que = request.form.get("que", "")

        new_row = {"ten": ten, "que": que}

        try:
            df = pd.read_excel(DATA_FILE)
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        except:
            df = pd.DataFrame([new_row])

        os.makedirs("data", exist_ok=True)
        df.to_excel(DATA_FILE, index=False)

        return redirect("/?success=1")

    success = request.args.get("success")
    return render_template("nhap_ho_ten.html", success=success)

@app.route("/tai-ho-ten")
def tai_file():
    return send_from_directory("data", "ho_ten.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run()
