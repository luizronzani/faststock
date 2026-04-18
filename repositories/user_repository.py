from sqlalchemy.orm import Session
from models.user import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(User).all()

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create(self, name: str, email: str, password: str):
        user = User(name=name, email=email, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()

    def update(self, user_id: int, name: str, email: str, password: str):
        user = self.get_by_id(user_id)
        if not user:
            return None

        user.name = name
        user.email = email
        user.password = password

        self.db.commit()
        self.db.refresh(user)
        return user