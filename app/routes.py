from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Karl'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Big_Chungus'},
            'body': 'Elon Musk talked about Harambe 2 years after the meme was dead smdh'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
