from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('page01.html')


@app.route('/results')
def result():
    return 'Results of search:'


@app.route("/user/<username>")
def username():
    return 'User %s' % username


@app.route("/newuser")
def create_userpage():
    return "Create profile"


if __name__ == '__main__':


   app.run(debug=True)