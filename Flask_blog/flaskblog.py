
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_kEY'] = '96b9dfdd948e108fd07bee8247e1516b'
csrf = CSRFProtect(app)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
@csrf.exempt
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
@csrf.exempt
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
