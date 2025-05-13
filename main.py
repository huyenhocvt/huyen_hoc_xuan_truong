
from flask import Flask, render_template_string
from roiter.lap_cong_viec import lap_cong_viec_bp

app = Flask(__name__)
app.secret_key = "lapcongviec_2025"

app.register_blueprint(lap_cong_viec_bp)

@app.route("/")
def index():
    return render_template_string(""" 
    <h2>CHỨC NĂNG</h2>
    <div class='roiter-group'>
        <h3>CÔNG VIỆC</h3>
        <a href="/lap-cong-viec/">Lập công việc</a>
    </div>
    """)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
