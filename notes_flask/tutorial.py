from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
          return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contact():
      return "<p>dont contact me</p>"

@app.route("/<name>")
def user(name):
      return f"<h1>hello, {name}!</h1>"


if __name__ == "__main__":
        app.run(debug=True)

#What does Flask do?
    #it allows multiple pages on a website.

#What are the steps to setting up a Flask project?
    #set the flask library and add what its going to say.

#How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)

#What are templates?