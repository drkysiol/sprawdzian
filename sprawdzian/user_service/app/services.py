from .models import User

users = []

def create_user(first_name, last_name, birth_year, group):
    user = User(len(users) + 1, first_name, last_name, birth_year, group)
    users.append(user)
    return user

def get_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None

def update_user(user_id, first_name=None, last_name=None, birth_year=None, group=None):
    user = get_user(user_id)
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if birth_year:
            user.birth_year = birth_year
        if group:
            user.group = group
        return user
    return None

def delete_user(user_id):
    global users
    users = [user for user in users if user.id != user_id]
