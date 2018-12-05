_users = {

    '222222': {
    'id': '222222',
    'fio': 'Igor Novikov',
    'datebirth': '26.12.01',
    'adress': 'SPB, Sedova 55',
    'metro': 'Lomonosovskaya',
    'tel': '345678',
    'info': 'Not a social guy'
    },
    '223452': {
    'id': '223452',
    'fio': 'Gleb Vyacheslavovich',
    'datebirth': '11.11.93',
    'adress': 'SPB, Macdonalds, Galerea',
    'metro': 'Pl. Vosstaniya',
    'tel': '46900987',
    'info': 'I like dogs'
    },
    '0987654':{
    'id': '0987654',
    'fio': 'Bradley Cooper',
    'datebirth': 'dont wanna share',
    'adress': 'SPB, Grand Europe Hotel',
    'metro': 'Nevskiy Prospect',
    'tel': '98765443232',
    'info': 'Love my wife'
    }
}

# Get users filtered by name
def get_users_by_name(q):
    results = []
    # SEARCH
    return results


def get_user(username):
    return _users.get(username)