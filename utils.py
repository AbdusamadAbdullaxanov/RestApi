from passlib.context import CryptContext

passwordd = CryptContext(schemes=['bcrypt'], deprecated="auto")


def hash_pwd(password: str):
    return passwordd.hash(password)


def verify_pwd(ordinary: str, hashed: str) -> bool:
    return passwordd.verify(ordinary, hashed)


if __name__ == '__main__':
    h = hash_pwd("1234567")
    print(h)
    print(verify_pwd("1234567", h))
