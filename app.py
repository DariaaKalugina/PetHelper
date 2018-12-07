from flask import Flask
from flask import render_template
import db
from flask import request, redirect
import sqlite3
app = Flask(__name__)



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def index():
    return render_template('page01.html')


@app.route('/profile')
def profile():
    return 'Ваш профиль'


@app.route('/ads')
def ads():
    return 'Объявления'



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
        user['name'] = request.form.get('name')
        user['datebirth'] = request.form.get('datebirth')
        user['adress'] = request.form.get('adress')
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
                      "(username, name, datebirth, adress, metro, tel, info) "
                      "VALUES "
                      "('{username}','{name}','{datebirth}','{adress}','{metro}','{tel}','{info}')"
                      "".format(**user))

            conn.commit()

            user_created = True

        conn.close()

        # redirect to user page

        return redirect('/profile/%s/' % user['username'])

    return render_template(

        "add_user.html",
        user_created=user_created,
        error_message=error_message

    )


@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('page01.html', q=q, users=users)


app.run()