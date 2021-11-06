from flask import jsonify, render_template, request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect

from app import app
from app.forms import LoginForm


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

@app.route('/hello', methods=['GET', 'POST'])
def hello():
# POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')  

@app.route('/login', methods=['GET', 'POST'])  
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
