from flask import Flask, request
from flask import render_template
import db
from flask import request

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



@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('page01.html', users=users)


if __name__ == '__main__':
   app.run(debug=True)