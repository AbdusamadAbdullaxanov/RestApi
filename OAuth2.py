from jose import jwt, JWTError
from configuration import settings
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer

ALGORITHM = settings.algorithm
SECRETKEY = settings.secretkey
EXPIREHOURS = settings.expirehours
scheme = OAuth2PasswordBearer(tokenUrl="/users/sign-up")


def access_token(id: int, email: str, password: str) -> str:
    expire = datetime.now() + timedelta(hours=EXPIREHOURS)
    hardcode = {"id": str(id), "email": email, "password": password, "expire_date": str(expire)}
    encoded = jwt.encode(hardcode, SECRETKEY, algorithm=ALGORITHM)
    return encoded


def verify_token(token: str, error):
    try:
        decoded = jwt.decode(token, SECRETKEY, algorithms=[ALGORITHM])
        if not decoded or decoded is None:
            raise error
        return decoded.get("id")
    except JWTError:
        error.detail = "From JWTError: " + str(error.detail)
        raise error


def get_current_user_id(token: str = Depends(scheme)):
    credentials_error = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token recieved")
    return verify_token(token, credentials_error)


if __name__ == '__main__':
    print(access_token(3, "pythondeveloper441@gmail.com", "$enterpassword$"))
    print(verify_token(
        access_token(3, "pythondeveloper441@gmail.com", "$enterpassword$"),
        HTTPException(status_code=400, detail="Invalid credentials")))
    print(scheme)
