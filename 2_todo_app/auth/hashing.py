from pwdlib import PasswordHash


pwd_hash = PasswordHash.recommended()


def hash_password(plain_password: str):
    return pwd_hash.hash(plain_password)


def verify_password(plain_pwd: str, hashed_pwd: str):
    return pwd_hash.verify(plain_pwd, hashed_pwd)
