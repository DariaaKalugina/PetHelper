import sqlite3

conn = sqlite3.connect('app.db')
# Create a cursor - a
c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    fio TEXT,
    password TEXT,
    datebirth TEXT,
    adress TEXT,
    metro TEXT,
    tel TEXT,
    info TEXT,
    photo TEXT
)
''')

conn.commit()


# Our base data
users = [
    {
        'username': 'Igoresha',
        'fio': 'Igor Novikov',
        'datebirth': '26.12.01',
        'adress': 'SPB, Sedova 55',
        'metro': 'Lomonosovskaya',
        'tel': '345678',
        'info': 'Not a social guy'
    },
    {
        'username': 'Glebushka',
        'fio': 'Gleb Vyacheslavovich',
        'datebirth': '11.11.93',
        'adress': 'SPB, Macdonalds, Galerea',
        'metro': 'Pl. Vosstaniya',
        'tel': '46900987',
        'info': 'I like dogs'
    },
    {
        'username': 'Bread',
        'fio': 'Bradley Cooper',
        'datebirth': 'dont wanna share',
        'adress': 'SPB, Grand Europe Hotel',
        'metro': 'Nevskiy Prospect',
        'tel': '98765443232',
        'info': 'Love my wife'
    },
]

c.execute('''
    UPDATE users
    SET tel="444444444444"
    WHERE username="Bread"
''')
conn.commit()

#Adding it in the loop
for user in users:
    c.execute("INSERT INTO users "
              "(username, fio, datebirth, adress, metro, tel, info)"
              "VALUES "
              "('{username}', '{fio}', '{datebirth}', '{adress}', '{metro}', '{tel}', '{info}')".FORMAT(**user))
    conn.commit


# Add second table
c.execute('''
    CREATE TABLE advert (
        idAD INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT,
        animalkind TEXT,
        nickname TEXT,
        requirements TEXT,
        datetime DATETIME
    )
''')
conn.commit()

advert = [
    { 'service': 'Wash my cat pls',
      'animalkind': 'cat',
      'nickname': 'Tisha',
      'requirements': 'Guys, хочу мыть кота раз в месяц (у меня дома). Лично я боюсь царапин. Это ведь не сложно? Буду рада, пишите. Он спокойный, но очень пугливый.',
      'datetime': '2019-01-15'
    }
]

c.execute('''
    INSERT INTO advert (nickname, service, animalkind)
    VALUES
    ("Tisha","Watch", "Cat")
''')
conn.commit()

# Many to many connection
c.execute('''
    CREATE TABLE response (
        idR INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        ad_id INTEGER
    )
''')

conn.commit()

c.execute("INSERT INTO response (user_id, ad_id) VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO response (user_id, ad_id) VALUES (3, 1)")
conn.commit()


c.execute("SELECT u.* "
          "FROM response ue "
          "JOIN users u ON (u.id=ue.user_id) "
          "WHERE ue.ad_id=1")


conn.close()
