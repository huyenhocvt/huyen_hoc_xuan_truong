from flask import Blueprint, render_template

do_nha_bp = Blueprint("do_nha_bp", __name__)

@do_nha_bp.route("/do-nha")
def do_nha():
    return render_template("do_nha.html")
