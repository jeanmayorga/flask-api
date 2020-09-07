
# list of users
list_of_users = [
    {"id": 1, "name": 'Jhon'},
    {"id": 2, "name": 'Peter'}
]


# controllers
def get_users():
    return list_of_users


def get_user(user_id):
    for user in list_of_users:
        if(user['id'] == int(user_id)):
            return user


def insert_user(new_user):
    last_user = list_of_users[-1]
    new_id = int(last_user['id']) + 1

    new_user.update({"id": new_id})

    list_of_users.append(new_user)

    return new_user


def delete_user(user):
    return list_of_users.remove(user)


def update_user(user_id, user_update_data):
    for index, user in enumerate(list_of_users):
        if(user['id'] == int(user_id)):
            user.update(user_update_data)
            user_update_data[index] = user
            return user
