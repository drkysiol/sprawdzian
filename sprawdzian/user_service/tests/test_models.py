from app.models import User

def test_user_age():
    user = User(1, 'John', 'Doe', 1990, 'user')
    assert user.age == 34 

def test_user_group():
    user = User(1, 'John', 'Doe', 1990, 'user')
    assert user.group == 'user'
