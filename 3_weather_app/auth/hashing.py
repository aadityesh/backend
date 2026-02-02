from pwdlib import PasswordHash

pwd_hash = PasswordHash.recommended()


def hash_password(plain_pwd) -> str:
    return pwd_hash.hash(plain_pwd)


def verify_password(plain_pwd, hashed_pwd) -> bool:
    return pwd_hash.verify(plain_pwd, hashed_pwd)
