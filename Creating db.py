import sqlite3

conn = sqlite3.connect('app.db')
# Create a cursor - a
c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT,
    datebirth TEXT,
    adress TEXT,
    metro TEXT,
    tel TEXT,
    info TEXT
)
''')

conn.commit()


# Our base data
users = [
    {
        'id': '222222',
        'fio': 'Igor Novikov',
        'datebirth': '26.12.01',
        'adress': 'SPB, Sedova 55',
        'metro': 'Lomonosovskaya',
        'tel': '345678',
        'info': 'Not a social guy'
    },
    {
        'id': '223452',
        'fio': 'Gleb Vyacheslavovich',
        'datebirth': '11.11.93',
        'adress': 'SPB, Macdonalds, Galerea',
        'metro': 'Pl. Vosstaniya',
        'tel': '46900987',
        'info': 'I like dogs'
    },
{
        'id': '0987654',
        'fio': 'Bradley Cooper',
        'datebirth': 'dont wanna share',
        'adress': 'SPB, Grand Europe Hotel',
        'metro': 'Nevskiy Prospect',
        'tel': '98765443232',
        'info': 'Love my wife'
    },
]

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
