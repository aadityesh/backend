from fastapi import FastAPI, Depends
from database.setup import create_db_and_tables, get_db
from crud import user, weather
from schemas import UserLogin
from auth.token import verify_token
from fastapi.security import OAuth2PasswordRequestForm
from cache.redis import connect_to_cache

app = FastAPI()

create_db_and_tables()


@app.post("/login/token")
def login_handler(data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    return user.login(data, db)


@app.get('/weather/{location}')
def get_weather_handler(location: str, username=Depends(verify_token), r=Depends(connect_to_cache)):
    if username:
        return weather.get_weather_data(location, r)
