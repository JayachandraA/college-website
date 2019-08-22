from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admissions")
def about():
    return "Admissions"


@app.route("/placements")
def placements():
    return "Placements"


@app.route("/contact-us")
def contact_us():
    return "Contact us"


@app.route("/about-us")
def about_us():
    return "About"



@app.route("/nav_script")
def nav_script():
    return render_template("nav_script.js")

if __name__ == "__main__":
    app.run(debug=True)
