from app.services import update_user

def test_update_user():
    user_id = 1
    user = {
        'first_name': 'John',
        'last_name': 'Doe',
        'birth_year': 1990,
        'group': 'user'
    }
    updated_user = update_user(user_id, first_name='Jane', group='premium')
    assert updated_user.first_name == 'Jane'
    assert updated_user.group == 'premium'
    assert updated_user.birth_year == user['birth_year']
    assert updated_user.last_name == user['last_name']
