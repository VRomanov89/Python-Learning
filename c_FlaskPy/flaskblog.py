# Course - https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1&t=0s

from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Corey',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 20218'
    },
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 20218'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)