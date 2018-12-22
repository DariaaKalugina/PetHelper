from flask import Flask
from flask import render_template
from flask import request, redirect
import sqlite3
import db
app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def index():
    # connecting to db
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users")
    users = list(c.fetchall())

    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('page01.html', users=users)


@app.route('/sing_in')
def profile():
    return render_template('sing_in.html')


@app.route('/ads')
def ads():
    return render_template('ads.html')


@app.route('/newad')
def newad():
    return render_template('newad.html')


@app.route('/user/<username>/')
def user_page(username):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here

    c.execute("SELECT * FROM users WHERE username LIKE'%%%s%%'" % username)
    users = list(c.fetchall())

    # Close connection
    conn.close()
    return render_template("userpage.html", user=username)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():

    user_created = False
    error_message = ""

    if request.method == 'POST':

        # add new user data

        user = {}
        user['username'] = request.form.get('username')
        user['fio'] = request.form.get('fio')
        user['password'] = request.form.get('password')
        user['datebirth'] = request.form.get('datebirth')
        user['metro'] = request.form.get('metro')
        user['tel'] = request.form.get('tel')
        user['info'] = request.form.get('info')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users where username='%s'" % user['username'])

        if c.fetchone():
            # user with this login is already in my database
            error_message = "user_exists"
        else:

            c.execute("INSERT INTO users "
                      "( username, password, datebirth, metro, tel, info) "
                      "VALUES "
                      "('{username}', '{password}', '{datebirth}','{metro}','{tel}','{info}')".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        return redirect('/user/%s/' % user['username'])

    return render_template(
        "add_user.html",
        user_created=user_created,
        error_message=error_message
    )


@app.route('/search')
def search_for_person():
    q = request.args.get('query')

    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users WHERE fio LIKE '%{q}%' OR username LIKE '%{q}%'"
              "".format(q=q))
    users = list(c.fetchall())

    conn.close()

    return render_template('search_results.html', q=q, user=users)

app.run()