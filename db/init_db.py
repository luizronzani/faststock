from db.base import Base
from db.session import engine

# IMPORTAR TODAS AS MODELS
from models import user # importante

def init_db():
    Base.metadata.create_all(bind=engine)