from flask import Blueprint, render_template, request
import pandas as pd

do_nha_bp = Blueprint("do_nha_bp", __name__)
df = pd.read_excel("data/72_nha.xlsx")

@do_nha_bp.route("/do-nha", methods=["GET", "POST"])
def do_nha():
    ket_qua = None
    huong_list = sorted(df["do_so_huong"].dropna().unique().tolist())
    van_list = sorted(df["van"].dropna().unique().tolist())

    if request.method == "POST":
        huong = request.form.get("huong")
        van = request.form.get("van")
        row = df[(df["do_so_huong"] == huong) & (df["van"] == int(van))]
        if not row.empty:
            ket_qua = row.iloc[0].to_dict()

    return render_template("do_nha.html", ket_qua=ket_qua,
                           huong_list=huong_list, van_list=van_list)
