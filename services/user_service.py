from fastapi import HTTPException

from repositories.user_repository import UserRepository


class UserService:

    def __init__(self, db):
        self.repo = UserRepository(db)

    def create_user(self, data):
        existing = self.repo.get_by_email(data.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email já existe")

        return self.repo.create(
            name=data.name,
            email=data.email,
            password=data.password
        )

    def list_users(self):
        return self.repo.get_all()
    
    def edit_user(self, user_id, data):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        return self.repo.update(
            user_id=user_id,
            name=data.name,
            email=data.email,
            password=data.password
        )
