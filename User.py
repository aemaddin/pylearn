class User:
    id = 0
    first_name = ''
    middle_name = ''
    last_name = ''


def create(**attributes):
    user = User()

    user.id = attributes['id']
    user.first_name = attributes['first_name']
    user.last_name = attributes['last_name']
    user.middle_name = attributes['middle_name']

    return user


def search(_id):
    for user in sample_data():
        if user.id == _id:
            return user

    return 0


def sample_data():
    return [
        create(id=1, first_name='Amr', middle_name='Emad', last_name='Ahmed'),
        create(id=2, first_name='Mohamed', middle_name='Emad', last_name='Ahmed'),
        create(id=3, first_name='Ahmed', middle_name='Emad', last_name='Ahmed'),
        create(id=4, first_name='Abdullah', middle_name='Emad', last_name='Ahmed'),
        create(id=5, first_name='Ali', middle_name='Hassan', last_name='Mohamed'),
        create(id=6, first_name='Mahmoud', middle_name='Islam', last_name='Khalil'),
        create(id=7, first_name='Nader', middle_name='Said', last_name='Mohsen'),
        create(id=8, first_name='Mostafa', middle_name='Met-wally', last_name='Ahmed'),
        create(id=9, first_name='Rashid', middle_name='Saeed', last_name='Raed'),
    ]
