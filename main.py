from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/admissions")
def about():
    return render_template("admissions.html")


@app.route("/placements")
def placements():
    return render_template('placements.html')


@app.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")


@app.route("/about-us")
def about_us():
    return render_template("about-us.html")


@app.route("/campus-life/library")
def library():
    return render_template('library.html')


@app.route('/2048')
def game_2048():
    return render_template('2048-game.html')


@app.route("/campus-life/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/campus-life/sports")
def sports():
    return 'sports'


if __name__ == "__main__":
    app.run(debug=False)


app.add_url_rule("/campus-life", '/library', library)
app.add_url_rule("/campus-life", '/gallery', gallery)
app.add_url_rule("/campus-life", '/sports', sports)