
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_kEY'] = '29587d70b2dcd3fab719378a64b2ba44'

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
def RegistrationForm():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def LoginForm():
    form = LoginForm()
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(debug=True)
