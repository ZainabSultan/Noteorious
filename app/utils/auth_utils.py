# function that takes in email and password, and returns token from typing import Annotated
import jwt
from datetime import datetime, timedelta, timezone


class TokenService:

    def __init__(self, secret: str, algorithm: str, expiration: int = 15) -> None:
        self.secret = secret
        self.algorithm = algorithm
        self.expiration = expiration

    def create(self, subject: str, expires_delta: timedelta | None = None) -> str:
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes = self.expiration))
        jwt_payload = {'sub' : subject, 'exp' : expire, 'iat' : datetime.now(timezone.utc)}
        token = jwt.encode(jwt_payload, self.secret, self.algorithm)
        return token

    def decode(self, token) -> str:
        payload = jwt.decode(token, self.secret, algorithms = [self.algorithm])
        print(payload)
        username = payload.get('sub')
        return username