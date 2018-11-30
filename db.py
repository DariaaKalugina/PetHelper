_users = {
    'paul': {
    'name': 'Pavel Okopnyi',
    'birth': '29.01.1984',
    'workplace': 'UiB'
    },

    'igor': {
    'name': 'Igor Novikov',
    'birth': '30.04.1973',
    'workplace': 'ArtLebedev'
    },

    'boris': {
    'name': 'Boris Ivanov',
    'birth': '26.02.19',
    'workplace': 'HSE Sedova'
    },

    'alena': {
    'name': 'Alena Popova',
    'birth': 'Data Scientist',
    'workplace': 'ITMO'
    }
}


_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)



def get_users_by_name(q):
    results = _user_list

    return results
