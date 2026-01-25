from models.users import User

# /session


def create_user(data):
    try:
        new_user = User()
        new_user.name = data.name
        new_user.email = data.email
        new_user.password = data.password
        new_user.username = data.username
        new_user.save()
        return {
            "msg": "User created successfully"
        }
    except Exception as e:
        print(f"Exception: {e}")
        return {
            "msg": "User creation failed"
        }
