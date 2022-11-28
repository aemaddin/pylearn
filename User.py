class User:
    first_name = ''
    last_name = ''


def create(**attributes):
    user = User()

    user.first_name = attributes['first_name']
    user.last_name = attributes['last_name']

    return user
