from flask import Flask
from flask import render_template


web = Flask(__name__)

@web.route("/") #HOME
def homepage():
    return render_template("homepage.html")


if __name__ == "__main__":
    web.run(debug=True)