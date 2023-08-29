from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/course")
def course():
    return render_template("courses.html")
@app.route("/trainers")
def trainers():
    return render_template("trainers.html")

if __name__ == "__main__":
    app.run(debug=True)