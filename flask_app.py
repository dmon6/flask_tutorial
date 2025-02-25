from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Dennis Monton',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Dennis Monton',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2018'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/hello')
def hello():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run(debug=True)
