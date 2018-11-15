from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>PetHelper home page</h2>'


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