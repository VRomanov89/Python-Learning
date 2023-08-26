# Course - https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1&t=0s

from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p><h1>Hello, World!</h1></p>"

@app.route("/about")
def about():
    return "<p><h1>About Page</h1></p>"


if __name__ == '__main__':
    app.run(debug=True)