from authlib.jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
oauth_scheme = OAuth2PasswordBearer(tokenUrl='login/token')
ALGO = 'HS256'
SECRET_KEY = 'my_secret_key'
ACCESS_TOKEN_EXPIRY_MINUTES = 30


def create_token(data):
    header = {"alg": ALGO}
    payload = {
        "sub": data.username
    }
    token = jwt.encode(header=header, payload=payload, key=SECRET_KEY)
    return {
        "access_token": token,
        "token_type": "Bearer"
    }


def verify_token(token: str = Depends(oauth_scheme)):
    try:

        print(f"token: {token}")
        claim = jwt.decode(token, key=SECRET_KEY)
        claim.validate()
        username = claim.get('sub')
        if username is None:
            print("Error while verifying token")
        return username

    except Exception as e:
        print(f"verify token - {e}")
