from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(prefix="/users")


@router.get("", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.list_users()

@router.post("", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(data)

@router.put("/{user_id}", response_model=UserResponse)
def edit_user(user_id: int, data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.edit_user(user_id, data)
