from authlib.jose import jwt, JoseError
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timezone, timedelta
from utils import schemas

ALGO = 'HS256'
SECRET_KEY = 'my_secret_key'
ACCESS_TOKEN_EXPIRY_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/token")


def create_token(data: schemas.CreateToken):
    """

        Input: 
            data: {"sub": data.username}

        Inside the function:
            header =  {"alg": ALGO}
            payload = {
                "sub" : "username",
                "exp" : 2025-11-20 11:55:30
            }
    """

    header = {"alg": ALGO}
    payload = data.copy()
    exp = datetime.now(timezone.utc) + \
        timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    payload["exp"] = exp
    token = jwt.encode(header=header, payload=payload, key=SECRET_KEY)
    return {'access_token': token, 'token_type': 'bearer'}


def verify_token(token: str = Depends(oauth2_scheme)):

    try:
        claim = jwt.decode(token, SECRET_KEY)
        claim.validate()
        username = claim.get('sub')
        if username is None:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials")
        return username
    except Exception as e:
        print(f"Error in verify token {e}")
