from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/buttons")
def buttons():
    return render_template("buttons.html")


@app.route("/layout/grid")
def layout_grid():
    return render_template("layout/grid.html")


@app.route("/layout/columns")
def layout_columns():
    return render_template("layout/columns.html")


@app.route("/layout/grid")
def show_grid():
    return render_template("layout/grid.html")


@app.route("/layout/fixed")
def layout_fixed():
    return render_template("layout/fixed.html")


@app.route("/layout/container")
def layout_container():
    return render_template("layout/container.html")


@app.route("/navigation")
def navigation():
    return render_template("navigation.html")


@app.route("/form-ui")
def form_ui():
    return render_template("form_ui.html")


@app.route("/table-list")
def table_list():
    return render_template("table_list.html")


@app.route("/info-card-ui")
def info_card_ui():
    return render_template("info_card_ui.html")


@app.route("/modal-ui")
def modal_ui():
    return render_template("modal_ui.html")


@app.route("/message_alert")
def message_alert():
    return render_template("message_alert.html")


@app.route("/special_ui")
def special_ui():
    return render_template("special_ui.html")


@app.route("/layout-ui")
def layout_ui():
    return render_template("layout_ui.html")


if __name__ == "__main__":
    app.run(debug=True)
